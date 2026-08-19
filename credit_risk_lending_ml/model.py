import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder,StandardScaler
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score,precision_score,recall_score,f1_score,roc_auc_score,confusion_matrix
from sklearn.ensemble import IsolationForest

def run():
 df=pd.read_csv('credit_applicants.csv'); df['is_thin_file']=df.credit_bureau_score.isna().astype(int); X=df.drop(columns='default'); y=df.default
 Xtr,Xte,ytr,yte=train_test_split(X,y,test_size=.25,stratify=y,random_state=42)
 num=[c for c in X.columns if c not in ['applicant_id','employment_type']]; cat=['employment_type'];
 pre=ColumnTransformer([('num',Pipeline([('imp',SimpleImputer(strategy='median')),('sc',StandardScaler())]),num),('cat',OneHotEncoder(handle_unknown='ignore'),cat)])
 models={'Logistic Regression':LogisticRegression(max_iter=2000),'Decision Tree':DecisionTreeClassifier(random_state=42)}
 for n,m in models.items():
  p=Pipeline([('pre',pre),('model',m)]); p.fit(Xtr,ytr); pred=p.predict(Xte); prob=p.predict_proba(Xte)[:,1]; print(n,accuracy_score(yte,pred),precision_score(yte,pred),recall_score(yte,pred),f1_score(yte,pred),roc_auc_score(yte,prob)); print(confusion_matrix(yte,pred))
 b=pd.read_csv('txn_behaviour.csv'); Z=StandardScaler().fit_transform(b[['txn_hour','is_new_device','txn_amount_inr']]); iso=IsolationForest(random_state=42,contamination=15/265).fit(Z); b['anomaly']=iso.predict(Z)==-1; seeded=b.txn_id.str.startswith('BTXNA'); print('IsolationForest seeded recall',b.loc[seeded,'anomaly'].mean())
if __name__=='__main__': run()
