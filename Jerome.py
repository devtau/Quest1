import socket
import sys
import traceback

class Jerome:

	def __init__ (self, ip = '192.168.0.250', port = 2424):

		self.ip = ip
		self.port = port
		
		self.sock = socket.socket()
		self.sock.settimeout(1.0)
		try:
			self.sock.connect((ip, port))
			print('Connect to Jerome ' + self.ip)
		except:
			print('Error connect Jerome ' + self.ip)
			traceback.print_exc(file=sys.stdout)



	def __del__ (self):
		self.sock.close()
		print('Disconnect from Jerome ' + self.ip)


	def command(self, data, param_1 = '', param_2 = '', param_3 = '', param_4 = '', param_5 = ''):
		comma_1 = '' if param_1 == '' else ','
		comma_2 = '' if param_2 == '' else ','
		comma_3 = '' if param_3 == '' else ','
		comma_4 = '' if param_4 == '' else ','
		comma_5 = '' if param_5 == '' else ','
		cmd = f"$KE,{data}{comma_1}{param_1}{comma_2}{param_2}{comma_3}{param_3}{comma_4}{param_4}{comma_5}{param_5}\r\n".encode('utf-8')
		print(cmd)
		return cmd

	def recieve_result(self):
		result = self.sock.recv(256).decode("utf-8")
		print(result)
		if result == '#SLINF\r\n':
			result = self.recieve_result()
		return result



	# for RELAY 1-4
	# $KE,REL,<OutLine>,<Value>[,Delay]
	# 0-off, 1-on, 2-switch
	def set_relay(self, relayNumber = 'ALL', state='0000', delay = ''):
		self.sock.send(self.command('REL', relayNumber, state, delay))
		return self.recieve_result()
	
	# $KE,RDR,<ReleNumber>
	def get_relay(self, relayNumber = 'ALL'):
		self.sock.send(self.command('RDR', relayNumber))
		return self.recieve_result()



	# for OUT 1-5
	# $KE,WR,<OutLine>,<Value>[,Delay]
	# 0-off, 1-on, 2-switch
	def set_out(self, outNumber, state, delay = ''):
		self.sock.send(self.command('WR', outNumber, state, delay))
		return self.recieve_result()

	# $KE,WRA,<ArrayOfValues>
	def set_out_all(self, mask):
		self.sock.send(self.command('WRA', mask))
		return self.recieve_result()

	# $KE,RID,<OutLine>
	def get_out(self, outNumber = 'ALL'):
		self.sock.send(self.command('RID', outNumber))
		return self.recieve_result()
	


	# PWM OUT 1-4 = 0% - 100%
	# $KE,PSM,<LineNumber>,SET,<Value>
	# value 0-off PWM, 1-on PWM
	def set_pwm(self, outNumber, value):
		self.sock.send(self.command('PSM', outNumber, 'SET', value))
		return self.recieve_result()

	# $KE,PWM,<LineNumber>,SET,<PowerValue>
	def set_pwm_value(self, outNumber, powerValue):
		self.sock.send(self.command('PWM', outNumber, 'SET', powerValue))
		return self.recieve_result()

	# $KE,PWM,<LineNumber>,DRV,<Start>,<Stop>,<Time>
	def set_pwm_smooth(self, outNumber, start, stop, time):
		self.sock.send(self.command('PWM', outNumber, 'DRV', start, stop, time))
		return self.recieve_result()



	# for IN 1-8
	# $KE,RD,<InLine>
	def get_in(self, lineNumber):
		try:
			self.sock.send(self.command('RD', lineNumber))
			return int(self.recieve_result()[-3:-2])
		except:
			return None




	# other command
	def device_info(self):
		self.sock.send(self.command('INF'))
		return self.recieve_result()

	def device_reset(self):
		self.sock.send(self.command('RST'))
		return self.recieve_result()



if __name__ == '__main__':
	print('class Jerome')
	j_test = Jerome('192.168.1.101')
	print(j_test.device_info())
	to_jerome_command = ''
	while to_jerome_command != '$KE,\r\n'.encode('utf-8'):
		to_jerome_command = input('Input command: ')
		to_jerome_command = f'$KE,{to_jerome_command}\r\n'.encode('utf-8')
		print(to_jerome_command)
		j_test.sock.send(to_jerome_command)
		print(j_test.recieve_result())




