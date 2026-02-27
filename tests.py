from colorama import Fore
def test(prom):
    c = []
    for a in prom :
        if a is None or a == " ":
            print("Found invalid empty value in price_each column.")
            break
        c.append(float(a))
    return c


b = ["20","30","44.5"," ","20"]


print(b)
r = test(b)
x = sum(r )
print(r)
print(x)
print(Fore.RED + "Error Red")
print(Fore.BLUE + "Error Blue")
print(Fore.BLACK + "Error Black")
