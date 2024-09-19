'''
Tracy Ye
JST
SoftDev
Friday's activity on python dictionaries. How to return a random output in dictionary?
2024-09-16
<Time spent>
'''
import random

krewes = {
           4: [ 
		'DUA','TAWAB','EVA','JACK','VICTOR','EVAN','JASON','COLYI','IVAN','TANZEEM',
		'TAHMIM','STANLEY','LEON','NAOMI','NIA','ANASTASIA','JADY','BRIAN','JACOB',
		'ALEX','CHONGTIAN','DANNY','MARCO','ABIDUR','ANKITA','ANDY','ETHAN','AMANDA',
		'AIDAN','LINDA','QIANJUN','JIAYING','KISHI'
		],
           5: [ 
                'ADITYA','MARGIE','RACHEL','ALEXANDER','ZIYAD','DANNY','ENDRIT','CADEN',
                'VEDANT','SUHANA','KYLE','KEVIN','RAYMOND','CHRISTOPHER','JONATHAN','SASHA',
                'NAFIYU','TIM','WILL','DANIEL','BENJAMIN','CLAIRE','CHLOE','STELLA','TRACY',
                'JESSICA','JACKIE','WEN YUAN','YINWEI','TIFFANY','JAYDEN DANIEL','PRINCEDEN' 
              ]
         }

def dict():
    period = random.choice(list(krewes))
    return random.choice(krewes[period])
    
# print(dict())

def dictInt():
    keyLen = len(krewes.keys())
    randomKey = random.randint(0,keyLen)
    key = list(krewes.keys())[randomKey]
    
    valuesLen = len(krewes[key])
    randomValue = random.randint(0,valuesLen)
    value = krewes[key][randomValue]
    return value
    
print(dictInt())
