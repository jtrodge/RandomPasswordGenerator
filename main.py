import random as rand

letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
numbers = ['0','1','2','3','4','5','6','7','8','9']
chars = ['!','@','#','$','%','^','&','&','(',')',',','.','?','<','>']
pwd = letters + numbers + chars
rand_pwd = []
rand.shuffle(pwd)
i = 0
while i < 9:
    rand_pwd.append(pwd[i])
    i+=1

rand_pwd.insert(rand.randint(rand.randrange(0,5), rand.randrange(5,10)), letters[rand.randrange(0,len(letters))].upper())

print(rand_pwd)
