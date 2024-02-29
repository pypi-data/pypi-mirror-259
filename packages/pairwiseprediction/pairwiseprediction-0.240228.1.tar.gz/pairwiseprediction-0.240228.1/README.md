Handle a regression problem inducing the model on pairs A,B of instances.

Last column of `X` is the continuous target. `y` is ignored.

Four modes are hipotetically possible, although only mode 2 is provided by now to ease compatibility with sklearn: 
    * a classification algorithm is trained to tell when instance A has higher target than instance B
        * 1) the prediction is based on interpolation which is the type of result expected from a regression
        * 2) the interpolated value can be converted to a hard prediction through binarization
    * a regression algorithm is trained to predict the difference between target values of A,B
        * 3) the prediction is the value provided directly by the regressor
        * 4) the regression value can be converted to a hard prediction through binarization
