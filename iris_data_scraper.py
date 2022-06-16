import pickle
import requests

url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
data = requests.get(url).text
l1 = data.split("\n")
l2 = [item.split(",") for item in l1 if len(item) !=0]
print(l2)

with open("pickle.pkl", "wb") as f:
    pickle.dump(l2,f)

#To read pickle file just use these code bellow
# with open("pickle.pkl", "rb") as f:
#     print(pickle.load(f))