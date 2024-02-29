import numpy as np
from sklearn.base import BaseEstimator, ClassifierMixin
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import StratifiedKFold, cross_val_score

from pairwiseprediction.combination import pairwise_diff, pairwise_hstack
from pairwiseprediction.interpolation import interpolate_for_classification


class PairwiseClassifier(BaseEstimator, ClassifierMixin):
    r"""

    :param algorithm: Internal algorithm to predict pairs.
    :param pairwise: Type of combination: "difference" or "concatenation".
    :param threshold: How much difference between target values should be considered as relevant within a pair?
    :param proportion: Is the threshold an absolute value (difference) or relative value (proportion)?
    :param center: Default value is the mean of the training sample.
    :param only_relevant_pairs_on_prediction: Whether to keep only relevant differences during interpolation.
    :param n_jobs: Number of processess in parallel
    :param kwargs: Arguments for user-provided `algorithm`.

    >>> import numpy as np
    >>> from sklearn.datasets import load_diabetes
    >>> from sklearn.ensemble import RandomForestClassifier
    >>> a, b = load_diabetes(return_X_y=True)
    >>> me = np.mean(b)
    >>> y = (b > me).astype(int)
    >>> alg = RandomForestClassifier(n_estimators=3, random_state=0, n_jobs=-1)
    >>> np.mean(cross_val_score(alg, a, y, cv=StratifiedKFold(n_splits=2)))  # doctest:+ELLIPSIS +NORMALIZE_WHITESPACE
    0.69...
    >>> c = b.reshape(len(b), 1)
    >>> X = np.hstack([a, c])
    >>> alg = PairwiseClassifier(n_estimators=3, threshold=20, only_relevant_pairs_on_prediction=False, random_state=0, n_jobs=-1)
    >>> np.mean(cross_val_score(alg, X, y, cv=StratifiedKFold(n_splits=2)))  # doctest:+ELLIPSIS +NORMALIZE_WHITESPACE
    0.72...
    """

    def __init__(self, algorithm=RandomForestClassifier, pairwise="concatenation", threshold=0, proportion=False, center=None, only_relevant_pairs_on_prediction=False, **kwargs):
        self.algorithm = algorithm
        self.alg = algorithm(**kwargs)
        self.pairwise = pairwise
        self.threshold = threshold
        self.proportion = proportion
        self.center = center
        self.only_relevant_pairs_on_prediction = only_relevant_pairs_on_prediction

    # def get_params(self, deep=False):
    #     return {}  # "n_estimators": self.n_estimators, "n_jobs": self.n_jobs, "random_state": self.random_state, "diff": self.diff}

    def fit(self, X, y=None):
        """
        WARNING: y is ignored; permutation test wont work
        TODO: see if permutation test accept pandas; use index to fix warning above

        :param X:
        :param y:
        :return:
        """
        self.Xw = X if isinstance(X, np.ndarray) else np.array(X)
        X = y = None

        if self.center is None:
            self.center = np.mean(self.Xw[:, -1])

        handle_last_as_y = "%" if self.proportion else True
        filter = lambda tmp: (tmp[:, -1] < -self.threshold) | (tmp[:, -1] >= self.threshold)
        pairwise = True
        if self.pairwise == "difference":
            pairs = lambda a, b: pairwise_diff(a, b, pct=handle_last_as_y == "%")
        elif self.pairwise == "concatenation":
            pairs = lambda a, b: pairwise_hstack(a, b, handle_last_as_y=handle_last_as_y)
        elif self.pairwise == "none":
            if self.proportion:
                raise Exception(f"Just use delta=9 instead of pct,delta=0.1  (assuming you are looking for 20% increase")
            boo = self.Xw[(self.Xw[:, -1] < self.center - self.threshold) | (self.Xw[:, -1] >= self.center + self.threshold)]
            self.Xw = self.Xw[boo]
            pairwise = False
        else:
            raise Exception(f"Not implemented for {self.pairwise=}")
        # self.classes_ = unique_labels(y)

        # sort
        self.idxs = np.argsort(self.Xw[:, -1].flatten(), kind="stable").flatten()
        self.Xw = self.Xw[self.idxs]

        if pairwise:  # pairwise transformation
            tmp = pairs(self.Xw, self.Xw)
            pairs_Xy_tr = tmp[filter(tmp)]
            Xtr = pairs_Xy_tr[:, :-1]
            ytr = (pairs_Xy_tr[:, -1] >= 0).astype(int)
        else:
            Xtr = self.Xw[:, :-1]
            w = self.Xw[:, -1]
            ytr = (w >= self.center).astype(int)

        self.alg.fit(Xtr, ytr)
        self.Xw_tr = self.Xw[abs(self.Xw[:, -1] - self.center) >= self.threshold] if self.only_relevant_pairs_on_prediction else self.Xw
        return self

    def predict(self, X):
        # check_is_fitted(self)
        # TODO: check if state net ween runs is a problem for self.rf,idxs,Xw,hstack
        Xw_ts = X if isinstance(X, np.ndarray) else np.array(X)
        X = Xw_ts[:, :-1]  # discard label to avoid data leakage

        pairwise = True
        if self.pairwise == "difference":
            pairs = lambda a, b: pairwise_diff(a, b)
        elif self.pairwise == "concatenation":
            pairs = lambda a, b: pairwise_hstack(a, b)
        elif self.pairwise == "none":
            if self.proportion:
                raise Exception(f"For no pairwise, just use delta=9 instead of pct,delta=0.1  (assuming you are looking for 20% increase")
            pairwise = False
        else:
            raise Exception(f"Not implemented for {self.pairwise=}")

        if pairwise:
            targets = self.Xw_tr[:, -1]
            l = []
            for i in range(X.shape[0]):
                x = X[i : i + 1, :]
                Xts = pairs(x, self.Xw_tr[:, :-1])
                zts = self.alg.predict(Xts)

                # interpolation
                conditions = 2 * zts - 1
                # print(targets)
                # print()
                # print(conditions)
                # print("11111111111111111111111111")
                z = interpolate_for_classification(targets, conditions)
                l.append(int(z >= self.center))
            return np.array(l)
        return self.alg.predict(X)

    def __repr__(self, **kwargs):
        return "PW" + repr(self.alg)

    # def __sklearn_clone__(self):
    #     return PairwiseClassifier(self.n_estimators, self.n_jobs, self.random_state, self.diff)
