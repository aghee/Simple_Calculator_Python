#Simple python calculator- Add, subtract, multiply, divide, modulo in that order
def add(a,b):
    c=a+b
    return c
def subtract(a,b):
    f=a-b
    return f
print('1.Add')
print('2.Subtract')

while True:
    g=input('enter choice from the menu listed!:')

    if g in ('1','2'):
        try:
            h=float(input('enter first number:'))
            i=float(input('enter second number:'))
        except ValueError:
            print('incorrect value,please try again!')
            continue
        if g=='1':
            print(add(h,i))
        elif g=='2':
            print(subtract(h,i))
        done_yet=input('are you done calculating? Y/N:')
        if done_yet=='Y':
            break
    else:
        print('Not accepted!Please select from the choices 1,2!!!') 
       
    


