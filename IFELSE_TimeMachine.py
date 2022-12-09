name = input()
if name == 'Trung':
    print("Wellcome home Mr.Trung")
    print("How ol r u")
    age = int(input())
    if age == 20:
        print("U r at 2022")
    elif age > 20:
        print("U r in the future")
    else:
        print("U r in the past")
else:
    print("Hello, how can i help u")
    guest = input()
    print("I dont have any idea about:\""+guest+"\"")
