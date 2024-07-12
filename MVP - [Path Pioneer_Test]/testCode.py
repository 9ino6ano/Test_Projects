text = "Yoooooooooo\nThis is some text \nHave A Good One!!\n "
text2 = "Have a nice day!! See ya"

name = "John Doe"
email = "JohnDoe@gmail.com"
field = "Network"
Expert_level = "Beginner"

user_profile = [
   {'name: ' + name,
    'email: ' + email,
    'field: ' + field,
    'level of expertise: ' +Expert_level}
]

print(str(user_profile.name))

with open('PyTest.txt', 'w') as file:
   file.write(text+"\n")
with open('PyTest.txt', 'a') as file:
   file.write(text2+"\n")
   print()
   file.write(str(user_profile)+"\n")
