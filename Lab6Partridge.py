def decoder(encoded_password):
    decoded_password = ""

    for digit in encoded_password:
        if int(digit) == 0:
            decoded_password += "7"
        elif int(digit) == 1:
            decoded_password += "8"
        elif int(digit) == 2:
            decoded_password += "9"
        else:
            decoded_password += str(int(digit) - 3)

    return decoded_password