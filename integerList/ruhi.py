myDict = {}
MyList = []

n = input()
n = int(n)


a = map(int,input().split())
MyList = list(a)

for x in MyList:
    if x in myDict:
        myDict[x] += 1
        print("True")
        exit()
    else:
        myDict[x] = 1

print("False")
