#მომხარებელს შემოატანინე 2 რიცხვი, შემდეგ პირველ შემოტანილი რიცხვიდან მეორე შემოატილ რიცხვამდე, დაითვალე ყველა ლუწი რიცხვების ჯამი
number = int(input("enter number: "))
number2 = int(input("enter number2: "))
number3 = 1
 
for i in range(number,number2):
     if i % 2 == 0:
         number3 += i
print(number3)