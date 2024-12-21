import pygame

def main():
    pygame.init() #Activa recursos
    roca = pygame.image.load("enemigo.bmp")
    h = roca.get_height()
    w = roca.get_width()
    t = w
    ventana = pygame.display.set_mode((8*w,8*h))
    estado = True
    while estado:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                estado = False
        mov()
        actualizar(ventana,roca,i,j)
    pygame.quit()


def mov():
    global i,j
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
       i = i - 2
    if keys[pygame.K_RIGHT]:
        i = i + 2
    if keys[pygame.K_UP]:
        j = j - 2
    if keys[pygame.K_DOWN]:		
        j = j + 2
		
def actualizar(ventana,roca,i,j):
    ventana.fill((0,0,0))
    ventana.blit(roca,(i,j))
    pygame.display.flip()
    pygame.time.delay(10)

i = 0
j = 0
main()
