"""
Create by Killer at 2019-05-08 14:18
"""

import pandas
import numpy

# Read the data
data = pandas.read_csv("data.csv")

# Split the data into X(intput) and y(label)
X = numpy.array(data[['x1', 'x2']])

y = numpy.array(data['y'])

# import statements for the classification algorithms
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC

# TODO: Pick an algorithm from the list:
# - Logistic Regreasion
classifier = LogisticRegression(solver='lbfgs')

classifier.fit(X, y)

# - Decision Trees
tree = DecisionTreeClassifier()
tree.fit(X, y)


# - Support Vector Machines
svm_ = SVC(kernel="rbf", gamma=200)
svm_.fit(X, y)

# Define a classifier(bonus: Specify some paramenter!)
# and use it to fit the data, make sure you name the variable as "classifier"

# Click on 'Test Run' to see how algorithm fit the data