from Data import Define
from Data import GameState, GameRoom 
from Data import In, Out, Relay
from Game import Game
from init_controller import jerome_controller 
from init_controller import back_sound 
from init_controller import voice_sound
# from PyQt5.QtCore import QTimer


def room_3():

	print(Game.step)

	if Game.step == 1:
		back_sound.play(2)
		# QTimer.singleShot(10*1000, lambda: voice_sound.play(0))
		Game.step += 1

	elif Game.step == 2:
		Game.state = GameState.WIN.value
		Game.room = GameRoom.PREVIEW.value
		Game.step = 1
