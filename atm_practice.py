b200,r200,b100,r100,b50,r50,b20,r20 = 0,0,0,0,0,0,0,0

def calcularBilletes(dinero):
    global b200,r200,b100,r100,b50,r50,b20,r20
    aux = 0
    if dinero>100 and (dinero%100 ==10 or dinero%100 == 30):
        dinero = dinero -50
        aux = 1
    b200 = dinero//200
    r200 = dinero % 200
    b100 = r200 // 100
    r100 = r200 % 100
    if r100 % 20 == 0:
        b50 = aux
        b20 = r100 // 20
    
    else:
        b50 = r100 // 50 + aux
        r50 = r100 % 50
        b20 = r50 // 20
            
	

monto = int(input("ingresa el monto a retirar: "))
calcularBilletes(monto)
print("los billetes de 200 son : ",b200)
print("los billetes de 100 son : ",b100)
print("los billetes de 50 son : ",b50)
print("los billetes de 20 son : ",b20)   
