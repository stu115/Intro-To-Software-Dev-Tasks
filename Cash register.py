from CashRegister import CashRegister

cg1 = CashRegister()

cg2 = CashRegister()

cg1.addItem(6)
cg1.addItem(7)
##print(cg1.getTotal())
##print(cg1.getCount())

cg1.clear()
print(cg1.getTotal())
print(cg1.getCount())
