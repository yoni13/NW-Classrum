import requests ,os ,hashlib

# update md5sum4model.txt
if os.path.isfile('md5sum4model.txt'):
    latest_md5sum = requests.get('https://gitlab.nicewhite.xyz/api/v4/projects/4/jobs/artifacts/jieba/raw/md5sum4model.txt?job=build').text
    with open('md5sum4model.txt','r') as f:
        local_md5sum = f.read()
    if latest_md5sum != local_md5sum:
        with open('md5sum4model.txt','w') as f:
            f.write(latest_md5sum)
else:
    with open('md5sum4model.txt','w') as f:
        f.write(requests.get('https://gitlab.nicewhite.xyz/api/v4/projects/4/jobs/artifacts/jieba/raw/md5sum4model.txt?job=build').text)


# update md5sum4vec.txt
if os.path.isfile('md5sum4vec.txt'):
    latest_md5sum = requests.get('https://gitlab.nicewhite.xyz/api/v4/projects/4/jobs/artifacts/jieba/raw/md5sum4vec.txt?job=build').text
    with open('md5sum4vec.txt','r') as f:
        local_md5sum = f.read()
    if latest_md5sum != local_md5sum:
        with open('md5sum4vec.txt','w') as f:
            f.write(latest_md5sum)
else:
    with open('md5sum4vec.txt','w') as f:
        f.write(requests.get('https://gitlab.nicewhite.xyz/api/v4/projects/4/jobs/artifacts/jieba/raw/md5sum4vec.txt?job=build').text)

# update model
if os.path.isfile('subject_recognition_model.joblib'):
    with open('md5sum4model.txt','r') as f:
        local_md5sum = f.read()
    model_md5sum = hashlib.md5(open('subject_recognition_model.joblib','rb').read()).hexdigest()
    if model_md5sum != local_md5sum:
        os.remove('subject_recognition_model.joblib')
        with open('subject_recognition_model.joblib','wb') as f:
            f.write(requests.get('https://gitlab.nicewhite.xyz/api/v4/projects/4/jobs/artifacts/jieba/raw/subject_recognition_model.joblib?job=build').content)
else:
    with open('subject_recognition_model.joblib','wb') as f:
        f.write(requests.get('https://gitlab.nicewhite.xyz/api/v4/projects/4/jobs/artifacts/jieba/raw/subject_recognition_model.joblib?job=build').content)


# update vec
if os.path.isfile('subject_reconition_vec.joblib'):
    with open('md5sum4vec.txt','r') as f:
        local_md5sum = f.read()
    vec_md5sum = hashlib.md5(open('subject_reconition_vec.joblib','rb').read()).hexdigest()
    if vec_md5sum != local_md5sum:
        os.remove('subject_reconition_vec.joblib')
        with open('subject_reconition_vec.joblib','wb') as f:
            f.write(requests.get('https://gitlab.nicewhite.xyz/api/v4/projects/4/jobs/artifacts/jieba/raw/subject_reconition_vec.joblib?job=build').content)
else:
    with open('subject_reconition_vec.joblib','wb') as f:
        f.write(requests.get('https://gitlab.nicewhite.xyz/api/v4/projects/4/jobs/artifacts/jieba/raw/subject_reconition_vec.joblib?job=build').content)