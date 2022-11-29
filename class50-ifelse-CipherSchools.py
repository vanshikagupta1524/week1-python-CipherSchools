 


age=input("please input your age:")
age=int(age)

if age==0 or age<0 :
    print("you cant watch")

if 0<age<=3:
    print("Ticket price : Free")

elif 3<age<=10:
    print("Ticket price : 150") 

elif 10<age<=60:
    print("ticket price: 250")

else:
    print("Ticket")