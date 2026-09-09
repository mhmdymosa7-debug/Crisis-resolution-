from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
import csv
import os

class ReliefApp(App):
    def build(self):
        self.layout = BoxLayout(orientation='vertical', padding=20, spacing=15)
        
        self.layout.add_widget(Label(text="[b]نظام تتبع الإغاثة - السودان[/b]", markup=True, font_size=20))
        
        self.region_input = TextInput(hint_text='المنطقة / الولاية', multiline=False)
        self.layout.add_widget(self.region_input)
        
        self.shelter_input = TextInput(hint_text='اسم مركز الإيواء', multiline=False)
        self.layout.add_widget(self.shelter_input)
        
        self.count_input = TextInput(hint_text='عدد النازحين (رقم فقط)', input_filter='int', multiline=False)
        self.layout.add_widget(self.count_input)
        
        save_btn = Button(text='حفظ البيانات محلياً', background_color=(0.1, 0.6, 0.3, 1))
        save_btn.bind(on_press=self.save_data)
        self.layout.add_widget(save_btn)
        
        self.status_label = Label(text='أدخل البيانات واضغط حفظ')
        self.layout.add_widget(self.status_label)
        
        return self.layout

    def save_data(self, instance):
        region = self.region_input.text
        shelter = self.shelter_input.text
        count = self.count_input.text
        
        if not region or not shelter or not count:
            self.status_label.text = "الرجاء تعبئة جميع الحقول!"
            return
            
        file_exists = os.path.exists('local_relief.csv')
        
        with open('local_relief.csv', mode='a', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            if not file_exists:
                writer.writerow(['Region', 'Shelter', 'Count']) # كتابة العناوين أول مرة
            writer.writerow([region, shelter, count])
        
        self.status_label.text = f"تم حفظ بيانات '{shelter}' بنجاح!"
        self.region_input.text = ""
        self.shelter_input.text = ""
        self.count_input.text = ""

if __name__ == '__main__':
    ReliefApp().run()
