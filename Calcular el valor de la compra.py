valor_compra=float(input("Ingrese el valor de su compra, si es supeior a 200 obtendra un descuento?"))
IVA= valor_compra*0.12
if valor_compra < 200:
    total=valor_compra+IVA
    print("el valor de la compra es:", str(valor_compra))
    print("el valor del IVA es:", str(IVA))
    print("total a pagar",total)
if valor_compra >= 200:
    descuento=valor_compra*0.02
    total_sin_descuento=valor_compra+IVA
    total=valor_compra+IVA-descuento
    print("el valor de su compra es:", str(valor_compra))
    print("el valor del IVA es:", str(IVA))
    print("total a pagar sin descuento", str(total_sin_descuento))
    print("Su descuento es:",str(descuento))
    print("total a pagar",(total))
else:
    print("su compra es inferior a $200, no hay descuento")


