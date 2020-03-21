import os
import joblib
from sklearn.feature_extraction.text import CountVectorizer


def check_lines(lines):
    one_line_file = ''.join(lines)
    current_path = os.path.abspath(os.path.dirname(__file__))
    vocabulary_model_path = os.path.join(
        current_path, '../models/vocabulary.pkl')
    vocabulary = joblib.load(vocabulary_model_path)
    vectorizer = CountVectorizer(vocabulary=vocabulary)
    dtm = vectorizer.transform([one_line_file])
    dtm.toarray()
    viruses_model_path = os.path.join(
        current_path, '../models/viruses_model.pkl')
    clf = joblib.load(viruses_model_path)
    result = clf.predict(dtm)
    if result == 'ok':
        return True
    else:
        return False


def start_scanning():
    quarantine = f"{os.environ['HOME']}/quarantine"
    os.makedirs(quarantine, exist_ok=True)
    print("Type scan root folder")
    root = input()

    for path, subdirs, files in os.walk(root):
        for name in files:
            filename = os.path.join(path, name)
            with open(filename, 'r') as f:
                if not check_lines(f.readlines()):
                    f.close()
                    print(f"""Warning!! File {filename} has dengurous code!
                    Would you like to delete(1) or move to quarantine(2) file?""")
                    action = int(input())
                    if action == 1:
                        os.remove(filename)
                    elif action == 2:
                        os.rename(os.path.join(path, name),
                        os.path.join(quarantine, name))
                    else:
                        print("Unknown command")
