#მომხმარებელს შემოატანინეთ რიცხვი და 0-დან ამ რიცხცამდე დაპრინტეთ ყველა რიცხვი.
for i in range(100):
     print(i)
 
#მომხმარებლის შემოტანილ რიცხვამდე ყველა რიცხვი შეკრიბეთ.
for i in range(50):
     print(i + 50)

#მომხმარებლის შემოტანილ რიცხვამდე 3-ის გამოტოვებით დაპრინტეთ ყველა რიცხვი
for i in range(1,50,3):
     print(i)

#მომხმარებლის შემოტანილ რიცხვამდე 4-ის გამოტოვებით დაპრინტეთ ყველა რიცხვიs ნამრავლი
for i in range(1,50,4):
     print(i * 4)

#მომხარებელს შემოატანინე 2 რიცხვი, შემდეგ პირველ შემოტანილი რიცხვიდან მეორე შემოატილ რიცხვამდე, დაითვალე ყველა ლუწი რიცხვების ჯამი

name = input('enter number: 2 4 6 8')
name2 = input('enter number: 2 4 6 8')
print(name + name2)

#მომხარბელს შემოატანინე სიტყვა მანამ სანამ არ შემოიტანს Guram
name = input("enter name")
while  name != "gurami":
  input("again")

#მომხარებელს შემოატანინე რიცხვი მანამ სანამ უარყოფითს არ შემოიტანს
name = input("enter number")
while name != -1:
     name = input("again")
 
#მომხარებელს შემოატანინე რიცხვი, მანამ სანამ 5 ს არ შემოიტანს და შემდეგ როცა შემოიტანს 5 სდაპირნტეთ "Guram teacher"
number = input("enter number")
while number == 5:
     print("Gurami Teacher")
else:
     number = input("enter number")
    
#მომხარებელს შემოატანინეთ პინკოდი, სანამ 9877 არ შეიტანს,და როცა შეიტანს გამოიტანოს მისი მცდელობების რაოდენება გამრავლებული 2 ზე
pin = input("enter number")
password = pin +1
while pin == 9877:
     print(password)
 
