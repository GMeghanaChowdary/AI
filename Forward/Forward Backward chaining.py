global facts 
global rules 
rules = True
facts =[["plant","mango"],["eating","mango"], ["seed","sprouts"]]

def assert_fact(fact): 
    global facts 
    global rules 
    if not fact in facts: 
        facts+=[fact] 
        rules=True 
while rules: 
    rules=False 
    for A1 in facts: 
        if A1[0]=="seed": 
               assert_fact(["plant",A1[1]]) 
        if A1[0]=="plant": 
                assert_fact(["fruit",A1[1]]) 
        if A1[0]=="plant" and ["eating",A1[1]] in facts: 
                assert_fact(["human",A1[1]])
