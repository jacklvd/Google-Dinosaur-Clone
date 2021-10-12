import pygame
import random

class Dinosaur:

    #needed variables
    X_POS = 80
    Y_POS = 310
    Y_POS_DUCK = 340
    JUMP_VEL = 8.5

    #declare variables for the dinosaur actions
    def __init__(self, duck, run, jump):

        self.duck_img = duck
        self.run_img = run
        self.jump_img = jump

        self.dino_duck = False
        self.dino_run = True
        self.dino_jump = False

        self.step_index = 0
        self.jump_vel = self.JUMP_VEL
        #store images to display them continuously to make it look animated
        self.image = self.run_img[0]
        #display the image
        self.dino_rect = self.image.get_rect()
        #position of images
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS

    def update(self, userInput):

        #execute the used variables and function
        if (self.dino_duck):
            self.duck()
        if (self.dino_run):
            self.run()
        if (self.dino_jump):
            self.jump()

        if (self.step_index >= 10):
            self.step_index = 0

        #make the dinosaur jump
        if (userInput[pygame.K_UP] and not self.dino_jump):
            self.dino_duck = False
            self.dino_run = False
            self.dino_jump = True
        #make the dinosaur duck
        elif (userInput[pygame.K_DOWN] and not self.dino_jump):
            self.dino_duck = True
            self.dino_run = False
            self.dino_jump = False
        #if none of those apply dinosaur simply run
        elif not (self.dino_jump or userInput[pygame.K_DOWN]):
            self.dino_duck = False
            self.dino_run = True
            self.dino_jump = False

    def duck(self):
        #to make the action duck then straight back
        self.image = self.duck_img[self.step_index // 5]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS_DUCK
        #count step to make the images display continuously
        self.step_index += 1

    def run(self):
        #to make the action running
        self.image = self.run_img[self.step_index // 5]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS
        #count step to make the images display continuously
        self.step_index += 1

    def jump(self):
        #to make the jump action
        self.image = self.jump_img
        #to make dinosaur fall down
        if self.dino_jump:
            self.dino_rect.y -= self.jump_vel * 4
            self.jump_vel -= 0.8
        #to make the dinosaur jump up
        if self.jump_vel < - self.JUMP_VEL:
            self.dino_jump = False
            self.jump_vel = self.JUMP_VEL

    #display images of dinosaur duck, jump, run, or stand
    def draw(self, SCREEN):
        SCREEN.blit(self.image, (self.dino_rect.x, self.dino_rect.y))

class Cloud:
    #declare needed variables
    def __init__(self, SCREEN_WIDTH, cloud):
        
        self.screen_width = SCREEN_WIDTH
        self.x = self.screen_width + random.randint(700, 900)
        self.y = random.randint(50, 100)
        self.image = cloud
        self.width = self.image.get_width()
        self.game_speed = 20
    #update the screen everytime to make cloud seems moving
    def update(self):
        self.x -= self.game_speed
        if self.x < -self.width:
            self.x = self.screen_width + random.randint(2500, 3000)
            self.y = random.randint(50, 100)

    def draw(self, SCREEN):
        SCREEN.blit(self.image, (self.x, self.y))

class Obstacle:
    #main class for other obstacles to inherit
    def __init__(self, image, type):
        self.image = image
        self.type = type
        self.rect = self.image[self.type].get_rect()
        self.rect.x = 900
        self.game_speed = 20

    def update(self, obstacles):
        self.rect.x -= self.game_speed
        if self.rect.x < -self.rect.width:
            obstacles.pop()

    def draw(self, SCREEN):
        SCREEN.blit(self.image[self.type], self.rect)

class SmallCactus(Obstacle):

    def __init__(self, image):
        self.type = random.randint(0, 2)
        super().__init__(image, self.type)
        self.rect.y = 325

class LargeCactus(Obstacle):

    def __init__(self, image):
        self.type = random.randint(0, 2)
        super().__init__(image, self.type)
        self.rect.y = 300

class Bird(Obstacle):
    
    def __init__(self, image):
        self.type = 0
        super().__init__(image, self.type)
        self.rect.y = 250
        self.index = 0

    def draw(self, SCREEN):
        if self.index >= 9:
            self.index = 0
        SCREEN.blit(self.image[self.index//5], self.rect)
        self.index += 1