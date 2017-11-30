# Data Preprocessing Template

#IMPORT LIBRARIES
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#IMPORT THE DATASET
dataset = pd.read_csv("Data.csv")

#DEAL WITH MISSING VALUES (replacing with average in this case)
from sklearn.preprocessing import Imputer
imputer = Imputer(missing_values = "NaN", strategy = "mean", axis = 0)
imputer = imputer.fix(x[:, 1:3])
x[:, 1:3] = imputer.transform(x[:, 1:3])

#ASSIGN INDEPENDENT AND DEPENDANT VARIABLES TO X AND Y, RESPECTIVELY
x = dataset.iloc[:, :-1]
y = dataset.iloc[:, 3]

#SPLIT DATASET INTO TRAINING AND TEST DATA
from sklearn.cross_validation import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.2, random_state = 0)

#ENCODE CATEGORICAL DATA (if needed)
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
#switch nation names into integer values (e.g. France = 0, Germany = 1, Spain = 2)
label_encoder = LabelEncoder()
x:[:, 0] = label_encoder_x.fit_transform(x[:, 0])
#switch nation variable into three dummy variables, one for each nation
onehotencoder = OneHotEncoder()
x = onehotencoder.fit_transform(x).toarray()
#turn dependent variable into dummy variable
labelencoder_y = LabelEncoder()
y = labelencoder_y.fit_transform(y)

#FEATURE SCALING (if needed)
from sklearn.preprocessing import StandardScaler
sc_x = StandardScaler()
x_train = sc_x.fit_transform(x_train)
x_test = sc_x.transform(x_test)
