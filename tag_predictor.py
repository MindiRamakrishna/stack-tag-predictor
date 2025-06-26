import pandas as pd
import re
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.preprocessing import MultiLabelBinarizer
from sklearn.linear_model import LogisticRegression
from sklearn.multiclass import OneVsRestClassifier
from sklearn.metrics import classification_report
from collections import Counter

# === Step 1: Load Excel files ===
path = r"C:\Users\HAVE A NICE DAY\Desktop\Project1\stacksample"
questions = pd.read_excel(f"{path}\\Questions.xlsx")
tags = pd.read_excel(f"{path}\\Tags.xlsx")

# === Step 2: Prepare data ===
# Group tags by Question ID
tags_grouped = tags.groupby("Id")["Tag"].apply(list).reset_index()

# Merge with questions
df = questions.merge(tags_grouped, left_on="Id", right_on="Id")

# Combine Title + Body
df["Text"] = df["Title"].fillna("") + " " + df["Body"].fillna("")

# Clean text
def clean(text):
    text = re.sub(r'<[^>]+>', ' ', text)  # remove HTML
    text = re.sub(r'[^a-zA-Z]', ' ', text)  # keep only letters
    return text.lower()

df["Text"] = df["Text"].apply(clean)

# === Step 3: Select Top 10 Tags ===
all_tags = [tag for tags_list in df["Tag"] for tag in tags_list]
top_tags = [tag for tag, _ in Counter(all_tags).most_common(10)]

# Filter rows with at least one top tag
df = df[df["Tag"].apply(lambda taglist: any(tag in top_tags for tag in taglist))]
df["Tag"] = df["Tag"].apply(lambda tags: [tag for tag in tags if tag in top_tags])

# === Step 4: Label encoding ===
mlb = MultiLabelBinarizer()
y = mlb.fit_transform(df["Tag"])

# === Step 5: Text Vectorization ===
vectorizer = TfidfVectorizer(max_features=10000)
X = vectorizer.fit_transform(df["Text"])

# === Step 6: Train-Test Split ===
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# === Step 7: Model Training ===
model = OneVsRestClassifier(LogisticRegression(max_iter=1000))
model.fit(X_train, y_train)

# === Step 8: Evaluate ===
y_pred = model.predict(X_test)
print(classification_report(y_test, y_pred, target_names=mlb.classes_))
