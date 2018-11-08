import pandas as pd

J=pd.read_csv('data.csv', index_col=0)
K=pd.read_csv('labels.csv',index_col=0)
K['Type']=K['Class'].map({'PRAD':'Prostate', 'LUAD':'Lung', 'BRCA':'Breast', 'KIRC':'Kidney', 'COAD':'Colon'})
K=K.join(J)
K.to_csv('labelled_data.csv')
