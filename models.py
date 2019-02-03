import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
import pickle
import requests
import json

# We train a model to predict the levels of refugge arrivals in the Greek islands
# based on the google searches for Facebook in the Turkish region of Balikesir Province the week before.


dataset = pd.read_csv('DF.csv', sep= ';')



#rescale the vol of arrivales in order to have 
#  the magnitude of values in x and y 

X = dataset.iloc [:, [96]].values

y = dataset.iloc[:, [1]].values

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.33, random_state = 0)

regressor = RandomForestRegressor(n_estimators = 100, random_state = 42)


regressor.fit(X_train, y_train)
y_pred = regressor.predict(X_test)

pickle.dump(regressor, open('model.pkl','wb'))


model = pickle.load(open('model.pkl','rb'))

#print(model.predict([[sys.argv[1]]]))




