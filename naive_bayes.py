#-------------------------------------------------------------------------
# AUTHOR: Wan Suk Lim
# FILENAME: naive_bayes.py
# SPECIFICATION: Naive bayes
# FOR: CS 4210- Assignment #2
# TIME SPENT: 40 hrs
#-----------------------------------------------------------*/

#IMPORTANT NOTE: DO NOT USE ANY ADVANCED PYTHON LIBRARY TO COMPLETE THIS CODE SUCH AS numpy OR pandas. You have to work here only with standard vectors and arrays

#importing some Python libraries
from sklearn.naive_bayes import GaussianNB
import csv

db = []
dbTest = []
X = []
Y = []
A = []

#reading the training data
#--> add your Python code here
with open('weather_training.csv', 'r') as csvfile:
  reader = csv.reader(csvfile)
  for i, row in enumerate(reader):
      if i > 0: #skipping the header
         db.append (row)

#transform the original training features to numbers and add to the 4D array X. For instance Sunny = 1, Overcast = 2, Rain = 3, so X = [[3, 1, 1, 2], [1, 3, 2, 2], ...]]
#--> add your Python code here
# X =
a = int(1)
b = int(1)
c = int(1)
d = int(1)
dict = {}
if db:
    for i, row in enumerate(db):
        temp = []
        for j, ele in enumerate(row):
            #print("i: " ,i, " j: ", j)
            if j == 5:
                X.append(temp)
                continue
            if ele in dict:
                temp.append(dict[ele])
            else:
                if (j == 1):
                    dict[ele] = a
                    temp.append(dict[ele])
                    a = a + 1
                elif (j == 2):
                    dict[ele] = b
                    temp.append(dict[ele])
                    b = b + 1
                elif (j == 3):
                    dict[ele] = c
                    temp.append(dict[ele])
                    c = c + 1
                elif (j == 4):
                    dict[ele] = d
                    temp.append(dict[ele])
                    d = d + 1

#print("dict: ", dict)
#print("X: ", X)
#print("number of X: ", len(X))

#transform the original training classes to numbers and add to the vector Y. For instance Yes = 1, No = 2, so Y = [1, 1, 2, 2, ...]
#--> add your Python code here
# Y =
dictY = {"Yes": 1, "No": 2}
if db:
    for i, row in enumerate(db):
        Y.append(dictY[row[5]])

#fitting the naive bayes to the data
clf = GaussianNB()
clf.fit(X, Y)

#reading the data in a csv file
#--> add your Python code here
with open('weather_test.csv', 'r') as csvfile:
  reader = csv.reader(csvfile)
  for i, row in enumerate(reader):
      if i > 0: #skipping the header
         dbTest.append (row)

#print(dbTest)

if dbTest:
    for i, row in enumerate(dbTest):
        temp = []
        for j, ele in enumerate(row):
            #print("i: " ,i, " j: ", j)
            if j == 5:
                A.append(temp)
                continue
            if ele in dict:
                temp.append(dict[ele])


#print("dict: ", dict)
#print("A: ", A)
#print("number of A: ", len(A))

#printing the header os the solution
print ("Day".ljust(15) + "Outlook".ljust(15) + "Temperature".ljust(15) + "Humidity".ljust(15) + "Wind".ljust(15) + "PlayTennis".ljust(15) + "Confidence".ljust(15))

#use your test samples to make probabilistic predictions.
#--> add your Python code here
#-->predicted = clf.predict_proba([[3, 1, 2, 1]])[0]
predicted = clf.predict_proba(A)
#print("predicted: ", predicted)
if dbTest:
    for i, row in enumerate(dbTest):
        if predicted[i][0] >= 0.75:
            print (row[0].ljust(15) + row[1].ljust(15) + row[2].ljust(15) + row[3].ljust(15) + row[4].ljust(15) + "Yes".ljust(15) + str(predicted[i][0]).ljust(15))

        elif predicted[i][1] >= 0.75:
            print (row[0].ljust(15) + row[1].ljust(15) + row[2].ljust(15) + row[3].ljust(15) + row[4].ljust(15) + "No".ljust(15) + str(predicted[i][1]).ljust(15))

