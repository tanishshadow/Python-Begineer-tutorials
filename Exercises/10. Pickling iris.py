import pickle
import requests
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
file = requests.get(url).text
data = file.splitlines()
t = open("test.txt", "r+")
t.write(file)
comp_list = [[i] for i in data]
t.close()
file_dup = "iris.pkl"
file_obj = open(file_dup, "wb")
pickle.dump(comp_list, file_obj)
file_obj.close()
file_obj = open(file_dup, "rb")
show = pickle.load(file_obj)
print(show)
file_obj.close()
# import pickle
# import requests
# url='https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
# respons=requests.get(url)
# respons_text=respons.text
# data=respons_text.splitlines()
# red=[[i] for i in data]
# #pickling the python object
# fileobj=open('irisData.pkl','wb')
# pickle.dump(red,fileobj)
# fileobj.close()

# #Reading Of Pickel file
# fileobj=open('irisData.pkl','rb')
# data=pickle.load(fileobj)
# print(data)
