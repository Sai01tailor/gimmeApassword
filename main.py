from random import randint, choice
from pyscript import document,window
from time import sleep
upper = "ABCDEFGHIKLMNOPQRSTVXYZ"
lower = upper.lower()
dig = "1234567890"
special = '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
ans = []

# Function to generate the password
def getit(a):
    ans.append(upper[randint(0, len(upper) - 1)])  # Uppercase letter
    ans.append(dig[randint(0, len(dig) - 1)])      # Digit
    ans.append(special[randint(0, len(special) - 1)])  # Special character
    ans.append(lower[randint(0, len(lower) - 1)])  # Lowercase letter

    for i in range(randint(8, 13) - 4):  # Add random characters (adjusting for first 4)
        k = choice([upper, lower, dig, special])
        ans.append(k[randint(0, len(k) - 1)])

    ansSTR = "".join(ans)
    ans.clear()  # Clear the list for the next generation
    document.querySelector("#password").value = ansSTR  # Set password in the input
    return ansSTR


# Function to copy the password to the clipboard using JavaScript
def copy_password(a):
    password = document.querySelector("#password").value
    window.navigator.clipboard.writeText(password)
    return msg()
 # Use the Clipboard API

# Assign event handlers to buttons
document.querySelector("#gen").onclick = getit
document.querySelector("#copy").onclick = copy_password

def msg():
      if((document.querySelector("#password").value !="")):
            window.alert("password copied")