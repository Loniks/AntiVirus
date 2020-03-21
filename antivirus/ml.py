import os
import joblib
from sklearn.neighbors import KNeighborsClassifier
from sklearn.feature_extraction.text import CountVectorizer


def build_model():
    features = []
    labels = []

    # fill data in futures and labels
    current_path = os.path.abspath(os.path.dirname(__file__))
    good_resource_path = os.path.join(current_path, 'resources/db/viruses')
    get_data(good_resource_path, features, labels, False)
    bad_resource_path = os.path.join(
        current_path, 'resources/db/normal_scripts'
        )
    get_data(bad_resource_path, features, labels)
    # build vocabulary
    vect = CountVectorizer()
    vect.fit(features)
    simple_train_dtm = vect.transform(features)
    simple_train_dtm.toarray()
    # build clasifier
    knn = KNeighborsClassifier(n_neighbors=1)
    knn.fit(simple_train_dtm, labels)
    # store models
    vector_model_path = os.path.join(current_path, '../models/vocabulary.pkl')
    joblib.dump(vect.vocabulary_, vector_model_path)
    viruses_model_path = os.path.join(
        current_path, '../models/viruses_model.pkl')
    joblib.dump(knn, viruses_model_path, compress=9)


def get_data(folder_path, features, labels, is_ok=True):
    for path, subdirs, files in os.walk(folder_path):
        for name in files:
            filename = os.path.join(path, name)
            with open(filename, 'r') as f:
                one_line_file = ''.join(f.readlines())
                features.append(one_line_file)
                if is_ok:
                    labels.append('ok')
                else:
                    labels.append('bad')
                f.close()
