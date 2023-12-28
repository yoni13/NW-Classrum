
import jieba

def tokenize_zh(text):
    words = jieba.lcut(text)
    return words
stop_words = ['。 ', '， ']
import joblib

# 載入模型
loaded_model = joblib.load('subject_recognition_model.joblib')
vectorizer = joblib.load('subject_reconition_vec.joblib')

AllSubjectNum = ["1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20"]
SubjectNames = ["英文","國文","地理","家政","公民","體育","歷史","資訊","音樂","物理","化學","數學","健康","地科","視覺藝術","班級事物","生物","作文","童軍",'輔導']

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
        round +=1
