import kivy
from kivy.app import App
from kivy.uix.label import Label

kivy.require("1.9.0")


class NeuralRandom(App):
    def build(self):
        return Label(text="HER")


neuralRandom = NeuralRandom()
neuralRandom.run()