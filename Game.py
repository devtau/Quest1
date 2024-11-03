from Data import GameState, GameRoom 

class Game:

	loop_flag = False
	time = 0
	time_limit = 4*60*60

	state = GameState.GAME.value
	room = GameRoom.PREVIEW.value
	step = 1
	
	counter = 0
	operator_command = 0


if __name__ == '__main__':
	print('class Game')
	print(Game.state)
	print(Game.room)
