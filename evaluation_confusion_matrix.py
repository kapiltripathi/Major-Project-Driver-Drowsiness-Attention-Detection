import pandas as pd
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score
from sklearn.metrics import classification_report
import numpy

CSVFILE='c3.csv'
test_df=pd.read_csv(CSVFILE)
actualValue=test_df['actual']
predictedValue=test_df['predicted']
actualValue=actualValue.values
predictedValue=predictedValue.values
cmt=confusion_matrix(actualValue,predictedValue)
print 'confusion_matrix: ',cmt
ac=accuracy_score(actualValue,predictedValue)
print 'accuracy:',ac
print 'Report : '
print classification_report(actualValue,predictedValue)
