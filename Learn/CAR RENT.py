quant_km = float(input('Digite a quantidade de KM percorrido pelo carro:'))
quant_dia = float(input('Digite a quantidade de dias percorrido com o carro:'))
print(f'O valor a ser pago eh R${(quant_km*0.15)+(quant_dia*60):.2f}')
