#encode password by adding 3 to each digit- Brianna Chua
def encoder(password):
    new_password = ''
    for i in password:
        new_password = new_password + str(int(i) + 3)
    return new_password

#decode password - Andrew Grachoff
def decoder(encodedPassword):
    decodedPassword = []
    for c in encodedPassword:
        if int(c) > 3:
            decodedPassword.append(str(int(c) - 3))
        else:
            decodedPassword.append(str(int(c) + 7))

    return "".join(decodedPassword)

#main menu display and option action- Brianna Chua
if __name__ == '__main__':
    encoded_password = ''
    while True:
        print("Menu")
        print("--------------")
        print("1. Encoder")
        print("2. Decoder")
        print("3. Quit")

        user_input = int(input("Please enter an option: "))

        if user_input == 1:
            password = input("Please enter your password to encode? ")
            encoded_password = encoder(password)
            print("Your password has been encoded and stored!")
            continue
        if user_input == 2:
            print("The encoded password is "+ encoded_password + " and the original password is " + decoder(encoded_password))
            continue
        if user_input == 3:
            break
