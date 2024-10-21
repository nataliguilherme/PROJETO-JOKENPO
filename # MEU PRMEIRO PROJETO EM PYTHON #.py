# MEU PRMEIRO PROJETO EM PYTHON #
from random import randint
from time import sleep
itens = ('pedra','papel','tesoura')
computador = randint(0, 2)
print('''Faça sua jogada
[0] PEDRA
[1] PAPEL
[2] TESOURA

''')
jogador=int(input('FAÇA SEU MOVIMENTO'))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print("Pô!")
sleep(2)
print('..'*3) 
sleep(1) 
print('fazendo muitos calculos')
sleep(2)
print('quase la')
sleep(3)
print('voce consideraria aceitar sua derrota?')
desistencia = ('Y','N')
desistencia = input('Y ou N?')    
if desistencia == 'Y' : print ('MAIS UMA VITORIA DO GRANDIOSO JOKENPO SIMULATOR')
else: print('Saco, vamo la...')
sleep(3)
print(f'GRANDE SIMULADOR DE JOKENPO JOGOU:{itens[computador]}')
print(f'Jogador jogou:{itens[jogador]}')
sleep(1)
if computador == 0:  
    if jogador == 0:    
        print('EMPATE, COM VOCE? NUNCA!! VAMOS MAIS UMA VEZ!')
    elif jogador == 1:  
        print('JOGADOR TRAPACEU, QUERO REVANCHE!')
    elif jogador == 2:  
        print('MAIS UMA VITORIA DO GRANDIOSO JOKENPO SIMULATOR')
    else:   
        print('Ow, sao só 3 opções irmao.')
if computador == 1:  
    if jogador == 1:    
        print('EMPATE, COM VOCE? NUNCA!! VAMOS MAIS UMA VEZ!')
    elif jogador == 2:  
        print('JOGADOR TRAPACEU, QUERO REVANCHE!')
    elif jogador == 0:  
        print('MAIS UMA VITORIA DO GRANDIOSO JOKENPO SIMULATOR')
    else:   
        print('Ow, sao só 3 opções irmao.')        
if computador == 2:  
    if jogador == 2:    
        print('EMPATE, COM VOCE? NUNCA!! VAMOS MAIS UMA VEZ!')
    elif jogador == 0:  
        print('JOGADOR TRAPACEU, QUERO REVANCHE!')
    elif jogador == 1:  
        print('MAIS UMA VITORIA DO GRANDIOSO JOKENPO SIMULATOR')
    else:   
        print('Ow, sao só 3 opções irmao.')  
print('Gotaria de jogar novamente?')
resposta=('SIM' , 'NAO')
resposta=input('SIM ou NAO?')
if(resposta == 'SIM') :  
     print('Massa, nao sei colocar isso ainda')
else: print('Adeus!')
