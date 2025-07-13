import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import pickle

# Load pima diabetes dataset from uci
url = "https://raw.githubusercontent.com/jbrownlee/Datasets/master/pima-indians-diabetes.data.csv"
columns = ["Pregnancies", "Glucose", "BloodPressure", "SkinThickness", "Insulin", 
           "BMI", "DiabetesPedigreeFunction", "Age", "Outcome"]
df = pd.read_csv(url, names=columns)
print(df.shape)
# print(df.columns)

# Selecting features and target
X = df.drop('Outcome',axis = 1)
y = df['Outcome']

# train model
clf = RandomForestClassifier()
clf.fit(X,y)

# save model
with open("model.pkl",'wb') as f:
    pickle.dump(clf,f)