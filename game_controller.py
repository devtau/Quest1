from Data import Define
from Data import GameState, GameRoom
from Data import In, Out, Relay
from Game import Game
from preview import preview
from room_1 import room_1
from room_2 import room_2
from room_3 import room_3
from time import sleep

from init_controller import jerome_controller 
from init_controller import back_sound 
from init_controller import voice_sound

from PyQt5.QtCore import QTimer


def game_controller():

	print(GameState(Game.state))
	if Game.state == GameState.GAME.value:
		game()
	elif Game.state == GameState.WIN.value:
		win()
	elif Game.state == GameState.LOSE.value:
		lose()
	elif Game.state == GameState.ASSEMBLE.value:
		assemble()
	elif Game.state == GameState.EMERGENCY.value:
		emergency()
	elif Game.state == GameState.SERVICE.value:
		pass


def game():
	print(GameRoom(Game.room))
	if Game.room == GameRoom.PREVIEW.value:
		preview()
	elif Game.room == GameRoom.ROOM_1.value:
		room_1()
	elif Game.room == GameRoom.ROOM_2.value:
		room_2()
	elif Game.room == GameRoom.ROOM_3.value:
		room_3()


def win():
	QTimer.singleShot(1*1000, lambda: back_sound.stop())
	QTimer.singleShot(2*1000, lambda: voice_sound.play(7))
	# jerome_controller.set_relay(Relay.DOOR_EXIT_MAGNET.value, Define.ACTIVATE.value)
	Game.loop_flag = False

	
def lose():
	QTimer.singleShot(1*1000, lambda: back_sound.stop())
	QTimer.singleShot(2*1000, lambda: voice_sound.play(6))
	jerome_controller.set_relay(Relay.DOOR_EXIT_MAGNET.value, Define.ACTIVATE.value)
	Game.loop_flag = False

def assemble():
	pass

def emergency():
	jerome_controller.set_out_all('00000')
	jerome_controller.set_relay('ALL', '0000')



if __name__ == '__main__':
	print('game_controller')
	print(GameRoom(Game.room))
	print(Game.room)
		