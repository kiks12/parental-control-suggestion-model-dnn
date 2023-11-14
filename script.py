import firebase_admin
import pandas as pd
from firebase_admin import firestore
from firebase_admin import credentials
import time

df = pd.read_csv("./Android-Apps/final-final.csv")
cred = credentials.Certificate("./serviceAccountKey.json")

app = firebase_admin.initialize_app(cred)
db = firestore.client()

suggestions = db.collection("suggestions")

# LAST IS 1507

for i in range(len(df)):
    print(i)
    new_doc = suggestions.document()
    data = {
        "packageName": str(df.loc[i, "Package Name"]),
        "label": str(df.loc[i, "App"]),
        "contentRating": int(df.loc[i, "Content Rating"]),
        "age": int(df.loc[i, "Age"]),
    }
    new_doc.set(data)
    time.sleep(3)


