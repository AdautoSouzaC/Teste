
dias = float(input("Quantos dias alugado?:"))
km = float(input("quantos km rodados?:"))
pago = (dias * 60) + (km * 0.15)

print("O totao a pagar é de R$ {:.2f}".format(pago))