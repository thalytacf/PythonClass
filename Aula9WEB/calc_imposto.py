
def calc_inss (salario):
    if (salario>0 and salario <= 1751.81):
        inss = salario * 0.08
    elif (salario>1751.81 and salario <= 2919.72):
        inss = salario * 0.09
    elif (salario>2919.72 and salario <= 5839.45):
        inss = salario * 0.11
    else:
        inss = 642.3395 
    return ins

def calc_irrf (salario, inss):
    if (salario>2826.65 and salario <= 3751.05):
        irrf = ((salario - inss)  * 0.15)- 354.80
    elif (salario>1903.98 and salario <= 2826.65):
        irrf = ((salario - inss) * 0.075)- 142.80
    elif (salario>3751.05 and salario <= 4664.68):
        irrf = ((salario - inss) * 0.225)- 636.13
    elif (salario>4664.69):
        irrf = ((salario - inss) * 0.275)- 869.36
    return irrf