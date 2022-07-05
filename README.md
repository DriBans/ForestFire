# ForestFire Detection

This is my first project that will highlight my skills through GitHub. I will use the [Forest Fire Dataset in Kaggle](https://www.kaggle.com/datasets/elikplim/forest-fires-data-set) to predict the forest fire damage using regression analysis.

Note that the author of this dataset states that `this is a very difficult regression task. It can be used to test regression methods. Also, it could be used to test outlier detection methods, since it is not clear how many outliers are there. Yet, the number of examples of fires with a large burned area is very small.`

Here are the attributes information:

- X - x-axis spatial coordinate within the Montesinho park map: 1 to 9
- Y - y-axis spatial coordinate within the Montesinho park map: 2 to 9
- month - month of the year: "jan" to "dec"
- day - day of the week: "mon" to "sun"
- FFMC - FFMC index from the FWI system: 18.7 to 96.20
- DMC - DMC index from the FWI system: 1.1 to 291.3
- DC - DC index from the FWI system: 7.9 to 860.6
- ISI - ISI index from the FWI system: 0.0 to 56.10
- temp - temperature in Celsius degrees: 2.2 to 33.30
- RH - relative humidity in %: 15.0 to 100
- wind - wind speed in km/h: 0.40 to 9.40
- rain - outside rain in mm/m2 : 0.0 to 6.4
- area - the burned area of the forest (in ha): 0.00 to 1090.84.

There are two approaches for this analysis:
- I will do a complete predictive analysis on the entire data (The data provided by Kaggle is already cleaned)
- I will use regression and classification models to make the prediction.

Result:
As we want to create a quick model using the basic regression and classification tasks in this project. The regression model allowed us to predict the output, then we approached it with a classification task to predict whether it is 0 or not. We know that this regression model was hard to build sp, the score was low. Classification model barely showed a little, but those two models don't indicate they they are good enough to make prediction.

There could be many ways to improve the performance of the models, but one way I would improve on this model is applying XGBoost. XGBoost would allow us to use a gradient boosting library that is known to be highly efficient, flexible and portable. In this case I would conside RMSE and probably also consider skewness and outliers before performing a model fit.
