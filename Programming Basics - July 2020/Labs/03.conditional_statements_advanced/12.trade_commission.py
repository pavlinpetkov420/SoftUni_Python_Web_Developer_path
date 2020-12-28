city = input()
sales = float(input())
commission = 0.0
is_invalid = False
if city == 'Sofia':
    if sales < 0:
        is_invalid = True
    elif 0 <= sales <= 500:
        commission = sales * 0.05
    elif 500 < sales <= 1000:
        commission = sales * 0.07
    elif 1000 < sales <= 10000:
        commission = sales * 0.08
    elif sales > 10000:
        commission = sales * 0.12
elif city == 'Varna':
    if sales < 0:
        is_invalid = True
    elif 0 <= sales <= 500:
        commission = sales * 0.045
    elif 500 < sales <= 1000:
        commission = sales * 0.075
    elif 1000 < sales <= 10000:
        commission = sales * 0.10
    elif sales > 10000:
        commission = sales * 0.13
elif city == 'Plovdiv':
    if sales < 0:
        is_invalid = True
    elif 0 <= sales <= 500:
        commission = sales * 0.055
    elif 500 < sales <= 1000:
        commission = sales * 0.08
    elif 1000 < sales <= 10000:
        commission = sales * 0.12
    elif sales > 10000:
        commission = sales * 0.145
else:
    is_invalid = True
if not is_invalid:
    print(f'{commission:.2f}')
else:
    print('error')