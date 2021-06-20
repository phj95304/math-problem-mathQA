import random
import math
import json
import itertools
from inspect import getmembers, isfunction

places = ['(가)', '(나)', '(다)', '(라)', '(마)', '(바)', '(사)', '(아)', '(자)', '(차)', '(카)', '(타)', '(파)', '(하)']
people = ['남진','석진','윤기','호석','지민','태형','정국','유정','민영','은지','유나']

class EQ_augment():
    
    def aug_prob1(self):
        a = random.randint(1, 100)
        b = random.randint(1, 100)
        personA = random.choice(people)
        new_question = "상자 안에 {}개의 공이 있습니다. {}이가 {}개의 공을 상자 안에 더 넣었습니다. 상자 안에 있는 공은 모두 몇 개입니까?".format(a, personA,b)
        equation = "{} + {}".format(a, b)
        return {'question':new_question, 'equation':equation, 'answer':"{}".format(eval(equation))}


    def aug_prob2(self):
        a = random.randint(1, 10)
        b = random.randint(1, 10)
        if a > b: a,b=b,a
        if a % 2 == 0:
            new_question = "{}부터 {}까지의 짝수의 합을 구하시오.".format(a, b)
            equation = "sum ( [ i for i in range( {} , {} , 2 ) ] )".format(a, b+1)
        else:
            new_question = "{}부터 {}까지의 홀수의 합을 구하시오.".format(a, b)
            equation = "sum ( [ i for i in range( {} , {} , 2 ) ] )".format(a, b+1)
        return {'question':new_question, 'equation':equation, 'answer':"{}".format(eval(equation))}


    def aug_prob3(self):
        
        fruit = ['과일','사과', '배', '감', '귤', '포도', '수박', '복숭아', '바나나', '참외']
        veges = ['채소','토마토','무','당근','오이','배추','상추','고추','양파','마늘','가지'] 
        choose = fruit + veges

        chosenA = random.choice(choose)

        a = random.randint(1, 300)
        b = random.randint(1, 300)
        new_question = "한 상자에는 {0}이 {1}개씩 들어있습니다. {2}개의 상자 안에 있는 {0}은 모두 몇 개일까요?".format(chosenA,a, b)
        equation = "{} * {}".format(a, b)

        return {'question':new_question, 'equation':equation, 'answer':"{}".format(eval(equation))}


    def aug_prob4(self):
        a = random.randint(1,100)
        b=  random.randint(1,100)
        c=  random.randint(1,100)
        d=  random.randint(1,100)
        e = random.randint(1,100)

        chosen_people = random.sample(people,3)

        new_question = "{}의 수학 점수는 각각 {}점, {}점, {}점입니다. 이 셋을 제외한 학급의 수학 점수 평균은 {}점입니다. {}네 학급 인원수가 {}명일 때, 학급 수학 평균 점수는 몇 점입니까".format(' , '.join(chosen_people),a, b, c, d, random.choice(chosen_people),e)
        equation = "( ( {} - {} ) * {} + {} + {} + {} ) / {}".format(e, 3, d , a, b, c, e)

        if isinstance(eval(equation),int):
            return {'question':new_question, 'equation':equation, 'answer':"{}".format(eval(equation))}
        return {'question':new_question, 'equation':equation, 'answer':"{:.2f}".format(eval(equation))}


    def aug_prob5(self):
        a = random.randint(1,100)
        b=  random.randint(1,100)
        if a < b: a,b=b,a
        chosen_person = random.choice(people)
        new_question = "{}명의 학생들이 한 줄로 줄을 섰습니다. {}의 앞에 {}명의 학생들이 서 있습니다. {}의 뒤에 서 있는 학생은 몇 명입니까?".format(a,chosen_person,b,chosen_person)
        equation = "{} - ( {} + 1 )".format(a,b)

        return {'question':new_question, 'equation':equation, 'answer':"{}".format(eval(equation))}


    def aug_prob6(self):
        a = random.randint(1,100)
        
        chosen = random.sample(people,3)
        personA = chosen[0]
        personB = chosen[1]
        personC = chosen[2]

        new_question = "달리기 시합에서 {0}는 {1} 등을 했고, {2}는 {3} 등을 했습니다. {4}는 {2}보다 잘했지만 {0}보다는 못했습니다. {4}의 등수는 몇 등입니까?".format(personA,a,personB, a+2, personC) 
        equation = " ( {} + {} ) / 2".format(a, a+2)
        return {'question':new_question, 'equation':equation, 'answer':"{}".format(int(eval(equation)))}


    def aug_prob7(self):
        a = random.randint(1, 100)
        b = random.randint(1, 100)
        if a < b: a,b = b,a
        personA = random.choice(people)
        new_question = "키가 작은 사람부터 순서대로 {0}명이 한 줄로 서 있습니다. {1}가 앞에서부터 {2}번째에 서 있습니다. 키가 큰 사람부터 순서대로 다시 줄을 서면 {1}는 앞에서부터 몇 번째에 서게 됩니까?".format(a,personA, b)
        equation = "{} - {} + 1".format(a, b)
        return {'question':new_question, 'equation':equation, 'answer':"{}".format(eval(equation))}


    def aug_prob9(self):
        num_to_jarisu = {1:'한', 2:'두', 3:'세', 4:'네', 5:'다섯', 6:'여섯', 7:'일곱', 8:'여덟', 9:'아홉'}
        num = random.randint(1, 9)
        arrs = list(set([random.randint(1,9) for _ in range(num)]))
        new_question = "{}개의 숫자 ".format(len(arrs)) +  " ,".join(["{}"]*len(arrs)).format(*arrs) + "를 한 번씩만 사용하여 {} 자리수를 만들려고 합니다. 만들 수 있는 {} 자리 수는 모두 몇 개입니까?".format(num_to_jarisu[len(arrs)], num_to_jarisu[len(arrs)])
        equation = "math.factorial({})".format(len(arrs))
        return {'question':new_question, 'equation':equation, 'answer':"{}".format(eval(equation))}


    def aug_prob10(self):
        fruit = ['과일','사과', '배', '감', '귤', '포도', '수박', '복숭아', '바나나', '참외']
        veges = ['채소','토마토','무','당근','오이','배추','상추','고추','양파','마늘','가지'] 
        sweet = ['디저트','사탕','초콜릿', '아이스크림', '감자칩'] # 디저트
        category = random.choice(['과일','야채','디저트'])
        if category == '과일': category = fruit
        elif category == '야채': category = veges
        else: category = sweet
        chosenfruit = [i for i in category[1:] if random.randint(0,1)]
        while not len(chosenfruit): chosenfruit = [i for i in category[1:] if random.randint(0,1)]
        choosenum = random.randint(1,len(chosenfruit))
        new_question = "{} 중에서 {}가지의 {}을 골라서 사는 경우는 모두 몇 가지입니까?".format(', '.join(chosenfruit), choosenum, category[0] )
        equation = "len ( list ( itertools.combinations ( [ {} ] , {} ) ) )".format(', '.join(['\'{}\''.format(str(i)) for i in chosenfruit]),choosenum)
        return {'question':new_question, 'equation':equation, 'answer':"{}".format(eval(equation))}


    def aug_prob11(self):
        N = random.randint(1, 10)
        arrs = [random.randint(1, 100) for _ in range(N)]
        new_question = "{}개의 수 {}가 있습니다. 그 중에서 가장 큰 수와 가장 작은 수의 차는 얼마입니까?".format(N, ' ,'.join(map(str, arrs)))
        equation = "max ( [ {} ] ) - min ( [ {} ] ) ".format(' , '.join([str(i) for i in arrs]), ' , '.join([str(i) for i in arrs]))
        return {'question':new_question, 'equation':equation, 'answer':"{}".format(eval(equation))}


    def aug_prob12(self):
        direction = ['오른','왼']
        num_to_jarisu = {1:'한', 2:'두', 3:'세', 4:'네'}
        num = random.randint(1, 4)
        LR = random.choice(direction)
        if LR=='오른':
            comp = float('{:.2f}'.format(random.uniform(100,1000)))
            divnum1 = 10**num
            divnum2 = 1
            res = '커'
        else:
            comp = float('{:.2f}'.format(random.uniform(1,100)))
            divnum1 = 10**num
            divnum2 = 10**num - 1
            res = '작아'
        new_question = "어떤 소수의 소수점을 {}쪽으로 {} 자리 옮기면 원래보다 {} 만큼 {}집니다. 원래의 소수를 구하시오.".format(LR,num,comp,res)
        equation = "{} * {} / {}".format(comp,divnum1,divnum2)
        if isinstance(eval(equation),int):
            return {'question':new_question, 'equation':equation, 'answer':"{}".format(eval(equation))}
        return {'question':new_question, 'equation':equation, 'answer':"{:.2f}".format(eval(equation))}


    def aug_prob16(self):
        operator = ['+','-']
        
        operate = random.choice(operator)
        if operate =='+':
            numA = random.randint(10,100)
            numB = random.randint(1,10)
            new_question =         "서로 다른 두 자연수 A , B가 있습니다. A {} B = {}, B = {} * A 일 때, A 를 구하시오.".format(                                                                                 operate,numA,numB)
        else:
            numA = -random.randint(10,100)
            numB = random.randint(2,10)
            new_question =         "서로 다른 두 자연수 A , B가 있습니다. A {} B = -{}, B = {} * A 일 때, A 를 구하시오.".format(                                                                                 operate,numA,numB)
        equation= "{} / ( {} {} {} )".format(numA,1,operate,numB)
        if isinstance(eval(equation),int):
            return {'question':new_question, 'equation':equation, 'answer':"{}".format(eval(equation))}
        return {'question':new_question, 'equation':equation, 'answer':"{:.2f}".format(eval(equation))}


    def aug_prob17(self):
        operator = ['+','-']

        numA = random.randint(1,1000)
        numB = random.randint(1,1000)
        numC = random.randint(1,1000)
        operateA = random.choice(operator)
        operateB = random.choice(operator)
        new_question =     "어떤 수에서 {}을 {}야 하는데 잘못하여 {}을 {} 결과가 {}이 나왔습니다. 바르게 계산한 결과를 구하시오.".format(            numA,'더해' if operateA=='+' else '빼', numB, '더한' if operateB=='+' else '뺀', numC)
        equation = "{} {} {} {} {}".format(numC,'+' if operateB == '-' else '-',numB,operateA,numA)

        return {'question':new_question, 'equation':equation, 'answer':"{}".format(eval(equation))}


    def aug_prob19(self):
        operatorA = ['+','-', '/']
        operatorB = ['+','-','*']

        numA = random.randint(1,1000)
        numB = random.randint(1,1000)
        numC = random.randint(1,1000)
        operateA = random.choice(operatorA)
        operateB = random.choice(operatorB)
        new_question =     "어떤 수에서 {}을 {}더니 {}가 되었습니다. 어떤 수에서 {}를 {}면 얼마가 되는지 구하시오.".format(            numA,'더했' if operateA=='+' else ('빼' if operateA=='-' else '나누었'),                                                    numB, numC,'더하' if operateB=='+' else ('곱하' if operateB=='*' else '빼'))
        equation = "{} {} {} {} {}".format(numB,                                       '+' if operateA == '-' else ('-' if operateA == '+' else '*'),numA,operateB,numC)
        return {'question':new_question, 'equation':equation, 'answer':"{}".format(eval(equation))}


    def aug_prob20(self):
        operatorA = ['+','-', '*']

        numA = random.randint(1,1000)
        numB = random.randint(1,1000)
        numC = random.randint(1,100)
        operateA = random.choice(operatorA)
        new_question =     "{}에 어떤 수를 {}야 할 것을 잘못하여 {}에 어떤 수를 곱했더니 {}이 되었습니다. 바르게 계산하면 얼마인지 구하시오.".format(    numA,'더해' if operateA=='+' else ('빼' if operateA=='-' else '곱해'),            numB,numB*numC)
        equation = "{} {} ( {} / {} ) ".format(numA,operateA,numB * numC,numB)

        return {'question':new_question, 'equation':equation, 'answer':"{}".format(int(eval(equation)))}


    def aug_prob21(self):
        operate = random.choice(['+','-'])
        numS = random.randint(1,100)
        numI = random.randint(1,100)
        number = random.randint(3,8)
        numA = number + random.randint(5,100)
        numB = number + random.randint(5,100)
        if numA > numB: numA,numB=numB,numA

        listA = [i*numI+numS for i in range(1,number+1)]
        new_question =     "{}와 같은 규칙에서 {} 번째 놓일 수와 {} 번째 놓일 수를 각각 A 와 B 라 할 때, B {} A 를 구하시오.".format(    ' , '.join([str(i) for i in listA]),numA,numB, operate)
        equation = "{} * ( {} {} {} ) ".format(listA[1] - listA[0], numB, operate, numA)

        return {'question':new_question, 'equation':equation, 'answer':"{}".format(int(eval(equation)))}


    def aug_prob30(self):
        operator = ['+','-']
        operateA = random.choice(operator)
        operateB = random.choice(operator)
        numA = random.randint(1,1000)
        numB = random.randint(1,1000)
        if numA > numB: numA,numB=numB,numA
        numC = random.randint(1,1000)

        new_question = "{} 보다 어떤 수만큼 {} 수는 {}입니다. 어떤 수보다 {} {} 수는 얼마입니까?".format(        numA, '큰' if operateA=='+' else '작은',numB,numC, '큰' if operateB=='+' else '작은')
        if operateA == '+':
            equation = "{} - {} {} {}".format(numB,numA,operateB,numC)
        else:
            if numA < numB: numA,numB=numB,numA
            equation = "{} - {} {} {}".format(numA,numB,operateB,numC)
        return {'question':new_question, 'equation':equation, 'answer':"{}".format(int(eval(equation)))}


    def aug_prob31(self):
        numA = random.randint(0,1000)
        numB = random.randint(0,1000)
        if numA > numB: numA,numB=numB,numA
        numC = random.randint(numA,numB)

        new_question = "{}에서 {}까지의 수가 있을 때, {}보다 크고, {}보다 작은 수는 얼마입니까?".format(        numA, numB, numC,numC+2)
        equation = "( {} + {} ) / 2".format(numC, numC+2)
        return {'question':new_question, 'equation':equation, 'answer':"{}".format(int(eval(equation)))}


    def aug_prob34(self):
        numA = random.randint(0,100)
        numB = random.randint(0,100)
        if numA < numB: numA,numB=numB,numA

        personA = random.choice(people)
        new_question = "{0}와 동생의 나이를 합하면 {1}이고, 두 사람의 나이 차는 {2}입니다. {0}의 동생은 몇 살일까요?".format(personA,numA, numB,)
        equation = "( {} - {} ) / 2".format(numA, numB)
        return {'question':new_question, 'equation':equation, 'answer':"{}".format(int(eval(equation)))}


    def aug_prob35(self):
        operatorA = ['넘쳤습니다', '가득 차지 않았습니다']
        operatorB = ['많이', '적게']
        operateA = random.choice(operatorA)
        operateB = random.choice(operatorB)

        chosen = random.sample(places,2)


        new_question = "{} 컵에 물을 가득 넣어 {} 컵에 부었더니 물이 {}. 어느 컵에 물이 더 {} 들어갈까요?".format(chosen[0],chosen[1],operateA,operateB)
        if operateA =='넘쳤습니다':
            equation = "{}".format('{}'.format(chosen[0]) if operateB == '많이' else '{}'.format(chosen[1]))
        else:
            equation = "{}".format('{}'.format(chosen[1]) if operateB == '많이' else '{}'.format(chosen[0]))
        return {'question':new_question, 'equation':equation, 'answer':"{}".format(equation)}


    def aug_prob36(self):
        arrs =  [random.randint(1, 15) for _ in range(2)]
        range_val = ['두', '세']
        range_val = random.choices(range_val)[0]
        start_idx = 10 if range_val =='두' else 100
        end_idx = 100 if range_val =='두' else 1000
        new_question = "2 개의 수 {} 로 나누어 떨어질 수 있는 {} 자리 수는 모두 몇 개 있습니까?".format( ', '.join(map(str, arrs)), range_val)
        equation = "len ( [ arr for arr in range({}, {}) if arr % {} == 0 and arr % {} == 0 ] )".format(start_idx, end_idx, arrs[0], arrs[1])
        return {'question': new_question, 'equation': equation, 'answer': eval(equation)}


    def aug_prob36_(self):
        arrs = [random.randint(1, 15) for _ in range(3)]
        range_val = ['두', '세']
        range_val = random.choices(range_val)[0]
        start_idx = 10 if range_val =='두' else 100
        end_idx = 100 if range_val =='두' else 1000
        new_question = "3 개의 수 {} 로 나누어 떨어질 수 있는 {} 자리 수는 모두 몇 개 있습니까?".format( ', '.join(map(str, arrs)), range_val)
        equation = "len ( [ arr for arr in range({}, {}) if arr % {} == 0 and arr % {} == 0 and arr % {} == 0] )".format(start_idx, end_idx, arrs[0], arrs[1], arrs[2])
        return {'question': new_question, 'equation': equation, 'answer': eval(equation)}


    def aug_prob27(self):
        a = random.randint(1, 9)
        b = random.randint(1, 9)

        c = random.randint(1, 9)
        d = random.randint(1, 9)

        while True:
            if a+b != c+d:
                break
            a = random.randint(1, 9)
            b = random.randint(1, 9)
        chosen_people = random.sample(people,2)
        personA = chosen_people[0]
        personB = chosen_people[1]

        new_question = "{}이는 {}와 {}를 모았습니다. {}이는 {}과 {}을 모았습니다. 누가 모은 수가 더 큽니까?".format(personA,a, b, personB,c, d)
        equation = "'{}' if {}+{} > {}+{} else '{}'".format(personA,a, b,c, d, personB)
        return {'question': new_question, 'equation': equation, 'answer': eval(equation)}


    def aug_prob29(self):
        comp_var = ['큰', '작은']
        comp_var = random.choice(comp_var)
        N = random.randint(1, 10)
        target_val = float('{:.2f}'.format(random.uniform(1, 100)))
        arrs = [float('{:.2f}'.format(random.uniform(1, 100))) for _ in range(N)]
        new_question = "{}개의 수 {}이 있습니다. 이 중에서 {}보다 {} 수는 모두 몇 개 입니까?".format(N, ', '.join(map(str, arrs)), str(target_val), comp_var)

        if comp_var == '큰':
            equation = "len ( [ val for val in [ {} ] if val > {} ] ) ".format(', '.join(map(str, arrs)),target_val)
        else:
            equation = "len ( [ val for val in [ {} ] if val < {} ] ) ".format(', '.join(map(str, arrs)),target_val)

        return {'question': new_question, 'equation': equation, 'answer': eval(equation)}


    def aug_prob32(self):
        N = random.randrange(3, 20)
        arrs = [random.randrange(1, 100) for _ in range(N)]
        comp1 = random.choice(arrs)
        comp2 = random.choice(arrs)
        exist = False
        while not exist:
            comp1 = random.choice(arrs)
            comp2 = random.choice(arrs)
            if comp1 > comp2: comp1, comp2 = comp2, comp1
            for i in range(comp1+1,comp2):
                if i in arrs: exist = True
            

        comp_var = ['큰', '작은']
        comp_var = random.choice(comp_var)

        new_question = "주어진 숫자가 {} 일 경우 {} 보다 크고 {} 보다 작은 수 중 가장 {} 수는 무엇입니까?".format(', '.join(map(str, arrs)), comp1, comp2, comp_var)
        if comp_var == '큰':
            equation = "max ( sorted ( [ i for i in [ {} ] if i > {} and i < {} ] ) )".format(', '.join(map(str, arrs)), comp1, comp2)
        else:
            equation = "min ( sorted ( [ i for i in [ {} ] if i > {} and i < {} ] ) )".format(', '.join(map(str, arrs)), comp1, comp2)
        return {'question': new_question, 'equation': equation, 'answer': eval(equation)}


if __name__ == '__main__':
    function_list = getmembers(EQ_augment, isfunction)
    eq_aug_obj = EQ_augment()
    problem_file = open('problemsheet.augment.json','w',encoding='utf-8')
    answer_file = open('answersheet.augment.json','w',encoding='utf-8')
    idx = 100000
    dataQ = {}
    dataA = {}
    for func_name in function_list:
        print("start {}".format(func_name[0]))
        data_func = []
        attempt_try = 0
        while len(data_func) < 200 and attempt_try < 10000:
            data = eval('eq_aug_obj.{}()'.format(func_name[0]))
            if data in data_func:
                attempt_try+=1
                continue
            data_func.append(data)
            idx+=1
            question_data = {'question':data['question']}
            dataQ[str(idx)] = question_data
            answer_data = {'answer':data['answer'],'equation':data['equation']}
            dataA[str(idx)] = answer_data
        print("end {}".format(func_name[0]))

    json.dump(dataQ,problem_file,indent=4,ensure_ascii=False)
    json.dump(dataA,answer_file,indent=4,ensure_ascii=False)



    
        ############################
        #### ToDO:
        #### 1. 함수 실행 및 augmentation 
        #### 2. equation 뿐만 아니라 명칭에 대한 string augmentation 수행 
        ############################