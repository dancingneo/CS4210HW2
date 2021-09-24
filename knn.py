#-------------------------------------------------------------------------
# AUTHOR: Wan Suk Lim
# FILENAME: knn.py
# SPECIFICATION: knn
# FOR: CS 4210- Assignment #2
# TIME SPENT: 30 hrs
#-----------------------------------------------------------*/

#IMPORTANT NOTE: DO NOT USE ANY ADVANCED PYTHON LIBRARY TO COMPLETE THIS CODE SUCH AS numpy OR pandas. You have to work here only with standard vectors and arrays

#importing some Python libraries
from sklearn.neighbors import KNeighborsClassifier
import csv

db = []
er = 0
totalRow = 0

#reading the data in a csv file
with open('binary_points.csv', 'r') as csvfile:
  reader = csv.reader(csvfile)
  for i, row in enumerate(reader):
      if i > 0: #skipping the header
         db.append (row)


#loop your data to allow each instance to be your test set
for i, instance in enumerate(db):

    #add the training features to the 2D array X removing the instance that will be used for testing in this iteration. For instance, X = [[1, 3], [2, 1,], ...]]. Convert each feature value to
    # float to avoid warning messages
    #--> add your Python code here
    X = []
    #print(i, instance)
    for j, row in enumerate(db):
        temp = []
        if j == i:
            continue
        X.append([float(f) for f in row[:2]])

    #print("X: ", X)

    #transform the original training classes to numbers and add to the vector Y removing the instance that will be used for testing in this iteration. For instance, Y = [1, 2, ,...]. Convert each
    #  feature value to float to avoid warning messages
    #--> add your Python code here
    Y = []
    dictY = {"+": 1, "-": 2}

    for j, row in enumerate(db):
        if j == i:
            continue
        Y.append(dictY[row[2]])

    #print("Y: ", Y)

    #store the test sample of this iteration in the vector testSample
    #--> add your Python code here
    testSample = []
    testSample.append([float(f) for f in instance[:2]])

    #fitting the knn to the data
    clf = KNeighborsClassifier(n_neighbors=1, p=2)
    clf = clf.fit(X, Y)

    #use your test sample in this iteration to make the class prediction. For instance:
    #class_predicted = clf.predict([[1, 2]])[0]
    #--> add your Python code here
    class_predicted = clf.predict(testSample)[0]

    #print("class_predicted: ", class_predicted)

    #compare the prediction with the true label of the test instance to start calculating the error rate.
    #--> add your Python code here
    if class_predicted != dictY[instance[2]]:
        er = er + 1

    totalRow = totalRow + 1
    #print("er: ", er, " totalRow: ", totalRow)

#print the error rate
#--> add your Python code here
error_rate = er / totalRow
print("error rate: ", error_rate)





