from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

class SmartCalculatorApp(App):
    def build(self):
        self.icon = 'icon.png' # تعيين أيقونة افتراضية إن وجدت
        root_layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        
        # شاشة العرض الرياضية
        self.solution = TextInput(
            text='', 
            font_size=32, 
            readonly=True, 
            halign='right', 
            multiline=False,
            size_hint_y=None,
            height=70
        )
        root_layout.add_widget(self.solution)
        
        # أزرار الحاسبة مرتبة بشبكة احترافية
        buttons = [
            ['C', '(', ')', '/'],
            ['7', '8', '9', '*'],
            ['4', '5', '6', '-'],
            ['1', '2', '3', '+'],
            ['.', '0', '<-', '=']
        ]
        
        grid_layout = GridLayout(cols=4, spacing=8, size_hint=(1, 1))
        
        for row in buttons:
            for label in row:
                btn = Button(
                    text=label, 
                    font_size=24,
                    background_color=(0.2, 0.2, 0.2, 1) if label not in ['=', 'C'] else (0.1, 0.5, 0.8, 1)
                )
                btn.bind(on_press=self.on_button_press)
                grid_layout.add_widget(btn)
                
        root_layout.add_widget(grid_layout)
        return root_layout

    def on_button_press(self, instance):
        current = self.solution.text
        button_text = instance.text
        
        if button_text == 'C':
            self.solution.text = ''
        elif button_text == '<-':
            self.solution.text = current[:-1]
        elif button_text == '=':
            try:
                # تقييم العملية الرياضية بأمان
                allowed_chars = "0123456789+-*/.() "
                if all(c in allowed_chars for c in current) and current.strip():
                    solution = str(eval(current))
                    self.solution.text = solution
                else:
                    self.solution.text = "خطأ"
                except Exception:
                    self.solution.text = "عملية غير صالحة"
        else:
            if current == "خطأ" or current == "عملية غير صالحة":
                current = ""
            self.solution.text = current + button_text

if __name__ == '__main__':
    SmartCalculatorApp().run()
