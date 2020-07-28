y=int(input("Enter the year:"))
m=int(input("Enter the month:"))
if(m<=0 or m>12):
    print("Invalid month")
elif(m==1 or m==3 or m==5 or m==7 or m==8 or m==10 or m==12):
    print("Number of days is 31")
elif((m==2) and (y%4)==0 and (y%400)==0 or (y%100)!=0):
    print("Number of days is 29")
elif(m==2):
    print("Number of days is 28")
else:
    print("Number of days is 30")
