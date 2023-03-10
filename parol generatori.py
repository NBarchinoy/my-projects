import random
belgilar = '+-/*!@#$%^&*qwertyuioplkjgfdsazxcvbnm1234567890QWERTYUIOPLKJHGFDSAZXCVBNM'
# nomer = input('Parollar sonini kiriting:/n>>>')
uzunligi = input('Parol necha xonadan iborat bo\'lsin:/n>>>')
uzunligi = int(uzunligi)
# nomer = int(nomer)

# for n in range(nomer):
password = ''
for i in range(uzunligi):
  password += random.choice(belgilar)

print(password)