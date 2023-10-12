import pygame

# setup de variáveis obrigatórias
pygame.init()
screen = pygame.display.set_mode((1024, 768))
pygame.display.set_caption('Battle')
clock = pygame.time.Clock()
running = True

#baixar imagens
#imagens de fundo
background_img = pygame.image.load('c:\\Users\\joaom\Downloads\\teste3ps.png').convert_alpha()
background_img = pygame.transform.scale(background_img,(1024,768))
#função pra desenhar o fundo
def draw_bg():
    screen.blit(background_img, (0,0))

def main():
    global running;
    while running:
        #desenhar fundo
        draw_bg()
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
