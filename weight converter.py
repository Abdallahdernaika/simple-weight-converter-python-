#weight
ask = input('what is your weight? ')
type_of = input('is it in (l) or (k)? ')
if type_of.upper() == "L":
    pounds =  int(ask) * 0.45359237
    D = f'your weight is {pounds} K'
    print(D)
elif type_of.upper() == "K":
    kilo = int(ask)/0.45359237
    W = f'your eight in lbs is {kilo}'
    print(W)
print('Thank you for using dernaika weight tech!!!!')
