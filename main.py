PRJNOM = "fulmkartojSW29501103.py"

import json
from kivy.app import App
from kivy.resources import resource_find
from kivy.utils import get_color_from_hex
from kivy.uix.boxlayout import BoxLayout

LANG_COLORS = {
    "EN": "#1E90FF",
    "EO": "#00C853",
    "DE": "#FF0000"
}

class MainScreen(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.cards = self.load_vocab_safe()
        self.card_index = 0
        self.revealed = False
        self.lang_order = ["EN", "EO", "DE"]
        self.show_card()

    def load_vocab_safe(self):
        try:
            vocab_path = resource_find("vocab.json")
            if not vocab_path:
                return []
            with open(vocab_path, encoding="utf-8") as f:
                data = json.load(f)
            return data.get("cards", [])
        except Exception as e:
            print("Vocab load failed:", e)
            return []

    def show_card(self):
        if not self.cards:
            self.ids.lang1.text = "JSON not found"
            self.ids.lang1.color = (1, 0, 0, 1)
            self.ids.lang2.text = ""
            self.ids.lang3.text = ""
            return
        LANGA, LANGB, LANGC = self.lang_order
        card = self.cards[self.card_index]
        self.ids.lang1.text = f"{LANGA.lower()}: {card.get(LANGA, '')}"
        self.ids.lang1.color = get_color_from_hex(LANG_COLORS[LANGA])
        self.ids.lang2.text = ""
        self.ids.lang3.text = ""
        self.revealed = False

    def on_reveal(self):
        if not self.cards:
            return
        LANGA, LANGB, LANGC = self.lang_order
        card = self.cards[self.card_index]
        if not self.revealed:
            self.ids.lang2.text = f"{LANGB.lower()}: {card.get(LANGB, '')}"
            self.ids.lang2.color = get_color_from_hex(LANG_COLORS[LANGB])
            self.ids.lang3.text = f"{LANGC.lower()}: {card.get(LANGC, '')}"
            self.ids.lang3.color = get_color_from_hex(LANG_COLORS[LANGC])
            self.revealed = True
        else:
            self.card_index = (self.card_index + 1) % len(self.cards)
            self.show_card()

    def on_rotate(self):
        self.lang_order = self.lang_order[1:] + self.lang_order[:1]
        self.show_card()


class FulmKartojApp(App):
    def build(self):
        return MainScreen()

    def on_start(self):
        self.root.ids.header_label.text = PRJNOM


if __name__ == "__main__":
    FulmKartojApp().run()
