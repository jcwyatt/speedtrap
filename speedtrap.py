import datetime
#speed trap
print("Speed Trap Calculator. Distance = 1 Mile.")

dist = 1

#t1 = input("Time through first gate : (hh:mm:ss) : ")
#t2 = input("Time through second gate : (hh:mm:ss) : ")

t1 = datetime.time(1, 2, 3)
t2 = datetime.time(2, 3, 4)

print(t2,t1)


#s1 = '10:33:26'
#s2 = '11:15:49' # for example
#FMT = '%H:%M:%S'
#tdelta = datetime.strptime(s2, FMT) - datetime.strptime(s1, FMT)