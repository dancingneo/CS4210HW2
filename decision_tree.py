#-------------------------------------------------------------------------
# AUTHOR: Wan Suk Lim
# FILENAME: decision_tree.py
# SPECIFICATION: decision tree
# FOR: CS 4210- Assignment #2
# TIME SPENT: 30 hrs
#-----------------------------------------------------------*/

#IMPORTANT NOTE: DO NOT USE ANY ADVANCED PYTHON LIBRARY TO COMPLETE THIS CODE SUCH AS numpy OR pandas. You have to work here only with standard vectors and arrays

#importing some Python libraries
from sklearn import tree
import csv

dataSets = ['contact_lens_training_1.csv', 'contact_lens_training_2.csv', 'contact_lens_training_3.csv']
testSets = ['contact_lens_test.csv']

for ds in dataSets:

    dbTraining = []
    X = []
    Y = []

    #reading the training data in a csv file
    with open(ds, 'r') as csvfile:
         reader = csv.reader(csvfile)
         for i, row in enumerate(reader):
             if i > 0: #skipping the header
                dbTraining.append (row)

    #transform the original training features to numbers and add to the 4D array X. For instance Young = 1, Prepresbyopic = 2, Presbyopic = 3, so X = [[1, 1, 1, 1], [2, 2, 2, 2], ...]]
    #--> add your Python code here

    a = int(1)
    b = int(1)
    c = int(1)
    d = int(1)
    dict = {}
    if dbTraining:
        for i, row in enumerate(dbTraining):
            temp = []
            for j, ele in enumerate(row):
                #print("i: " ,i, " j: ", j)
                if j == 4:
                    X.append(temp)
                    continue
                if ele in dict:
                    temp.append(dict[ele])
                else:
                    if (j == 0):
                        dict[ele] = a
                        temp.append(dict[ele])
                        a = a + 1
                    elif (j == 1):
                        dict[ele] = b
                        temp.append(dict[ele])
                        b = b + 1
                    elif (j == 2):
                        dict[ele] = c
                        temp.append(dict[ele])
                        c = c + 1
                    elif (j == 3):
                        dict[ele] = d
                        temp.append(dict[ele])
                        d = d + 1

    #print("dict: ", dict)
    #print("X: ", X)
    #print("number of X: ", len(X))

    #transform the original training classes to numbers and add to the vector Y. For instance Yes = 1, No = 2, so Y = [1, 1, 2, 2, ...]
    #--> add your Python code here

    dictY = {"Yes": 1, "No": 2}
    if dbTraining:
        for i, row in enumerate(dbTraining):
            Y.append(dictY[row[4]])

    #print("Y: ", Y)

    lowest_accuracy = int (1)
    #loop your training and test tasks 10 times here
    for i in range (10):
    #for i in range(1): #change

       #fitting the decision tree to the data setting max_depth=3
       clf = tree.DecisionTreeClassifier(criterion = 'entropy', max_depth=3)
       clf = clf.fit(X, Y)

       #read the test data and add this data to dbTest
       #--> add your Python code here
       dbTest = []

       for ts in testSets:
           # reading the training data in a csv file
           with open(ts, 'r') as csvfile:
               reader = csv.reader(csvfile)
               for i, row in enumerate(reader):
                   if i > 0:  # skipping the header
                       dbTest.append(row)

       #print("dbTest: ", dbTest)
       #for data in dbTest:
       # transform the features of the test instances to numbers following the same strategy done during training, and then use the decision tree to make the class prediction. For instance:
       A = []
       B = []
       if dbTest:
           for i, row in enumerate(dbTest):
               temp = []
               for j, ele in enumerate(row):
                   # print("i: " ,i, " j: ", j)
                   if j == 4:
                       A.append(temp)
                       continue
                   if ele in dict:
                       temp.append(dict[ele])

       #print(dict)
       #print("A: ", A)
       #print("number of A: ", len(A))

       # transform the original testing classes to numbers and add to the vector B. For instance Yes = 1, No = 2, so B = [1, 1, 2, 2, ...]
       # --> add your Python code here
       if dbTest:
           for row in dbTest:
               B.append(dictY[row[4]])

       #print("B: ", B)
       #transform the features of the test instances to numbers following the same strategy done during training, and then use the decision tree to make the class prediction. For instance:
       #class_predicted = clf.predict([[3, 1, 2, 1]])[0]           -> [0] is used to get an integer as the predicted class label so that you can compare it with the true label
       #--> add your Python code here
       # fitting the decision tree to the data setting max_depth=3
       class_predicted = []
       for row in A:
           class_predicted.append(clf.predict([row])[0])

       #print("class_predicted:\n", class_predicted)

       #compare the prediction with the true label (located at data[4]) of the test instance to start calculating the accuracy.
       #--> add your Python code here
       #print("the true label:\n", B)
       ad = 0
       for i, row in enumerate(class_predicted):
           #print("class_predicted[i]: ", class_predicted[i], "B: ", B[i])
           if class_predicted[i] == B[i]:
               ad = ad + 1

       #print("ad: ", ad, "len(B): ", len(B))
       accuracy = ad / len(B)

       #print("Accuracy: ", accuracy)

        #find the lowest accuracy of this model during the 10 runs (training and test set)
        #--> add your Python code here
       if accuracy < lowest_accuracy:
           lowest_accuracy = accuracy

    #print the lowest accuracy of this model during the 10 runs (training and test set) and save it.
    #your output should be something like that: final accuracy when training on contact_lens_training_1.csv: 0.2
    #--> add your Python code here
    print("final accuracy when training on", ds, ": ", lowest_accuracy)




