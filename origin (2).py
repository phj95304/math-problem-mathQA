# This code is contributed by avishekarora
import json
import math
import re
import pandas as pd

class  extractor:
    def __init__(self):
        self.data = []
        self.idx = 1

    def remove_brackets(self, term):
        a = 0
        while True:
            # Find opening bracket
            try:
                a = term.index("(", a)
            except ValueError:
                # No (more) opening brackets found
                break
            # Find corresponding closing bracket
            b = a
            while True:
                b = term.index(")", b + 1)
                if term[a + 1:b].count("(") == term[a + 1:b].count(")"):
                    break
            # Assemble new term by removing current pair of brackets
            if term[a-3:a] == 'log' or term[a-4:a]=='comb' or term[a-3:a] == 'gcd' or term[a-4:a] == 'sqrt' or term[a-3:a] == 'max' \
                or term[a-5:a] == 'floor':
                # print("term:{}".format(term))
                new_term = term
                a+=1
                continue
            new_term = term[:a] + term[a + 1:b] + term[b + 1:]
            # If new term produces a different value, keep term as it is and try with the next pair of brackets
            try:
                # print(term)
                # print("new term:{}".format(new_term))
                if eval(term) != eval(new_term):
                    a += 1
                    continue
                else:
                    term = new_term
            except ZeroDivisionError:
                a+=1
                continue
            except AttributeError:
                a+=1
                continue
            except ValueError:
                a+=1
                continue
            except OverflowError:
                a+=1
                continue
            except NameError:
                a+=1
                continue
            except Exception:
                a+=1
                continue
                
            # Adopt new term
        return term

    def dumper(self, answer, equation):

        self.data.append({str(self.idx) : {"answer":answer, "equation":equation}})
        with open("./answersheet.json", "w", encoding="utf-8") as answer_file:
            json.dump(self.data, answer_file, indent=2)
        

    # Python Program to convert prefix to Infix
    def prefixToInfix(self,formula):
        stack = []
        # read prefix in reverse order
        i = len(formula) - 1
        is_num = re.compile("([0-9]+)")

        while i >= 0:
            if formula[i] == 'max':
                string = "max" + "(" + stack.pop() + "," + stack.pop() + ")"
                stack.append(string)
                i -= 1

            elif formula[i] == 'min':
                string = "min" + "(" + stack.pop() + "," + stack.pop() + ")"
                stack.append(string)
                i -= 1

            elif formula[i] == 'log':
                string = "math.log" + "(" + stack.pop() + ")"
                stack.append(string)
                i -= 1

            elif formula[i] == 'sqrt':
                string = "math.sqrt" + "(" + stack.pop() + ")"
                stack.append(string)
                i -= 1        

            elif formula[i] == 'factorial':
                string = "math.factorial" + "(" + stack.pop() + ")"
                stack.append(string)
                i -= 1     

            elif formula[i] == 'gcd':
                string = "math.gcd" + "(" + stack.pop() + "," + stack.pop() + ")"
                stack.append(string)
                i -= 1     

            elif formula[i] == 'lcm':
                string = "math.lcm" + "(" + stack.pop() + "," + stack.pop() + ")"
                stack.append(string)
                i -= 1     

            elif formula[i] == 'round':
                string = "math.round" + "(" + stack.pop() + ")"
                stack.append(string)
                i -= 1    

            elif formula[i] == 'floor':
                string = "math.floor" + "(" + stack.pop() + ")"
                stack.append(string)
                i -= 1    

            elif formula[i] == 'circle_area':
                string = "math.pi" + "*" + stack.pop() + "**2"
                stack.append(string)
                i -= 1    

            elif formula[i] == 'circumface':
                string = "math.pi" + "*" + stack.pop() + "*2"
                stack.append(string)
                i -= 1    

            elif formula[i] == 'rectangle_perimeter':
                string = "2" + "*" + stack.pop()
                stack.append(string)
                i -= 1    

            elif formula[i] == 'rectangle_area':
                string = stack.pop() + "*" + stack.pop()
                stack.append(string)
                i -= 1    

            elif formula[i] == 'square_perimeter':
                string = stack.pop() + "*4"
                stack.append(string)
                i -= 1    

            elif formula[i] == 'square_area':
                string = stack.pop() + "**2"
                stack.append(string)
                i -= 1    

            elif formula[i] == 'choose' and is_num.search(formula[i]):
                string = "math.comb" + "(" + int(float(stack.pop())) + "," + int(float(stack.pop()))+ ")"
                stack.append(string)
                i -= 1    

            elif formula[i] == 'permutation':
                string = "math.perm" + "(" + stack.pop() + "," + stack.pop()+ ")"
                stack.append(string)
                i -= 1    

            elif formula[i] == 'rhombus_perimeter':
                string = "2" + "*" + stack.pop()
                stack.append(string)
                i -= 1    
            elif formula[i] == 'rhombus_area':
                string = stack.pop() + "*" + stack.pop() + "/2"
                stack.append(string)
                i -= 1    

            elif formula[i] == 'triangle_perimeter':
                string = stack.pop() + "+" + stack.pop() + "+" + stack.pop()
                stack.append(string)
                i -= 1    

            elif formula[i] == 'triangle_area':
                string = stack.pop() + "*" + stack.pop() + "/2"
                stack.append(string)
                i -= 1    

            elif self.isOperator(formula[i]):
                #symbol is operator
                str = "(" + stack.pop() + formula[i] + stack.pop() + ")"
                stack.append(str)
                i -= 1

            elif is_num.search(formula[i]) != None:#숫자면
                stack.append(formula[i])
                i -= 1

            else:
                i -= 1
                return None
        
        return stack.pop()
    
    def isOperator(self,c):
        if c == "*" or c == "+" or c == "-" or c == "/" or c == "^" or c == "(" or c == ")" or c == "**":
            return True
        else:
            return False

    def reader(self,file_path):
        json_file = open(file_path)
        data = json.load(json_file)
        
        EquList = []
        answerList = []

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
                
            #print(answer)

            formula = entity["annotated_formula"]
            formula = formula.replace("(", ",")
            formula = formula.replace(", ", ",")
            formula = formula.replace(")", "")
            formula = formula.replace("const_0_", "0.")
            formula = formula.replace("const_1_", "1.")
            formula = formula.replace("const_2_", "2.")
            formula = formula.replace("const_3_", "3.")
            formula = formula.replace("const_", "")
            
            ##print(formula)
            formula = formula.split(",")
            ##print(formula)
            refined_formula = []
            for i in formula:
                while i[0] == "0" and len(i)>1 and i[1]!='.':
                    i = i[1:]
                refined_formula.append(i)
            formula = refined_formula

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

                elif i =="reminder":
                    formula[id]="%"

                else:#숫자
                    pass
            #print(formula)
            if self.prefixToInfix(formula) !=None:
                equation = self.prefixToInfix(formula)
            
            #print(equation)
            # 불필요한 () 제거 
            equation_mini = self.remove_brackets(equation)
            #print(equation_mini)
            
            #띄어쓰기 
            #100*36*100/(3*10)/(3*10)
            pointer = equation_mini[0]
            pattern= re.compile("([0-9]+)")
            for ch in equation_mini[1:]:
                current = pattern.match(ch)
                previous = pattern.match(pointer[-1])
                #숫자, 숫자
                if current == '.' or previous == '.':
                    pointer+=ch
                elif previous != None and current != None:
                    pointer += ch
                    #print(pointer)
                elif previous != None and current == None:
                    pointer += " "
                    pointer += ch
                    #print(pointer)
                elif previous == None and current != None:
                    pointer += " "
                    pointer += ch
                    #print(pointer)

                elif previous == None and current == None:
                    pointer += ch
                    #print(pointer)
            
            
            final_eq = pointer.replace("(", " (")
            final_eq = final_eq.replace(")", ") ")
            #print(final_eq)
#             self.dumper(answer, final_eq)
#             self.idx+=1

            EquList.append(final_eq)
            answerList.append(answer)

        df = pd.DataFrame(EquList, columns=['equation'])
        dfAnswer = pd.DataFrame(answerList, columns=['answer'])

        all  = pd.concat([df,dfAnswer], axis=1)
        all.to_csv("./output.tsv",sep='\t',header=None, index=None)
            


file_path = "./mathQA.json"
extractor = extractor()
extractor.reader(file_path)