# -*- coding: utf-8 -*-
"""DS Diabetes Prediction.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1joUjmRUGIHRk1ZVypKfc8td4BCB3Ot4n

**Data Science  Final Project**
---


**STD Name**:Mohammed Yehia Ashour
<br>
**STD ID**:1301195595

---

Project Link [Github](https://github.com/Moudyash/preprocessing_and_visualization)
<br>
Drive Download link
[DataSet ](https://drive.google.com/file/d/1t00znmEsiPkrUWZ2L1UjZeZL_ImHZD_l/view?usp=share_link)
<br>
Mediafire Download link
[DataSet ](https://www.mediafire.com/file/j45l7bz7tkyxkm0/diabetes.csv/file)
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.graph_objects as go

print('''


██████╗░██████╗░███████╗██████╗░██████╗░░█████╗░░█████╗░███████╗░██████╗░██████╗██╗███╗░░██╗░██████╗░
██╔══██╗██╔══██╗██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝██║████╗░██║██╔════╝░
██████╔╝██████╔╝█████╗░░██████╔╝██████╔╝██║░░██║██║░░╚═╝█████╗░░╚█████╗░╚█████╗░██║██╔██╗██║██║░░██╗░
██╔═══╝░██╔══██╗██╔══╝░░██╔═══╝░██╔══██╗██║░░██║██║░░██╗██╔══╝░░░╚═══██╗░╚═══██╗██║██║╚████║██║░░╚██╗
██║░░░░░██║░░██║███████╗██║░░░░░██║░░██║╚█████╔╝╚█████╔╝███████╗██████╔╝██████╔╝██║██║░╚███║╚██████╔╝
╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═╝░░░░░╚═╝░░╚═╝░╚════╝░░╚════╝░╚══════╝╚═════╝░╚═════╝░╚═╝╚═╝░░╚══╝░╚═════╝░
''')

# Load the dataset
data = pd.read_csv(r"C:\Users\Medo\Desktop\Diabetes Prediction\diabetes.csv")

data.head().T.style.set_properties(**{'background-color': 'grey',
                           'color': 'white',
                           'border-color': 'white'})

"""**Data Dictionary**

---


      Columns         	Description


---


    Pregnancies: 	  To express the Number of pregnancies
    Glucose: 	      To express the Glucose level in blood
    BloodPressure: 	To express the Blood pressure measurement
    SkinThickness: 	To express the thickness of the skin
    Insulin:       	To express the Insulin level in blood
    BMI: 	          To express the Body mass index
    DiabetesPedigreeFunction: 	To express the Diabetes percentage
    Age: 	          To express the age
    Outcome:       	To express the final result 1 is Yes and 0 is No

# *** Preprocessing  Section***:

Check null value counts
"""

data.isnull().sum()

"""

Check duplicated data
"""

#Check if Glucose contains a zero value 
data.Glucose.unique()

"""The glucose value cannot be zero, so replacing the zero values with the mean of the glucose column

"""

data.Glucose=data.Glucose.replace(0,int(data.Glucose.mean()))
int(data.Glucose.mean())

#Check if BloodPressure contains a zero value 
data.BloodPressure.unique()

"""
Filling the zero values with the median( Blood pressure column)



"""

data.BloodPressure.replace(0,int(data.BloodPressure.mean()))
int(data.BloodPressure.mean())

#Check if SkinThickness contains a zero value 

data.SkinThickness.unique()

"""Filling the zero values with the median( SkinThickness column)


"""

data.SkinThickness.replace(0,int(data.SkinThickness.mean()))
int(data.SkinThickness.mean())

#Check if Insulin contains a zero value 

data.Insulin.unique()

"""Filling the zero values with the median( Insulin column)


"""

data.Insulin.replace(0,int(data.Insulin.mean()))
int(data.Insulin.mean())

#Check if BMI contains a zero value 

data.BMI.unique()

"""#Filling the zero values with the min( BMI column)


"""

data.BMI.replace(0,data.BMI.mean(),inplace=True)
data.BMI.mean()

#Check if DiabetesPedigreeFunction contains a zero value 
data.DiabetesPedigreeFunction.unique()

#Check if Age contains a zero value 

data.Age.unique()

"""#Check if data contains a zero value 

"""

checkNullData=data.drop("Outcome", axis=1)
print(checkNullData.isnull().sum())
checkNullData.isnull().head()

"""   # *** Visualization Section***:"""

print('''

██╗░░░██╗██╗░██████╗██╗░░░██╗░█████╗░██╗░░░░░██╗███████╗░█████╗░████████╗██╗░█████╗░███╗░░██╗
██║░░░██║██║██╔════╝██║░░░██║██╔══██╗██║░░░░░██║╚════██║██╔══██╗╚══██╔══╝██║██╔══██╗████╗░██║
╚██╗░██╔╝██║╚█████╗░██║░░░██║███████║██║░░░░░██║░░███╔═╝███████║░░░██║░░░██║██║░░██║██╔██╗██║
░╚████╔╝░██║░╚═══██╗██║░░░██║██╔══██║██║░░░░░██║██╔══╝░░██╔══██║░░░██║░░░██║██║░░██║██║╚████║
░░╚██╔╝░░██║██████╔╝╚██████╔╝██║░░██║███████╗██║███████╗██║░░██║░░░██║░░░██║╚█████╔╝██║░╚███║
░░░╚═╝░░░╚═╝╚═════╝░░╚═════╝░╚═╝░░╚═╝╚══════╝╚═╝╚══════╝╚═╝░░╚═╝░░░╚═╝░░░╚═╝░╚════╝░╚═╝░░╚══╝''')

import matplotlib.pyplot as plt
from plotly.subplots import make_subplots
import plotly.graph_objects as go

def bool_pie_chart(data):

    fig = make_subplots(rows=2, cols=4, specs = [[{'type': 'domain'}, {'type': 'domain'}, {'type': 'domain'}, {'type': 'domain'}],
         [{'type': 'domain'}, {'type': 'domain'}, {'type': 'domain'}, {'type': 'domain'}]])
     
    labels = ["Yes","No"]

    values = data['Pregnancies'].value_counts().values
    fig.add_trace(go.Pie(labels=labels, values=values, name="Pregnancies", title="Pregnancies"),1, 1)
    
    values = data['Glucose'].value_counts().values
    fig.add_trace(go.Pie(labels=labels, values=values, name="Glucose", title="Glucose"),1, 2)
               
    values = data['BloodPressure'].value_counts().values
    fig.add_trace(go.Pie(labels=labels, values=values, name="BloodPressure", title="BloodPressure"),1, 3)    
        
    values = data['SkinThickness'].value_counts().values
    fig.add_trace(go.Pie(labels=labels, values=values, name="SkinThickness", title="SkinThickness"),1, 4)    
                
    values = data['Insulin'].value_counts().values
    fig.add_trace(go.Pie(labels=labels, values=values, name="Insulin", title="Insulin"),2, 1)    

    values = data['BMI'].value_counts().values
    fig.add_trace(go.Pie(labels=labels, values=values, name="BMI", title="BMI"),2, 2)    
    values = data['DiabetesPedigreeFunction'].value_counts().values
    fig.add_trace(go.Pie(labels=labels, values=values, name="DiabetesPedigreeFunction", title="DPF"),2, 3)    
    values = data['Age'].value_counts().values
    fig.add_trace(go.Pie(labels=labels, values=values, name="Age", title="Age"),2, 4)    
          
    fig.update_traces(hole=.55, hoverinfo="label+percent+name")

    fig.update_layout(title_text="Boolean feature evalutation")
    fig.show()

bool_pie_chart(data)

data.hist(figsize=(10,10))
plt.show()

import plotly.express as px
fig = px.scatter(data, x=data.BloodPressure, y=data.Glucose, color=data.Glucose, title="BloodPressure & Glucose'")
fig.show()

def num_distplot(df, x=None, width=8, height=6):
    plt.figure(figsize=(width,height))
    sns.distplot(df[x], rug=True, hist=True)
    plt.title(x)
    plt.show()
    
num_distplot(data,"Outcome")

sns.pairplot(data)

plt.figure(figsize=(10,6))

#sns.lmplot(data=data, x='CGPA', y='Chance of Admit',hue="Research"
# Create the plot
ax = sns.lmplot(data=data, x='Glucose', y='BMI', hue='Outcome', scatter_kws={'alpha': 0.5}, line_kws={'linewidth': 2})

# Add a title
plt.suptitle('Relationship between Glucose and BMI of Admit')
# Label the axes

plt.xlabel('Glucose')
plt.ylabel('BMI')

sns.scatterplot(x='Pregnancies', y='Glucose', data=data,hue="BloodPressure",color='purple', size=10)
plt.show()

plt.figure(figsize=(16,10))
sns.countplot("Pregnancies",data=data)

plt.figure(figsize=(16,10))
sns.countplot("Pregnancies",data=data,hue="Outcome")

#this code will reduction the age data to 4 groups (20-30||30-50||50-70||70-90)
age=pd.cut(data["Age"],bins=[20,30,50,70,90],labels=["Age(20-30)","Age(30-50)","Age(50-70)","Age(70-90)"])

plt.figure(figsize=(10,10))
sns.countplot(age,hue=data["Outcome"])

"""   # *** predictive modelling  Section***:"""

print('''

██████╗░██████╗░███████╗██████╗░██╗░█████╗░████████╗██╗██╗░░░██╗███████╗
██╔══██╗██╔══██╗██╔════╝██╔══██╗██║██╔══██╗╚══██╔══╝██║██║░░░██║██╔════╝
██████╔╝██████╔╝█████╗░░██║░░██║██║██║░░╚═╝░░░██║░░░██║╚██╗░██╔╝█████╗░░
██╔═══╝░██╔══██╗██╔══╝░░██║░░██║██║██║░░██╗░░░██║░░░██║░╚████╔╝░██╔══╝░░
██║░░░░░██║░░██║███████╗██████╔╝██║╚█████╔╝░░░██║░░░██║░░╚██╔╝░░███████╗
╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═╝░╚════╝░░░░╚═╝░░░╚═╝░░░╚═╝░░░╚══════╝

███╗░░░███╗░█████╗░██████╗░███████╗██╗░░░░░██╗░░░░░██╗███╗░░██╗░██████╗░
████╗░████║██╔══██╗██╔══██╗██╔════╝██║░░░░░██║░░░░░██║████╗░██║██╔════╝░
██╔████╔██║██║░░██║██║░░██║█████╗░░██║░░░░░██║░░░░░██║██╔██╗██║██║░░██╗░
██║╚██╔╝██║██║░░██║██║░░██║██╔══╝░░██║░░░░░██║░░░░░██║██║╚████║██║░░╚██╗
██║░╚═╝░██║╚█████╔╝██████╔╝███████╗███████╗███████╗██║██║░╚███║╚██████╔╝
╚═╝░░░░░╚═╝░╚════╝░╚═════╝░╚══════╝╚══════╝╚══════╝╚═╝╚═╝░░╚══╝░╚═════╝░
''')

"""#CLASSIFICATION

# **KNeighbors**
"""

X = data.drop('Outcome', axis=1)
y = data['Outcome']
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30)
from sklearn.neighbors import KNeighborsClassifier
classifier = KNeighborsClassifier(n_neighbors=24)
classifier.fit(X_train, y_train)
y_pred = classifier.predict(X_test)
from sklearn.metrics import classification_report, confusion_matrix ,accuracy_score
print(accuracy_score(y_test, y_pred))
print(confusion_matrix(y_test, y_pred))
print(classification_report(y_test, y_pred))

for i in range(1, 50):
    knn = KNeighborsClassifier(n_neighbors=i)
    knn.fit(X_train, y_train)
    pred_i = knn.predict(X_test)
    print(i," " ,accuracy_score(y_test,pred_i))

"""# **DecisionTree**"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
dataset = data
dataset.head()
X = dataset.drop('Outcome', axis=1)
y = dataset['Outcome']
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20)
from sklearn.tree import DecisionTreeClassifier
classifier = DecisionTreeClassifier()
classifier.fit(X_train, y_train)
y_pred = classifier.predict(X_test)
from sklearn.metrics import classification_report, confusion_matrix ,accuracy_score
print(accuracy_score(y_test, y_pred))

print(confusion_matrix(y_test, y_pred))
print(classification_report(y_test, y_pred))

"""# **GaussianNB**"""

import pandas as pd
import numpy as np

dataset = data
dataset.head()
X = dataset.drop('Outcome', axis=1)
y = dataset['Outcome']
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30)
from sklearn.naive_bayes import GaussianNB
GNB = GaussianNB().fit(X_train, y_train)

y_pred = GNB.predict(X_test)
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
print(accuracy_score(y_test, y_pred))

print(confusion_matrix(y_test, y_pred))
print(classification_report(y_test, y_pred))

"""#CLUSTERING"""

import pandas as pd
import numpy as np

dataset = data
dataset.head()
X = dataset.drop('Outcome', axis=1)
y = dataset['Outcome']

from sklearn.cluster import KMeans
kmeans=KMeans(2).fit(X)
y_pred=kmeans.predict(X)
y_pred

from sklearn.metrics import cluster
contingency_matrix=cluster.contingency_matrix(y, y_pred)
contingency_matrix

np.sum(np.amax(contingency_matrix,axis=0))/np.sum(contingency_matrix)

print(cluster.adjusted_rand_score(y,y_pred))
print(cluster.normalized_mutual_info_score(y,y_pred))

from scipy.cluster.hierarchy import dendrogram,linkage
from matplotlib import pyplot as plt

# linked= linkage(x,'single')
# linked= linkage(x,'complete')
# linked= linkage(x,'average')
linked= linkage(X,'ward')
labelist=range(1,151)

#plt.figure(figsize=(125,20))
#plt
#dendrogram(linked,orientation='top',labels=labelist,distance_sort='descending')
#ax=plt.gca()
#ax.tick_params(axis='x',which='major',labelsize=15)
#plt.show()

Pregnancies = int(input ("Enter Pregnancies :"))
Glucose = int(input ("Enter Glucose :"))
BloodPressure = int(input ("Enter BloodPressure :"))
SkinThickness = int(input ("Enter SkinThickness :"))
Insulin = int(input ("Enter Insulin :"))
BMI = float(input ("Enter BMI :"))
DiabetesPedigreeFunction = float(input ("Enter DiabetesPedigreeFunction :"))
Age = int(input ("Enter Age :"))
def final_model(Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,DiabetesPedigreeFunction,BMI,Age):
  predict_dataset=dataset
  A = predict_dataset.drop('Outcome', axis=1)
  B = predict_dataset['Outcome']
  from sklearn.model_selection import train_test_split
  A_train, A_test, B_train, B_test = train_test_split(A, B, test_size=0.30)

  from sklearn.linear_model import LogisticRegression
  model = LogisticRegression()
  model.fit(A_train, B_train)
  y_predict = model.predict(A_test)
  y_predict = model.predict([[Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,DiabetesPedigreeFunction,BMI,Age]])
  print(y_predict)

  if y_predict==1:
      print("Diabetic")
  else:
      print("Non Diabetic")



final_model(Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,DiabetesPedigreeFunction,BMI,Age)