import json

def extractor(json_file_path, ENG_question_file_path):
    global idx
    json_file = open(json_file_path)
    question_file = open(ENG_question_file_path, "w")
    data = json.load(json_file)

    for entity in data:
        question = entity["Problem"]

        #wrtite the problem from MATHQA in English
        question_file.write(question)
        question_file.write("\n")
        


 
if __name__ == "__main__":
    json_file_path = "../mathQA.json"
    question_file_path = "./mathQA_question.txt"

    extractor(json_file_path, question_file_path)
