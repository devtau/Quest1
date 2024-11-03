from Data import Define
from Data import GameState, GameRoom 
from Data import In, Out, Relay
from Game import Game
from init_controller import jerome_controller 
from init_controller import back_sound 
from init_controller import voice_sound 
from PyQt5.QtCore import QTimer


def room_1():

	print(Game.step)

	if Game.step == 1:
		back_sound.play(0)
		Game.step += 1
	
	elif Game.step == 2:
		if jerome_controller.get_in(In.TELEFON_SOLVED.value) == Define.ACTIVATE.value or Game.operator_command == 102:
			print(0, "решили телефон.")
			jerome_controller.set_out(Out.TABLE_BOX_MAGNET.value, Define.OPEN.value)
			Game.step += 1 
		Game.operator_command = 0

	elif Game.step == 3:
		if jerome_controller.get_in(In.FOTOROBOT_SOLVED.value) == Define.ACTIVATE.value or Game.operator_command == 103:
			print(0, "решили фотопортрет.")
			jerome_controller.set_out(Out.TABLE_DOOR_MAGNET.value, Define.OPEN.value)
			Game.step += 1
		Game.operator_command = 0

	elif Game.step == 4:
		if jerome_controller.get_in(In.RADIO_SOLVED.value) == Define.NONE.value or Game.operator_command == 104:
			if Game.operator_command == 104:
				jerome_controller.set_relay(Relay.RADIO_GO.value, Define.ACTIVATE.value)
				Game.operator_command = 0	
			print(0, "решили радио.")
			QTimer.singleShot(40*1000, lambda: back_sound.play(2))
			Game.step += 1

	elif Game.step == 5:
		if jerome_controller.get_in(In.DOOR_EXIT.value) == Define.NONE.value:
			print(0, "открыли дверь выход.")
			# jerome_controller.set_relay(Relay.DOOR_EXIT_MAGNET.value, Define.ACTIVATE.value)
			QTimer.singleShot(20*1000, lambda: jerome_controller.set_relay(Relay.DOOR_EXIT_MAGNET.value, Define.ACTIVATE.value))
			Game.step += 1

	elif Game.step == 6:
		Game.state = GameState.WIN.value
		Game.room = GameRoom.PREVIEW.value
		Game.step = 1


