# # O'zgaruvchi nomlari

username = "Barchinoy Normuhammadova"
userName = "Shahrizoda Ergasheva"
user_name = "Lola Tursunova"
user_Name = "Umida Azizova"
UserName = "admin"
Username = "admin2"
USERNAME = "admin3"
User_name = "admin4"

print(username)
print(userName)
print(ser_name)
print(user_Name)
print(UserName)
print(Username)
print(USERNAME)
print(User_name)

# "string" ma'lumot turi

your_firsname = "Barchinoy"
your_lastname = "Normuhammadova"
your_skills = """computer literacy,
# chess game"""

print(your_firsname)
print(your_lastname)
print(your_skills)

# Maxsus belgilar

symbole = 'Qur\'on\nQo\'shiq\nShe\'r'
symbole_2 = "\tkompyuter"
print(symbole)
print = symbole_2

# f-string
firstname = "Barchinoy"
age = 19
full_info = f"My name is {firstname}. My age: {age}"
print(full_info)

#or
firsname = "Barchinoy"
age = 19
full_info = "My name is {}. My age: {}".format(firsname, age)
print(full_info)

 #or
full_info =  "My name is {firstname}. My age: {age}". format(firsname= "Barchinoy", age=19)
print(Full_info)

 #or % belgisidan foydalanish
print("My name is %s. My age: %d" % ("Barchinoy", 19))

#string metodlari
print("Developer".upper())
print("Developer".lower())
print("Developer Junior".capitalize())
print("Developer Junior".title())
print("Developer Junior".split(''))
print("   Developer".lstrip())
print("Developer    ".rstrip())
print("  Developer    ".strip())
print("".zfill(5))
print("-".join(Developer))
print("Developer".count("e"))
print("Developer".index("l"))
print(len("Developer"))
print("Developer"[0:6])
print("Developer"[0:])
print("Developer"[:-3])
print("Developer"[::3])
print("Developer"[::-1])

#Raqamlar
#integer
age = 19
price = 200 + 500
print(age)
#float
temp = 26.6
pi = 3.2026
print(type(temp))
#complex
z = complex(6,3)
print(type(z))

#boolean
isCool = False
isHot = True
4>2 #True
4<2 #False
4 == 2 #False
Print(3>2)
