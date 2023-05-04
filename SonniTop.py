from random import randint
o = randint(1,10)
k=1
while o>0:

    a = int(input("o`ylagan soninggizni kiriting "))
    if a>o:
        print("o`ylagam sonim bundan kichik ")
    if a<o:
        print("o`ylagan sonim bundan katta ")
    if a==o:
        print("Tabriklaymiz! siz topdingiz ")
        print(f'siz {k} ta urinishda topdingiz')
        print("Yana o`ynaysizmi? ha/yoq")
        g = input("ha/yoq-->")
        if g == "ha":
            continue
        else:
            break
    k = k + 1
print("endi siz bir son o`ylang [1,10]")
while o>0:
 print(o)

h = input("tog'ri/katta/kichik-->")
if h=='katta':
    a = randint(o,10)
print(a)
if h=='kichik':
    b = randint(1,o)

print(b)
if h=='togri':
     beak



