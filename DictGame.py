dic = {}
lst_win = []
lst_rec = []
while True:
    name = input("Enter the name of team(enter q for quit)=")
    if name == "Q" or name == "q":
        print()
        break
    else:
        win = int(input('Enter the no of win match='))
        loss = int(input("Enter the no of loss match="))
        print()
        dic[name] = [win, loss]
        lst_win.append(win)
        if win > 0:
            lst_rec += [name]

nam = input("Enter the name of team for winning=")
print("Winning percentage=", dic[nam][0] * 100 / (dic[nam][0] + dic[nam][1]))
print()
print("Winning list of all team=", lst_win)
print("Team who has winning records are ", lst_rec)
