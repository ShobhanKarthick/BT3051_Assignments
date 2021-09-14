def getSubString(string, x, y, w, z):

    try:
        x=int(x)
        y=int(y)
        w=int(w)
        z=int(z)
    except:
        return "Invalid input, only numbers accepted for x, y, w, z"

    if (y > len(string)):
        return "y is larger than length of string! Why would you do that?"

    if (z > len(string)):
        return "z is larger than length of string! Why would you do that?"
    
    if (x > (len(string) - y)):
        return str(x) + " charcters not available after position" + str(y)
    if (w > (len(string) - z)):
        return str(w) + " charcters not available after position" + str(z)
    else:
        return [string[y:(y+x)], string[z:(z+w)]]
   
string = input("Enter your string:")
x = input("Enter your x:")
y = input("Enter your y:")
w = input("Enter your w:")
z = input("Enter your z:")

output = getSubString(string, x, y, w, z)
if(type(output) == list):
    print(output[0], output[1])
else:
    print(output)
