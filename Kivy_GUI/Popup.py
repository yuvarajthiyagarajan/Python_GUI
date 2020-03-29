import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.popup import Popup
from kivy.lang import Builder

class Widgets(Widget):
	def btn(self):
		show_popup()

class P(FloatLayout):
	pass

def show_popup():
	show = P()

	popupWindow = Popup(title="Popup Window", content=show, size_hint=(None,None), size=(400,400))

	popupWindow.open()

kv = Builder.load_file("my2.kv")

class MyApp(App):
	def build(self):
		return Widgets()

if __name__ == "__main__":
	MyApp().run()