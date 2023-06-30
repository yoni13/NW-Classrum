from pymongo.mongo_client import MongoClient
from dotenv import load_dotenv
from bs4 import BeautifulSoup
import os, json, requests, time, random
load_dotenv()
db = "mongodb+srv://yoni:"+os.getenv('passwd')+"@cluster0.o0k9job.mongodb.net/?retryWrites=true&w=majority"

# Create a new client and connect to the server
client = MongoClient(db)
def urlget(key,page):
    return 'https://search.books.com.tw/search/query/cat/1/qsub/001/qqsub/24/sort/1/v/1/spell/3/ms2/ms2_1/page/'+str(page)+'/key/'+key
# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

# Create a new database
db = client['keyword-db']
loopnum = 0
while True:
    loopnum += 1
    r = requests.get(urlget('翰林',loopnum))
    if r.status_code != 200:
        break
    soup = BeautifulSoup(r.text, 'html5lib')
    for data in soup.find_all('img',class_='b-lazy'):
        if data.get('class')[0] == 'cover' or data.get('class')[0] == 'ban':
            pass
        else:
            print(data.get('alt'))
    time.sleep(random.randint(10,30))