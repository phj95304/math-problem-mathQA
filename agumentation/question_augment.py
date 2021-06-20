import random
import math
from inspect import getmembers, isfunction

class EQ_augment():
    
    def aug_prob1():
        a = random.randint(1, 100)
        b = random.randint(1, 100)
        new_question = "상자 안에 {}개의 공이 있습니다. 석진이가 {}개의 공을 상자 안에 더 넣었습니다. 상자 안에 있는 공은 모두 몇 개입니까?".format(a, b)
        equation = "{} + {}".format(a, b)
        return {'question':new_question, 'equation':equation, 'answer':"{}".format(eval(equation))}


    def aug_prob2():
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


    def aug_prob3():
        a = random.randint(1, 300)
        b = random.randint(1, 300)
        new_question = "한 상자에는 감이 {}개씩 들어있습니다. {}개의 상자 안에 있는 감은 모두 몇 개일까요?".format(a, b)
        equation = "{} * {}".format(a, b)

        return {'question':new_question, 'equation':equation, 'answer':"{}".format(eval(equation))}


    def aug_prob4():
        a = random.randint(1,100)
        b=  random.randint(1,100)
        c=  random.randint(1,100)
        d=  random.randint(1,100)
        e = random.randint(1,100)

        new_question = "지민, 정국, 태형이의 수학 점수는 각각 {}점, {}점, {}점입니다. 이 셋을 제외한 학급의 수학 점수 평균은 {}점입니다. 지민이네 학급 인원수가 {}명일 때, 학급 수학 평균 점수는 몇 점입니까".format(a, b, c, d, e)
        equation = "( ( {} - {} ) * {} + {} + {} + {} ) / {}".format(e, 3, d , a, b, c, e)

        if isinstance(eval(equation),int):
            return {'question':new_question, 'equation':equation, 'answer':"{}".format(eval(equation))}
        return {'question':new_question, 'equation':equation, 'answer':"{:.2f}".format(eval(equation))}


    def aug_prob5():
        a = random.randint(1,100)
        b=  random.randint(1,100)
        if a < b: a,b=b,a
        new_question = "{}명의 학생들이 한 줄로 줄을 섰습니다. 윤기의 앞에 {}명의 학생들이 서 있습니다. 윤기의 뒤에 서 있는 학생은 몇 명입니까?".format(a,b)
        equation = "{} - ( {} + 1 )".format(a,b)

        return {'question':new_question, 'equation':equation, 'answer':"{}".format(eval(equation))}


    def aug_prob6():
        a = random.randint(1,100)
        new_question = "달리기 시합에서 남준이는 {} 등을 했고, 윤기는 {} 등을 했습니다. 호석이는 윤기보다 잘했지만 남준이보다는 못했습니다. 호석이의 등수는 몇 등입니까?".format(a, a+2) 
        equation = " ( {} + {} ) / 2".format(a, a+2)
        return {'question':new_question, 'equation':equation, 'answer':"{}".format(int(eval(equation)))}


    def aug_prob7():
        a = random.randint(1, 100)
        b = random.randint(1, 100)
        if a < b: a,b = b,a
        new_question = "키가 작은 사람부터 순서대로 {}명이 한 줄로 서 있습니다. 호석이가 앞에서부터 {}번째에 서 있습니다. 키가 큰 사람부터 순서대로 다시 줄을 서면 호석이는 앞에서부터 몇 번째에 서게 됩니까?".format(a, b)
        equation = "{} - {} + 1".format(a, b)
        return {'question':new_question, 'equation':equation, 'answer':"{}".format(eval(equation))}


    def aug_prob9():
        num_to_jarisu = {1:'한', 2:'두', 3:'세', 4:'네', 5:'다섯', 6:'여섯', 7:'일곱', 8:'여덟', 9:'아홉'}
        num = random.randint(1, 9)
        arrs = list(set([random.randint(1,9) for _ in range(num)]))
        new_question = "{}개의 숫자 ".format(len(arrs)) +  " ,".join(["{}"]*len(arrs)).format(*arrs) + "를 한 번씩만 사용하여 {} 자리수를 만들려고 합니다. 만들 수 있는 {} 자리 수는 모두 몇 개입니까?".format(num_to_jarisu[len(arrs)], num_to_jarisu[len(arrs)])
        equation = "math.factorial({})".format(len(arrs))
        return {'question':new_question, 'equation':equation, 'answer':"{}".format(eval(equation))}


    def aug_prob10():
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


    def aug_prob11():
        N = random.randint(1, 10)
        arrs = [random.randint(1, 100) for _ in range(N)]
        new_question = "{}개의 수 {}가 있습니다. 그 중에서 가장 큰 수와 가장 작은 수의 차는 얼마입니까?".format(N, ' ,'.join(map(str, arrs)))
        equation = "max ( [ {} ] ) - min ( [ {} ] ) ".format(' , '.join([str(i) for i in arrs]), ' , '.join([str(i) for i in arrs]))
        return {'question':new_question, 'equation':equation, 'answer':"{}".format(eval(equation))}


    def aug_prob12():
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


    def aug_prob16():
        operator = ['+','-']
        numB = random.randint(1,10)
        operate = random.choice(operator)
        if operate =='+':
            numA = random.randint(10,100)
            new_question =         "서로 다른 두 자연수 A , B가 있습니다. A {} B = {}, B = {} * A 일 때, A 를 구하시오.".format(                                                                                 operate,numA,numB)
        else:
            numA = -random.randint(10,100)
            new_question =         "서로 다른 두 자연수 A , B가 있습니다. A {} B = -{}, B = {} * A 일 때, A 를 구하시오.".format(                                                                                 operate,numA,numB)
        equation= "{} / ( {} {} {} )".format(numA,1,operate,numB)
        if isinstance(eval(equation),int):
            return {'question':new_question, 'equation':equation, 'answer':"{}".format(eval(equation))}
        return {'question':new_question, 'equation':equation, 'answer':"{:.2f}".format(eval(equation))}


    def aug_prob17():
        operator = ['+','-']

        numA = random.randint(1,1000)
        numB = random.randint(1,1000)
        numC = random.randint(1,1000)
        operateA = random.choice(operator)
        operateB = random.choice(operator)
        new_question =     "어떤 수에서 {}을 {}야 하는데 잘못하여 {}을 {} 결과가 {}이 나왔습니다. 바르게 계산한 결과를 구하시오.".format(            numA,'더해' if operateA=='+' else '빼', numB, '더한' if operateB=='+' else '뺀', numC)
        equation = "{} {} {} {} {}".format(numC,'+' if operateB == '-' else '-',numB,operateA,numA)

        return {'question':new_question, 'equation':equation, 'answer':"{}".format(eval(equation))}


    def aug_prob19():
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


    def aug_prob20():
        operatorA = ['+','-', '*']

        numA = random.randint(1,1000)
        numB = random.randint(1,1000)
        numC = random.randint(1,100)
        operateA = random.choice(operatorA)
        new_question =     "{}에 어떤 수를 {}야 할 것을 잘못하여 {}에 어떤 수를 곱했더니 {}이 되었습니다. 바르게 계산하면 얼마인지 구하시오.".format(    numA,'더해' if operateA=='+' else ('빼' if operateA=='-' else '곱해'),            numB,numB*numC)
        equation = "{} {} ( {} / {} ) ".format(numA,operateA,numB * numC,numB)

        return {'question':new_question, 'equation':equation, 'answer':"{}".format(int(eval(equation)))}


    def aug_prob21():
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


    def aug_prob30():
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


    def aug_prob31():
        numA = random.randint(0,1000)
        numB = random.randint(0,1000)
        if numA > numB: numA,numB=numB,numA
        numC = random.randint(numA,numB)

        new_question = "{}에서 {}까지의 수가 있을 때, {}보다 크고, {}보다 작은 수는 얼마입니까?".format(        numA, numB, numC,numC+2)
        equation = "( {} + {} ) / 2".format(numC, numC+2)
        return {'question':new_question, 'equation':equation, 'answer':"{}".format(int(eval(equation)))}


    def aug_prob34():
        numA = random.randint(0,100)
        numB = random.randint(0,100)
        if numA < numB: numA,numB=numB,numA

        new_question = "윤기와 동생의 나이를 합하면 {}이고, 두 사람의 나이 차는 {}입니다. 윤기의 동생은 몇 살일까요?".format(        numA, numB,)
        equation = "( {} - {} ) / 2".format(numA, numB)
        return {'question':new_question, 'equation':equation, 'answer':"{}".format(int(eval(equation)))}


    def aug_prob35():
        operatorA = ['넘쳤습니다', '가득 차지 않았습니다']
        operatorB = ['많이', '적게']
        operateA = random.choice(operatorA)
        operateB = random.choice(operatorB)

        new_question = "(가) 컵에 물을 가득 넣어 (나) 컵에 부었더니 물이 {}. 어느 컵에 물이 더 {} 들어갈까요?".format(        operateA,operateB)
        if operateA =='넘쳤습니다':
            equation = "{}".format('(가)' if operateB == '많이' else '(나)')
        else:
            equation = "{}".format('(나)' if operateB == '많이' else '(가)')
        return {'question':new_question, 'equation':equation, 'answer':"{}".format(equation)}


    def aug_prob11():
        arrs =  [random.randint(1, 15) for _ in range(2)]
        range_val = ['두', '세']
        range_val = random.choices(range_val)[0]
        start_idx = 10 if range_val =='두' else 100
        end_idx = 100 if range_val =='두' else 1000
        new_question = "2 개의 수 {} 로 나누어 떨어질 수 있는 {} 자리 수는 모두 몇 개 있습니까?".format( ', '.join(map(str, arrs)), range_val)
        equation = "len ( [ arr for arr in range({}, {}) if arr % {} == 0 and arr % {} == 0 ] )".format(start_idx, end_idx, arrs[0], arrs[1])
        return {'question': new_question, 'equation': equation, 'answer': eval(equation)}


    def aug_prob35():
        arrs = [random.randint(1, 15) for _ in range(3)]
        range_val = ['두', '세']
        range_val = random.choices(range_val)[0]
        start_idx = 10 if range_val =='두' else 100
        end_idx = 100 if range_val =='두' else 1000
        new_question = "3 개의 수 {} 로 나누어 떨어질 수 있는 {} 자리 수는 모두 몇 개 있습니까?".format( ', '.join(map(str, arrs)), range_val)
        equation = "len ( [ arr for arr in range({}, {}) if arr % {} == 0 and arr % {} == 0 and arr % {} == 0] )".format(start_idx, end_idx, arrs[0], arrs[1], arrs[2])
        return {'question': new_question, 'equation': equation, 'answer': eval(equation)}


    def aug_prob27():
        a = random.randint(1, 9)
        b = random.randint(1, 9)

        c = random.randint(1, 9)
        d = random.randint(1, 9)

        while True:
            if a+b != c+d:
                break
            a = random.randint(1, 9)
            b = random.randint(1, 9)

        new_question = "정국이는 {}와 {}를 모았습니다. 지민이는 {}과 {}을 모았습니다. 누가 모은 수가 더 큽니까?".format(a, b, c, d)
        equation = "'정국' if {}+{} > {}+{} else '지민'".format(a, b, c, d)
        return {'question': new_question, 'equation': equation, 'answer': eval(equation)}


    def aug_prob29():
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


    def aug_prob32():
        N = random.randrange(3, 10)
        arrs = [random.randrange(1, 100) for _ in range(N)]
        comp1 = random.randrange(1, 100)
        comp2 = random.randrange(1, 100)

        if comp1 > comp2: comp1, comp2 = comp2, comp1

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
    for func_name in function_list:
        print(func_name)
        
        ############################
        #### ToDO:
        #### 1. 함수 실행 및 augmentation 
        #### 2. equation 뿐만 아니라 명칭에 대한 string augmentation 수행 
        ############################