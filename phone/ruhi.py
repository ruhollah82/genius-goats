n = int(input())

numbers = []

for i in range(n):
    numbers.append(input())
    
def check(number):
    return number.isdigit()
    

def control(number) :
    if len(number) == 13 and number[0:3] == "+98" and check(number[1:]):
         return number
    elif len(number) == 12 and check(number) and number[0:2] == "98":    
         return "+"+number
    elif len(number) == 11 and check(number) and number[0:2] == "09":
          return "+98" + number[1:]
   
    return "invalid"
    
for i in range(n):
    numbers[i] = control(numbers[i])
    
for a in numbers:
    print(a)