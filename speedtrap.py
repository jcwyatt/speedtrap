import datetime as dt
#speed trap

def timeValidate(t):

	#check the length
	if len(t) != 8:
		print(t, "invalid length, must be hh:mm:ss")
		return False

	#check for numbers in the right places

	numPosns=(0,1,3,4,6,7)
	for i in numPosns:
		if not t[i].isnumeric():
			print (t,"invalid time format, must be numeric eg 01:04:02.")
			return False

	#check values are valid times
	if int(t[0:2])>23 or int(t[3:5])>59 or int(t[6:8])>59:
		print(t,"invalid time. Check values for hours, minutes, seconds.")
		return False

	#check format has correct separators:
	colonPosns=(2,5)
	for i in colonPosns:
		if t[i]!=":":
			print (t, "invalid separator. Must be ':'")
			return False

	return True


print("Speed Trap Calculator. \nDistance = 1 Mile.")

dist = 1
#input("All times are 6 digit 24hr format, eg:03:44:02\nPress 'Enter' key to continue.")
#t1 = input("Enter time through first gate : (hh:mm:ss) : ")
#t2 = input("Enter time through second gate : (hh:mm:ss) : ")

#print(t2,t1)

s1 = '00:06:00'
s2 = '00:06:08' # for example

#validate the times
valid = timeValidate(s1)
valid = timeValidate(s2)

#convert to timedeltas
t1 = dt.timedelta(hours=int(s1[0:2]),minutes=int(s1[3:5]),seconds=int(s1[6:8]))
t2 = dt.timedelta(hours=int(s2[0:2]),minutes=int(s2[3:5]),seconds=int(s2[6:8]))

elapsedSeconds = (t2-t1).total_seconds()

print('time',elapsedSeconds,'s')

speed = int(1*3600/elapsedSeconds)
print ("Speed =",speed,"mph")


