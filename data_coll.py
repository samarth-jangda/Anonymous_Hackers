# Only used with Flask-app.py of the chatbot
from os import listdir
x = listdir("C:\\data")
from json import load
from pandas.io.json import json_normalize
y = {"files" : []}
for file in x :
    with open ("C:\\data\\" + file , mode = "r",encoding = 'utf-8') as json_file : y["files"].append(load(json_file))

df = json_normalize(y["files"])
#df["Age"]
#type(df.at[0,"Age"])
df.to_csv("C:\\Excel_speech_data\\Sample.csv",index = False,encoding = 'utf-8')


