peso = float(input('Qual é o seu peso ?'))
altura = float(input('Qual é a sua altura ?'))
imc = peso / altura ** 2

if imc < 18.5:
    print('\33[32mSeu IMC Mede : {:.1f}'.format(imc))
    print('\33[31mCuidado você está abaixo do seu peso ideal!\33[m')

elif 18.5 <= imc < 25.0:
    print('\33[32mSeu IMC Mede : {:.1f}'.format(imc))
    print('\33[34mVocê Está no seu peso Ideal!\33[m')

elif 25.0 <= imc < 30.0:
    print('\33[32mSeu IMC Mede : {:.1f}'.format(imc))
    print('\33[33mVocê Está Com sobrepeso!\33[m')

elif 30.0 <= imc < 40.0:
    print('\33[32mSeu IMC Mede : {:.1f}'.format(imc))
    print('\33[31mCuidado Você está Com Obesidade!\33[m')

else:
    print('\33[32mSeu IMC Mede : {:.1f}'.format(imc))
    print('\33[31mProcure ajuda você está Com obesidade Morbida sua Saúde pode ser prejudicada!\33[m')
