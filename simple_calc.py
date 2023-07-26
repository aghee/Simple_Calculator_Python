#Simple python calculator- Add, subtract, multiply, divide, modulo in that order
#b1 branch created from main when main had two menu options only- add and subtract
#Second branch from main created, b2, this branch is at the same status as the status that main was in at the time of creating the branch
#Testing close pull request feature-push from b2
#Testing close pull request feature-push from main
#For some weird reason pull requests are no longer being created in remote when i push changes to branch. What could be the issue?
#Testing again at 'contribute dropdown'
#Sorted merge conflict
#What happens when you close a pull request?-- Changes only remain on the branch and are not merged with main 
def add(a,b):
    c=a+b
    return c
def subtract(a,b):
    f=a-b
    return f
def divide(a,b):
    j=a/b
    return j
def multiply(a,b):
    k=a*b
    return k
def modulo(a,b):
    l=a%b
    return l
print('1.Add')
print('2.Subtract')
print('3.Divide')
print('4.Multiply')
print('5.Modulo')


while True:
    g=input('enter choice from the menu listed!:')

    if g in ('1','2','3','4','5'):
        try:
            h=float(input('enter first number:'))
            i=float(input('enter second number:'))
        except ValueError:
            print('incorrect value,please try again!')
            continue
        if g=='1':
            print('The sum of the two numbers is',h ,'+', i ,'=' , add(h,i))
        elif g=='2':
            print(subtract(h,i))
        done_yet=input('are you done calculating? Y/N:')
        if done_yet=='Y':
            break
    else:
        print('Not accepted!Please select from the choices 1,2!!!') 
       
    


