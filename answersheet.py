import pandas as pd
import json
import sys

def Equation(path):
    df = pd.read_csv(path, sep='\t', names=["equation",'answer'])

    answerLst = []
    for i in range(0,len(df)):
        ob_idx= str(i+1)
        ob_answer = df.iloc[i].answer
        ob_equation = df.iloc[i].equation

        answerLst.append( {ob_idx:{"answer":ob_answer,"equation":ob_equation}})

    with open("./answersheet.json", "w", encoding="utf-8") as answer_file:
        json.dump(answerLst, answer_file, indent=2)

    sys.exit()

Equation("./output.tsv")