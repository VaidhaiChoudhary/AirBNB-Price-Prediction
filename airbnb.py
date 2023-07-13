import pandas as pd

df = pd.read_csv(r"C:\Users\DELL\Downloads\AB_NYC_2019.csv")
'''print(df)
print(df.head(5))
print(df.columns)
print(df.shape)'''

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

# Which neighborhood_group has the most AirBnB?
#from matplotlib.pyplot as plt 
#print(df['neighbourhood_group'].value_counts().sort_index().plot.barh())

# Encoding neighbourhood_group
df["neighbourhood_group_label"] = df.neighbourhood_group.astype('category').cat.codes

# Neighbourhood Group and Label
neighbourhood_groups_and_labels = df[["neighbourhood_group","neighbourhood_group_label"]].sort_values("neighbourhood_group_label").drop_duplicates() 
neighbourhood_groups_and_labels = tuple(zip(neighbourhood_groups_and_labels.iloc[:,1], 
                                            neighbourhood_groups_and_labels.iloc[:,0]))

print(neighbourhood_groups_and_labels)

# Encoding (neigh.grp=5, neigh.=221, roomtype=3)
categorical_feature_mask = df.dtypes==object
categorical_cols = df.columns[categorical_feature_mask].tolist()
df.drop(columns=["neighbourhood_group_label"], inplace=True)
for column in df[categorical_cols]:
    df[column] = df[column].astype('category').cat.codes

last_col = df.pop('price')
df.insert(len(df.columns), 'price', last_col)
print(df.head(5))

#99% of target variable(price) betweem 0-800 hence removing other 1% outiers
import numpy as np
print(np.quantile(df.price, 0.99))
df = df[df.price <= 800]

from sklearn.model_selection import train_test_split
X, y = df.iloc[:,:-1], df.iloc[:,-1]
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2, random_state=42) # train-test split of 80-20

print(X_train.shape)
print(X_test.shape)
print(y_train.shape)
print(y_test.shape)

# Feature scaling
# Standardizing
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
train_scaled = scaler.fit_transform(X_train)
test_scaled = scaler.transform(X_test)


# LINEAR REGRESSION
from sklearn.linear_model import LinearRegression
model = LinearRegression()
print(model.fit(train_scaled, y_train))

#Accuracy
print(model.score(X_test, y_test))

# Evaluation
from sklearn.metrics import mean_squared_error
from sklearn.metrics import mean_absolute_error
from math import sqrt

# for train set
mse = mean_squared_error(y_train, model.predict(train_scaled))
mae = mean_absolute_error(y_train, model.predict(train_scaled))
print("mse = ",mse," & mae = ",mae," & rmse = ", sqrt(mse))

# for test set
test_mse = mean_squared_error(y_test, model.predict(test_scaled))
test_mae = mean_absolute_error(y_test, model.predict(test_scaled))
print("mse = ",test_mse," & mae = ",test_mae," & rmse = ", sqrt(test_mse))

# predict = model.predict(X_train)
import numpy as np
#import matplotlib.pyplot as plt
#import seaborn as sns
#matplotlib inline
predictions = model.predict( X_test)
#plt.scatter(y_test,predictions)
#plt.xlabel('Y Test')
#plt.ylabel('Predicted Y')

# predict
y_pred=model.predict(X_test)
print(y_pred)



'''# LOGISTIC REGRESSION
def accuracy(y_true,y_pred):
  accuracy = np.sum(y_true == y_pred)/len(y_true)
  return accuracy

from sklearn.linear_model import LogisticRegression
model = LogisticRegression(random_state=70)
print(model.fit(train_scaled, y_train))

predictions = model.predict(X_test)
y_pred=model.predict(X_test)
print(y_pred)

print(mse = metrics.mean_squared_error(y_test, y_pred))
#print("Accuracy: ",accuracy(y_test, predictions))
from sklearn.metrics import accuracy_score
print ("Accuracy : ", accuracy_score(y_test, y_pred))'''
 

'''# DECISION TREE
# import the regressor
from sklearn.tree import DecisionTreeRegressor 
model = DecisionTreeRegressor(random_state = 0)  
print(model.fit(train_scaled, y_train))

predictions = model.predict(X_test)
y_pred=model.predict(X_test)
print(y_pred)
  
print(mse = metrics.mean_squared_error(y_test, y_pred))
# Calculate the accuracy of the model
print(model.score(X_test, y_test))'''



'''# RANDOM FOREST
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, r2_score, mean_squared_error, mean_squared_log_error # metrics
np.random.seed(0)
model = RandomForestRegressor(n_estimators=100, random_state=0)
print(model.fit(train_scaled, y_train))
y_predTrain = model.predict(X_train)
y_pred = model.predict(X_test)

print("RMSE prediction on train = {0}".format(np.sqrt(mean_squared_error(y_predTrain, y_train))))
print("R2 Score prediciton on train = {0}".format(r2_score(y_train,y_predTrain)))

print("\nRMSE prediction on test = {0}".format(np.sqrt(mean_squared_error(y_pred, y_test))))
print("R2 Score prediciton on test = {0}".format(r2_score(y_test,y_pred)))

#from sklearn.metrics import accuracy_score
#print ("Accuracy : ", accuracy_score(y_test, y_pred))'''


'''# K NEAREST NEIGHBOUR
from sklearn.neighbors import KNeighborsRegressor
model = KNeighborsRegressor(n_neighbors=7)
  
print(model.fit(train_scaled, y_train))
predictions = model.predict(X_test)
y_pred=model.predict(X_test)
print(y_pred)
  
print(mse = metrics.mean_squared_error(y_test, y_pred))
# Calculate the accuracy of the model
print(model.score(X_test, y_test))'''


# save the model to disk using pickle 
import pickle
filename = 'airbnb_model.pkl'
pickle.dump(model, open(filename, 'wb'))

# load the model from disk
loaded_model = pickle.load(open(filename, 'rb'))
result = loaded_model.predict(X_test)
print(result)

# predict X_new
X_new = [[3,0,40,-73,1,1,10,0.10,6,365]]  
y_pred = model.predict(X_new)
print(y_pred)

# load the model from disk
loaded_model = pickle.load(open(filename, 'rb'))
result = loaded_model.predict(X_new)
print(result)





