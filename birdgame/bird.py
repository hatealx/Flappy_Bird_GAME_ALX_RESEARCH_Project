import pygame
from random import randint, random
pygame.init()

screen = pygame.display.set_mode((480, 700))

# changing window's title
pygame.display.set_caption("freppy bird")

# LOADING BACKGROUND IMAGE
background = pygame.image.load('C:/pygame_projects/birdgame/files/sky.jpg')
begin = pygame.image.load('C:/pygame_projects/birdgame/files/begin.png')


# loading numbers
one = pygame.image.load('C:/pygame_projects/birdgame/files/one.png')
two = pygame.image.load('C:/pygame_projects/birdgame/files/two.png')
three = pygame.image.load('C:/pygame_projects/birdgame/files/three.png')
four = pygame.image.load('C:/pygame_projects/birdgame/files/four.png')
five = pygame.image.load('C:/pygame_projects/birdgame/files/five.png')
six = pygame.image.load('C:/pygame_projects/birdgame/files/six.png')
seven = pygame.image.load('C:/pygame_projects/birdgame/files/seven.png')
eight = pygame.image.load('C:/pygame_projects/birdgame/files/eight.png')
nine = pygame.image.load('C:/pygame_projects/birdgame/files/nine.png')
zero = pygame.image.load('C:/pygame_projects/birdgame/files/zero.png')

# loading musics
hit = pygame.mixer.Sound('C:/pygame_projects/birdgame/files/hit.wav')
die = pygame.mixer.Sound('C:/pygame_projects/birdgame/files/die.wav')
point = pygame.mixer.Sound('C:/pygame_projects/birdgame/files/point.wav')


numbers_dic = {
    '0': zero, '1': one, '2': two, '3': three, '4': four,
    '5': five, '6': six, '7': seven, '8': eight, '9': nine
}


clock = pygame.time.Clock()

def game_over():
    global death_tour, bird_y, xbar, startg

    if death_tour == 0:
        die.play()
    bird_y += 7
    xbar = 0
    screen.blit(background, (0, 0))
    bird = screen.blit(bird_flips[2], (bird_x, bird_y))
    game_over = screen.blit(gameover, (150, 300))
    display_score(score, 220, 350)

    startg = False
    birdup = 0
    death_tour += 1

xb = 0
# loading gameover image
gameover = pygame.image.load('C:/pygame_projects/birdgame/files/gameover.png')


# bird fliping images and position
bird1 = pygame.image.load('C:/pygame_projects/birdgame/files/bird1.png')
bird2 = pygame.image.load('C:/pygame_projects/birdgame/files/bird2.png')
bird3 = pygame.image.load('C:/pygame_projects/birdgame/files/bird3.png')
xbar = 500
bird_x = 150
bird_y = 200

bird_flips = [bird1, bird2, bird3]

flip = 0

# birds life
life = 3


# loading the bars  the bars

bar = pygame.image.load('C:/pygame_projects/birdgame/files/bar.png')
rbar = pygame.transform.flip(bar, True, True)

ybar1 = randint(-30, 0)
ybar2 = randint(600,750)

# Game starter marker
start = True
# gameloop keepin the screen window


death_tour = 0
collision_state = 0

cnybar = None

running = True

score = 0

startg = True

birdup = 3
pause = 5000


def display_score(scorei, x, y):
    score_format = '{:02d}'.format(scorei)
    for character in score_format:
        iscore = numbers_dic[character]
        screen.blit(iscore, (x, y))
        x += 30


state = False

while running:
    clock.tick(100)

    # background image
    screen.blit(background, (0, 0))

    # verifie if the game is started
    if start:
        a = screen.blit(begin, (150, 300))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            # event to start the Game
            if event.key == pygame.K_SPACE:
                start = False  # to remove the start image
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r and startg == False and life <= 0:

                score = 0
                life = 3
                bird_y = 200
                startg == True
                birdup = 4
                death_tour = 0

    if not start:

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 3:  # Left mouse button
                bird_y -= birdup
                if bird_y <= 0:
                    bird_y = 10

        if xbar <= 0:
            # defining position of new coming bars randomly
            xbar = 500
            ybar1 = randint(-100, 30)
            ybar2 = randint(300, 600)

        xbar -= 1
        # drawing the two bars
        bar0 = screen.blit(rbar, (xbar, ybar1))
        nybar = f"{ybar1}:{ybar2}"
        bar1 = screen.blit(bar, (xbar, ybar2))
        bars = [bar0, bar1]

        # dispalying the score
        display_score(score, 400, 650)

        # checking for collision between bird and the two bars

        # making the birds flip ,  controling remaining life
        if life >= 1:
            life_format = str(life)
            number_image = numbers_dic[life_format]
            life_draw = screen.blit(number_image, (10, 650))

            bird_y += 1
            bird = screen.blit(bird_flips[flip], (bird_x, bird_y))
            if flip == 2:
                flip = 0
            else:
                flip += 1
        else:
            game_over()

        if bird_y == 670:
            life = -1

           # to remove the start image

       # checking for collision and taking taking actions
        if bird.collidelist(bars) >= 0:
            state = True  # setting the collision state to True
            if collision_state == 0:
                hit.play()
                life -= 1
                cnybar = nybar  # Storing first positon  of collision and the y coordinates of the two bards
                collision_state += 1
            if collision_state > 0 and cnybar != nybar:  # cheking if there is a new bar y coordinates
                collision_state = 0  # restoring collision state
        if cnybar != nybar:
            state = False  # setting the collision state to false if the only a new bar is created

        # checking for collision and increasing   score if the bird passes the the two bars gap
        if bird_x - xbar == 50 and state != True:
            point.play()
            score += 1

    
    pygame.display.update()

pygame.quit()