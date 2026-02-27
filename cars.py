yes = input("yesteraday: ")
tod = input("today: ")
list(yes)
list(tod)
res = 0
for i in yes:
    if i in tod:
        res +=1