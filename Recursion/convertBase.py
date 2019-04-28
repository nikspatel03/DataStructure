"""
convert base function using recursion

"""

def convertBase(num, base):
    digits = "0123456789ABCDEF"
    if num < base:
        return digits[num]
    else:
        return convertBase(num // base, base) + str((num % base))

print(convertBase(25,2),"11001")
print(convertBase(10,2),"1010")
print(convertBase(25,16),"19")
