print('''1>ADD
2>SUBTRACT
3>MULTIPLY
4>DIVIDE
5>MODULO
6>EXIT''')
while True:
      o=int(input('Enter Option: '))
      if o==1:
            a=int(input('Enter number1: '))
            b=int(input('Enter number2: '))
            print('Addition result is',a+b)
      elif o==2:
            a=int(input('Enter number1: '))
            b=int(input('Enter number2: '))
            print('Subtraction result is',a-b)
      elif o==3:
            a=int(input('Enter number1: '))
            b=int(input('Enter number2: '))
            print('Product is',a*b)
      elif o==4:
            a=int(input('Enter number1: '))
            b=int(input('Enter number2: '))
            print('Quotient is',a/b)
      elif o==5:
            a=int(input('Enter number1: '))
            b=int(input('Enter number2: '))
            print('Remainder is',a%b)
      elif o==6:
            print('Want to exit? Okay then')
            break
      else:
            print('Invalid choice')
