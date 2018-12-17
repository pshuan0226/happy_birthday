#!/usr/bin/python

import pygame

pygame.mixer.init(44100, -16, 2, 2048)
hb = pygame.mixer.Sound("hp.mp3")

while 1:
    print("""
    Hi Mom! Happy Birthday :-)
    1) Happy Birthday Song
    2) A Hug?
    3) A Cake
    4) Love?
    """)
    user = raw_input("What would you like? ")
    if user == "1":
    	try:
        	pygame.mixer.Sound.play(hb)
            pygame.event.wait()
        except:
        	print("Sorry mom I failed you :-(")
    elif user == "2":
        print("""
            (      \              .-'    `-.              /   )____
          (____     \_____       /  (O  O)  \       _____/     ____)
         (____            `-----(      )     )-----'            ____)
          (____     _____________\  .____.  /_____________     ____)
            (______/              `-.____.-'              \______)

        """)
    elif user == "3":
        print("""
                      (        (
             ( )      ( )          (
      (       Y        Y          ( )
     ( )     |"|      |"|          Y
      Y      | |      | |         |"|
     |"|     | |.-----| |---.___  | |
     | |  .--| |,~~~~~| |~~~,,,,'-| |
     | |-,,~~'-'___   '-'       ~~| |._
    .| |~       // ___            '-',,'.
   /,'-'     <_// // _  __             ~,\
  / ;     ,-,     \\_> <<_' ____________;_)
  | ;    {(_)} _,      ._>>`'-._          |
  | ;     '-'\_\/>              '-._      |
  |\ ~,,,      _\__            ,,,,,'-.   |
  | '-._ ~~,,,            ,,,~~ __.-'~ |  |
  |     '-.__ ~~~~~~~~~~~~ __.-'       |__|
  |\         `'----------'`           _|
  | '=._                         __.=' |
  :     '=.__               __.='      |
   \         `'==========='`          .'
    '-._                         __.-'
        '-.__               __.-'
        """)
    elif user == "4":
        print("How can I give you love when I'm not loved :-(\n")
    else:
        break
