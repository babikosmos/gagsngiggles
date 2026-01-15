import csv
import os
import random
from datetime import date

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label

            
DILEMMA = {
    "name": "Aesthetic vs Ethical",
    "choices": ["Aesthetic", "Ethical"],
    "base_weights": {
        "Aesthetic": 0.5,
        "Ethical": 0.5
    }
}

MOODS = {
    "Calm": {"Ethical": 0.1},
    "Anxious": {"Aesthetic": 0.15},
    "Reflective": {"Ethical": 0.2}
}

CSV_FILE = "existential_log.csv"

            
def initialize_csv():
    if not os.path.exists(CSV_FILE):
        with open(CSV_FILE, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([
                "date",
                "dilemma",
                "choice",
                "mood",
                "outcome",
                "probability_used",
                "life_leap"
            ])
            
def calculate_weights(mood):
    weights = DILEMMA["base_weights"].copy()

    if mood in MOODS:
        for choice, modifier in MOODS[mood].items():
            weights[choice] += modifier

    total = sum(weights.values())
    for choice in weights:
        weights[choice] /= total

    return weights
    
                            
def resolve_outcome(choice):
    if choice == "Ethical":
        return "Meaningful but costly", 1
    else:
        return "Pleasurable but fleeting", 0                                                                            
                                    
def log_decision(choice, mood, probability):
    outcome, leap = resolve_outcome(choice)

    with open(CSV_FILE, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([
            date.today().isoformat(),
            DILEMMA["name"],
            choice,
            mood,
            outcome,
            round(probability, 2),
            leap
        ])       
                 
        
class ExistentialUI(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation="vertical", **kwargs)

        self.mood = "Calm"

        self.label = Label(text="Choose your path.")
        self.add_widget(self.label)

        for mood in MOODS:
            btn = Button(text=f"Mood: {mood}")
            btn.bind(on_press=self.set_mood)
            self.add_widget(btn)

        for choice in DILEMMA["choices"]:
            btn = Button(text=choice)
            btn.bind(on_press=self.make_choice)
            self.add_widget(btn)

    def set_mood(self, instance):  
        self.mood = instance.text.replace("Mood: ", "")
        self.label.text = f"Mood set to {self.mood}"

    def make_choice(self, instance): 
        weights = calculate_weights(self.mood)
        choice = random.choices(
            DILEMMA["choices"],
            weights=[weights[c] for c in DILEMMA["choices"]]
        )[0]

        log_decision(choice, self.mood, weights[choice])

        self.label.text = f"You chose {choice}"            
 
class ExistentialApp(App):
    def build(self):
        initialize_csv()
        return ExistentialUI()

if __name__ == "__main__":
       ExistentialApp().run()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 
	                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  