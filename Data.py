from enum import Enum, auto


class Define(Enum):
	TIME_LOOP = 128
	OPEN_DELAY = 4
	VOLUME = 57

	ACTIVATE = 1
	NONE = 0
	SWITCH = 2

	OPEN = 0
	CLOSE = 1



class GameState(Enum):
	GAME = 0
	WIN = 1
	LOSE = 2
	ASSEMBLE = 3
	EMERGENCY = 4
	SERVICE = 5


class GameRoom(Enum):
	PREVIEW = 0
	ROOM_1 = 1
	ROOM_2 = 2
	ROOM_3 = 3


class In(Enum):
	TELEFON_SOLVED = 1
	FOTOROBOT_SOLVED = 2
	RADIO_SOLVED = 3
	DOOR_EXIT = 4
	NONE_2 = 5
	NONE_3 = 6



class Out(Enum):
	GLOBUS_12V = 1
	TABLE_BOX_MAGNET = 2
	TABLE_DOOR_MAGNET = 3
	NONE_2 = 4
	NONE_3 = 5


class Relay(Enum):
	LIGHT_ROOM_1 = 1
	DOOR_EXIT_MAGNET = 2
	RADIO_GO = 3
	KODE_DOOR = 4


class Jerome(Enum):
	IP = '192.168.1.101'


class Sound(Enum):
	BACK_SOUND = ["./sound/fon_1.mp3", "./sound/fon_2.mp3", "./sound/fon_3.mp3"]
	VOICE_SOUND = ["./sound/tip_1.mp3", "./sound/tip_2.mp3", "./sound/tip_3.mp3",
					"./sound/tip_4.mp3", "./sound/tip_5.mp3", "./sound/tip_6.mp3",
					"./sound/lose.mp3", "./sound/win.mp3", "./sound/detective.mp3" ]


status_msg = [

	# State Game
	[
		# preview
		[
			'',
			''
		],

		# room_1
		[
			'',
			'',
			'Ожидаем пока прослушают телефон...',
			'Ожидаем пока сложат фоторобот...',
			'Ожидаем пока настроят радио...',
			'Ожидаем пока откроют дверь на выход...',
			''
		],
		# room_2
		[
			'',
			''
		],
		# room_3
		[
			'',
			''
		],
	],


	# State Win
	[
		[
			'',
			'Игра закончена. Игроки выиграли.'
		]
	],


	# State Lose
	[
		[
			'',
			'Игра закончена. Игроки проиграли.',
		]
	],


	# State Assemble
	[
		[
			'',
			'Режим сборки.'
		]
	],
	

	# State Emergency
	[
		[
			'',
			'Экстренная остановка игры.'
		]
	]
]

if __name__ == '__main__':

	import Data

	print('class Data')
	print(list(Data.Jerome))
	print(Data.Jerome.IP.name)
	print(Data.Jerome.IP.value)

