num = 0

answer = input("what would you like to convert to?")

if answer == "celsius":
    num = int(input("how many degrees ferenheit is it?"))
elif answer == "ferenheit":
    num = int(input("how many degrees celsius is it?"))
else:
    print("the answer is not valid")

cel = num*1.8+32
fer = (num-32)*(5/9)

if answer == "celsius":
    print(fer)
elif answer == "ferenheit":
    print(cel)
else:
    print(" ")