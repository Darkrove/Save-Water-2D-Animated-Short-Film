try:
    import pygame
    import time
except ModuleNotFoundError:
    print("unable to import pygame.\n\n\nWARNING: plzzz install pygame module using pip commmand.")
    exit()

#fix size for window
SIZE = WIDTH, HEIGHT = 1180, 550
#main window color
BACKGROUND_COLOR=pygame.Color('white') 
#frame per second
FPS = 4
#color code
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)

# class-> 1 , image->1 and 2(.png) , fps=4 
# directory->'C:\Users\sajjad shaikh\Desktop\Final Project(sem 2)\python_pro\image' 
# pygame.sprite.Sprite-> parent class
class water_falling_1(pygame.sprite.Sprite):
    #constructor for class
    def __init__(self):
        #calling parent class method using super function
        super().__init__()
        #empty list for appending images
        self.images = []
        try:
            #python.tranform.scale-> resizing images , python.image.load-> open images 
            self.images.append(pygame.transform.scale(pygame.image.load(r'C:\Users\sajjad shaikh\Desktop\Final Project(sem 2)\python_pro\image\1.png'),(1170,540)))
            self.images.append(pygame.transform.scale(pygame.image.load(r'C:\Users\sajjad shaikh\Desktop\Final Project(sem 2)\python_pro\image\1.png'),(1170,540)))
            self.images.append(pygame.transform.scale(pygame.image.load(r'C:\Users\sajjad shaikh\Desktop\Final Project(sem 2)\python_pro\image\2.png'),(1170,540)))
            self.images.append(pygame.transform.scale(pygame.image.load(r'C:\Users\sajjad shaikh\Desktop\Final Project(sem 2)\python_pro\image\2.png'),(1170,540)))
        except FileNotFoundError:
            print("unable to load images.\n\n\nWARNING: Image not found.")
        #index for empty list
        self.index = 0
        #self.image-> parent class method
        self.image = self.images[self.index]
        #pygame.Rect-> to store and manipulate rectangular areas pygame.Rect(left, top, width. height)
        self.rect = pygame.Rect(5, 5, 150, 1250)
    #for updating frame
    def update(self):
        self.index += 1
            
        try:
            if self.index == len(self.images):
                self.index = 0
        except IndexError:
            print('EVERYTHING IS NORMAL')
        finally:
            self.image = self.images[self.index]


# class-> 2 , image-> 3 and 4(.png) , fps-> 4 
# directory-> 'C:\Users\sajjad shaikh\Desktop\Final Project(sem 2)\python_pro\image'  
# pygame.sprite.Sprite-> parent class
class man_1(pygame.sprite.Sprite):
    #constructor for class
    def __init__(self):
        #calling parent class method using super function
        super().__init__()
        #empty list for appending images
        self.images = []
        try:
            #python.tranform.scale-> resizing images , python.image.load-> open images 
            self.images.append(pygame.transform.scale(pygame.image.load(r'C:\Users\sajjad shaikh\Desktop\Final Project(sem 2)\python_pro\image\3.png'),(1170,540)))
            self.images.append(pygame.transform.scale(pygame.image.load(r'C:\Users\sajjad shaikh\Desktop\Final Project(sem 2)\python_pro\image\3.png'),(1170,540)))
            self.images.append(pygame.transform.scale(pygame.image.load(r'C:\Users\sajjad shaikh\Desktop\Final Project(sem 2)\python_pro\image\4.png'),(1170,540)))
            self.images.append(pygame.transform.scale(pygame.image.load(r'C:\Users\sajjad shaikh\Desktop\Final Project(sem 2)\python_pro\image\4.png'),(1170,540)))
        except FileNotFoundError:
            print('unable to load images.\n\n\nWARNING: Image not found.')
        #index for empty list
        self.index = 0
        #self.image-> parent class method
        self.image = self.images[self.index]
        #pygame.Rect-> to store and manipulate rectangular areas pygame.Rect(left, top, width. height)
        self.rect = pygame.Rect(5, 5, 150, 1250)
    #for updating frame
    def update(self):
        self.index += 1
            
        try:
            if self.index == len(self.images):
                self.index = 0
        except IndexError:
            print('EVERYTHING IS NORMAL')
        finally:
            self.image = self.images[self.index]

# class-> 3 , image-> 5 and 6(.png) , fps-> 4 
# directory-> 'C:\Users\sajjad shaikh\Desktop\Final Project(sem 2)\python_pro\image'  
# pygame.sprite.Sprite-> parent class
class water_falling_2(pygame.sprite.Sprite):
    #constructor for class
    def __init__(self):
        #calling parent class method using super function
        super().__init__()
        #empty list for appending images
        self.images = []
        try:
            #python.tranform.scale-> resizing images , python.image.load-> open images 
            self.images.append(pygame.transform.scale(pygame.image.load(r'C:\Users\sajjad shaikh\Desktop\Final Project(sem 2)\python_pro\image\5.png'),(1170,540)))
            self.images.append(pygame.transform.scale(pygame.image.load(r'C:\Users\sajjad shaikh\Desktop\Final Project(sem 2)\python_pro\image\5.png'),(1170,540)))
            self.images.append(pygame.transform.scale(pygame.image.load(r'C:\Users\sajjad shaikh\Desktop\Final Project(sem 2)\python_pro\image\6.png'),(1170,540)))
            self.images.append(pygame.transform.scale(pygame.image.load(r'C:\Users\sajjad shaikh\Desktop\Final Project(sem 2)\python_pro\image\6.png'),(1170,540)))
        except FileNotFoundError:
            print('unable to load images.\n\n\nWARNING: Image not found.')
        #index for empty list
        self.index = 0
        #self.image-> parent class method
        self.image = self.images[self.index]
        #pygame.Rect-> to store and manipulate rectangular areas pygame.Rect(left, top, width. height)
        self.rect = pygame.Rect(5, 5, 150, 1250)
    #for updating frame
    def update(self):
        self.index += 1
            
        try:
            if self.index == len(self.images):
                self.index = 0
        except IndexError:
            print('EVERYTHING IS NORMAL')
        finally:
            self.image = self.images[self.index]

# class-> 4 , image-> 8 and 7(.png) , fps-> 4 
# directory-> 'C:\Users\sajjad shaikh\Desktop\Final Project(sem 2)\python_pro\image'  
# pygame.sprite.Sprite-> parent class
class man_2(pygame.sprite.Sprite):
    #constructor for class
    def __init__(self):
        #calling parent class method using super function
        super().__init__()
        #empty list for appending images
        self.images = []
        try:
            #python.tranform.scale-> resizing images , python.image.load-> open images 
            self.images.append(pygame.transform.scale(pygame.image.load(r'C:\Users\sajjad shaikh\Desktop\Final Project(sem 2)\python_pro\image\7.png'),(1170,540)))
            self.images.append(pygame.transform.scale(pygame.image.load(r'C:\Users\sajjad shaikh\Desktop\Final Project(sem 2)\python_pro\image\7.png'),(1170,540)))
            self.images.append(pygame.transform.scale(pygame.image.load(r'C:\Users\sajjad shaikh\Desktop\Final Project(sem 2)\python_pro\image\8.png'),(1170,540)))
            self.images.append(pygame.transform.scale(pygame.image.load(r'C:\Users\sajjad shaikh\Desktop\Final Project(sem 2)\python_pro\image\8.png'),(1170,540)))
        except FileNotFoundError:
            print('unable to load images.\n\n\nWARNING: Image not found.')
        #index for empty list
        self.index = 0
        #self.image-> parent class method
        self.image = self.images[self.index]
        #pygame.Rect-> to store and manipulate rectangular areas pygame.Rect(left, top, width. height)
        self.rect = pygame.Rect(5, 5, 150, 1250)
    #for updating frame
    def update(self):
        self.index += 1
            
        try:
            if self.index == len(self.images):
                self.index = 0
        except IndexError:
            print('EVERYTHING IS NORMAL')
        finally:
            self.image = self.images[self.index]


# class-> 5 , image-> 9 and 10(.png) , fps-> 4 
# directory-> 'C:\Users\sajjad shaikh\Desktop\Final Project(sem 2)\python_pro\image'  
# pygame.sprite.Sprite-> parent class
class water_falling_3(pygame.sprite.Sprite):
    #constructor for class
    def __init__(self):
        #calling parent class method using super function
        super().__init__()
        #empty list for appending images
        self.images = []
        try:
            #python.tranform.scale-> resizing images , python.image.load-> open images 
            self.images.append(pygame.transform.scale(pygame.image.load(r'C:\Users\sajjad shaikh\Desktop\Final Project(sem 2)\python_pro\image\9.png'),(1170,540)))
            self.images.append(pygame.transform.scale(pygame.image.load(r'C:\Users\sajjad shaikh\Desktop\Final Project(sem 2)\python_pro\image\9.png'),(1170,540)))
            self.images.append(pygame.transform.scale(pygame.image.load(r'C:\Users\sajjad shaikh\Desktop\Final Project(sem 2)\python_pro\image\10.png'),(1170,540)))
            self.images.append(pygame.transform.scale(pygame.image.load(r'C:\Users\sajjad shaikh\Desktop\Final Project(sem 2)\python_pro\image\10.png'),(1170,540)))
        except FileNotFoundError:
            print('unable to load images.\n\n\nWARNING: Image not found.')
        #index for empty list
        self.index = 0
        #self.image-> parent class method
        self.image = self.images[self.index]
        #pygame.Rect-> to store and manipulate rectangular areas pygame.Rect(left, top, width. height)
        self.rect = pygame.Rect(5, 5, 150, 1250)
    #for updating frame
    def update(self):
        self.index += 1
            
        try:
            if self.index == len(self.images):
                self.index = 0
        except IndexError:
            print('EVERYTHING IS NORMAL')
        finally:
            self.image = self.images[self.index]


    
# class-> 6 , image-> 11 and 12(.png) , fps-> 4 
# directory-> 'C:\Users\sajjad shaikh\Desktop\Final Project(sem 2)\python_pro\image'  
# pygame.sprite.Sprite-> parent class
class man_3(pygame.sprite.Sprite):
    #constructor for class
    def __init__(self):
        #calling parent class method using super function
        super().__init__()
        #empty list for appending images
        self.images = []
        try:
            #python.tranform.scale-> resizing images , python.image.load-> open images 
            self.images.append(pygame.transform.scale(pygame.image.load(r'C:\Users\sajjad shaikh\Desktop\Final Project(sem 2)\python_pro\image\11.png'),(1170,540)))
            self.images.append(pygame.transform.scale(pygame.image.load(r'C:\Users\sajjad shaikh\Desktop\Final Project(sem 2)\python_pro\image\11.png'),(1170,540)))
            self.images.append(pygame.transform.scale(pygame.image.load(r'C:\Users\sajjad shaikh\Desktop\Final Project(sem 2)\python_pro\image\12.png'),(1170,540)))
            self.images.append(pygame.transform.scale(pygame.image.load(r'C:\Users\sajjad shaikh\Desktop\Final Project(sem 2)\python_pro\image\12.png'),(1170,540)))
        except FileNotFoundError:
            print('unable to load images.\n\n\nWARNING: Image not found.')
        #index for empty list
        self.index = 0
        #self.image-> parent class method
        self.image = self.images[self.index]
        #pygame.Rect-> to store and manipulate rectangular areas pygame.Rect(left, top, width. height)
        self.rect = pygame.Rect(5, 5, 150, 1250)
    #for updating frame
    def update(self):
        self.index += 1
            
        try:
            if self.index == len(self.images):
                self.index = 0
        except IndexError:
            print('EVERYTHING IS NORMAL')
        finally:
            self.image = self.images[self.index]


# class-> 7 , image-> 13,14,15,16,17,18 and 19(.png) , fps-> 4 
# directory-> 'C:\Users\sajjad shaikh\Desktop\Final Project(sem 2)\python_pro\image'  
# pygame.sprite.Sprite-> parent class
class water_falling_4(pygame.sprite.Sprite):
    #constructor for class
    def __init__(self):
        #calling parent class method using super function
        super().__init__()
        #empty list for appending images
        self.images = []
        try:
            #python.tranform.scale-> resizing images , python.image.load-> open images 
            self.images.append(pygame.transform.scale(pygame.image.load(r'C:\Users\sajjad shaikh\Desktop\Final Project(sem 2)\python_pro\image\13.png'),(1170,540)))
            self.images.append(pygame.transform.scale(pygame.image.load(r'C:\Users\sajjad shaikh\Desktop\Final Project(sem 2)\python_pro\image\13.png'),(1170,540)))
            self.images.append(pygame.transform.scale(pygame.image.load(r'C:\Users\sajjad shaikh\Desktop\Final Project(sem 2)\python_pro\image\14.png'),(1170,540)))
            self.images.append(pygame.transform.scale(pygame.image.load(r'C:\Users\sajjad shaikh\Desktop\Final Project(sem 2)\python_pro\image\14.png'),(1170,540)))
            self.images.append(pygame.transform.scale(pygame.image.load(r'C:\Users\sajjad shaikh\Desktop\Final Project(sem 2)\python_pro\image\15.png'),(1170,540)))
            self.images.append(pygame.transform.scale(pygame.image.load(r'C:\Users\sajjad shaikh\Desktop\Final Project(sem 2)\python_pro\image\15.png'),(1170,540)))
            self.images.append(pygame.transform.scale(pygame.image.load(r'C:\Users\sajjad shaikh\Desktop\Final Project(sem 2)\python_pro\image\16.png'),(1170,540)))
            self.images.append(pygame.transform.scale(pygame.image.load(r'C:\Users\sajjad shaikh\Desktop\Final Project(sem 2)\python_pro\image\16.png'),(1170,540))) 
            self.images.append(pygame.transform.scale(pygame.image.load(r'C:\Users\sajjad shaikh\Desktop\Final Project(sem 2)\python_pro\image\17.png'),(1170,540)))
            self.images.append(pygame.transform.scale(pygame.image.load(r'C:\Users\sajjad shaikh\Desktop\Final Project(sem 2)\python_pro\image\17.png'),(1170,540)))
            self.images.append(pygame.transform.scale(pygame.image.load(r'C:\Users\sajjad shaikh\Desktop\Final Project(sem 2)\python_pro\image\18.png'),(1170,540)))
            self.images.append(pygame.transform.scale(pygame.image.load(r'C:\Users\sajjad shaikh\Desktop\Final Project(sem 2)\python_pro\image\18.png'),(1170,540)))
            self.images.append(pygame.transform.scale(pygame.image.load(r'C:\Users\sajjad shaikh\Desktop\Final Project(sem 2)\python_pro\image\19.png'),(1170,540)))
            self.images.append(pygame.transform.scale(pygame.image.load(r'C:\Users\sajjad shaikh\Desktop\Final Project(sem 2)\python_pro\image\19.png'),(1170,540)))       
        except FileNotFoundError:
            print('unable to load images.\n\n\nWARNING: Image not found.')
        #index for empty list
        self.index = 0
        #self.image-> parent class method
        self.image = self.images[self.index]
        #pygame.Rect-> to store and manipulate rectangular areas pygame.Rect(left, top, width. height)
        self.rect = pygame.Rect(5, 5, 150, 1250)
    #for updating frame
    def update(self):
        self.index += 1
            
        try:
            if self.index == len(self.images):
                self.index = 0
        except IndexError:
            print('EVERYTHING IS NORMAL')
        finally:
            self.image = self.images[self.index]
            
# class-> 8 , image-> 20 and 21(.png) , fps-> 4 
# directory-> 'C:\Users\sajjad shaikh\Desktop\Final Project(sem 2)\python_pro\image'  
# pygame.sprite.Sprite-> parent class
class man_4(pygame.sprite.Sprite):
    #constructor for class
    def __init__(self):
        #calling parent class method using super function
        super().__init__()
        #empty list for appending images
        self.images = []
        try:
            #python.tranform.scale-> resizing images , python.image.load-> open images 
            self.images.append(pygame.transform.scale(pygame.image.load(r'C:\Users\sajjad shaikh\Desktop\Final Project(sem 2)\python_pro\image\20.png'),(1170,540)))
            self.images.append(pygame.transform.scale(pygame.image.load(r'C:\Users\sajjad shaikh\Desktop\Final Project(sem 2)\python_pro\image\20.png'),(1170,540)))
            self.images.append(pygame.transform.scale(pygame.image.load(r'C:\Users\sajjad shaikh\Desktop\Final Project(sem 2)\python_pro\image\21.png'),(1170,540)))
            self.images.append(pygame.transform.scale(pygame.image.load(r'C:\Users\sajjad shaikh\Desktop\Final Project(sem 2)\python_pro\image\21.png'),(1170,540)))
        except FileNotFoundError:
            print('unable to load images.\n\n\nWARNING: Image not found.')
        #index for empty list
        self.index = 0
        #self.image-> parent class method
        self.image = self.images[self.index]
        #pygame.Rect-> to store and manipulate rectangular areas pygame.Rect(left, top, width. height)
        self.rect = pygame.Rect(5, 5, 150, 1250)
    #for updating frame
    def update(self):
        self.index += 1
            
        try:
            if self.index == len(self.images):
                self.index = 0
        except IndexError:
            print('EVERYTHING IS NORMAL')
        finally:
            self.image = self.images[self.index]


# class-> 9 , image-> 22(.png) , fps-> 4 
# directory-> 'C:\Users\sajjad shaikh\Desktop\Final Project(sem 2)\python_pro\image'  
# pygame.sprite.Sprite-> parent class
class man_5(pygame.sprite.Sprite):
    #constructor for class
    def __init__(self):
        #calling parent class method using super function
        super().__init__()
        #empty list for appending images
        self.images = []
        #python.tranform.scale-> resizing images , python.image.load-> open images 
        try: 
            self.images.append(pygame.transform.scale(pygame.image.load(r'C:\Users\sajjad shaikh\Desktop\Final Project(sem 2)\python_pro\image\22.png'),(1170,540)))
        except FileNotFoundError:
            print('unable to load images.\n\n\nWARNING: Image not found.')
        #index for empty list
        self.index = 0
        #self.image-> parent class method
        self.image = self.images[self.index]
        #pygame.Rect-> to store and manipulate rectangular areas pygame.Rect(left, top, width. height)
        self.rect = pygame.Rect(5, 5, 150, 1250)
    #for updating frame
    def update(self):
        self.index += 1
            
        try:
            if self.index == len(self.images):
                self.index = 0
        except IndexError:
            print('EVERYTHING IS NORMAL')
        finally:
            self.image = self.images[self.index]


# class-> 10 , image-> 23,24,25,26,27(.png) , fps-> 4 
# directory-> 'C:\Users\sajjad shaikh\Desktop\Final Project(sem 2)\python_pro\image'  
# pygame.sprite.Sprite-> parent class
class man_6(pygame.sprite.Sprite):
    #constructor for class
    def __init__(self):
        #calling parent class method using super function
        super().__init__()
        #empty list for appending images
        self.images = []
        try:
            #python.tranform.scale-> resizing images , python.image.load-> open images 
            self.images.append(pygame.transform.scale(pygame.image.load(r'C:\Users\sajjad shaikh\Desktop\Final Project(sem 2)\python_pro\image\23.png'),(1170,540)))
            self.images.append(pygame.transform.scale(pygame.image.load(r'C:\Users\sajjad shaikh\Desktop\Final Project(sem 2)\python_pro\image\23.png'),(1170,540)))
            self.images.append(pygame.transform.scale(pygame.image.load(r'C:\Users\sajjad shaikh\Desktop\Final Project(sem 2)\python_pro\image\24.png'),(1170,540)))
            self.images.append(pygame.transform.scale(pygame.image.load(r'C:\Users\sajjad shaikh\Desktop\Final Project(sem 2)\python_pro\image\24.png'),(1170,540)))
            self.images.append(pygame.transform.scale(pygame.image.load(r'C:\Users\sajjad shaikh\Desktop\Final Project(sem 2)\python_pro\image\25.png'),(1170,540)))
            self.images.append(pygame.transform.scale(pygame.image.load(r'C:\Users\sajjad shaikh\Desktop\Final Project(sem 2)\python_pro\image\25.png'),(1170,540)))
            self.images.append(pygame.transform.scale(pygame.image.load(r'C:\Users\sajjad shaikh\Desktop\Final Project(sem 2)\python_pro\image\26.png'),(1170,540)))
            self.images.append(pygame.transform.scale(pygame.image.load(r'C:\Users\sajjad shaikh\Desktop\Final Project(sem 2)\python_pro\image\26.png'),(1170,540)))
            self.images.append(pygame.transform.scale(pygame.image.load(r'C:\Users\sajjad shaikh\Desktop\Final Project(sem 2)\python_pro\image\27.png'),(1170,540)))
            self.images.append(pygame.transform.scale(pygame.image.load(r'C:\Users\sajjad shaikh\Desktop\Final Project(sem 2)\python_pro\image\27.png'),(1170,540)))
        except FileNotFoundError:
            print('unable to load images.\n\n\nWARNING: Image not found.')
        #index for empty list
        self.index = 0
        #self.image-> parent class method
        self.image = self.images[self.index]
        #pygame.Rect-> to store and manipulate rectangular areas pygame.Rect(left, top, width. height)
        self.rect = pygame.Rect(5, 5, 150, 1250)
    #for updating frame
    def update(self):
        self.index += 1
            
        try:
            if self.index == len(self.images):
                self.index = 0
        except IndexError:
            print('EVERYTHING IS NORMAL')
        finally:
            self.image = self.images[self.index]

# class-> 11 , image-> 28(.png) , fps-> 4 
# directory-> 'C:\Users\sajjad shaikh\Desktop\Final Project(sem 2)\python_pro\image'  
# pygame.sprite.Sprite-> parent class
class man_7(pygame.sprite.Sprite):
    #constructor for class
    def __init__(self):
        #calling parent class method using super function
        super().__init__()
        #empty list for appending images
        self.images = []
        try:
            #python.tranform.scale-> resizing images , python.image.load-> open images
            self.images.append(pygame.transform.scale(pygame.image.load(r'C:\Users\sajjad shaikh\Desktop\Final Project(sem 2)\python_pro\image\28.png'),(1170,540)))
        except FileNotFoundError:
            print('unable to load images.\n\n\nWARNING: Image not found.')    
        #index for empty list
        self.index = 0
        #self.image-> parent class method
        self.image = self.images[self.index]
        #pygame.Rect-> to store and manipulate rectangular areas pygame.Rect(left, top, width. height)
        self.rect = pygame.Rect(5, 5, 150, 1250)
    #for updating frame
    def update(self):
        self.index += 1
            
        try:
            if self.index == len(self.images):
                self.index = 0
        except IndexError:
            print('EVERYTHING IS NORMAL')
        finally:
            self.image = self.images[self.index]

# class-> 12 , image-> 29 (.png) , fps-> 4 
# directory-> 'C:\Users\sajjad shaikh\Desktop\Final Project(sem 2)\python_pro\image'  
# pygame.sprite.Sprite-> parent class
class text_1(pygame.sprite.Sprite):
    #constructor for class
    def __init__(self):
        #calling parent class method using super function
        super().__init__()
        #empty list for appending images
        self.images = []
        try:
            #python.tranform.scale-> resizing images , python.image.load-> open images
            self.images.append(pygame.transform.scale(pygame.image.load(r'C:\Users\sajjad shaikh\Desktop\Final Project(sem 2)\python_pro\image\29.png'),(1170,540)))
        except FileNotFoundError:
            print('unable to load images.\n\n\nWARNING: Image not found.')
        #index for empty list
        self.index = 0
        #self.image-> parent class method
        self.image = self.images[self.index]
        #pygame.Rect-> to store and manipulate rectangular areas pygame.Rect(left, top, width. height)
        self.rect = pygame.Rect(5, 5, 150, 1250)
    #for updating frame
    def update(self):
        self.index += 1
            
        try:
            if self.index == len(self.images):
                self.index = 0
        except IndexError:
            print('EVERYTHING IS NORMAL')
        finally:
            self.image = self.images[self.index]

# class-> 13 , image-> 30(.png) , fps-> 4 
# directory-> 'C:\Users\sajjad shaikh\Desktop\Final Project(sem 2)\python_pro\image'  
# pygame.sprite.Sprite-> parent class
class text_2(pygame.sprite.Sprite):
    #constructor for class
    def __init__(self):
        #calling parent class method using super function
        super().__init__()
        #empty list for appending images
        self.images = []
        try:
            #python.tranform.scale-> resizing images , python.image.load-> open images
            self.images.append(pygame.transform.scale(pygame.image.load(r'C:\Users\sajjad shaikh\Desktop\Final Project(sem 2)\python_pro\image\30.png'),(1170,540)))
        except FileNotFoundError:
            print('unable to load images.\n\n\nWARNING: Image not found.')
        #index for empty list
        self.index = 0
        #self.image-> parent class method
        self.image = self.images[self.index]
        #pygame.Rect-> to store and manipulate rectangular areas pygame.Rect(left, top, width. height)
        self.rect = pygame.Rect(5, 5, 150, 1250)
    #for updating frame
    def update(self):
        self.index += 1
            
        try:
            if self.index == len(self.images):
                self.index = 0
        except IndexError:
            print('EVERYTHING IS NORMAL')
        finally:
            self.image = self.images[self.index]
#main 
def main():
    #initialize the mixer module
    pygame.mixer.init()
    try:
        #laoding sound
        pygame.mixer.music.load('Save Water - 2D Animated Short Film.mp3')
    except FileNotFoundError:
        print("unable to load audio.\n\n\nWARNING: audio file not found.")
    #playing sound
    pygame.mixer.music.play()
    #size of window
    screen = pygame.display.set_mode(SIZE)
    #caption
    pygame.display.set_caption('save water')
    try:
        icon = pygame.image.load(r'C:\Users\sajjad shaikh\Desktop\Final Project(sem 2)\python_pro\image\drop.png')
    except FileNotFoundError:
        print('unable to load images.\n\n\nWARNING: Image not found.')
    finally:
        pygame.display.set_icon(icon)
    # slide-> 1 , time_sec-> 4 , fps-> 4 , class-> water_falling_1
    my_sprite = water_falling_1()
    my_group = pygame.sprite.Group(my_sprite)
    #return time
    clock = pygame.time.Clock()
    timer= 3
    dt = 0
    done = False 
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        timer -= dt
        if timer <=0:
            break

        my_group.update()
        screen.fill(BLACK)
        my_group.draw(screen)
        pygame.display.update()
        dt = clock.tick(4) / 1000

    # slide-> 2 , time_sec-> 4 , fps-> 4 , class-> man_1()
    my_sprite = man_1()
    my_group = pygame.sprite.Group(my_sprite)
    #return time
    clock = pygame.time.Clock()
    timer= 3
    dt = 0
    done = False
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        timer -= dt
        if timer <=0:
            break


        my_group.update()
        screen.fill(BLACK)
        my_group.draw(screen)
        pygame.display.update()
        dt = clock.tick(4) / 1000

    # slide-> 3, time_sec-> 4 , fps-> 4 , class-> water_falling_2()
    my_sprite = water_falling_2()
    my_group = pygame.sprite.Group(my_sprite)
    #return time
    clock = pygame.time.Clock()
    timer= 3
    dt = 0
    done = False
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        timer -= dt
        if timer <=0:
            break

        
        my_group.update()
        screen.fill(BLACK)
        my_group.draw(screen)
        pygame.display.update()
        dt = clock.tick(4) / 1000


    # slide-> 4 , time_sec-> 4 , fps-> 4 , class-> man_2()
    my_sprite = man_2()
    my_group = pygame.sprite.Group(my_sprite)
    #return time
    clock = pygame.time.Clock()
    timer= 4
    dt = 0
    done = False
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        timer -= dt
        if timer <=0:
            break


        my_group.update()
        screen.fill(BLACK)
        my_group.draw(screen)
        pygame.display.update()
        dt = clock.tick(4) / 1000

    

    # slide-> 5 , time_sec-> 4 , fps-> 4 , class-> water_falling_3()
    my_sprite = water_falling_3()
    my_group = pygame.sprite.Group(my_sprite)
    #return time
    clock = pygame.time.Clock()
    timer= 4
    dt = 0
    done = False
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        timer -= dt
        if timer <=0:
            break


        my_group.update()
        screen.fill(BLACK)
        my_group.draw(screen)
        pygame.display.update()
        dt = clock.tick(4) / 1000

    # slide-> 6 , time_sec-> 4 , fps-> 4 ,class-> man_3()
    my_sprite = man_3()
    my_group = pygame.sprite.Group(my_sprite)
    #return time
    clock = pygame.time.Clock()
    timer= 4
    dt = 0
    done = False
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        timer -= dt
        if timer <=0:
            break


        my_group.update()
        screen.fill(BLACK)
        my_group.draw(screen)
        pygame.display.update()
        dt = clock.tick(4) / 1000

    # slide-> 7 , time_sec-> 4 , fps-> 4 , class-> water_falling_4()
    my_sprite = water_falling_4()
    my_group = pygame.sprite.Group(my_sprite)
    #return time
    clock = pygame.time.Clock()
    timer= 3
    dt = 0
    done = False
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        timer -= dt
        if timer <=0:
            break


        my_group.update()
        screen.fill(BLACK)
        my_group.draw(screen)
        pygame.display.update()
        dt = clock.tick(4) / 1000

    # slide-> 8 , time_sec-> 4 , fps-> 4 , class-> man_1()
    my_sprite = man_1()
    my_group = pygame.sprite.Group(my_sprite)
    #return time
    clock = pygame.time.Clock()
    timer= 4
    dt = 0
    done = False
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        timer -= dt
        if timer <=0:
            break


        my_group.update()
        screen.fill(BLACK)
        my_group.draw(screen)
        pygame.display.update()
        dt = clock.tick(4) / 1000


    # slide-> 9 , time_sec-> 4 , fps-> 4 , class-> man_4()
    my_sprite = man_4()
    my_group = pygame.sprite.Group(my_sprite)
    #return time
    clock = pygame.time.Clock()
    timer= 4
    dt = 0
    done = False
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        timer -= dt
        if timer <=0:
            break


        my_group.update()
        screen.fill(BLACK)
        my_group.draw(screen)
        pygame.display.update()
        dt = clock.tick(4) / 1000


# slide-> 10 , time_sec-> 4 , fps-> 4 , class-> man_1()
    my_sprite = man_1()
    my_group = pygame.sprite.Group(my_sprite)
    #return time
    clock = pygame.time.Clock()
    timer= 4
    dt = 0
    done = False
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        timer -= dt
        if timer <=0:
            break


        my_group.update()
        screen.fill(BLACK)
        my_group.draw(screen)
        pygame.display.update()
        dt = clock.tick(4) / 1000



# slide-> 11 , time_sec-> 4 , fps-> 4 , class-> man_5()
    my_sprite = man_5()
    my_group = pygame.sprite.Group(my_sprite)
    #return time
    clock = pygame.time.Clock()
    timer= 4
    dt = 0
    done = False
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        timer -= dt
        if timer <=0:
            break


        my_group.update()
        screen.fill(BLACK)
        my_group.draw(screen)
        pygame.display.update()
        dt = clock.tick(4) / 1000

# slide-> 12 , time_sec-> 4 , fps-> 4 , class-> man_6()
    my_sprite = man_6()
    my_group = pygame.sprite.Group(my_sprite)
    #return time
    clock = pygame.time.Clock()
    timer= 2
    dt = 0
    done = False
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        timer -= dt
        if timer <=0:
            break


        my_group.update()
        screen.fill(BLACK)
        my_group.draw(screen)
        pygame.display.update()
        dt = clock.tick(4) / 1000

# slide-> 13 , time_sec-> 4 , fps-> 4 , class-> man_7()
    my_sprite = man_7()
    my_group = pygame.sprite.Group(my_sprite)
    #return time
    clock = pygame.time.Clock()
    timer= 4
    dt = 0
    done = False
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        timer -= dt
        if timer <=0:
            break


        my_group.update()
        screen.fill(BLACK)
        my_group.draw(screen)
        pygame.display.update()
        dt = clock.tick(4) / 1000

# slide-> 14 , time_sec-> 4 , fps-> 4 , class-> text_1()
    my_sprite = text_1()
    my_group = pygame.sprite.Group(my_sprite)
    #return time
    clock = pygame.time.Clock()
    timer= 6
    dt = 0
    done = False
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        timer -= dt
        if timer <=0:
            break


        my_group.update()
        screen.fill(BLACK)
        my_group.draw(screen)
        pygame.display.update()
        dt = clock.tick(4) / 1000


# slide-> 15 , time_sec-> 4 , fps-> 4 , class-> text_2()
    my_sprite = text_2()
    my_group = pygame.sprite.Group(my_sprite)
    #return time
    clock = pygame.time.Clock()
    timer= 6
    dt = 0
    done = False
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        timer -= dt
        if timer <=0:
            break


        my_group.update()
        screen.fill(BLACK)
        my_group.draw(screen)
        pygame.display.update()
        dt = clock.tick(4) / 1000

if __name__ == '__main__':
    main()
    pygame.quit() 

