from Data import Define
from Data import GameState, GameRoom 
from Data import In, Out, Relay
from Game import Game
from init_controller import jerome_controller 
from init_controller import back_sound 
from init_controller import voice_sound 
# from PyQt5.QtCore import QTimer


def room_2():

	print(Game.step)

	if Game.step == 1:
		back_sound.play(1)
		Game.step += 1

	elif Game.step == 2:
		Game.room = GameRoom.ROOM_3.value
		Game.step = 1 
