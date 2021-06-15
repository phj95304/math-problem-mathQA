import json
import re

import googletrans
from googletrans import Translator


def dumper(question):
    global idx
    global data
    #print(question)
    data.append({str(idx) : {"question":question}})

    with open("./questionsheet_MATHQA.json", "w", encoding="utf-8") as testfile:
        json.dump(data, testfile, ensure_ascii=False, indent=2)


# def extractor(json_file_path): json file load and translate
#     global idx
#     json_file = open(json_file_path)
#     data = json.load(json_file)

#     for entity in data:
#         question = entity["Problem"]

#         translator = Translator()
#         trans = translator.translate(question, src='en', dest='ko')
    
#         #write the problem from MATHQA in KOR json type 
#         #print(trans.text)
#         dumper(trans.text)
#         idx+=1

#한국어로 번역된 파일을 이용해 json 생성
def extractor(text_file_path):
    global idx
    data = open(text_file_path)
    for i in data:
        dumper(i)
        idx+=1



 
if __name__ == "__main__":
    json_file_path = "./mathQA.json"
    text_file_path = "./question_KOR.txt"
    idx = 1
    data = []
    extractor(text_file_path)
    