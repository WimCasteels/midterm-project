import pickle
import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split

from sklearn.feature_extraction import DictVectorizer
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import roc_auc_score


# parameters

max_depth=4
min_samples_leaf = 200
output_file = f'model_depth={max_depth}_samples={min_samples_leaf}.bin'

# data preparation

df = pd.read_csv('data/secondary_data.csv', delimiter = ';')
df["class"] = (df["class"] == 'p').astype(int)

numerical = ['cap-diameter', 'stem-height', 'stem-width']
categorical = ['cap-shape', 'cap-surface', 'cap-color','does-bruise-or-bleed', 'gill-attachment', 'gill-spacing', 'gill-color',
       'stem-root', 'stem-surface', 'stem-color','veil-type', 'veil-color', 'has-ring', 'ring-type', 'spore-print-color','habitat', 'season']

df_full_train, df_test = train_test_split(df, test_size=0.2, random_state=1, shuffle=False)
df_train, df_val = train_test_split(df_full_train, test_size=0.25, random_state=1, shuffle=False)


# training 

def train(df_train, y_train, max_depth, min_samples_leaf):
    dicts = df_train[categorical + numerical].to_dict(orient='records')

    dv = DictVectorizer(sparse=False)
    X_train = dv.fit_transform(dicts)

    model = DecisionTreeClassifier(max_depth=max_depth, min_samples_leaf=min_samples_leaf)
    model.fit(X_train, y_train)
    
    return dv, model

def predict(df, dv, model):
    dicts = df[categorical + numerical].to_dict(orient='records')

    X = dv.transform(dicts)
    y_pred = model.predict_proba(X)[:, 1]

    return y_pred

# validation

print(f'doing validation with max_depth={max_depth} and min_samples_leaf={min_samples_leaf}')

dv, model = train(df_train, df_train['class'].values, max_depth=max_depth, min_samples_leaf = min_samples_leaf)
y_pred = predict(df_val, dv, model)

auc = roc_auc_score(df_val['class'].values, y_pred)
print(f'auc on validation set is {auc}')


# training the final model

print('training the final model')

dv, model = train(df_full_train, df_full_train['class'].values, max_depth=max_depth, min_samples_leaf = min_samples_leaf)
y_pred = predict(df_test, dv, model)

y_test = df_test['class'].values
auc = roc_auc_score(y_test, y_pred)

print(f'auc={auc}')


# Save the model

with open(output_file, 'wb') as f_out:
    pickle.dump((dv, model), f_out)

print(f'the model is saved to {output_file}')