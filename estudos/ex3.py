usuario = input('ola, digite seu nome: ')
idade = int(input('digite sua idade; '))
altura = float(input('digite sua altura; '))
peso = float(input('digite seu peso; '))
imc = peso / altura**2
print(f'{usuario}, vamos realizar o calculo de seu IMC')
print(f'{usuario}, aos {idade} de idade seu peço é de {peso}, seu IMC esta em {imc:.2f}')
if imc< 18.5:
    print('abaixo do peso')
elif imc>18.5 and imc<24.9:
    print('voce esta no peso normal')
else: 
    print('a verificação falhou')    
