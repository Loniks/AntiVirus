import os
from sklearn.externals import joblib
from sklearn.feature_extraction.text import CountVectorizer

def checkLines(lines):
    one_line_file = ''.join(lines)
    vocabulary = joblib.load('vocabulary.pkl')
    vectorizer = CountVectorizer(vocabulary=vocabulary)
    dtm = vectorizer.transform([one_line_file])
    dtm.toarray()
    clf = joblib.load('viruses_model.pkl')
    result = clf.predict(dtm)
    if result == 'ok':
        return True;
    else:
        return False;

quarantine = os.environ['HOME']+'\quarantine'

os.makedirs(quarantine, exist_ok=True)

print("Type scan root folder")

root = input()

for path, subdirs, files in os.walk(root):
    for name in files:
        filename = os.path.join(path, name)
        with open(filename, 'r') as f:
            if not checkLines(f.readlines()):
                f.close()
                print("Warning!! File {} has dengurous code! \n Would you like to delete(1) or move to quarantine(2) file?".format(filename))
                action = int(input())
                if action == 1:
                    os.remove(filename)
                elif action == 2:
                    os.rename(os.path.join(path, name),
                       os.path.join(quarantine, name))
                else:
                    print("Unknown command")
                    
                




