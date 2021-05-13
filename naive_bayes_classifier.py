import pickle

import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
import numpy as np
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix, roc_curve
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB

data = pd.read_csv('./spam_ham_dataset.csv')

# dropping the ID column as it is of no use in analysis
data.drop('Unnamed: 0', axis=1, inplace=True)

vectorizer = CountVectorizer()
spam_ham = vectorizer.fit_transform(data['text'])

X = spam_ham
Y = data['label'].values

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)
NB_classifier = MultinomialNB()
NB_classifier.fit(X_train, Y_train)

Y_pred_train = NB_classifier.predict(X_train)
Y_pred_test = NB_classifier.predict(X_test)

print(X_train.shape)
print(X_test[0])

cm_test = confusion_matrix(Y_test, Y_pred_test)
cm_train = confusion_matrix(Y_train, Y_pred_train)

accuracy_score(Y_test, Y_pred_test)
print(classification_report(Y_pred_test, Y_test))

# ----Uncomment this code to Save the Model
# save the model to disk
# filename = 'NB_spam_model.pkl'
# pickle.dump(NB_classifier, open(filename, 'wb'))
