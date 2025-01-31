from fastapi import FastAPI,Request
import os,json,jieba,joblib,datetime,time
from fastapi.middleware.cors import CORSMiddleware
from scirknn import scirknn_lite
import numpy as np

def tokenize_zh(text):
    words = jieba.lcut(text)
    return words

import __main__
__main__.tokenize_zh = tokenize_zh


stop_words = ['。 ', '， ']

# 載入模型
loaded_model = scirknn_lite.MLPClassifier("clf.rknn")
vectorizer = joblib.load('subject_reconition_vec.joblib')
label_encoder = joblib.load('subject_recognition_label.joblib')

AllSubjectNum = {'1': '英文', '2': '國文', '3': '地理', '4': '家政', '5': '公民', '6': '體育', '7': '歷史', '8': '資訊', '9': '音樂', '10': '物理', '11': '化學', '12': '數學', '13': '健康', '14': '地科', '15': '視覺藝術', '16': '班級事物', '17': '生物', '18': '作文', '19': '童軍', '20': '輔導'}
WeekdayTranslate = ['星期一','星期二','星期三','星期四','星期五','星期六','星期日']

def MakePred(name):
    new_data = [name]
    new_data_vectorized = vectorizer.transform(new_data).toarray()
    predicted_subject, predicted_proba = loaded_model.predict(new_data_vectorized)
    return label_encoder.inverse_transform(predicted_subject)[0], predicted_proba[0, predicted_subject[0]].tolist()

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

timetable = [
    [1,14,12,3,10,2,7,5],
    [12,11,15,1,8,6,10,2],
    [5,2,12,17,18,7,16,1],
    [9,4,3,2,1,6,12,12],
    [2,2,16,20,12,1,11,10]
    ,[],[]
]

# Pre build jieba cache
MakePred('國習')

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,allow_methods=["*"],
    allow_headers=["*"],
)



@app.post('/subject')
async def subject(request:Request):
    RequestJson = json.loads(await request.body())
    text = str(RequestJson['text'])
    subject_num, proba = MakePred(text)
    if proba < 0.5:
        return {
            'text':text,
            'subject':'',
            'nextclasstime':'',
            'proba': proba
        }
    today_weekday = datetime.datetime.today().weekday()
    next_class_weekday = GetNextClassWeekday(today_weekday,subject_num,timetable)
    next_class_period = FindNextPeriodTime(subject_num,next_class_weekday,timetable)
    return {
        'text':text,
        'subject':AllSubjectNum[subject_num],
        'nextclasstime': WeekdayTranslate[next_class_weekday] + '第'+str(next_class_period)+'節 | ' + AllSubjectNum[subject_num],
        'proba': proba
    }
