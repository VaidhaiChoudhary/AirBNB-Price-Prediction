import pandas as pd

df = pd.read_csv(r"C:\Users\DELL\Downloads\AB_NYC_2019.csv")
print(df)
print(df.head(5))
print(df.columns)
print(df.shape)

# Droppin unnecessary columns
df.drop(columns=["id", "name", "host_id", "host_name", "last_review"], inplace = True)
print("\nThis dataset contains {} rows\n".format(df.shape[0]))
print(df.head(5))

print(df.info())
print(df.describe())
print(df.isnull().sum())
df.duplicated().sum() 
df.drop_duplicates(inplace=True)
df.fillna({'reviews_per_month':0}, inplace=True) #filled missing data with 0
print(df.isnull().sum())


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.preprocessing import LabelEncoder, OneHotEncoder, StandardScaler
from sklearn.linear_model import LinearRegression, Lasso, Ridge
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.decomposition import PCA
from sklearn.metrics import r2_score, mean_squared_error, mean_absolute_error
#from yellowbrick.target import BalancedBinningReference
#from yellowbrick.regressor import PredictionError, ResidualsPlot
import os
import warnings
warnings.filterwarnings("ignore")

# applying log transformation for price column
df["price"] = np.log1p(df["price"])
X = df.drop("price", axis = 1)
y = df["price"]

# train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 42)
X_train = X_train.reset_index(drop=True)
X_test = X_test.reset_index(drop=True)

# Encoding
ohe = OneHotEncoder(handle_unknown = 'ignore')
columns = ["neighbourhood_group", "neighbourhood", "room_type"]
ohe_df_train = pd.DataFrame(ohe.fit_transform(X_train[columns]).toarray(), columns=ohe.get_feature_names_out())
X_train_ohe = X_train.join(ohe_df_train).drop(columns, axis=1)

ohe_df_test = pd.DataFrame(ohe.transform(X_test[columns]).toarray(), columns=ohe.get_feature_names_out())
X_test_ohe = X_test.join(ohe_df_test).drop(columns, axis=1)

# Feature Scaling
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train_ohe)
X_test = scaler.transform(X_test_ohe)


# Models/Estimators

'''# RIDGE REGRESSION
ridge = Ridge(alpha=1.0)    
print(ridge.fit(X_train, y_train))
y_pred = ridge.predict(X_test)
print(y_pred)

print("test_score", r2_score(y_test, y_pred))
print("train_score", ridge.score(X_train, y_train))
print("mae", mean_absolute_error(y_test, y_pred))
print("mse" ,mean_squared_error(y_test, y_pred))
print("rmse", np.sqrt(mean_squared_error(y_test, y_pred)))
print("rmse_cv", np.sqrt(-cross_val_score(ridge, X_train, y_train, scoring='neg_mean_squared_error', cv=5).mean()))
#print(test_score, train_score, mae, mse, rmse, rmse_cv)'''

    
    
# LASSO REGRESSION
lasso = Lasso(alpha = 0.0001)     
print(lasso.fit(X_train, y_train))
y_pred = lasso.predict(X_test)
print(y_pred)
   
print("test_score",  r2_score(y_test, y_pred))
print("train_score", lasso.score(X_train, y_train))
print("mae", mean_absolute_error(y_test, y_pred))
print("mse" , mean_squared_error(y_test, y_pred))
print("rmse", np.sqrt(mean_squared_error(y_test, y_pred)))
print("rmse_cv", np.sqrt(-cross_val_score(lasso, X_train, y_train, scoring='neg_mean_squared_error', cv=5).mean()))
    

    
'''# DECISION TREE   
dtr = DecisionTreeRegressor(min_samples_leaf=60)   # DECISION TREE
print(dtr.fit(X_train, y_train))
y_pred= dtr.predict(X_test)
print(y_pred)
   
print("test_score", r2_score(y_test, y_pred))
print("train_score",dtr.score(X_train, y_train))
print("mae",  mean_absolute_error(y_test, y_pred))
print("mse", mean_squared_error(y_test, y_pred))
print("rmse", np.sqrt(mean_squared_error(y_test, y_pred)))
print("rmse_cv", np.sqrt(-cross_val_score(dtr, X_train, y_train, scoring='neg_mean_squared_error', cv=5).mean()))'''
    
    
    
'''# RANDOM FOREST   
rfr = RandomForestRegressor(random_state = 42,  
                                n_estimators = 100,
                                min_samples_split = 10,
                                min_samples_leaf = 1,
                                max_features = 'sqrt',
                                max_depth = 30,
                                bootstrap = True)
print(rfr.fit(X_train, y_train))
y_pred= rfr.predict(X_test)
print(y_pred)

print("test_score", r2_score(y_test, y_pred))
print("train_score", rfr.score(X_train, y_train))
print("mae", mean_absolute_error(y_test, y_pred))
print("mse" , mean_squared_error(y_test, y_pred))
print("rmse", np.sqrt(mean_squared_error(y_test, y_pred)))
print("rmse_cv", np.sqrt(-cross_val_score(rfr, X_train, y_train, scoring='neg_mean_squared_error', cv=5).mean()))'''



# save the model to disk using pickle 
import pickle
filename = 'finalized_rfr.pkl'
pickle.dump(lasso, open(filename, 'wb'))

# load the model from disk
loaded_model = pickle.load(open(filename, 'rb'))
result = loaded_model.predict(X_test)
print(result)


# predict X_new
X_new = [[3,0,40,-73,1,1,10,0.10,6,365]]  
y_pred = lasso.predict(X_new)
print(y_pred)

# load the model from disk
loaded_model = pickle.load(open(filename, 'rb'))
result = loaded_model.predict(X_new)
print(result)