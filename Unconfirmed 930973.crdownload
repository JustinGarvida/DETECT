from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
from ucimlrepo import fetch_ucirepo
import pymongo

#Connecting to Mongo database via client server, using URI and creating the questions database. 
clientServer = pymongo.MongoClient("mongodb://localhost:27017")
questionsDatabase = clientServer["questionsdb"]
collection = questionsDatabase["collections"] #collections represents all of the stored questions that will be utilized. 

data = {
  "question1": "What is your sex?",

  "question2": "Do you smoke?", 

  "question3": "Do you take birth control pills?"
}

data = {}

for key, question in data.items(): 
  userAnswer = input(f"{question}")
  data[key] = userAnswer

collection.insert_one(data)

query = {"question2": "Do you smoke?"}

res = collection.find_one(query)

if res: 
  print("Data for the question is:", res["question2"])
else: 
  print("Data not found for the question")


# fetch dataset 
breast_cancer = fetch_ucirepo(id=14) 

# data (as pandas dataframes) 
X = breast_cancer.data.features 
y = breast_cancer.data.targets 

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = RandomForestClassifier(random_state=42)

model.fit(X_train, y_train)

