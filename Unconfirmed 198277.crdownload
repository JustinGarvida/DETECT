import pymongo

clientServer = pymongo.MongoClient("mongodb://localhost:27017")
questionsDatabase = clientServer["questionsdb"]
collection = questionsDatabase["collections"]

data = {
  "question1": "What is your sex?",

  "question2": "Do you smoke?", 

  "question3": "Do you take birth control pills?"
}


collection.insert_one(data)

query = {"question2": "Do you smoke?"}

res = collection.find_one(query)

if res: 
  print("Data for the question is:", res["question2"])
else: 
  print("Data not found for the question")
  
