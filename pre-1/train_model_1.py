import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split,GridSearchCV
from sklearn.metrics import f1_score,confusion_matrix,recall_score,precision_score,accuracy_score
from xgboost import XGBClassifier
from xgboost import plot_importance
import xgboost as xgb
from sklearn.externals import joblib
data = pd.read_csv('../database/train.csv')

per = np.random.permutation(data.shape[0])
new_data = data.iloc[per,:]
new_data.head()

X = new_data[['A','B','C']]
y = new_data['H']
# print(X.corr())
# pre_X = pre_data.iloc[:,0:3]

X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.25,random_state=42)
print(X_train.shape)
print(X_test.shape)
print(y_test.sum())


from collections import Counter
from imblearn.combine import SMOTEENN
smote_enn = SMOTEENN(random_state=0)
x_resampled, y_resampled = smote_enn.fit_sample(X_train, y_train)
print(sorted(Counter(y_resampled).items()))

dtrain = xgb.DMatrix(pd.DataFrame(x_resampled,columns=['A','B','C']), y_resampled)
dtest = xgb.DMatrix(X_test)
best_recall = 0
best_acc = 0
for i in range(1,10):
    for j in np.linspace(0,1,21):
        for k in range(2,15):
            param = {'max_depth':i,'objective':'binary:logistic',
                     'eval_metric':'auc'}
            num_round = k
            bst = xgb.train(param,dtrain,num_round,learning_rates=[i for i in np.linspace(0,1,k)])

            pred = bst.predict(dtest)
            pred[pred< j] = 0
            pred[pred>=j] = 1
            if recall_score(y_test,pred)>0.7 and accuracy_score(y_test,pred)>0.7:
                print('*' * 20, i, '*' * 20, j, '*' * 20, k, '*' * 20)
                print(pred.sum())
                print(recall_score(y_test, pred))
                print(accuracy_score(y_test, pred))
                if recall_score(y_test,pred)>best_recall:
                    best_recall = recall_score(y_test,pred)
                    best_acc = accuracy_score(y_test,pred)
                    joblib.dump(bst, './model/best_model_new_{}_{}_{}_{}_{}.model'.format(i, round(j,2), k,round(best_recall,2),round(best_acc,2)))