from flask import Flask, request, redirect, send_from_directory, abort
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from werkzeug.utils import secure_filename
import os,json,jieba,joblib,datetime,time,requests
from flask_cors import cross_origin


def tokenize_zh(text):
    words = jieba.lcut(text)
    return words

import __main__
__main__.tokenize_zh = tokenize_zh


stop_words = ['。 ', '， ']

# 載入模型
loaded_model = joblib.load('subject_recognition_model.joblib')
vectorizer = joblib.load('subject_reconition_vec.joblib')

AllSubjectNum = ["1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20"]
SubjectNames = ["英文","國文","地理","家政","公民","體育","歷史","資訊","音樂","物理","化學","數學","健康","地科","視覺藝術","班級事物","生物","作文","童軍",'輔導']
WeekdayTranslate = ['星期一','星期二','星期三','星期四','星期五','星期六','星期日']

def MakePred(name):
    new_data = [name]
    new_data_vectorized = vectorizer.transform(new_data)
    predicted_subject = loaded_model.predict(new_data_vectorized)
    return predicted_subject[0]

def SubjNumTranslator(theNum):
    round = 0
    for Num in AllSubjectNum:
        if Num == theNum:
            return SubjectNames[round]
        round += 1

# Today weekday is an int,subject num is an string,timetable is a dict,
def GetNextClassWeekday(today_weekday,subject_num,timetable):
    if today_weekday + 1 > 6:
        weekday_num = 0
    else:
        weekday_num  = today_weekday + 1

    while True:
        if int(subject_num) in timetable[weekday_num]:
            break
        else:
            if weekday_num + 1 > 6:
                weekday_num = 0
            else:
                weekday_num += 1

    return weekday_num

# We use class_ to avoid conflix with python class
def FindNextPeriodTime(subject_num,next_class_weekday,timetable):
    period = 0
    for class_ in timetable[next_class_weekday]:
        period += 1
        if str(class_) == subject_num:
            return period

timetable = [[1,12,17,14,3,2,4,5],[12,2,15,1,8,6,10,2],[10,2,3,12,17,7,16,1],[9,12,5,10,1,2,7,12],[2,6,16,20,12,11,1,10],[],[]]
# Pre build jieba cache
MakePred('國習')

app = Flask(__name__)

limiter = Limiter(
    get_remote_address,
    app=app,
    default_limits=[],
    storage_uri="memory://",
)

UPLOAD_FOLDER = 'temp'
ALLOWED_EXTENSIONS = set(['pdf', 'png', 'jpg', 'jpeg', 'gif'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

@app.route('/')
def root():
    return redirect('https://nw-classrum.nicewhite.xyz/')


@app.route('/subject', methods=['POST'])
@cross_origin(send_wildcard=True)
#@limiter.limit("1/2second", override_defaults=True)
def subject():
    RequestJson = request.get_json()
    text = RequestJson['text']
    subject_num = MakePred(text)
    today_weekday = datetime.datetime.today().weekday()
    next_class_weekday = GetNextClassWeekday(today_weekday,subject_num,timetable)
    next_class_period = FindNextPeriodTime(subject_num,next_class_weekday,timetable)
    return {'subject':SubjNumTranslator(subject_num), 'nextclasstime': WeekdayTranslate[next_class_weekday] + '第'+str(next_class_period)+'節 | ' + SubjNumTranslator(subject_num)}


@app.route('/ping')
def ping():
    return str(time.time())

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0')
