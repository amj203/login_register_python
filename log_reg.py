def login(name,password):
	succes = False
	file = open('log_reg.txt','r')
	for i in file:
		a,b = i.split(',')
		b = b.strip()
		if (a == name and b == password):
			succes = True
			break
	if succes:
		print('Loged In')
	else:
		print('Invalid Account')		
		
	file.close()	
	return	
	
def register(name,password):
	file = open('log_reg.txt','a')
	file.write(f'\n{name},{password}')
	print('Registered succesfully')

	file.close()
	return

action = input('Login OR Register: ')
name = input('User name: ')
password = input('Password: ')

if action == 'Login' or action == 'log':
	login(name,password)
	
elif action == 'Register' or action == 'reg':
	register(name,password)			