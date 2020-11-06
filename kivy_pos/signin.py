from kivy.app import App
from kivy.uix.boxlayout import BoxLayout


class SigninWindow(BoxLayout):
	
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)

	def validate_user(self):
		user = self.ids.username_field
		pwd = self.ids.pwd_field
		info = self.ids.info

		username = user.text
		password = pwd.text

		if username == "" or password == "":
			info.text ='[color=#FF0000]username and/ or password required[/color]'
		else:
			if username == "admin" and password == "admin":
				info.text ='[color=#00FF00]You have successfully logged in[/color]'
			else:
				info.text ='[color=#FF0000]Incorrect Login Details!!![/color]'


class SigninApp(App):

	def build(self):
		return SigninWindow()


if __name__ == '__main__':
	sa = SigninApp()
	sa.run()
	
	