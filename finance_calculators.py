import math
#math is imported as it will be used when making calculations later on in the program

var_choice = str(input('Choose either \'investment\' or \'bond\' from the menu below to proceed: \ninvestment \t- to calculate how much interest you\'ll earn on interest. \nbond \t\t- to calculate the amount you\'ll have to pay on a home loan. \n')) 
var_choice = str(var_choice.upper())
interest = ''
var_input = False
#some of the variables are initialised above, var_choice determines whether the user is making an investment or repaying
#a bond. i then change var_choice to uppercase in order to make it easier to distinguish between the choices, and the 
#user can use lower or uppercase when entering their input.
#interest is initialised to a blank space so that it can be used when the user decides which interest they want to use
#var_input will be used below in a while loop, which will ensure that the user enters the correct input


while var_input == False:
    if (var_choice == 'INVESTMENT') or (var_choice == 'BOND'):
        var_input = True
    else:    
        var_choice = str(input('Please enter valid input: '))
        var_choice = str(var_choice.upper())
#the above while loop only ends when the user enters either investment or bond. if the user enters incorrect input,
#a message will be displayed prompting the user to enter correct input        
 
if var_choice == 'INVESTMENT':
    var_amount = float(input('Please enter the amount that you will be investing: '))
    var_int_rate = float(input('Please enter the interest rate (without the percentage symbol) : '))
    var_int_rate = var_int_rate/100
    var_year = int(input('Please enter the number of years that you want to invest for: '))
    interest = str(input('Please specify whether you want \'simple\' or \'compound\' interest: '))
    interest = str(interest.upper())
    var_input = False
    while var_input == False:
        if (interest == 'SIMPLE') or (interest == 'COMPOUND'):
            var_input = True
        else:
            interest = str(input('Please enter valid input: '))
            interest = str(interest.upper())
    if interest == 'SIMPLE' :
        var_answer = float(var_amount*(1 + var_int_rate * var_year))
        var_answer = round(var_answer,2)
        print('Your total after the investment period will be: R{}'.format(var_answer))
    elif interest == 'COMPOUND':
        var_answer = float(var_amount * math.pow((1 + var_int_rate),var_year))
        var_answer = round(var_answer,2)
        print('Your total after the investment period will be: R{}'.format(var_answer))
#the above code runs if the user chooses Investment. interest is also changed to uppercase in order to reduce the 
#possibility of errors. there is also a while loop for interest so that the correct input is attained. there are no 
#while loops for the string as the user should'nt be able to make a mistake when giving input. it would also make the 
#program unnecessarily long. var_input is reused in the while loop. var_answer is rounded to 2 decimals as we are working
#with currency. in both simple and compound interest, var_answer is displayed with an appropriate message.
#i have obtained the formulae for compound and simple interest from the HyperionDev learner guide provided to me.
 
elif var_choice == 'BOND':
    house_value = float(input('Please enter the value of the house: '))
    interest_bond = float(input('Please enter the interest rate: '))
    interest_bond = interest_bond/100
    interest_bond = interest_bond/12
    num_months = int(input('Please enter the number of years you will be repaying the bond: '))
    num_months = num_months * 12
    var_answer = float((interest_bond*house_value)/(1 - math.pow((1+interest_bond),-num_months)))
    var_answer = round(var_answer,2)
    print('Your monthly repayment will be R{}'.format(var_answer))
#the above code runs when Bond is chosen. there is no string input needed from the user after Bond is chosen so 
#I have not added a while loop. math is used when doing the calculation for the monthly repayment as an exponent 
#calculation is needed. var_answer is also rounded to 2 decimals and displayed with an appropriate message.
#the formula for the bond repayment is obtained from the HyperionDev learner guide provided to me.
    
input('Press ENTER to exit.')
# I am stopping Python from closing once the program has run using code from https://stackoverflow.com/questions/12375173/how-to-stop-python-closing-immediately-when-executed-in-microsoft-windows#