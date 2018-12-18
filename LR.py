import pandas as pd
import numpy as np
from sklearn import preprocessing
import matplotlib.pyplot as plt
plt.rc("font", size=14)
from sklearn.linear_model import LogisticRegression
from sklearn.cross_validation import train_test_split
import seaborn as sns
from sklearn import metrics
sns.set(style="white")
sns.set(style="whitegrid", color_codes=True)

data = pd.read_csv('project_data/SimulatedLRData.txt', header=0)
print(data)
print(type(data))
print(data.shape)
print(list(data.columns))
X = data.loc[:, data.columns != 'Label']
y = data.loc[:, data.columns == 'Label']
print(X)
print(y)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)
print(X_test)
print(y_test)

LR = LogisticRegression()
LR.fit(X_train, y_train)
predict = LR.predict(X_test)
score = LR.score(X_test, y_test)
print(score)
cm = metrics.confusion_matrix(y_test, predict)
print(cm)


from sklearn.metrics import roc_auc_score
from sklearn.metrics import roc_curve
logit_roc_auc = roc_auc_score(y_test, LR.predict(X_test))
fpr, tpr, thresholds = roc_curve(y_test, LR.predict_proba(X_test)[:,1])
plt.figure()
plt.plot(fpr, tpr, label='Logistic Regression (area = %0.2f)' % logit_roc_auc)
plt.plot([0, 1], [0, 1],'r--')
plt.xlim([0.0, 1.0])
plt.ylim([0.0, 1.05])
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('Receiver operating characteristic')
plt.legend(loc="lower right")
plt.savefig('Log_ROC')
plt.show()
