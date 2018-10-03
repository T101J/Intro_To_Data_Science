from sklearn import tree
from sklearn import svm
from sklearn.metrics import accuracy_score
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
import numpy as np 

# Data and Labels [height, weight, shoe_size], [male, female]
X = [[181, 80, 44], [177, 70, 43], [160, 60, 38], [154, 54, 37], [166, 65, 40],
     [190, 90, 47], [175, 64, 39],
     [177, 70, 40], [159, 55, 37], [171, 75, 42], [181, 85, 43]]

Y = ['male', 'male', 'female', 'female', 'male', 'male', 'female', 'female',
     'female', 'male', 'male']

#classifiers
clf1 = tree.DecisionTreeClassifier()
clf2 = svm.SVC()
clf3 = KNeighborsClassifier()
clf4 = GaussianNB()

#train the models
clf1 = clf1.fit(X,Y)
clf2 = clf2.fit(X,Y)
clf3 = clf3.fit(X,Y)
clf4 = clf4.fit(X,Y)
 
 #tests
pred1 = clf1.predict(X)
acc1 = accuracy_score(Y, pred1) * 100
print('Accuracy for DecisionTree: {}'.format(acc1))

pred2 = clf2.predict(X)
acc2 = accuracy_score(Y, pred2) * 100
print('Accuracy for SVM: {}'.format(acc2))

pred3 = clf3.predict(X)
acc3 = accuracy_score(Y, pred3) * 100
print('Accuracy for KNN: {}'.format(acc3))

pred4 = clf4.predict(X)
acc4 = accuracy_score(Y, pred4) * 100
print('Accuracy for GaussianNB: {}'.format(acc4))

#print the best result 
index = np.argmax([acc2, acc3, acc4])
classifiers = {0: 'SVM', 1: 'KNN', 2: 'GaussianNB'}
print('Best gender classifier is {}'.format(classifiers[index]))

#results
#Accuracy for DecisionTree: 100.0
#Accuracy for SVM: 100.0
#Accuracy for KNN: 72.72727272727273
#Accuracy for GaussianNB: 81.81818181818183
#Best gender classifier is SVM