from django.shortcuts import render
from django.http import HttpResponse


def home(req):
    if req.method == 'POST':
        a = list(range(0,10))
        inputt = req.POST['input'].split()

        def div(x,y):
            return x/y

        def mul(x,y):
            return x*y

        def add(x,y):
            return x+y

        def sub(x,y):
            return x-y



        for i in range(len(inputt)):
            if '/' in inputt:
                pos = inputt.index('/')
                num1 = float(inputt[pos-1])
                num2 = float(inputt[pos+1])
                inputt.pop(pos-1)
                inputt.pop(pos)
                inputt.pop(pos-1)
                x = div(num1,num2)
                inputt.insert(pos-1,x)
             
        
        for i in range(len(inputt)):
            
            if 'x' in inputt:
                pos = inputt.index('x')
                num1 = float(inputt[pos-1])
                num2 = float(inputt[pos+1])
                inputt.pop(pos-1)
                inputt.pop(pos)
                inputt.pop(pos-1)
                x = mul(num1,num2)
                inputt.insert(pos-1,x)
                
        for i in range(len(inputt)):
            
            if '+' in inputt:
                pos = inputt.index('+')
                num1 = float(inputt[pos-1])
                num2 = float(inputt[pos+1])
                inputt.pop(pos-1)
                inputt.pop(pos)
                inputt.pop(pos-1)
                x = add(num1,num2)
                inputt.insert(pos-1,x)
                
        for i in range(len(inputt)):
            
            if '-' in inputt:
                pos = inputt.index('-')
                num1 = float(inputt[pos-1])
                num2 = float(inputt[pos+1])
                inputt.pop(pos-1)
                inputt.pop(pos)
                inputt.pop(pos-1)
                x = sub(num1,num2)
                inputt.insert(pos-1,x)


        ans = inputt[0]

        return render(req,'cal.html',{'numbers':a,'ans':ans})

    elif req.method == 'GET':

        a = list(range(0,10))
        return render(req,'cal.html',{'numbers':a})