import numpy as np
import pandas as pd
#from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import GradientBoostingClassifier
#from sklearn.ensemble import HistGradientBoostingClassifier
#from sklearn.linear_model import LogisticRegression
#from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OrdinalEncoder


import os
for dirname, _, filenames in os.walk('.'):
    for filename in filenames:
        print(os.path.join(dirname, filename))


train_data = pd.read_csv("C:\\Users\\27greenj\\Documents\\techinar\\data\\train.csv")
test_data = pd.read_csv("C:\\Users\\27greenj\\Documents\\techinar\\data\\test.csv")

numerical_columns = ["PassengerId", "Pclass", "Age", "SibSp", "Parch", "Fare"]
categorical_columns = ["Sex", "Embarked"]

y = train_data["Survived"]
feature_columns = numerical_columns + categorical_columns
X = train_data[feature_columns]
X_test = test_data[feature_columns]

train_X, val_X, train_y, val_y = train_test_split(X, y, random_state = 1, test_size = 0.2, stratify = y)

numerical_transformer = SimpleImputer(strategy='mean')
categorical_transformer = Pipeline(steps=[
    ('imputer', SimpleImputer(strategy='most_frequent')),
    ('ordinal', OrdinalEncoder())
])

preprocessor = ColumnTransformer(transformers=[
    ('num', numerical_transformer, numerical_columns),
    ('cat', categorical_transformer, categorical_columns)
])

best_score = 0
best_depth = 0
for md in range(1, 100):
    model = GradientBoostingClassifier()
    my_pipeline = Pipeline(steps=[
        ('preprocessor', preprocessor),
        ('model', model)
    ])
    my_pipeline.fit(train_X, train_y)
    score = accuracy_score(val_y, my_pipeline.predict(val_X))
    print(f"Max depth: {md}, Accuracy: {score}")
    if score > best_score:
        best_score = score
        best_depth = md

print(f"The best score was {best_score} with a depth of {best_depth}")

model = GradientBoostingClassifier()
my_pipeline.fit(X, y)
predictions = my_pipeline.predict(X_test)

output = pd.DataFrame({'PassengerId': test_data.PassengerId, 'Survived': predictions})
output.to_csv('submission.csv', index=False)
print("Your submission was successfully saved!")
