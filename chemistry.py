from chempy import balance_stoichiometry
__author__ = 'Kumar Aditya'
reac, prod = balance_stoichiometry(
    {'K2Cr2O7', 'H2SO4'}, {'K2SO4', 'Cr2(SO4)3', 'H2O', 'O2'})
print(reac, prod, "\n")
reac1, prod1 = balance_stoichiometry(
    {'KI', 'KIO3', 'H2SO4'}, {'K2SO4', 'H2O', 'I2'}
)
print(reac1, prod1)
