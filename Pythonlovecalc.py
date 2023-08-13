# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
name12 = name1.lower()
name22 = name2.lower()

t1,t2 = name12.count("t"), name22.count("t")
r1, r2 = name12.count("r"), name22.count("r")
u1,u2 = name12.count("u"), name22.count("u")
e1,e2 =name12.count("e"), name22.count("e")

l1,l2 = name12.count("l"),name22.count("l")
o1,o2 = name12.count("o"), name22.count("o")
v1,v2 =name12.count("v"), name22.count("v")
e1,e2 =name12.count("e"), name22.count("e")

t3 = t1 + t2
r3 = r1+r2
u3 = u1+u2
e3 = e1+e2
true = (t3+r3+u3+e3)*10

l3=l1+l2
o3=o1+o2
v3=v1+v2
e3=e1+e2
love = l3+o3+v3+e3

score = true + love

if score<10 or score>90:
    print(f"Your score is {score}, you go together like coke and mentos.")
elif 40<score<50 :
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}.")
