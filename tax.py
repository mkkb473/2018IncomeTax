import sys

salary = int(sys.argv[1])

taxRates = {36000:0.03, 144000: 0.1, 300000: 0.2, 420000: 0.25, 660000: 0.3, 960000: 0.35, 99999999999: 0.45}
START = 60000

temp = salary - START
idvTax = 0
preBar = 0
for bar, rate in taxRates.items():
    if temp <= 0:
        break
    if temp - (bar - preBar) <= 0:
        idvTax += rate * temp
        break
    else:
        idvTax += rate * (bar - preBar)
    temp -= bar - preBar
    preBar = bar
    print(bar, preBar, temp)

print("Your yearly income: {}\nYour yearly tax: {}\nYour actual yearly income: {}".format(salary, idvTax, salary - idvTax))
