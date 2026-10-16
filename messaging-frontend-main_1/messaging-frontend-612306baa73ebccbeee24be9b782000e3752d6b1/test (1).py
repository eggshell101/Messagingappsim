from flask import Flask
import pickle
import requests

app = Flask(__name__)

ip = "192.168.3.33"

try:
        with open('everything.dat','rb') as e:
                queue = pickle.load(e)
except:
        queue = {}

def save():
        global queue
        
        with open('everything.dat','wb') as e:
                pickle.dump(queue, e)

@app.route("/")
def hello_world():
    return "Hello, Dyutimaan!"

@app.route("/createconv/<conversation>", methods = ['GET','POST'])
def cc(conversation):
        try:
                queue[conversation]
        except:
                queue.update({ conversation : [] })
                save()
                return conversation
        else:
                return 'error'

@app.route("/putmsg/<conversation>/<username>/<message>", methods = ['GET', 'POST'])
def msg(conversation,username,message):
        global queue
        
        try:
                queue[conversation] += [(username, message)]
                save()

                if message[0] == '!':
                        requests.post(f"{ip}:5000/newcommand/{conversation}/{message[1:]}/")
                        print(ip)
                return message
        except Exception as e:
                return str(e)

@app.route("/getmsgs/<conversation>", methods = ['GET'])
def gmsgs(conversation):
        global queue
        
        strout = ''
        
        for msg in queue[conversation]:
                strout += msg[0]+': '+msg[1]+'\n'
                
        return strout

@app.route("/killconv/<conversation>", methods = ['GET','POST'])
def killconv(conversation):
        global queue
        
        try:
                del queue[conversation]
                save()
                return conversation
        except:
                return 'error'

@app.route("/getallconvs/", methods = ['GET'])
def getallconvs():
        global queue

        res = []
        
        for conversation in queue:
                res += [conversation]

        return res
