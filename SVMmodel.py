import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn import svm
from sklearn.metrics import accuracy_score
import pickle
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#++++++                    Coded BY : Ahmed Hassan                                ++++++ 
#++++++                             : Abdelrhman Yasser                           ++++++ 
#++++++                             : Mahmoud Rabea                               ++++++ 
#++++++                             : Misara Ahmed                                ++++++                                         
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#Read Data From CSV File 
df = pd.read_csv("diabetes.csv")
#Data cleaning from nonlogic values
for i in range(len(df['Insulin'])):
  if df['Insulin'][i] == 0:
        df['Insulin'][i] = df['Insulin'].mean()
  if df['BloodPressure'][i]<60:
    df['BloodPressure'][i] = df['BloodPressure'].mean()
  if df['SkinThickness'][i] < 3.3:
    df['SkinThickness'][i]=df['SkinThickness'].mean()
#Set X as features of our model and Y as the prediction of the model
X = df.drop(columns = 'Outcome', axis=1)
Y = df['Outcome']
#X_test = dg.drop(columns = 'Outcome', axis=1)
#Y_test = dg['Outcome']
#Split data to train set and test set
X_train, X_test, Y_train, Y_test = train_test_split(X,Y, test_size = 0.2, stratify=Y, random_state=2)
#print(X.shape, X_train.shape, X_test.shape)
classifier = svm.SVC(kernel='linear')

#training the support vector Machine Classifier
classifier.fit(X_train, Y_train)

# accuracy score on the training data
X_train_prediction = classifier.predict(X_train)
training_data_accuracy = accuracy_score(X_train_prediction, Y_train)

print('Accuracy score of the training data : ', training_data_accuracy)

# accuracy score on the test data
X_test_prediction = classifier.predict(X_test)
test_data_accuracy = accuracy_score(X_test_prediction, Y_test)

print('Accuracy score of the test data : ', test_data_accuracy)

input_data =[]
data_type =[
"Pregnancies",	"Glucose","BloodPressure","SkinThickness","Insulin","BMI","DiabetesPedigreeFunction","Age"]
#Take data from user if you want to predict
for i in range(0,8):
  x=float(input("Enter Paitent"+data_type[i]+":"))
  input_data.append(x)
# changing the input_data to numpy array
input_data_as_numpy_array = np.asarray(input_data)

# reshape the array as we are predicting for one instance
input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)
prediction = classifier.predict(input_data_reshaped)
print(prediction)
#Saving the model to sav file
#pickle.dump(classifier,open('final_model.sav','wb'))
if (prediction[0] == 0):
  print('The person is not diabetic')
else:
  print('The person is diabetic')