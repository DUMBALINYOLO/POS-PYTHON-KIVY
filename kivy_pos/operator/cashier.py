from kivy.app import App
from kivy.uix.boxlayout import BoxLayout


class CashierWindow(BoxLayout):

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)


class CashierApp(App):

	def build(self):
		return CashierWindow()



if __name__ == '__main__':
	oa = CashierApp()
	oa.run()
		


		