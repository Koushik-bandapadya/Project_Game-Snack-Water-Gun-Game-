import random

def gamewin(comp,you):
    if comp==you:
        return None
    if comp=='s':
        if you=='w':
            return False
        elif you=='g':
            return True
    if comp=='w':
        if you=='g':
            return False
        elif you=='s':
            return True
    if comp=='g':
        if you=='s':
            return False
        elif you=='w':
            return True


print("Comp Turn: Snake(s) Water(w) or Gun(g)?")
randNo=random.randint(1,3)

if randNo==1:
    comp='s'
elif randNo==2:
    comp='w'
elif randNo==3:
    comp='g'

you=input("Your Turn: Snake(s) Water(w) or Gun(g)?" )

a=gamewin(comp,you)

print(f"\n Computer chosse:{comp}\n")
print(f"Computer chosse:{you}\n")

if a==None:
    print("The game is a tie!")
elif a:
    print("You Win!")
else:
    print("You lose!")

