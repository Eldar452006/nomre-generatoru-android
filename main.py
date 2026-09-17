from kivy.app import App
from kivy.metrics import dp
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout
from kivy.core.clipboard import Clipboard


class NumberGeneratorApp(App):
    def build(self):
        self.title = "Nömrə Generatoru"

        root = BoxLayout(orientation="vertical", padding=dp(18), spacing=dp(12))

        title = Label(
            text="📱 NÖMRƏLƏRİ GENERATORU",
            font_size=dp(22),
            size_hint_y=None,
            height=dp(45),
            bold=True,
        )
        root.add_widget(title)

        root.add_widget(Label(
            text="Başlanğıc nömrəni yaz (məs: 050 501 22 00)",
            size_hint_y=None,
            height=dp(30),
            halign="left",
            text_size=(None, None),
        ))

        self.number_input = TextInput(
            text="050 501 22 00",
            multiline=False,
            font_size=dp(20),
            size_hint_y=None,
            height=dp(52),
        )
        root.add_widget(self.number_input)

        root.add_widget(Label(
            text="Son iki rəqəm neçə olsun?",
            size_hint_y=None,
            height=dp(30),
        ))

        self.end_input = TextInput(
            text="99",
            multiline=False,
            input_filter="int",
            font_size=dp(20),
            size_hint_y=None,
            height=dp(52),
        )
        root.add_widget(self.end_input)

        buttons = BoxLayout(size_hint_y=None, height=dp(52), spacing=dp(8))

        generate_btn = Button(text="🚀 YARAT", font_size=dp(17))
        generate_btn.bind(on_press=self.generate_numbers)
        buttons.add_widget(generate_btn)

        copy_btn = Button(text="📋 KOPYALA", font_size=dp(17))
        copy_btn.bind(on_press=self.copy_numbers)
        buttons.add_widget(copy_btn)

        clear_btn = Button(text="🗑️ TƏMİZLƏ", font_size=dp(17))
        clear_btn.bind(on_press=self.clear_all)
        buttons.add_widget(clear_btn)

        root.add_widget(buttons)

        self.result = TextInput(
            text="",
            readonly=False,
            multiline=True,
            font_size=dp(17),
            padding=[dp(10), dp(10)],
        )
        root.add_widget(self.result)

        self.status = Label(
            text="Hazırdır.",
            size_hint_y=None,
            height=dp(30),
            font_size=dp(14),
        )
        root.add_widget(self.status)

        return root

    def generate_numbers(self, *_):
        raw = self.number_input.text.strip()
        end_text = self.end_input.text.strip()

        if len(raw) < 2:
            self.status.text = "❌ Nömrə çox qısadır."
            return

        try:
            end_number = int(end_text)
        except ValueError:
            self.status.text = "❌ Son rəqəm düzgün deyil."
            return

        if not 0 <= end_number <= 99:
            self.status.text = "❌ Son rəqəm 0-99 arası olmalıdır."
            return

        prefix = raw[:-2]
        numbers = [f"{prefix}{i:02d}" for i in range(0, end_number + 1)]
        self.result.text = "\n".join(numbers)
        self.status.text = f"✅ {len(numbers)} nömrə yaradıldı."

    def copy_numbers(self, *_):
        text = self.result.text
        if not text.strip():
            self.status.text = "⚠️ Əvvəlcə nömrələri yaradın."
            return
        Clipboard.copy(text)
        self.status.text = "✅ Hamısı kopyalandı."

    def clear_all(self, *_):
        self.result.text = ""
        self.status.text = "Təmizləndi."


if __name__ == "__main__":
    NumberGeneratorApp().run()
