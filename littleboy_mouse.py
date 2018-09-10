
import pygame
pygame.init()

screen_size = (100,100)
black = (0, 0, 0)
white = (255, 255, 255)
blue = (0, 0, 255)
green = (0, 255, 0)
red = (255, 0, 0)
 
pi = 3.141592653

boy_pos = [5,17] # x and y
boy_size = (5,5,10,17) # x+ x- y+ y-
speed = [1,1] # speed for x and y
 
# Set the height and width of the screen
screen = pygame.display.set_mode(screen_size)
 
pygame.display.set_caption("Little Boy _mouse")
 
done = False
clock = pygame.time.Clock()

def draw_boy(screen, x, y):
	# Голова
	pygame.draw.ellipse(screen,black,[x - 4,y - 17,10,10],0)
	
	# Ноги
	pygame.draw.line(screen,black,[x,y],[x + 5,y + 10],2)
	pygame.draw.line(screen,black,[x,y],[x - 5,y + 10],2)
	
	# Тело
	pygame.draw.line(screen,red,[x,y - 10],[x,y],2)
	
	# Руки
	pygame.draw.line(screen,red,[x,y - 10],[x + 4,y],2)
	pygame.draw.line(screen,red,[x,y - 10],[x - 4,y],2)
	
 
while not done:
	for event in pygame.event.get():  # User did something
		if event.type == pygame.QUIT:  # If user clicked close
			done = True  # Flag that we are done so we exit this loop
	
	mouse_position = pygame.mouse.get_pos()
	
	if mouse_position[0] + boy_size[0] < screen_size[0] or mouse_position[0] - boy_size[1] > 0:
		boy_pos[0] = mouse_position[0]
	if mouse_position[1] + boy_size[2] < screen_size[0] or mouse_position[1] - boy_size[3] > 0:
		boy_pos[1] = mouse_position[1]

	screen.fill(white)
	draw_boy(screen, boy_pos[0], boy_pos[1])
	
	pygame.display.flip()
	clock.tick(60)
 
pygame.quit()
