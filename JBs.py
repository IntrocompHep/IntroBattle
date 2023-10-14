import pygame

# setup de variáveis obrigatórias
pygame.init()
screen = pygame.display.set_mode((1024, 768))
clock = pygame.time.Clock()
running = True
#imagens de fundo
background_img = pygame.image.load('fundo.png').convert_alpha()
background_img = pygame.transform.scale(background_img,(1024,768))
#função pra desenhar o fundo
def draw_bg():
    screen.blit(background_img, (0,0))

        
class PersonagemSprite(pygame.sprite.Sprite):
    def _init_(self, nome_personagem, vida, pontos_ataque, pontos_defesa):
        super()._init_()
        self.vida = vida
        self.ataque = pontos_ataque
        self.defesa = pontos_defesa
        nome_arquivo = nome_personagem + ".png"
        self.image = pygame.image.load(nome_arquivo)
        self.rect = pygame.rect.Rect(0, 0, 0, 0)
    def atacar(self, Inimigo):
        # calcular dano do ataque
        dano = self.ataque * (50 / (50 + Inimigo.defesa))
        # descontar da vida do outro personagem o dano do ataque
        Inimigo.vida = Inimigo.vida - dano
    
imagem_paladino = PersonagemSprite("Paladino", vida=100, pontos_ataque=10, pontos_defesa=20)
imagem_feiticeiro = PersonagemSprite("wizardfinal", vida=100, pontos_ataque=10, pontos_defesa=20)
imagem_arqueiro = PersonagemSprite("hunter sprite",  vida=100, pontos_ataque=10, pontos_defesa=20)
#movendo personagem
imagem_paladino.rect.move_ip(100, 300)
imagem_feiticeiro.rect.move_ip(100, 500)
imagem_arqueiro.rect.move_ip(100, 700)
#virando feiticeiro
imagem_feiticeiro.image = pygame.transform.flip(imagem_feiticeiro.image, True, False)

class Inimigo(pygame.sprite.Sprite):
    def _init_(self, nome_personagem, vida, pontos_ataque, pontos_defesa):
        super()._init_()
        self.vida = vida
        self.ataque = pontos_ataque
        self.defesa = pontos_defesa
        nome_arquivo = nome_personagem + ".png"
        self.image = pygame.image.load(nome_arquivo)
        self.rect = pygame.rect.Rect(0, 0, 0, 0)
    def atacar(self, PersonagemSprite):
        # calcular dano do ataque
        dano = self.ataque * (50 / (50 + PersonagemSprite.defesa))
        # descontar da vida do outro personagem o dano do ataque
        PersonagemSprite.vida = PersonagemSprite.vida - dano

imagem_caveira = Inimigo("caveira sprite 2",  vida=100, pontos_ataque=10, pontos_defesa=20)  
imagem_magoDoMal = Inimigo("Sprite-0001", vida=100, pontos_ataque=10, pontos_defesa=20)
# movendo imagem      
imagem_caveira.rect.move_ip(924,300)
imagem_magoDoMal.rect.move_ip(924,500)
# virando imagem
imagem_caveira.image = pygame.transform.flip(imagem_caveira.image, True, False)
imagem_magoDoMal.image = pygame.transform.flip(imagem_magoDoMal.image, True, False)
# criando o grupo
batalha = pygame.sprite.Group()
# adicionando o paladino a batalha
imagem_paladino.add(batalha)
imagem_arqueiro.add(batalha)
imagem_feiticeiro.add(batalha)
imagem_caveira.add(batalha)
imagem_magoDoMal.add(batalha)
batalha.draw(screen)

class Barra(pygame.sprite.Sprite):
    def _init_(self, barra_imagem):
        super()._init_()
        nome_arquivo = barra_imagem + ".png"
        self.image = pygame.image.load(nome_arquivo)
        self.rect = pygame.rect.Rect(0, 0, 0, 0)
#a barra de todos os personagens(vai ser uma pra todos)
barra_imagem0 = Barra("introcomp_mp_left")
barra_imagem01 = Barra("introcomp_mp")
barra_imagem02 = Barra("introcomp_mp_right")
barra_imagem0.rect.move_ip(99,200)
barra_imagem01.rect.move_ip(99,200)
barra_imagem02.rect.move_ip(99,200)

barra_inteiraPersonagem = pygame.sprite.Group()
barra_imagem0.add(barra_inteiraPersonagem)
barra_imagem01.add(barra_inteiraPersonagem)
barra_imagem02.add(barra_inteiraPersonagem)

barra_inteiraPersonagem.draw(screen)
#a barra de todos os inimigos(vai ser uma pra todos)    
barra_imagem1 = Barra("introcomp_hp_left")
barra_imagem2 = Barra("introcomp_hp ")
barra_imagem3 = Barra("introcomp_hp_right")
barra_imagem1.rect.move_ip(924,200)
barra_imagem2.rect.move_ip(924,200)
barra_imagem3.rect.move_ip(924,200)

barra_inteira = pygame.sprite.Group()
barra_imagem1.add(barra_inteira)
barra_imagem2.add(barra_inteira)
barra_imagem3.add(barra_inteira)

barra_inteira.draw(screen)

def main():
    global running
    while running:
        if (imagem_paladino.vida>0 or imagem_feiticeiro.vida>0 or imagem_arqueiro.vida>0) and (imagem_caveira.vida>0 or imagem_magoDoMal.vida>0):
            pass
        else:
            running = False
        # Área para identficação de eventos
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    imagem_paladino.atacar(imagem_caveira)
                    print(imagem_caveira.vida)
                    barra_inteira.clear(screen, pygame.surface.Surface((1024,768)))
                    barra_imagem3.remove(barra_inteira)
                    barra_inteira.draw(screen)
                    if imagem_caveira.vida<25:
                        barra_inteira.clear(screen, pygame.surface.Surface((1024,768)))
                        barra_imagem2.remove(barra_inteira)
                        barra_inteira.draw(screen)
                    elif imagem_caveira.vida<10:
                        barra_inteira.clear(screen, pygame.surface.Surface((1024,768)))
                elif event.key == pygame.K_w:
                    imagem_feiticeiro.atacar(imagem_caveira)
                    print(imagem_caveira.vida)
                    barra_inteira.clear(screen, pygame.surface.Surface((1024,768)))
                    barra_imagem3.remove(barra_inteira)
                    barra_inteira.draw(screen)
                    if imagem_caveira.vida<25:
                        barra_inteira.clear(screen, pygame.surface.Surface((1024,768)))
                        barra_imagem2.remove(barra_inteira)
                        barra_inteira.draw(screen)
                    elif imagem_caveira.vida<10:
                        barra_inteira.clear(screen, pygame.surface.Surface((1024,768)))
                elif event.key == pygame.K_d:
                    imagem_arqueiro.atacar(imagem_caveira)
                    print(imagem_caveira.vida)
                    barra_inteira.clear(screen, pygame.surface.Surface((1024,768)))
                    barra_imagem3.remove(barra_inteira)
                    barra_inteira.draw(screen)
                    if imagem_caveira.vida<25:
                        barra_inteira.clear(screen, pygame.surface.Surface((1024,768)))
                        barra_imagem2.remove(barra_inteira)
                        barra_inteira.draw(screen)
                    elif imagem_caveira.vida<10:
                        barra_inteira.clear(screen, pygame.surface.Surface((1024,768)))
                
                        
            if event.type == pygame.QUIT:
                running = False
        


        # Função para atualizar a tela periodicamente
        pygame.display.flip()
        # Limite de fps limitado a 60
        clock.tick(60)  

    pygame.quit()

main()
