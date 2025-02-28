age = int(input('your age'))
if age <= 12:
    print('Your discount is 50%')
elif age>=60:
    print('Your discount is 30%')
else: print('No discount')
password = input('enter your password')
if password == "secure123":
    print('Successful')
else: print('Access denied')
score = int(input('Enter students score'))
if score >= 90 >= 100:
    print('Your grade is A')
elif 80 <= score <= 89:
    print('Your grade is B')
elif 70 <= score <= 79:
    print('Your grade is C')
elif 0 <= score <= 70:
    print('Your grade is F')
else: print ('Enter a valid score')
balance = float(1255)
withdrawal_amount = float(input('Please enter your withdrawal amount'))
if withdrawal_amount %10 == 0 and balance >= withdrawal_amount:
    print('please take your money')
elif withdrawal_amount %10 == 0 and balance <= withdrawal_amount:
    print('insufficient funds')
elif withdrawal_amount %10 != 0 and balance >= withdrawal_amount:
    print('Please enter a valid amount')
else:
    print('Your request cannot be completed now')
color = input('what is the traffic light color?')
if color == 'red':
    print('stop')
elif color == 'yellow':
    print('wait')
elif color == 'green':
    print ('go!')
else: print('Traffic light is not working')
Number = int(input('enter your number'))
if Number %2 == 0 :
    print('you have entered an even number')
else: 
    print('you have entered an odd number')
Weight = int(input('enter your weight in kgs'))
Height = float(input('enter your height in meters'))
BMI = Weight/(Height**2)
print (BMI)
if BMI <= 18.5:
    print('Underweight')
elif 18.6 <= BMI <= 24.9:
    print('Normal')
elif 25.0 <= BMI <= 29.9:
    print('Normal')    
else:
    print('Obese')

Temperature = float(input('what is the teperature today in celcius?'))
if Temperature <= 0:
    print('Freezing. Be careful')
elif -100 < Temperature <= 15:
    print('Its cold. Stay warm')
elif 15 <= Temperature <= 20:
    print('The weather is warm today')   
elif 20 <= Temperature <= 28:
    print('No need for a jacket') 
else:
    print('Its hot outside')
Total_cart_amount = float(input('what is the total order amount?'))
Shipping_cost = Total_cart_amount*0.03
Total_cost = Total_cart_amount + Shipping_cost
if Total_cart_amount >= 50:
    print(f'You are eligible for a free shipping on this order and your total cost is {Total_cart_amount}')
elif Total_cart_amount < 50:
    print(f'You are not eligible for a free shipping on this order. Your shipping cost is {Shipping_cost} and your total is {Total_cost}')

