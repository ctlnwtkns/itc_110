food = {'mac':{'taste':'cheesy', 'origin':'USA', 'color':'yellowNo2'}}
print(food.get('mac', 'does not exist'))
print(food.get('mac', 'dne').get('taste', 'dne'))
