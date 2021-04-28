"""
Task 1

String manipulation

Write a Python program to get a string made of the first 2
 and the last 2 chars from a given string. If the string length is less than 2,
  return instead of the empty string.

Sample String: 'helloworld'

Expected Result : 'held'

Sample String: 'my'

Expected Result : 'mymy'

Sample String: ' x'

Expected Result: Empty String

Tips:

Use built-in function len() on an input string
Use positive indexing to get the first characters of a
string and negative indexing to get the last characters
"""
if __name__ == '__main__':
    while True:
        s1 = input("enter word-")
        if len(s1) >= 2:
            print(s1[0:2], s1[-1:-3:-1], sep="")
            break
        else:
            print("enter word with 2 or more")

"""
Task 2

The valid phone number program.

Make a program that checks if a string is in the right format for a phone number. 
The program should check that the string contains only numerical characters and is only 10 characters long.
 Print a suitable message depending on the outcome of the string evaluation.
"""
if __name__ == '__main__':
    tel = input("введіть свій номер телефону-")
    x = tel.isdigit()
    y = len(tel)
    while True:
        if x and y == 10:
            print("ok")
            break
        else:
            print("not ok\n введіть ще раз")
            tel = input("введіть свій номер телефону-")
"""
Task 3

The name check.

Write a program that has a variable with your name stored (in lowercase) and then asks for your name as input.
 The program should check if your input is equal to the stored name even if the given name has another case, e.g.,
 if your input is “Anton” and the stored name is “anton”, it should return True.
"""
if __name__ == '__main__':
    name = "Nika"
    name1 = input("enter name")
    flag = name1.find(name)
    print(flag)
"""
задача з зірочкою
дзвінок оператора
        

"""
if __name__ == '__main__':
    '''print(input(" вас звати надя?").find("yes"))'''
    if input(" вас звати надя?").find("yes") == 1:
        print(" вам зручно розмовляти?", end='')
        if input().find("yes") == 1:
            print(" ви робили за мовлення в магазині ххх")
            if input("ви замовляли ***?").find("yes") == 1:
                print("ваша адреса ###", end='')
                if input().find("yes") == 1:
                    print("добре, тоді ваше заповлення прибуде через два дні за адресою ###\nдо побачення")
                else:
                    print(f"вкажіть нову адресу-{input()}\nдо побачення")

            else:
                print("відкоректувати замовлення")
        else:
            print("добре, тоді я передзвоню вам пізніше")
            input("коли вам буде зручно розмовляти?")
    else:
        print("перепрошую, я помилилася номером")








