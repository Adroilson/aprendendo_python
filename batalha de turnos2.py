import random

def principal():
    while jogando[0]  == True:
        print('\n Pontos de vida = ',playerHP,' \n Pontos de especial = ',playerSP,'\n')
        ação = input('\n O que vai fazer?\n Atacar = digite a,  Defender = digite d,  Curar = digite c, Ataque com sp = digite m. \n\n\n\n--------> ')
        while ação != 'a' and ação != 'd' and ação != 'c' and ação != 'm':
            print(' \nOPÇÃO INVÁLIDA!!!!\n')
            print(' Pontos de vida = ',playerHP,' \n Pontos de especial = ',playerSP,'\n')
            ação = input('\n O que vai fazer?\n Atacar = digite a,  Defender = digite d,  Curar = digite c, Ataque com sp = digite m. \n')
        if ação == 'a':
            atacar()
        elif ação == 'd':
            defender()
        elif ação == 'c':
            curar()
        elif ação == 'm':
            magia()
        else:
            print('Opção invalida, jogo finalizado.')
            jogando[0] = False
        contabiliza_hp_inimigo()
        if flag[0] == 1:

            mirelo()


        if len(inimigos) == 0:
            inimigos.append('mortos')
            if bool(random.choice([1,1,1,1])) == True:
                print('Você despertou O TERRÍVEL ',chefe1[0],'!!!!!\n')
                print(chefe1[0],' entrou na batalha.\n')
                Nada =[input('\n******************** Para continuar aperte ENTER ********************\n')]
                Nada.clear()

                mirelo()
            else:
                print('                       Você venceu!!!!!...')
                print('\n\n\n☺ █▀█░  █▀▀█░  █▀▀█░  █▀▀░    █▀▀█░  █▀​█░   █▀▄▀█░  █▀▀ ☺\n☺ █▀█░  █░▄▄░  █▀█▀░  █▀░░    █░▄▄░  █▀​█░   █░█░█░  █▀ ☺\n☺ █░█░  █▄▄█░  █░░█░  █▄▄░    █▄▄█░  █░​█░   █░░░█░  █▄▄ ☺')
                jogando[0] = False
            #    miragem()
        Nada =[input('\n******************** Para continuar aperte ENTER ********************\n')]
        Nada.clear()
        if jogando[0]==True:

            turno_inimigo()

            Nada =[input('\n******************** Para continuar aperte ENTER ********************\n')]
            Nada.clear()

            contabiliza_playerHP()

def inverte():
    numero = 0
    reduzido = 1
    invertido = []
    copia = chefe1[1]
    while reduzido > 0:
        numero = copia%10
        reduzido = copia//10
        copia = reduzido
        invertido.append(numero)
    tuple(invertido)
    novo = map(str,invertido)
    novo = ''.join(novo)
    chefe1[1]= int(novo)

def atacar():

    if bool(random.choice(chance25))==True:#dano critico
        if flag[0] == 0:#inimigos comuns
            m = random.choice(inimigos)
            m[1]-= 50
            for i in (inimigos):
                i[1]-=20

            print('Seu ataque causou um dano crítico de 50 pontos no inimigo ',m[0],' !!!!!!!\n')
            Nada =[input('\n******************** Para continuar aperte ENTER ********************\n')]
            Nada.clear()

            print('Todos os inimigos sofreram consequencias do ataque e perderam 20 pontos de vida!\n')
            Nada =[input('\n******************** Para continuar aperte ENTER ********************\n')]
            Nada.clear()

        elif flag[0] == 1: #MIRELO
            x = random.randint(100,500)
            chefe1[1]-= x
            print( chefe1[0],' sofreu dano critico de ',x,' !!!!\n')
            Nada =[input('\n******************** Para continuar aperte ENTER ********************\n')]
            Nada.clear()

        #else:#flag = 3, lutando contra os imitadores

    else:#dano comum
        if flag[0] == 0:#inimigos comuns
            m = random.choice(inimigos)
            m[1]-=20
            print(' Inimigo ',m[0],' Recebeu o ataque.\n')
        elif flag[0] == 1: #MIRELO
            chefe1[1] -= 100
            print(chefe1[0],' sofreu seu ataque.\n ')


def magia():
    if playerSP[0] < 30:
        print('Sp insuficiente!!')
        Nada =[input('\n******************** Para continuar aperte ENTER ********************\n')]
        Nada.clear()

    else:
        if flag[0] == 0: #inimigos comuns
            playerSP[0] -=30
            if bool(random.choice(chance50))==True:#dano critico
                    m = random.choice(inimigos)

                    danocritico = [100,50]
                    m[1]=-danocritico[0]
                    for i in range(1,len(inimigos)):
                        inimigos[i][1]-=50
                    print('Seu ataque causou um dano crítico no inimigo ',m[0],' de ',danocritico[0],' !!!!!!!\n')
                    Nada =[input('\n******************** Para continuar aperte ENTER ********************\n')]
                    Nada.clear()

                    print('Todos os inimigos sofreram consequencias do ataque especial e perderam',danocritico[1],' !\n')

            else:
                for i in inimigos:
                    i[1] -= (random.randint(1,200))
                    print('Você causou um dano aleatorio nos inimigos\n')
        elif flag[0] == 1: #chefe 1
            if bool(random.choice(chance50))==True:#dano critico
                x = random.randint(100,1000)
                chefe1[1]-= x
                print( chefe1[0],' sofreu dano de ',x,' !!!!\n')
                Nada =[input('\n******************** Para continuar aperte ENTER ********************\n')]
                Nada.clear()
            else:
                inverte()
                print('Sua inesperiência com poderes mágicos causaram um efeito curioso...\n')
                playerHP[0] += random.randint(1,500)

                print(' Seu HP = ',playerHP[0],' e o hp de ',chefe1[0],' passou a ser',chefe1[1],'\n')
                print('\n')
                Nada =[input('\n******************** Para continuar aperte ENTER ********************\n')]
                Nada.clear()



def defender():
    pd = random.randint(2,4)
    defesa[0] = pd
    playerSP[0] += (random.randint(10,20))

    print('Você escolheu se defender, os ataques inimigos serão reduzidos a 1/',pd,' .\n')
def curar():
    if playerSP[0] < 10:
        print('SP insuficiente!!')
        Nada =[input('\n******************** Para continuar aperte ENTER ********************\n')]
        Nada.clear()

    else:
        playerSP[0] -=10
        c = random.randint(100,500)
        playerHP[0] += c
        print('Você se curou em ',c,' pontos.')
        Nada =[input('\n******************** Para continuar aperte ENTER ********************\n')]
        Nada.clear()

        if playerHP[0] > 500:
            playerHP[0] = 500

def contabiliza_hp_inimigo():
    if flag[0] == 0:#inimigos comuns
        for i in (inimigos):
            if i[1] <= 0:
                print('Inimigo ',i[0],' morreu.\n')
                inimigos.remove(i)
        for i in (inimigos):
            print(' Inimigo ',i[0],' tem ',i[1],' pontos de vida.\n')
    if flag[0] == 1:
        if chefe1[1] <=0 :
            print('  O ',chefe1[0],' foi mais uma vez derrotado, você venceu.\n Parabéns!!!!')
            print('\n\n\n☺ █▀█░  █▀▀█░  █▀▀█░  █▀▀░    █▀▀█░  █▀​█░   █▀▄▀█░  █▀▀ ☺\n☺ █▀█░  █░▄▄░  █▀█▀░  █▀░░    █░▄▄░  █▀​█░   █░█░█░  █▀ ☺\n☺ █░█░  █▄▄█░  █░░█░  █▄▄░    █▄▄█░  █░​█░   █░░░█░  █▄▄ ☺')

            jogando[0] = False
        else:
            print( chefe1[0],' tem ',chefe1[1],' pontos de vida.')


def mirelo():
    flag[0] = 1
    if bool(random.choice(chance50)) == True:
        d = random.randint(1,200)
        playerHP[0] -= d/defesa[0]
        x = d/defesa[0]
        defesa[0] = 1
        print(chefe1[0],' atacou e causou um dano de ',x,'pontos.\n')

    else:
        print(chefe1[0],' errou o ataque!!!\n')

def turno_inimigo():
    if flag[0] == 0:
        for i in range(len(inimigos)):
            if len(inimigos)==0:
                jogando[0]=False
            elif bool(random.choice(chance25)) == True:
                playerHP[0]-=25/defesa[0]
                x = 25/defesa[0]
                defesa[0] = 1
                print(' O inimigo ',inimigos[i][0], 'causou um DANO CRITICO DE ',x,' PONTOS!!!!!!')
            else:
                playerHP[0] -= 10/defesa[0]
                x = 10/defesa[0]
                print('O inimigo ',inimigos[i][0], ' causou um dano de ',x,' pontos')

def contabiliza_hp_chefe1():
    if flag[0] == 1:
        if chefe1[1] <= 0:
            print(                  chefe1[0],' foi derrotado! Você venceu!!!\n')
            print('\n\n\n☺ █▀█░  █▀▀█░  █▀▀█░  █▀▀░    █▀▀█░  █▀​█░   █▀▄▀█░  █▀▀ ☺\n☺ █▀█░  █░▄▄░  █▀█▀░  █▀░░    █░▄▄░  █▀​█░   █░█░█░  █▀ ☺\n☺ █░█░  █▄▄█░  █░░█░  █▄▄░    █▄▄█░  █░​█░   █░░░█░  █▄▄ ☺')
            jogando[0] = False
        else:
            print(chefe1[0],' tem ',chefe1[1],' pontos de vida.\n')
def contabiliza_playerHP():
    if playerHP[0] <= 0:
        print('              Game Over!!!')

        jogando[0] = False

defesa,playerHP,playerSP,chefe1,chefe2,chance25,chance50,flag = [1],[500],[100],['MIRELO',2000],[[i,500]for i in range(1,6)],[0,0,0,1],[0,0,1,1],[0]

print('Batalha de turnos.\n')
quantidade = input(' Digite a quantidade de inimigos:\n ')
while quantidade.isdecimal() == False:
    print('Digite apenas números\n')
    quantidade = input(' Digite a quantidade de inimigos:\n ')
quantidade =int(quantidade)

print(' \nVocê está lutando contra %i inimigos'%(quantidade))

Nada =[input('\n******************** Para continuar aperte ENTER ********************\n')]
Nada.clear()

inimigos = [[i,200]for i in range(1,(quantidade+1))]
jogando = [True]
principal()
