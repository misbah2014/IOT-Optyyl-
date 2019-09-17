from django.http import JsonResponse
from django.template import loader
import json
from Bot import ChatBot as bot
from time import gmtime, strftime

saving_data = ''
path = '/questions.txt'

def index(request):
    global saving_data
    if request.method == 'POST':
        jsonData = json.loads(request.body.decode('utf-8'))
        msg = jsonData["msg"]
        file = open(path,'a')
        saving_data = 'Question :'
        saving_data += msg
        saving_data += '\n'
        file.write(saving_data)
        saving_data = ''
        try:
            res = bot.ChatBot.getBot().response(msg)
            saving_data = 'Answer :'
            saving_data += res
            saving_data += '\n'
            file.write(saving_data)
            saving_data = ''
        except:
            print('Error in response')
            res = 'Sorry I am Not Perfectly Train right now '
        time = strftime("%Y-%m-%d %H:%M:%S", gmtime())
        file.close()
        return JsonResponse({
            "desc": "Success",
            "ques": msg,
            "res": res,
            "time": time
        })

    else:
        return JsonResponse({"desc": "Bad request"}, status=400)
