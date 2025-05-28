#1) პირდაპირ გამოიყენეთ string-ებზე lower, upper, capitalize, მეთოდები კომენტარებით დაწერეთ რა არის მეთოდი რით განსხვავდება ჩვეულებრივი ფუნქციისგან, რა არის dot ნოტაცია. ასევე გააკეთეთ 3 მაგალითი find მეთოდზე, აუცილებლად უნდა იყოს 3 შემთხვევა: error, -1, რაიმე პოზიციას (index)
# lower() 
word1 = "GeOrGiA"
print(word1.lower())

# upper()
word2 = "hello"
print(word2.upper())

#capitalize()
word3 = "world"
print(word3.capitalize())  
word1 = "Georgia"
position1 = word1.find('a')
print(position1)
word2 = "Georgia"
position2 = word2.find('z')
print(position2)
word3 = "banana"
position3 = word3.find('a')
print(position3) 
word4 = "apple"
position4 = word4.find('p')
print(position4)
