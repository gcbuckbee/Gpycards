# ============================================================================================
# cardgame.py
# ============================================================================================
# Shell for testing pycards 
# --------------------------------------------------------------------------------------------
# G. Buckbee
# 2016-Oct-31
# Updated 22-Nov-2016
# ============================================================================================
# Imports
# ===============================================================
from Cards import *
from CardTests import *
import pygame
from pygame.locals import *
import os
import time

# ============================================================================================
# Initializations
# ===============================================================
os.putenv('SDL_FBDEV', '/dev/fb1')
pygame.init()

# ---------------------------------------------
# Set up display
# ---------------------------------------------

pygame.mouse.set_visible(True)
lcd = pygame.display.set_mode((800,600))
lcd.fill((80,80,255))
pygame.display.update()


# -----------------------------------
# Test Routines.  Comment them out when not in use
# -----------------------------------

if test_all_card_objects(False):
    print("Passed All Tests")

# ============================================================================================
# Main Loop
# ===============================================================

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if (event.type == MOUSEBUTTONDOWN):
            pos = pygame.mouse_get_pos()
            print (pos)
    pygame.display.update()
    time.sleep(0.1)





