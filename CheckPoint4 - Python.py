import random

# RM 98310 - Angelo

print (""" 
      _                                 _            __     __         _   _             
     | |   ___     __ _    ___       __| |   __ _    \ \   / /   ___  | | | |__     __ _ 
  _  | |  / _ \   / _` |  / _ \     / _` |  / _` |    \ \ / /   / _ \ | | | '_ \   / _` |
 | |_| | | (_) | | (_| | | (_) |   | (_| | | (_| |     \ V /   |  __/ | | | | | | | (_| |
  \___/   \___/   \__, |  \___/     \__,_|  \__,_|      \_/     \___| |_| |_| |_|  \__,_|
                  |___/                                                                  
""" )

velha = [
        [" "," "," "],
        [" "," "," "],
        [" "," "," "]
]


def InicializarTabuleiro():
    for i in range(3):
        velha[i][0] = " "
        velha[i][1] = " "
        velha[i][2] = " "
    print ("    0   1   2")
    print ("0:  " + velha[0][0] + " | " + velha [0][1] + " | " + velha[0][2])
    print ("   -----------")
    print ("1:  " + velha[1][0] + " | " + velha [1][1] + " | " + velha[1][2])
    print ("   -----------")
    print ("2:  " + velha[2][0] + " | " + velha [2][1] + " | " + velha[2][2])


def ImprimirTabuleiro(): 
    global velha
    print ("    0   1   2")
    print ("0:  " + velha[0][0] + " | " + velha [0][1] + " | " + velha[0][2])
    print ("   -----------")
    print ("1:  " + velha[1][0] + " | " + velha [1][1] + " | " + velha[1][2])
    print ("   -----------")
    print ("2:  " + velha[2][0] + " | " + velha [2][1] + " | " + velha[2][2])
    print ("              ")

def ImprimirMenuPrincipal():
    print (""" 
                 Bem Vindo!!
           [1] Player Vs Player
           [2] Player Vs Maquina (modo Facil)
           [3] Player Vs Maquina (modo Dificil)
           [0] Sair do jogo
    """)
    resp = int(input("Selecione uma opção: "))
    return resp

def JogadaUsuario(jogador):
    l = LeiaCoordenadaLinha()
    c = LeiaCoordenadaColuna()
    pv = PosicaoValida(l,c)
    while pv == False:
        print("Posição Invalida! Tente de novo")
        ImprimirTabuleiro()
        l = LeiaCoordenadaLinha()
        c = LeiaCoordenadaColuna()
        pv = PosicaoValida(l,c)
    jogar(pv,l,c, jogador)
    

def jogar(posicao,linha,coluna, jogador):
    if posicao == True:
        velha[linha][coluna] = jogador

def LeiaCoordenadaLinha():
    linha = int(input("Linha: "))
    return linha

def LeiaCoordenadaColuna():
    coluna = int(input("Coluna: ")) 
    return coluna

def PosicaoValida(linha, coluna):
    if 0 <= linha < 3 and 0 <= coluna < 3:
        posicao = velha[linha][coluna]
        if posicao == " ":
            posicao = True
            return posicao
    return False

def VerificarVencedor():
    for i in range(3):
        # Confirmar vitoria por linha
        if velha[i][0] == velha[i][1] == velha[i][2] and velha[i][0] != " ":
            return True
        # Confirmar vitoria por coluna
        elif velha[0][i] == velha[1][i] == velha[2][i] and velha[0][i] != " ":
            return True
    # Confirmar vitoria por diagonal
    if (velha[0][0] == velha[1][1] == velha[2][2] and velha[0][0] != " ") or (velha[0][2] == velha[1][1] == velha[2][0] and velha[0][2] != " "):
        return True
    return False

def VerificarVelha():
    print("Deu Velha!")

def EncontrarEspacoVazio():
    EspacosVazios = []
    l = 0
    while l < len(velha):
        c = 0
        while c < len(velha[l]):
            if velha[l][c] == " ":
                EspacosVazios.append([l,c])
            c += 1
        l += 1
    return EspacosVazios

def JogadaMaquinaFacil(jogador):
    espacos = EncontrarEspacoVazio()
    [l,c] = random.choice(espacos)
    pv = PosicaoValida(l, c)
    jogar(pv,l,c,jogador)

def ModoJogador():
    pontosX = 0
    pontosO = 0
    jogador = "X"
    while (pontosX < 3) or (pontosO < 3):
        print (f"""
               Pontos
            Jogador 1 (X) -> {pontosX}
            Jogador 2 (O) -> {pontosO}       
               """)        
        jogadas = 0
        InicializarTabuleiro()
        while jogadas <= 8:
            JogadaUsuario(jogador)
            ImprimirTabuleiro()
            jogadas += 1
            v = VerificarVencedor()
            if v == True:
                print(f"GANHOU!!! jogador: {jogador}")
                if jogador == "X":
                    pontosX += 1
                elif jogador == "O":
                    pontosO += 1
                break
            if jogador == "X":
                jogador = "O"
            else:
                jogador = "X"
        if jogadas > 8:
            VerificarVelha()
    print (f"Jogador {jogador} GANHOU!! PARABÉNS!")
    print ("""
    [1] - jogar novamente!
    [0] - sair do programa
    """)
    R = int(input("Selecione uma opção: "))
    if R == 1:
        principal()
    elif R == 0:
        print ("Saindo do programa...")

def ModoMaquinaFacil():
    pontosX = 0
    pontosO = 0
    jogador = "X"
    while (pontosX < 3) or (pontosO < 3):
        print (f"""
               Pontos
            Jogador 1 (X) -> {pontosX}
            Jogador 2 (O) -> {pontosO}       
               """)        
        jogadas = 0
        InicializarTabuleiro()
        while jogadas <= 8:
            if jogador == "X":
                JogadaUsuario(jogador)
            else:
                JogadaMaquinaFacil(jogador)
            ImprimirTabuleiro()
            jogadas += 1
            v = VerificarVencedor()
            if v == True:
                print(f"GANHOU!!! jogador: {jogador}")
                if jogador == "X":
                    pontosX += 1
                elif jogador == "O":
                    pontosO += 1
                break
            if jogador == "X":
                jogador = "O"
            else:
                jogador = "X"
        if jogadas > 8:
            VerificarVelha()
    print (f"Jogador {jogador} GANHOU!! PARABÉNS!")
    print ("""
    [1] - jogar novamente!
    [0] - sair do programa
    """)
    R = int(input("Selecione uma opção: "))
    if R == 1:
        principal()
    elif R == 0:
        print ("Saindo do programa...")

def JogadaMaquinaDificil(jogador):
    espacos = EncontrarEspacoVazio()

    # Fazer a primeira jogada no centro, se estiver vazio
    if [1, 1] in espacos:
        l = 1
        c = 1
        posicao = PosicaoValida(l,c)
        jogar(posicao, 1, 1, jogador)
        return

    # Verificar se a máquina pode ganhar na próxima jogada
    for l, c in espacos:
        velha[l][c] = jogador
        if VerificarVencedor():
            return  # A máquina já venceu, não precisa jogar mais
        velha[l][c] = " "  # Desfaz a jogada para a próxima verificação

    # Verificar se o jogador adversário pode ganhar na próxima jogada
    jogador_adversario = "X" if jogador == "O" else "O"
    for l, c in espacos:
        velha[l][c] = jogador_adversario
        if VerificarVencedor():
            jogar(True, l, c, jogador)  # Bloqueia o jogador adversário
            return
        velha[l][c] = " "  # Desfaz a jogada para a próxima verificação

    # Se não for possível ganhar ou bloquear, faça uma jogada aleatória
    [l, c] = random.choice(espacos)
    jogar(True, l, c, jogador)

def ModoMaquinaDificil():
    pontosX = 0
    pontosO = 0
    jogador = "X"
    while (pontosX < 3) or (pontosO < 3):
        print(f"""
               Pontos
            Jogador 1 (X) -> {pontosX}
            Jogador 2 (O) -> {pontosO}
               """)
        jogadas = 0
        InicializarTabuleiro()
        while jogadas <= 8:
            if jogador == "X":
                JogadaUsuario(jogador)
            else:
                JogadaMaquinaDificil(jogador)
            ImprimirTabuleiro()
            jogadas += 1
            v = VerificarVencedor()
            if v == True:
                print(f"GANHOU!!! jogador: {jogador}")
                if jogador == "X":
                    pontosX += 1
                elif jogador == "O":
                    pontosO += 1
                break
            if jogador == "X":
                jogador = "O"
            else:
                jogador = "X"
            
        if jogadas > 8:
            VerificarVelha()
    print(f"Jogador {jogador} GANHOU!! PARABÉNS!")
    print("""
    [1] - jogar novamente!
    [0] - sair do programa
    """)
    R = int(input("Selecione uma opção: "))
    if R == 1:
        principal()
    elif R == 0:
        print("Saindo do programa...")

def principal():

    r = ImprimirMenuPrincipal()

    if r == 1 :
        ModoJogador() #Opção de jogar contra Player
    
    if r == 2: 
        ModoMaquinaFacil() #Opção de jogar contra a maquina no modo facil

    if r == 3:
        ModoMaquinaDificil() #Opção de jogar contra a Maquina no modo dificil

    if r == 0:
        print(" Saindo do jogo... ")
        

principal()