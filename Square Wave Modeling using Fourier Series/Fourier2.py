import pygame
import math

pygame.init()
window = pygame.display.set_mode((1500, 720))
font = pygame.font.SysFont(None, 40)
clock = pygame.time.Clock()
cpt = window.get_rect().center
cpt= [cpt[0]-500,cpt[1]]
angle = 0
angle2 = 0
angle3 = 0
angle4 = 0
radius = 100

points  = []
theta =0 
run = True
while run:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False  

    N=1
    N2 = 3
    N3 =5
    N4 = 7
    N5  =9
    N6  =11
    angle_rad = math.radians(angle)
    pt_x = cpt[0] + (radius*(4/math.pi)) * math.sin(N*angle_rad)
    pt_y = cpt[1] - (radius *(4/math.pi))* math.cos(N*angle_rad)
    pt_x2 = pt_x + (-radius*(4/(3*math.pi))) * math.sin(N2*angle_rad)
    pt_y2 = pt_y - (-radius *(4/(3*math.pi)))* math.cos(N2*angle_rad)
    pt_x3 = pt_x2 + (radius*(4/(5*math.pi))) * math.sin(N3*angle_rad)
    pt_y3 = pt_y2 - (radius *(4/(5*math.pi)))* math.cos(N3*angle_rad)
    pt_x4 = pt_x3 + (-radius*(4/(7*math.pi))) * math.sin(N4*angle_rad)
    pt_y4 = pt_y3 - (-radius *(4/(7*math.pi)))* math.cos(N4*angle_rad)
    pt_x5 = pt_x4 + (radius*(4/(9*math.pi))) * math.sin(N5*angle_rad)
    pt_y5 = pt_y4 - (radius *(4/(9*math.pi)))* math.cos(N5*angle_rad)
    pt_x6 = pt_x5 + (-radius*(4/(11*math.pi))) * math.sin(N6*angle_rad)
    pt_y6 = pt_y5 - (-radius *(4/(11*math.pi)))* math.cos(N6*angle_rad)
    pt_x7 = pt_x6 + (radius*(4/(13*math.pi))) * math.sin(13*angle_rad)
    pt_y7 = pt_y6 - (radius *(4/(13*math.pi)))* math.cos(13*angle_rad)
    pt_x8 = pt_x7 + (-radius*(4/(15*math.pi))) * math.sin(15*angle_rad)
    pt_y8 = pt_y7 - (-radius *(4/(15*math.pi)))* math.cos(15*angle_rad)
    
   
    
    angle -= 1   
    if angle <= -360:
        angle = 0
    

    window.fill((255, 255, 255))
    pygame.draw.circle(window, (0, 0, 0), cpt, radius*(4/(1*math.pi)), 2)
    pygame.draw.line(window, (0, 0, 255), cpt, (pt_x, pt_y), 2)
    pygame.draw.circle(window, (0, 0, 0), (pt_x, pt_y), radius*(4/(3*math.pi)), 2)
    pygame.draw.line(window, (0, 0, 255),(pt_x, pt_y), (pt_x2, pt_y2), 2)
    pygame.draw.circle(window, (0, 0, 0), (pt_x2, pt_y2), radius*(4/(5*math.pi)), 2)
    pygame.draw.line(window, (0, 0, 255),(pt_x2, pt_y2), (pt_x3, pt_y3), 2)
    pygame.draw.circle(window, (0, 0, 0), (pt_x3, pt_y3), radius*(4/(7*math.pi)), 2)
    pygame.draw.line(window, (0, 0, 255),(pt_x3, pt_y3), (pt_x4, pt_y4), 2)
    pygame.draw.circle(window, (0, 0, 0), (pt_x4, pt_y4), radius*(4/(9*math.pi)), 2)
    pygame.draw.line(window, (0, 0, 255),(pt_x4, pt_y4), (pt_x5, pt_y5), 2)
    pygame.draw.circle(window, (0, 0, 0), (pt_x5, pt_y5), radius*(4/(11*math.pi)), 2)
    pygame.draw.line(window, (0, 0, 255),(pt_x5, pt_y5), (pt_x6, pt_y6), 2)
    pygame.draw.circle(window, (0, 0, 0), (pt_x6, pt_y6), radius*(4/(13*math.pi)), 2)
    pygame.draw.line(window, (0, 0, 255),(pt_x6, pt_y6), (pt_x7, pt_y7), 2)
    pygame.draw.circle(window, (0, 0, 0), (pt_x7, pt_y7), radius*(4/(15*math.pi)), 2)
    pygame.draw.line(window, (0, 0, 255),(pt_x7, pt_y7), (pt_x8, pt_y8), 2)
    
    #pygame.draw.line(window, (0, 0, 255), (cpt[0]+400,cpt[1]), (cpt[0]+400+(90), cpt[1]), 2)
    
    
    
    
    points.append([cpt[0]+400+theta,pt_y8])
    for x, y  in points:

        pygame.draw.circle(window, (0, 0, 255), (x,y), 2, 2)
    
    theta+=1.5
    print(theta)
    if theta ==750:
        points =[]
        theta = 0
        window.fill((255, 255, 255))


    
    
    pygame.display.flip()

pygame.quit()
exit()