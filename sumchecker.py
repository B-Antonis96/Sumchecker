import hashlib as hl

# Declarations
check = bool
choices = ["SHA1", "SHA256", "MD5"]
print("Select the wanted Checksum calculation:")
for i in choices:
    print(f"{choices.index(i) + 1}. {i}")

# Input
choice = int(input("Enter number to choose: "))
if 1 <= choice <= 3:
    check = True
    filename = input("Enter the location of the image please: ")
    checksha = input("Enter the given Checksum code: ")
else:
    check = False
    print("Please enter a valid number!")

# Byte passing function
def bytespasser():
    with open(filename, "rb") as file:
        bytes = file.read()
        return bytes

# Chooser function
def chooser():
    if choice == 1:
        hash = hl.sha1(bytespasser()).hexdigest()
    elif choice == 2:
        hash = hl.sha256(bytespasser()).hexdigest()
    elif choice == 3:
        hash = hl.md5(bytespasser()).hexdigest()
    return hash

# Program logic
if check:
    readable_hash = chooser()
    if readable_hash == checksha.lower():
        print("Checksum is the same!")
    else:
        print("Checksum doesn't compare, the IMAGE may be faulty!")

# End program
input("Press ENTER to continue!")
