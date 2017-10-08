import os
from sklearn.neighbors import KNeighborsClassifier
from sklearn.externals import joblib
from sklearn.feature_extraction.text import CountVectorizer
import json


X = []
y = []


cwd = os.getcwd()

train_viruses = cwd+'\db\\viruses'
train_normal = cwd+'\db\\normal_scripts'


for path, subdirs, files in os.walk(train_viruses):
    for name in files:
        filename = os.path.join(path, name)
        with open(filename, 'r') as f:
            one_line_file = ''.join(f.readlines())
            X.append(one_line_file)
            y.append('bad')
            f.close()

for path, subdirs, files in os.walk(train_normal):
    for name in files:
        filename = os.path.join(path, name)
        with open(filename, 'r') as f:
            one_line_file = ''.join(f.readlines())
            X.append(one_line_file)
            y.append('ok')
            f.close()



vect = CountVectorizer()
vect.fit(X)
simple_train_dtm = vect.transform(X)
simple_train_dtm.toarray()

knn = KNeighborsClassifier(n_neighbors=1)
knn.fit(simple_train_dtm, y)

joblib.dump(vect.vocabulary_, 'vocabulary.pkl')
joblib.dump(knn, 'viruses_model.pkl', compress=9)

