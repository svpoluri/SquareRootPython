def squareRoot(root):
    if (root >= 0):
        y = root
        x = y**.5
        answer = str(x)
        print ("Your numbers root is:" + answer)
    elif (root < 0):
        imagine = root
        x_imagine = imagine**.5
        answer_imagine = abs(x_imagine)
        answer_imagine_magnitude = str(answer_imagine)
        print ("Your numbers root is:" + answer_imagine_magnitude + "i")

user_number = input("Please input the number that you want the root of")
user_number_converted = float(user_number)

squareRoot(user_number_converted)
