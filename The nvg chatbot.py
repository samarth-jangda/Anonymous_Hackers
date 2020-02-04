from flask import Flask, render_template,request,jsonify,make_response
from json import dumps
from datetime import datetime
from flask_assistant import tell,Assistant
from flask_ngrok import run_with_ngrok
numb:int = 0

app = Flask(__name__)
app.debug = True
run_with_ngrok(app)
assist = Assistant(app,project_id="coding-soft-wiasdt")
@app.route("/webhook")
@app.route("/home")

def home() :
    return render_template("index.html")
       # to get rich responses from user
app.config["INTEGRATIONS"] = ["Actions On Google"]


@assist.action('Default Welcome Intent')
def welcome():                              #trigger up the name intent used in next action
        speech = 'Microphone check 1,2 Hi! What can I do for you today'
        data = request.get_json(force = True)
        intent = data["queryResult"]["intent"]["Default Welcome Intent"]
        speech = 'Running'
        return tell(speech)

@assist.action('Age')                # name intent is being started
def person_age():         # belongs to action of father's occupation
    response1 = print('What is your current occupation?')
    data = request.get_json(force = True)
    intent = data["queryResult"]["intent"]["Age"]
    speech = 'Running'
    return tell(speech)

@assist.action('Occupation')   #father's occupation action started
def occupation():            #triggers up the local(sales) intent
    response2 =  print('Great ! Now tell me your past experience of coding. ')
    data = request.get_json(force = True)
    intent = data["queryResult"]["intent"]["Occupation"]
    speech = 'Running'
    return tell(speech)

@assist.action('experience')       # local(sales) intent started
def experience():           # it triggers nvg-spex
    response3 =  print('Good ! So which coding language you liked the most')
    data = request.get_json(force = True)
    intent = data["queryResult"]["intent"]["experience"]
    speech = 'Running'
    return tell(speech)

@assist.action('language')       # local(sales) intent started
def language():           # it triggers nvg-spex
    response3 =  print('Thanku for answering all the questions.')
    data = request.get_json(force = True)
    intent = data["queryResult"]["intent"]["language"]
    speech = 'Running'
    return tell(speech)

import codecs


def results():
    global numb
    # build a request object
    req = request.get_json(force=True)

    act = req.get("queryResult").get("queryText")          # this will be a jsonify response form
    call_info[call_ques[numb]] = act
    numb += 1

    if numb == len(call_ques) :
        with open(file = "C:\\data\\" + "Call_Info {}.json".format(datetime.now().strftime("%d-%m-%Y %H-%M-%S")), mode = "w",encoding='utf-8') as json_file:
            json_file.write(dumps(call_info, indent = 1000))

        #nbytes = {'utf-8': 1,'utf-16': 2,'utf-32': 4,}.get(encoding)
        #with open(file = "C:\\data\\" + "Call Info.txt", mode='rt') as txt_file:
            #print to_hex(txt_file.read(), nbytes)


@app.route("/webhook", methods = ["GET", "POST"])                         # so to fetch only hindi data we have to fatch data from
def webhook():                                                      #query text and save it in dataframe in form of array.
    return make_response(jsonify(results()))

    return jsonify(response_text)

if __name__ == "__main__" :
    call_info: dict = dict()
    call_ques: list = ["welcome", "AGE","Occupation","experience","language"]
    app.run()


from json import load
with open("C:\\data\\Call Info.txt",mode = "r") as txt_file:
    txt_content = load(txt_file)