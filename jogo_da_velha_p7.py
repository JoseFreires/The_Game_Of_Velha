import sys, pygame

pygame.init()
 
pygame.display.set_caption('The Game of Velha')

size = width, height = 600, 600
color_line = 255, 155, 80
background = 0,0,0
vez = 0
rodada = 0

xis = pygame.image.load("Images/xis.png")
bola = pygame.image.load("Images/bola.png")

velha = pygame.image.load("Images/velha legal.jpg")

xis = pygame.transform.scale(xis,(100,100))
bola = pygame.transform.scale(bola,(100,100))
velha = pygame.transform.scale(velha,(100,100))

matriz = [
          ['_','_','_'],
          ['_','_','_'],
          ['_','_','_']
          ]


quadrante_linha = [50 , 250, 450]
quadrante_coluna = [50, 250, 450]

screen = pygame.display.set_mode(size)

screen.fill(background)

#--> FUNÇÕES
def desenhar():
    pygame.draw.line(screen,color_line, (200,0),(200,600),5)
    pygame.draw.line(screen,color_line, (400,0),(400,600),5)
    
    pygame.draw.line(screen,color_line, (0,200),(600,200),5)
    pygame.draw.line(screen,color_line, (0,400),(600,400),5)


def faz_jogada(pos):
    index_linha = int(pos[0]/200)
    index_coluna = int(pos[1]/200)
    
    if (matriz[index_coluna][index_linha] == '_'):
        matriz[index_coluna][index_linha] = 'x'
        screen.blit(xis,(quadrante_linha[index_linha], quadrante_coluna[index_coluna]))
        return 0
    else:
        print("Posição ocupada")

def faz_jogada_2(posi):
    index_linha = int(posi[0]/200)
    index_coluna = int(posi[1]/200)
    
    if (matriz[index_coluna][index_linha] == '_'):
        matriz[index_coluna][index_linha] = 'o'
        screen.blit(bola,(quadrante_linha[index_linha], quadrante_coluna[index_coluna]))
        return 1
    
    else:
        print("Posição ocupada")

def reiniciar():
    for coluna in range(0,3):
        for linha in range(0,3):
            matriz[coluna][linha] = '_'
    
    vez = 0
    screen.fill(background)
    return 0

#def linha():


#--> The Game of Velha
while True:
    desenhar()

    if(rodada >= 9):
        screen.blit(velha,(100,100))
        reiniciar()


    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            click_pos = pygame.mouse.get_pos()

            if (vez== 0):
                if (faz_jogada(click_pos) == 0):
                    vez = 1
                    rodada =  rodada + 1

            elif(vez == 1):
                if (faz_jogada_2(click_pos) == 1):
                    vez = 0
                    rodada =  rodada + 1

#--> Local de verificação do ganho --------------------------------------------------------------------------------------------------------------------------

        # Linhas do X
        if (matriz[0][0] == "x") and  (matriz[0][1] == "x") and (matriz[0][2] == "x"):
            print("x","x","x")
            print("_","_","_")
            print("_","_","_")
            pygame.draw.line(screen,color_line, (0,100),(600,100),8)

            if (reiniciar() == 0):
                vez = 0
                rodada = 0

        if (matriz[1][0] == "x") and  (matriz[1][1] == "x") and (matriz[1][2] == "x"):
            print("_","_","_")
            print("x","x","x")
            print("_","_","_")
            pygame.draw.line(screen,color_line, (0,300),(600,300),8)

            if (reiniciar() == 0):
                vez = 0
                rodada = 0

        if (matriz[2][0] == "x") and  (matriz[2][1] == "x") and (matriz[2][2] == "x"):
            print("_","_","_")
            print("_","_","_")
            print("x","x","x")
            pygame.draw.line(screen,color_line, (0,500),(600,500),8)

            if (reiniciar() == 0):
                vez = 0
                rodada = 0
        
        # Linhas do O

        if (matriz[0][0] == "o") and  (matriz[0][1] == "o") and (matriz[0][2] == "o"):
            print("o","o","o")
            print("_","_","_")
            print("_","_","_")
            pygame.draw.line(screen,color_line, (0,100),(600,100),8)

            if (reiniciar() == 0):
                vez = 0
                rodada = 0

        if (matriz[1][0] == "o") and  (matriz[1][1] == "o") and (matriz[1][2] == "o"):
            print("_","_","_")
            print("o","o","o")
            print("_","_","_")
            pygame.draw.line(screen,color_line, (0,300),(600,300),8)

            if (reiniciar() == 0):
                vez = 0
                rodada = 0

        if (matriz[2][0] == "o") and  (matriz[2][1] == "o") and (matriz[2][2] == "o"):
            print("_","_","_")
            print("_","_","_")
            print("o","o","o")
            pygame.draw.line(screen,color_line, (0,500),(600,500),8)

            if (reiniciar() == 0):
                vez = 0
                rodada = 0

        # Colunas do X
        if (matriz[0][0] == "x") and  (matriz[1][0] == "x") and (matriz[2][0] == "x"):
            print("x","_","_")
            print("x","_","_")
            print("x","_","_")
            pygame.draw.line(screen,color_line, (0,100),(600,100),8)

            if (reiniciar() == 0):
                vez = 0
                rodada = 0

        if (matriz[0][1] == "x") and  (matriz[1][1] == "x") and (matriz[2][1] == "x"):
            print("_","x","_")
            print("_","x","_")
            print("_","x","_")
            pygame.draw.line(screen,color_line, (0,300),(600,300),8)

            if (reiniciar() == 0):
                vez = 0
                rodada = 0

        if (matriz[0][2] == "x") and  (matriz[1][2] == "x") and (matriz[2][2] == "x"):
            print("_","_","x")
            print("_","_","x")
            print("_","_","x")
            pygame.draw.line(screen,color_line, (0,500),(600,500),8)

            if (reiniciar() == 0):
                vez = 0
                rodada = 0

         # Colunas do O
        if (matriz[0][0] == "o") and  (matriz[1][0] == "o") and (matriz[2][0] == "o"):
            print("o","_","_")
            print("o","_","_")
            print("o","_","_")
            pygame.draw.line(screen,color_line, (0,100),(600,100),8)

            if (reiniciar() == 0):
                vez = 0
                rodada = 0

        if (matriz[0][1] == "o") and  (matriz[1][1] == "o") and (matriz[2][1] == "o"):
            print("_","o","_")
            print("_","o","_")
            print("_","o","_")
            pygame.draw.line(screen,color_line, (0,300),(600,300),8)

            if (reiniciar() == 0):
                vez = 0
                rodada = 0

        if (matriz[0][2] == "o") and  (matriz[1][2] == "o") and (matriz[2][2] == "o"):
            print("_","_","o")
            print("_","_","o")
            print("_","_","o")
            pygame.draw.line(screen,color_line, (0,500),(600,500),8)

            if (reiniciar() == 0):
                vez = 0
                rodada = 0

        # Diagonais do X

        if (matriz[0][2] == "x") and  (matriz[1][1] == "x") and (matriz[2][0] == "x"):
            print("_","_","x")
            print("_","x","_")
            print("x","_","_")
            pygame.draw.line(screen,color_line, (0,300),(600,300),8)

            if (reiniciar() == 0):
                vez = 0
                rodada = 0

        if (matriz[0][0] == "x") and  (matriz[1][1] == "x") and (matriz[2][2] == "x"):
            print("x","_","_")
            print("_","x","_")
            print("_","_","x")
            pygame.draw.line(screen,color_line, (0,500),(600,500),8)

            if (reiniciar() == 0):
                vez = 0
                rodada = 0

        # Diagonais do O

        if (matriz[0][2] == "o") and  (matriz[1][1] == "o") and (matriz[2][0] == "o"):
            print("_","_","o")
            print("_","o","_")
            print("o","_","_")
            pygame.draw.line(screen,color_line, (0,300),(600,300),8)

            if (reiniciar() == 0):
                vez = 0
                rodada = 0

        if (matriz[0][0] == "o") and  (matriz[1][1] == "o") and (matriz[2][2] == "o"):
            print("o","_","_")
            print("_","o","_")
            print("_","_","o")
            pygame.draw.line(screen,color_line, (0,500),(600,500),8)

            if (reiniciar() == 0):
                vez = 0
                rodada = 0


        


        
        

                
    pygame.display.flip()#Atualizador de Janela