from dotenv import load_dotenv
import os,json
load_dotenv()
from revChatGPT.V1 import Chatbot

chatbot = Chatbot(config={
    "email": os.getenv('email'),
    "password": os.getenv('password'),
})

Data4Exchange = {
   "1":"Math",
   "2":"Chinese",
   "3":"English",
   "4":"Science",
   "5":"Computer",
   "6":"Music",
   "7":"Art",
   "8":"PE",
   "9":"History",
   "10":"Geography",
   "11":"Civics",
   "12":"Other"
}

def GetChatText(text):
    try:
        # If the first character is a number and a dot,remove it
        FirstChar = int(text[0])
        RtextWithDot = text.replace(str(FirstChar), '')
        Rtext = RtextWithDot.replace('.', '')

    except:
        Rtext = text
    if Rtext[0] != ' ':
        Rtext = ' ' + Rtext
    RequestText = 'Which main subject of' + Rtext + '''?,If it's about math return 1,chinese 2,English 3,science 4,computer 5,music 6,art 7,PE 8,history 9,geography 10,civics 11,,other 12.response in json format only,formatis {'subject':<the number>}}'''
    for data in chatbot.ask(RequestText):
        Resp = data['message']
    RespNoBreak = Resp.replace('\n', '')
    RespNoSpace = RespNoBreak.replace(' ', '')
    JsonResp = json.loads(RespNoSpace)
    Data = Data4Exchange[str(JsonResp['subject'])]
    return {'subject':Data}
