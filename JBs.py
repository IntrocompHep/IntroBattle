# todos os import necessários
import pygame

# setup de variáveis obrigatórias
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

def main():
    while running:
        # Área para identficação de eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Área para renderizar o jogo
        #

        # Função para atualizar a tela periodicamente
        pygame.display.flip()
        # Limite de fps limitado a 60
        clock.tick(60)  

    pygame.quit()

main();