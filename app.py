# import *.ui to *.py
# python3 -m PyQt5.uic.pyuic /Users/admin/Documents/gui_zmey.ui -o /Users/admin/Google\ Диск/_PyCharm_Projects/_zmeyApp/_union/gui.py -x


# from PyQt5 import sip 

import sys
import time
import traceback
from PyQt5 import QtWidgets
from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QIcon

import gui_kvest2

from Data import Define
from Data import GameState, GameRoom 
from Data import In, Out, Relay
from Data import status_msg
from Game import Game
# from Signal import Signal
from init_controller import jerome_controller 
from game_controller import game_controller
from init_controller import back_sound 
from init_controller import voice_sound 


class Sennaja_kvest2(QtWidgets.QMainWindow, gui_kvest2.Ui_MainWindow):

	def __init__(self):
		super().__init__()

		# self.signal = Signal()
		# self.signal.your_signal.connect(self.action_your_signal)

		self.setupUi(self)

		self.stepButton_101.clicked.connect(self.func_stepButton)
		self.stepButton_102.clicked.connect(self.func_stepButton)
		self.stepButton_103.clicked.connect(self.func_stepButton)
		self.stepButton_104.clicked.connect(self.func_stepButton)
		self.stepButton_105.clicked.connect(self.func_stepButton)

		self.actionButton_201.clicked.connect(self.func_actionButton)
		self.actionButton_202.clicked.connect(self.func_actionButton)
		self.actionButton_203.clicked.connect(self.func_actionButton)
		self.actionButton_204.clicked.connect(self.func_actionButton)
		self.actionButton_205.clicked.connect(self.func_actionButton)
		self.actionButton_206.clicked.connect(self.func_actionButton)
		self.actionButton_207.clicked.connect(self.func_actionButton)
		self.actionButton_208.clicked.connect(self.func_actionButton)

		self.otherButton_301.clicked.connect(self.func_otherButton)
		self.otherButton_302.clicked.connect(self.func_otherButton)
		self.otherButton_303.clicked.connect(self.func_otherButton)
		self.otherButton_304.clicked.connect(self.func_otherButton)
		self.otherButton_305.clicked.connect(self.func_otherButton)
		self.otherButton_306.clicked.connect(self.func_otherButton)
		self.otherButton_307.clicked.connect(self.func_otherButton)
		self.otherButton_308.clicked.connect(self.func_otherButton)
		self.otherButton_309.clicked.connect(self.func_otherButton)
		self.otherButton_310.clicked.connect(self.func_otherButton)
		self.otherButton_311.clicked.connect(self.func_otherButton)
		self.otherButton_312.clicked.connect(self.func_otherButton)

		self.upTimeButton.clicked.connect(self.func_changeTimeLimitButton)
		self.downTimeButton.clicked.connect(self.func_changeTimeLimitButton)


		self.stepButton_101.clicked.connect(self.func_logStepButton)
		self.stepButton_102.clicked.connect(self.func_logStepButton)
		self.stepButton_103.clicked.connect(self.func_logStepButton)
		self.stepButton_104.clicked.connect(self.func_logStepButton)
		self.stepButton_105.clicked.connect(self.func_logStepButton)

		self.actionButton_201.clicked.connect(self.func_logActionButton)
		self.actionButton_202.clicked.connect(self.func_logActionButton)
		self.actionButton_203.clicked.connect(self.func_logActionButton)
		self.actionButton_204.clicked.connect(self.func_logActionButton)
		self.actionButton_205.clicked.connect(self.func_logActionButton)
		self.actionButton_206.clicked.connect(self.func_logActionButton)
		self.actionButton_207.clicked.connect(self.func_logActionButton)
		self.actionButton_208.clicked.connect(self.func_logActionButton)

		self.otherButton_301.clicked.connect(self.func_logOtherButton)
		self.otherButton_302.clicked.connect(self.func_logOtherButton)
		self.otherButton_303.clicked.connect(self.func_logOtherButton)
		self.otherButton_304.clicked.connect(self.func_logOtherButton)
		self.otherButton_305.clicked.connect(self.func_logOtherButton)
		self.otherButton_306.clicked.connect(self.func_logOtherButton)
		self.otherButton_307.clicked.connect(self.func_logOtherButton)
		self.otherButton_308.clicked.connect(self.func_logOtherButton)
		self.otherButton_309.clicked.connect(self.func_logOtherButton)
		self.otherButton_310.clicked.connect(self.func_logOtherButton)
		self.otherButton_311.clicked.connect(self.func_logOtherButton)
		self.otherButton_312.clicked.connect(self.func_logOtherButton)


	def func_stepButton(self):
		
		sender = self.sender().objectName()

		if sender == 'stepButton_101':
			Game.operator_command = 101
			Game.loop_flag = True
			Game.room = GameRoom.ROOM_1.value
			Game.step = 1
			jerome_controller.set_relay(Relay.LIGHT_ROOM_1.value, Define.NONE.value)

		elif sender == 'stepButton_102':
			Game.operator_command = 102
	
		elif sender == 'stepButton_103':
			Game.operator_command = 103

		elif sender == 'stepButton_104':
			Game.operator_command = 104
	
		elif sender == 'stepButton_105':
			# reset
			Game.loop_flag = False
			Game.time = 0

			Game.state = GameState.GAME.value
			Game.room = GameRoom.PREVIEW.value
			Game.step = 1

			Game.counter = 0
			Game.operator_command = 0

			self.time_label.setText("00:00")
			self.logTextEdit.clear()
			back_sound.stop()
			voice_sound.stop()

			jerome_controller.set_out(Out.GLOBUS_12V.value, Define.OPEN.value, Define.OPEN_DELAY.value)
			jerome_controller.set_out(Out.TABLE_BOX_MAGNET.value, Define.OPEN.value, Define.OPEN_DELAY.value)
			jerome_controller.set_out(Out.TABLE_DOOR_MAGNET.value, Define.OPEN.value, Define.OPEN_DELAY.value)
			jerome_controller.set_relay(Relay.LIGHT_ROOM_1.value, Define.NONE.value)
			jerome_controller.set_relay(Relay.DOOR_EXIT_MAGNET.value, Define.NONE.value)
			jerome_controller.set_relay(Relay.RADIO_GO.value, Define.NONE.value)
			jerome_controller.set_relay(Relay.KODE_DOOR.value, Define.NONE.value)

	



	def func_actionButton(self, pressed):
		
		sender = self.sender().objectName()
		# sender = self.sender().objectName()[-3:] #optimization
		# print("{} - {}".format(sender, pressed))
		pin_value = 1 if pressed else 0

		if sender == 'actionButton_201':
			jerome_controller.set_out(Out.TABLE_BOX_MAGNET.value, Define.SWITCH.value)

		elif sender == 'actionButton_202':
			jerome_controller.set_out(Out.TABLE_DOOR_MAGNET.value, Define.SWITCH.value)

		elif sender == 'actionButton_203':
			jerome_controller.set_relay(Relay.KODE_DOOR.value, Define.SWITCH.value)

		elif sender == 'actionButton_204':
			jerome_controller.set_relay(Relay.DOOR_EXIT_MAGNET.value, Define.SWITCH.value)

		elif sender == 'actionButton_205':
			jerome_controller.set_out(Out.GLOBUS_12V.value, Define.OPEN.value)
			jerome_controller.set_out(Out.TABLE_BOX_MAGNET.value, Define.OPEN.value)
			jerome_controller.set_out(Out.TABLE_DOOR_MAGNET.value, Define.OPEN.value)
			jerome_controller.set_relay(Relay.DOOR_EXIT_MAGNET.value, Define.ACTIVATE.value)
			jerome_controller.set_relay(Relay.KODE_DOOR.value, Define.ACTIVATE.value)
			jerome_controller.set_relay(Relay.RADIO_GO.value, Define.ACTIVATE.value)

		elif sender == 'actionButton_206':
			jerome_controller.set_relay(Relay.RADIO_GO.value, Define.SWITCH.value)

		elif sender == 'actionButton_207':
			jerome_controller.set_relay(Relay.LIGHT_ROOM_1.value, Define.SWITCH.value)

		elif sender == 'actionButton_208':
			jerome_controller.set_out(Out.GLOBUS_12V.value, Define.SWITCH.value)


	def func_otherButton(self):
		
		sender = self.sender().objectName()

		if sender == 'otherButton_301':
			back_sound.play(0)

		elif sender == 'otherButton_302':
			back_sound.play(1)

		elif sender == 'otherButton_303':
			back_sound.play(2)

		elif sender == 'otherButton_304':
			voice_sound.play(0)

		elif sender == 'otherButton_305':
			voice_sound.play(1)

		elif sender == 'otherButton_306':
			voice_sound.play(2)

		elif sender == 'otherButton_307':
			voice_sound.play(3)

		elif sender == 'otherButton_308':
			voice_sound.play(4)

		elif sender == 'otherButton_309':
			voice_sound.play(5)

		elif sender == 'otherButton_310':
			back_sound.stop()
			voice_sound.play(6)

		elif sender == 'otherButton_311':
			back_sound.stop()
			voice_sound.play(7)

		elif sender == 'otherButton_312':
			back_sound.stop()
			voice_sound.play(8)




	def func_changeTimeLimitButton(self):
		
		sender = self.sender().objectName()

		if sender == 'upTimeButton':
			if Game.time_limit < 4*60*60:
				Game.time_limit += 120
			else:
				Game.time_limit = 4*60*60
			self.time_limit_label.setText("Предельное время игры: {:0>2d} мин.".format(Game.time_limit//60))
		
		elif sender == 'downTimeButton':
			if Game.time_limit > 1*60*60:
				Game.time_limit -= 120
			else:
				Game.time_limit = 1*60*60
			self.time_limit_label.setText("Предельное время игры: {:0>2d} мин.".format(Game.time_limit//60))





	def func_logStepButton(self):
		sender = self.sender()
		if sender.objectName() == 'stepButton_101':
			self.logging(1, "Старт, игра началась...")
		elif sender.objectName() == 'stepButton_104':
			self.logging(1, "{}".format(sender.text()))
		else:
			self.logging(1, "пропусить {}".format(sender.text()))


	def func_logActionButton(self):
		sender = self.sender()
		self.logging(1, "изменил состояние. {}".format(sender.text()))


	def func_logOtherButton(self):
		sender = self.sender()
		self.logging(1, "запустил трек. {}".format(sender.text()))





	def loop(self):
		if Game.loop_flag:
			game_controller()


	def time_controller(self):
		if Game.loop_flag:
			Game.time += 1 
			self.time_label.setText("{:0>2d}:{:0>2d}".format(Game.time//60, Game.time%60))
			if Game.time > Game.time_limit:
				Game.state = GameState.LOSE.value
				Game.room = GameRoom.PREVIEW.value
				Game.step = 1

	def status_bar_info(self):
		self.statusbar.showMessage(status_msg[Game.state][Game.room][Game.step])
		# self.centralwidget.setStyleSheet("[accessibleName=\"stepButton_{}{:0>2d}\"]{}".format(Game.room, Game.step, '{font: bold 12px;}'))
		# self."stepButton_{}{:0>2d}".format(Game.room, Game.step).setStyleSheet("color: red;")
		# print("QPushButton[accessibleName=\"stepButton_{}{:0>2d}\"]{}".format(Game.room, Game.step, '{font: bold 12px;}'))

	def logging(self, user, msg):
		if user:
			self.logTextEdit.appendPlainText("Оператор: {}".format(msg))
		else:
			self.logTextEdit.appendPlainText("Игрок: {}".format(msg))



def run_app():

	app = QtWidgets.QApplication(sys.argv)
	app.setWindowIcon(QIcon('logo.png'))
	window = Sennaja_kvest2()

	try:
		time_loop = QTimer()
		time_loop.timeout.connect(window.loop)
		time_loop.start(Define.TIME_LOOP.value)

		time = QTimer()
		time.timeout.connect(window.time_controller)
		time.timeout.connect(window.status_bar_info)
		time.start(1000)

	except:
		print('Unexpected error')
		log = open('log.txt', 'a')
		log.write('='*80 + '\n')
		log.write(time.strftime('%Y-%m-%d, %H:%M:%S') + '\n')
		log.write('-'*80 + '\n')
		traceback.print_exc(file=log)
		traceback.print_exc(file=sys.stdout)
		log.close()
	
	window.show()
	sys.exit(app.exec_())




if __name__ == '__main__':

	run_app()



