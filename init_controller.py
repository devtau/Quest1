import Data
from Jerome import Jerome
from Game import Game 
from Sound import Sound
from PyQt5.QtMultimedia import QMediaPlaylist


jerome_controller = Jerome(Data.Jerome.IP.value)

back_sound = Sound(Data.Sound.BACK_SOUND.value, QMediaPlaylist.CurrentItemInLoop)
voice_sound = Sound(Data.Sound.VOICE_SOUND.value, QMediaPlaylist.CurrentItemOnce)


if __name__ == '__main__':
	print('init_controller')
	print(Game.room)