from sense_emu import SenseHat

"""import some functions"""
import random
from random import choice
from random import randint
from time import sleep


"""connect to the senseHat"""
sense = SenseHat()


"""set he colors : red, green, blue, yellow"""
r = (255,0,0)
g = (0,255,0)
b = (0,0,255)
y = (255,255,0)


"""define a function for random color"""
def random_colour():
        rand_r = randint(0, 255)
        rand_g = randint(0, 255)
        rand_b = randint(0, 255)
        rand_y = randint(0, 255)
        return (rand_r, rand_g, rand_b)


"""Display text one letter at a time, random colour"""
sense.show_letter("I", random_colour(), back_colour=r)
sleep(0.8)
sense.show_letter("L", random_colour(),back_colour=g)
sleep(0.5)
sense.show_letter("O", random_colour(),back_colour=b)
sleep(0.5)
sense.show_letter("V", random_colour(),back_colour=y)
sleep(0.5)
sense.show_letter("E", random_colour(),back_colour=r)
sleep(0.5)

"""Replace with your child's name"""
sense.show_letter("M", random_colour(), back_colour=r)
sleep(0.5)
sense.show_letter("Y", random_colour(),back_colour=g)
sleep(0.8)
sense.show_letter("K", random_colour(),back_colour=b)
sleep(0.5)
sense.show_letter("I", random_colour(),back_colour=y)
sleep(0.5)
sense.show_letter("D", random_colour(),back_colour=r)
sleep(0.5)


"""scroll goodnight my Darling"""
sense.show_message("Goodnight my Darling !",text_colour=y, back_colour=b, scroll_speed=0.08)


"""Optional infinite Sacha loop with a while True: """
sense.show_letter("L", random_colour(), back_colour=r)
sleep(0.5)
sense.show_letter("O", random_colour(),back_colour=g)
sleep(0.5)
sense.show_letter("V", random_colour(),back_colour=b)
sleep(0.5)
sense.show_letter("E", random_colour(),back_colour=y)
sleep(0.5)


"""clear the sense Hat"""
sense.clear()



