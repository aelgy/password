passward = 'a123456'
n = 3
while True:
	enter_pw = input('請輸入密碼： ')
	if enter_pw == passward:
		print('登入成功！')
		break
	else:
		n = n - 1
		print('密碼錯誤，還有', n ,'次機會')
		if n == 0:
			break
		