def decoder(encoded, n):
    decoded = ""

    for i in range(len(encoded)):
        if(encoded[i] == " "):
            decoded += " "
        else:
            if(encoded[i].isupper()):
                decoded += chr(((ord(encoded[i]) + n - 65) % 26) + 65)
            else:
                decoded += chr(((ord(encoded[i]) + n - 97) % 26) + 97)

    return decoded

if __name__ == "__main__":
    fin = open("q5_test.txt")
    data = fin.read().splitlines()
    fin.close()

    data[1] = int(data[1])
    text, n = data

    decoded = decoder(text, n)
    print(decoded)
