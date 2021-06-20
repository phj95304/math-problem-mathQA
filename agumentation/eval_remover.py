import csv
import math

def remover(path):
    f = open(path, 'r', encoding='utf-8')
    file =  open("./train_rem.csv", "w", encoding='utf-8')
    rdr = csv.reader(f)
    for line in rdr:
        id = line[0]
        question = list(line[1])
        question_ = line[1]
        expression = line[2]
        solution = line[3]

        #prolem에서 수식 제거
        if not "+" or "*" or  "-" in question:
            wr = csv.writer(file)
            wr.writerow([id, question_, expression, solution])

        
    file.close()
    f.close()

remover("./train.csv")