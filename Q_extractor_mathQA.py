import json
import re

import googletrans
from googletrans import Translator


def dumper(question):
    global idx
    global data
    print(question)
    data.append({str(idx) : {"question":question}})

    with open("./answersheet_MATHQA.json", "w", encoding="utf-8") as testfile:
        json.dump(data, testfile, ensure_ascii=False)


def extractor(json_file_path, ENG_question_file_path):
    global idx
    json_file = open(json_file_path)
    question_file = open(question_file_path, "w")
    data = json.load(json_file)

    for entity in data:
        question = entity["Problem"]

        translator = Translator()
        trans = translator.translate(question, src='en', dest='ko')
        #wrtite the problem from MATHQA in English
        question_file.write(question)
        question_file.write("\n")
        #write the problem from MATHQA in KOR json type 
        #print(trans.text)
        dumper(trans.text)
        idx+=1


 
if __name__ == "__main__":
    json_file_path = "./mathQA.json"
    question_file_path = "./mathQA_answer.json"

    idx = 1
    data = []
    extractor(json_file_path, question_file_path)
    jsonMaker(question_file_path)