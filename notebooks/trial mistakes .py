import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder
from sklearn.impute import SimpleImputer

# 1. Load data
df = pd.read_csv('C:\\Users\\thoma\\Downloads\\cca\\data\\new.csv')

X = df.drop("Arrest", axis=1)
y = df["Arrest"]

# 2. Define which columns to drop entirely (dates, IDs — not useful)
drop_cols = ["Date", "Case Number", "Location Description", "Updated On"]
X = X.drop(drop_cols, axis=1)

# 3. Identify categorical vs numerical columns
categorical_cols = list(X.select_dtypes(include=["object", "string"]).columns)
numerical_cols = list(X.select_dtypes(exclude=["object", "string"]).columns)

# 4. Split AFTER dropping junk columns
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 5. Define transformers
numerical_transformer = SimpleImputer(strategy='mean')

categorical_transformer = Pipeline(steps=[
    ('imputer', SimpleImputer(strategy='most_frequent')),
    ('onehot', OneHotEncoder(handle_unknown='ignore', sparse_output=False))
])

# 6. Bundle with ColumnTransformer
preprocessor = ColumnTransformer(transformers=[
    ('num', numerical_transformer, numerical_cols),
    ('cat', categorical_transformer, categorical_cols)
])

# 7. Full pipeline
my_pipeline = Pipeline(steps=[
    ('preprocessor', preprocessor),
    ('model', RandomForestClassifier(n_estimators=100, random_state=42))
])

# 8. Fit and evaluate — clean, no manual steps
my_pipeline.fit(X_train, y_train)
y_pred = my_pipeline.predict(X_test)

print("Accuracy:", accuracy_score(y_test, y_pred))