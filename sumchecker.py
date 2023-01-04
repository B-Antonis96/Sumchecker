import hashlib as hl

# Class: Terminal Colors
class TermColors:
    RIGHT = '\033[92m'
    WRONG = '\033[91m'
    DEFAULT = '\033[0m'

# Declarations
check = bool
choices = ["SHA1", "SHA256", "SHA512", "MD5"]
print("Select the wanted Checksum calculation:")
for i in choices:
    print(f"{choices.index(i) + 1}. {i}")

# Input
choice = int(input("Enter number to choose: "))
if 1 <= choice <= 4:
    check = True
    filename = input("Enter file location: ")
    checksha = input("Enter Checksum code: ")
else:
    check = False
    print("Please make a valid choice!")

# Byte passing function
def bytespasser():
    with open(filename, "rb") as file:
        bytes = file.read()
        return bytes

# Chooser function
def chooser():
    match choice:
        case 1:
            hash = hl.sha1(bytespasser()).hexdigest()
        case 2:
            hash = hl.sha256(bytespasser()).hexdigest()
        case 3:
            hash = hl.sha512(bytespasser()).hexdigest()
        case 4:
            hash = hl.md5(bytespasser()).hexdigest()
    return hash

# Program logic
if check:
    readable_hash = chooser()
    if readable_hash == checksha.lower():
        print(f"{TermColors.RIGHT}OK!{TermColors.DEFAULT}")
    else:
        print(f"{TermColors.WRONG}NOT VALID!{TermColors.DEFAULT}")

# End program
input("Press ENTER to continue!")

