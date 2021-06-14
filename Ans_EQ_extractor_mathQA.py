# This code is contributed by avishekarora
import json

class  extractor:
    def __init__(self):
        self.data = []
        self.idx = 1

    def dumper(self, answer, equation):

        self.data.append({str(self.idx) : {"answer":answer, "equation":equation}})
        with open("./answersheet.json", "w", encoding="utf-8") as answer_file:
            json.dump(self.data, answer_file, indent=2)
        

    # Python Program to convert prefix to Infix
    def prefixToInfix(self,prefix):
        stack = []
        # read prefix in reverse order
        i = len(prefix) - 1
        while i >= 0:
            if not self.isOperator(prefix[i]):
                # symbol is operand
                stack.append(prefix[i])
                i -= 1
            else:
                # symbol is operator
                str = "(" + stack.pop() + prefix[i] + stack.pop() + ")"
                stack.append(str)
                i -= 1
        
        return stack.pop()
    
    def isOperator(self,c):
        if c == "*" or c == "+" or c == "-" or c == "/" or c == "^" or c == "(" or c == ")" or c == "**":
            return True
        else:
            return False

    def reader(self,file_path):
        json_file = open(file_path)
        data = json.load(json_file)

        for entity in data:
            ## answer
            answer_cha = entity["correct"]
            answeer_opt = entity["options"]
            answeer_opt = answeer_opt.split(",")
            if answer_cha == "a":
                answer=answeer_opt[0]
                answer = answer[4:]
            elif answer_cha == "b":
                answer=answeer_opt[1]
                answer = answer[4:]
            elif answer_cha == "c":
                answer=answeer_opt[2]
                answer = answer[4:]
            elif answer_cha == "d":
                answer=answeer_opt[3]
                answer = answer[4:]
            else:
                answer=answeer_opt[4]
                answer = answer[3:]
                
            print(answer)

            formula = entity["annotated_formula"]
            formula = formula.replace("(", ",")
            formula = formula.replace(", ", ",")
            formula = formula.replace(")", "")
            formula = formula.replace("const_", "")
            #print(formula)
            formula = formula.split(",")
            #print(formula)

            # string oeprator => symbol operator
            id=-1
            for i in formula:
                id+=1
                if i == "add":
                    formula[id]="+"
                    
                elif i == "subtract":
                    formula[id]="-"
                    
                elif i == "multiply":
                    formula[id]="*"
                    
                elif i =="divide":
                    formula[id]="/"
                    
                elif i =="power":
                    formula[id]="**"
                else:#숫자
                    pass
                
            equation = self.prefixToInfix(formula)
            print(equation)
            self.dumper(answer, equation)
            self.idx+=1
            

            #answer랑  비교하는 함수(python runnable?)

            #write the equation to json file
            # with oepn("mathQQ_equation.json", 'w') as file:
            #     file.write(equation)




file_path = "./mathQA.json"
extractor = extractor()
formula = extractor.reader(file_path)


     
