'''
https://machinelearningmastery.com/arima-for-time-series-forecasting-with-python/

Autoregressive Integrated Moving Average Model
The ARIMA (AutoRegressive Integrated Moving Average) model stands as a statistical powerhouse for analyzing and forecasting time series data.

It explicitly caters to a suite of standard structures in time series data, and as such provides a simple yet powerful method for making skillful time series forecasts.

ARIMA is an acronym that stands for AutoRegressive Integrated Moving Average. It is a generalization of the simpler AutoRegressive Moving Average and adds the notion of integration.

Let’s decode the essence of ARIMA:

AR (Autoregression): This emphasizes the dependent relationship between an observation and its preceding or ‘lagged’ observations.
I (Integrated): To achieve a stationary time series, one that doesn’t exhibit trend or seasonality, differencing is applied. It typically involves subtracting an observation from its preceding observation.
MA (Moving Average): This component zeroes in on the relationship between an observation and the residual error from a moving average model based on lagged observations.
Each of these components is explicitly specified in the model as a parameter. A standard notation is used for ARIMA(p,d,q) where the parameters are substituted with integer values to quickly indicate the specific ARIMA model being used.

The parameters of the ARIMA model are defined as follows:

p: The lag order, representing the number of lag observations incorporated in the model.
d: Degree of differencing, denoting the number of times raw observations undergo differencing.
q: Order of moving average, indicating the size of the moving average window.
A linear regression model is constructed including the specified number and type of terms, and the data is prepared by a degree of differencing to make it stationary, i.e. to remove trend and seasonal structures that negatively affect the regression model.

Interestingly, any of these parameters can be set to 0. Such configurations enable the ARIMA model to mimic the functions of simpler models like ARMA, AR, I, or MA.

Adopting an ARIMA model for a time series assumes that the underlying process that generated the observations is an ARIMA process. This may seem obvious but helps to motivate the need to confirm the assumptions of the model in the raw observations and the residual errors of forecasts from the model.
'''

#example of loading a time series dataset

import pandas as pd
from pandas.plotting import autocorrelation_plot
from pandas import read_csv, to_datetime
from pandas import DataFrame
import datetime
from matplotlib import pyplot
from statsmodels.tsa.arima.model import ARIMA
from sklearn.metrics import mean_squared_error
from math import sqrt

df_load = read_csv('shampoo-sales.csv', header=0, index_col=0)
print(df_load.head())
df_load.plot()
#pyplot.show()

#pandas autoplot function
# Read the CSV file, potentially adjusting the header and index_col parameters as necessary
df = df_load.copy()

# If your DataFrame has only one column of interest for autocorrelation, select it to create a Series
# Replace 'column_name' with the actual name of your column of interest
series = df['Sales']

# If your data needs to be converted to numeric values (e.g., if they were read as strings),
# you can convert them using to_numeric and coerce errors to NaN, then drop them
series = pd.to_numeric(series, errors='coerce').dropna()

# Now, plot the autocorrelation
autocorrelation_plot(series)
#pyplot.show()

'''
ARIMA with Python
The statsmodels library stands as a vital tool for those looking to harness the power of ARIMA for time series forecasting in Python.

Building an ARIMA Model: A Step-by-Step Guide:

Model Definition: Initialize the ARIMA model by invoking ARIMA() and specifying the p, d, and q parameters.
Model Training: Train the model on your dataset using the fit() method.
Making Predictions: Generate forecasts by utilizing the predict() function and designating the desired time index or indices.
Let’s start with something simple. We will fit an ARIMA model to the entire Shampoo Sales dataset and review the residual errors.

We’ll employ the ARIMA(5,1,0) configuration:

5 lags for autoregression (AR)
1st order differencing (I)
No moving average term (MA)
'''

#installed statsmodels with pip

# Convert index to datetime
series.index = to_datetime(series.index, format='%m/%d/%Y')

# Convert index to period ('M' for monthly)
series.index = series.index.to_period('M')

# fit model
model = ARIMA(series, order=(5,1,0))
model_fit = model.fit()

# summary of fit model
print(model_fit.summary())

# line plot of residuals
residuals = DataFrame(model_fit.resid)
residuals.plot()
pyplot.show()

# density plot of residuals
residuals.plot(kind='kde')
pyplot.show()

# summary stats of residuals
print(residuals.describe())

'''
The distribution of the residual errors is displayed. 
The results show that indeed there is a bias in the prediction 
(a non-zero mean in the residuals).
'''


'''
Rolling Forecast ARIMA Model
The ARIMA model can be used to forecast future time steps.

The ARIMA model is adept at forecasting future time points. In a rolling forecast, the model is often retrained as new data becomes available, allowing for more accurate and adaptive predictions.

We can use the predict() function on the ARIMAResults object to make predictions. It accepts the index of the time steps to make predictions as arguments. These indexes are relative to the start of the training dataset used to make predictions.

How to Forecast with ARIMA:

Use the predict() function on the ARIMAResults object. This function requires the index of the time steps for which predictions are needed.
To revert any differencing and return predictions in the original scale, set the typ argument to ‘levels’.
For a simpler one-step forecast, employ the forecast() function.
We can split the training dataset into train and test sets, use the train set to fit the model and generate a prediction for each element on the test set.

A rolling forecast is required given the dependence on observations in prior time steps for differencing and the AR model. A crude way to perform this rolling forecast is to re-create the ARIMA model after each new observation is received.
'''

'''
How to Create an ARIMA Model for Time Series Forecasting in Python
by Jason Brownlee on November 18, 2023 in Time Series 843
 Tweet Share
A popular and widely used statistical method for time series forecasting is the ARIMA model.

ARIMA stands for AutoRegressive Integrated Moving Average and represents a cornerstone in time series forecasting. It is a statistical method that has gained immense popularity due to its efficacy in handling various standard temporal structures present in time series data.

Rolling Forecast ARIMA Model
The ARIMA model can be used to forecast future time steps.

The ARIMA model is adept at forecasting future time points. In a rolling forecast, the model is often retrained as new data becomes available, allowing for more accurate and adaptive predictions.

We can use the predict() function on the ARIMAResults object to make predictions. It accepts the index of the time steps to make predictions as arguments. These indexes are relative to the start of the training dataset used to make predictions.

How to Forecast with ARIMA:

Use the predict() function on the ARIMAResults object. This function requires the index of the time steps for which predictions are needed.
To revert any differencing and return predictions in the original scale, set the typ argument to ‘levels’.
For a simpler one-step forecast, employ the forecast() function.
We can split the training dataset into train and test sets, use the train set to fit the model and generate a prediction for each element on the test set.

A rolling forecast is required given the dependence on observations in prior time steps for differencing and the AR model. A crude way to perform this rolling forecast is to re-create the ARIMA model after each new observation is received.
'''

# evaluate an ARIMA model using a walk-forward validation

# split into train and test sets
X = series.values
size = int(len(X) * 0.66)
train, test = X[0:size], X[size:len(X)]
history = [x for x in train]
predictions = list()
# walk-forward validation
for t in range(len(test)):
 model = ARIMA(history, order=(5,1,0))
 model_fit = model.fit()
 output = model_fit.forecast()
 yhat = output[0]
 predictions.append(yhat)
 obs = test[t]
 history.append(obs)
 print('predicted=%f, expected=%f' % (yhat, obs))
# evaluate forecasts
rmse = sqrt(mean_squared_error(test, predictions))
print('Test RMSE: %.3f' % rmse)
# plot forecasts against actual outcomes
pyplot.plot(test)
pyplot.plot(predictions, color='red')
pyplot.show()


'''
We manually keep track of all observations in a list called history that is seeded with the training data and to which new observations are appended each iteration.

Putting this all together, below is an example of a rolling forecast with the ARIMA model in Python.

Running the example prints the prediction and expected value each iteration.

We can also calculate a final root mean squared error score (RMSE) for the predictions, providing a point of comparison for other ARIMA configurations.

predicted=343.272180, expected=342.300000
predicted=293.329674, expected=339.700000
predicted=368.668956, expected=440.400000
predicted=335.044741, expected=315.900000
predicted=363.220221, expected=439.300000
predicted=357.645324, expected=401.300000
predicted=443.047835, expected=437.400000
predicted=378.365674, expected=575.500000
predicted=459.415021, expected=407.600000
predicted=526.890876, expected=682.000000
predicted=457.231275, expected=475.300000
predicted=672.914944, expected=581.300000
predicted=531.541449, expected=646.900000
Test RMSE: 89.021
A line plot is created showing the expected values (blue) compared to the rolling forecast predictions (red). We can see the values show some trend and are in the correct scale.

ARIMA Rolling Forecast Line Plot
ARIMA Rolling Forecast Line Plot

The model could use further tuning of the p, d, and maybe even the q parameters.


Configuring an ARIMA Model
ARIMA is often configured using the classical Box-Jenkins Methodology. This process employs a meticulous blend of time series analysis and diagnostics to pinpoint the most fitting parameters for the ARIMA model.

The Box-Jenkins Methodology: A Three-Step Process:

Model Identification: Begin with visual tools like plots and leverage summary statistics. These aids help recognize trends, seasonality, and autoregressive elements. The goal here is to gauge the extent of differencing required and to determine the optimal lag size.
Parameter Estimation: This step involves a fitting procedure tailored to derive the coefficients integral to the regression model.
Model Checking: Armed with plots and statistical tests delve into the residual errors. This analysis illuminates the temporal structure that the model might have missed.
The process is repeated until either a desirable level of fit is achieved on the in-sample or out-of-sample observations (e.g. training or test datasets).

The process was described in the classic 1970 textbook on the topic titled Time Series Analysis: Forecasting and Control by George Box and Gwilym Jenkins. An updated 5th edition is now available if you are interested in going deeper into this type of model and methodology.

Given that the model can be fit efficiently on modest-sized time series datasets, grid searching parameters of the model can be a valuable approach.
'''

