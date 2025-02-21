def menu_choice(command):
    P=0
    r=0
    n=0
    monthly_payment=0
    custom_payments={}
    while True:
        command=input('\nChoose a variable: ')

        if command == 'n':
            n_input = input('\nAssign Loan Length Variable: ')
            try:
                n = 12 * int(n_input)
                print(f'\nSince the interest is calculated monthly, \nwe multiply the number of years by 12. \n\n{n} is the current Loan Length for this formula.\n')
            except ValueError:
                print('\nNext time, please enter a valid INTEGER value for the loan length.\n')
        elif command == 'm':
            monthly_payment=float(P*r*((1+r)**n)/(((1+r)**n)-1))
            monthly_payment='{:.2f}'.format(monthly_payment)
            print('-'*19)
            print(f'Monthly Payment Is:\n${monthly_payment}\n')
            print('-'*19)
        elif command.lower()=='p':
            P_input = input('\nAssign Principal Variable: ')
            try:
                P = 1*int(P_input)
                print(f'\n${P} is the current Principal Amount.\n')
            except ValueError:
                print('\nNext time, please enter a valid INTEGER value for the Principal.\n')
        elif command=='r':
            r_input=input('\nAssign Interest Rate as Percent: ')
            try:
                r_input=float(r_input)
                r=r_input/100
                r/=12
                print(f'First the percent is divided by 100 to give a decimal. \n {r_input}/100={r_input/100}\n')
                print(f'\nThen that decimal is divided by the billing cycles in a year.\n {r_input/100}/12={r_input/100/12} \nIt is an annual rate, meaning an interest rate for the whole year.\n')
                print('\nSo however many billing cycles are in the year (here we asume 12), the annual rate is divided into that many pieces.\n')
                print(f'\n{r} is the current Interst Rate.\n')
            except ValueError:
                print('\nNext time, please enter a valid INTEGER value for the Interest Rate.\n')
        elif command=='s':
            if P==0:
                P='P'
            if r==0:
                r='r'
            if n==0:
                n='n'
            if monthly_payment==0:
                monthly_payment='m'
            print()
            print(f'{monthly_payment} = {P} * {r} (1+{r})^{n}\n         ----------------------------------------------------')
            print(f'         (1+{r})^{n} - 1')
        elif command=="l":
            payment_schedule=generate_payment_schedule(P,r,n,monthly_payment,custom_payments)
            print_payment_schedule(payment_schedule)
        
        elif command == 'c':
            while True:
                print('\nPlease choose an option:')
                print('1. Enter a specific month to make a custom payment.')
                print('2. Enter a frequency of months to make a custom payment.')
                print('3. Clear custom payment mode.')
                print('4. Exit custom payment mode.')
                choice = input('Enter your choice (1-4): ')

                if choice == '1':
                    month = int(input(f'Enter the month (1-{n}): '))
                    amount = float(input('Enter the custom amount to pay: '))
                    custom_payments[month] = amount
                elif choice == '2':
                    frequency = int(input('Enter the payment frequency (in months): '))
                    amount = float(input('Enter the custom amount to pay: '))
                    for month in range(frequency, n+1, frequency):
                        custom_payments[month] = amount
                elif choice == '3':
                    custom_payments={}
                    print('Custom payments history cleared.')
                elif choice == '4':
                    print('\nReturing to Mortgage Calculator Menu with the following Custom Payments:\n')
                    print('Custom payments:', custom_payments)
                    break
                else:
                    print('Invalid input. PLease enter 1, 2, 3, or 4.')
                
        elif command=='q':
            print()
            print()
            print()
            print(' /              \\')
            print('| Program Closed |')
            print(' \              /')
            break
        else:
            print('\nINVALID OPTION\n')
        command=print_menu()

def generate_payment_schedule(P,r,n,monthly_payment,custom_payments):
    payment_schedule=[]
    remaining_balance=int(P)
    amount_paid=0

    for i in range(1,n+1):
        interest_payment=remaining_balance*r

        if remaining_balance<=float(monthly_payment):
            monthly_payment=remaining_balance*(1+r)
        
        if i in custom_payments:
            custom_payment=float(custom_payments[i])
            monthly_payment=0.0
            monthly_payment+=custom_payment
        
        money_toward_P=float(monthly_payment)-interest_payment
        remaining_balance=remaining_balance*(1+r)-float(monthly_payment)
        monthly_payment=float(monthly_payment)
        amount_paid+=monthly_payment
        monthly_payment=float(P*r*((1+r)**n)/(((1+r)**n)-1))
        payment_schedule.append({
            'Month': i,
            'Interest Payment':round(monthly_payment,2),
            'remaining_balance':round(remaining_balance,2),
            'amount_paid_so_far':round(amount_paid,2),
            'money_toward_P':round(money_toward_P,2),
            'money_toward_I':round(interest_payment,2)
            })
        if remaining_balance<=0:
            break
    return payment_schedule

def print_payment_schedule(payment_schedule):
    print()
    print(f"{'Month':<6} {'Amount Paid':<13} {'$ Towards Interest':<12} {'$ Towards P':<12} {'Remaining Balance':<18}")
    print("-"*71)

    for payment_info in payment_schedule:
        print(f"{payment_info['Month']:<6} ${payment_info['amount_paid_so_far']:<12} ${payment_info['money_toward_I']:<18} ${payment_info['money_toward_P']:<11} ${payment_info['remaining_balance']:<17}")

def print_menu():
    print('\nMORTGAGE CALCULATOR MENU')
    print('-'*24)
    print()
    print('m = P * r (1+r)^n\n    --------------')
    print('    (1+r)^n - 1')
    print('\nChoose a variable to investigate.\n')
    print('\nType "c" to input specific monthly payments.\n')
    print('\nType "s" to Show the equation with current values.\n')
    print('\nType "l" to print a complete payment List.\n')
    print('\n(Or type "q" to quit)')

#---------------------------------------------------------------
print_menu()
command=''
menu_choice(command)

