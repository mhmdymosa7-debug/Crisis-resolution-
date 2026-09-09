import flet as ft
import json
import os
import re

DATA_FILE = "app_database.json"

def load_data():
    if os.path.exists(DATA_FILE):
        try:
            with open(DATA_FILE, 'r', encoding='utf-8') as f:
                return json.load(f)
        except:
            return {}
    return {}

def save_data(data):
    with open(DATA_FILE, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

def extract_number(text):
    numbers = re.findall(r'\d+\.?\d*', str(text))
    if numbers:
        return float(numbers[0])
    return 0.0

def main(page: ft.Page):
    page.title = "نظام السجلات والملفات الذكية"
    page.rtl = True  # تفعيل الاتجاه من اليمين ليسار للدعم العربي الكامل
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.bgcolor = "#E1F5FE"  # خلفية سماوية فاتحة

    data = load_data()

    # شاشة تفاصيل الملف
    def open_detail_view(file_name):
        page.clean()
        
        person_input = ft.TextField(label="اسم الشخص / الطالب", hint_text="مثال: احمد سالم", border_radius=10)
        amount_input = ft.TextField(label="المبلغ", hint_text="مثال: 100 جنيه", border_radius=10)
        detail_input = ft.TextField(label="التفصيل", hint_text="مثال: اشترى زيت", border_radius=10)
        
        records_column = ft.ListView(expand=1, spacing=10, padding=10)
        total_text = ft.Text("المجموع الكلي: 0", size=16, weight=ft.FontWeight.BOLD, color="#01579B")

        def update_records_display():
            records_column.controls.clear()
            current_data = load_data()
            records = current_data.get(file_name, [])
            total_sum = 0.0
            
            if not records:
                records_column.controls.append(ft.Text("لا توجد سجلات في هذا الملف بعد", color="grey"))
            else:
                for r in records:
                    val = extract_number(r['amount'])
                    total_sum += val
                    card = ft.Card(
                        content=ft.Container(
                            content=ft.Column([
                                ft.Text(f"الاسم: {r['person']}", weight=ft.FontWeight.BOLD),
                                ft.Text(f"المبلغ: {r['amount']} | التفصيل: {r['detail']}")
                            ]),
                            padding=10
                        )
                    )
                    records_column.controls.append(card)
            
            total_text.value = f"المجموع الكلي: {total_sum}"
            page.update()

        def add_record(e):
            if person_input.value and amount_input.value and detail_input.value:
                current_data = load_data()
                if file_name in current_data:
                    current_data[file_name].append({
                        "person": person_input.value.strip(),
                        "amount": amount_input.value.strip(),
                        "detail": detail_input.value.strip()
                    })
                    save_data(current_data)
                    person_input.value = ""
                    amount_input.value = ""
                    detail_input.value = ""
                    update_records_display()

        add_btn = ft.ElevatedButton("إضافة السجل داخل الملف", on_click=add_record, bgcolor="#0288D1", color="white")
        
        # زر العودة والشريط السفلي
        def go_back(e):
            main_menu_view()

        back_btn = ft.ElevatedButton("العودة للرئيسية", on_click=go_back, bgcolor="#D32F2F", color="white")

        bottom_bar = ft.Row(
            [
                total_text,  # المجموع في الجهة اليسرى (بسبب اتجاه التطبيق أو تنظيمه)
                back_btn
            ],
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN
        )

        page.add(
            ft.Text(f"ملف: {file_name}", size=20, weight=ft.FontWeight.BOLD, color="#01579B"),
            person_input,
            amount_input,
            detail_input,
            add_btn,
            ft.Divider(),
            records_column,
            bottom_bar
        )
        update_records_display()

    # الشاشة الرئيسية (إدارة الملفات)
    def main_menu_view():
        page.clean()
        
        file_name_input = ft.TextField(label="اسم الملف الجديد", hint_text="مثال: حسابي أنا واحمد", border_radius=10)
        files_column = ft.ListView(expand=1, spacing=10, padding=10)

        def create_file(e):
            name = file_name_input.value.strip()
            if name:
                current_data = load_data()
                if name not in current_data:
                    current_data[name] = []
                    save_data(current_data)
                    file_name_input.value = ""
                    refresh_file_list()

        create_btn = ft.ElevatedButton("إنشاء ملف جديد", on_click=create_file, bgcolor="#388E3C", color="white")

        def refresh_file_list():
            files_column.controls.clear()
            current_data = load_data()
            if not current_data:
                files_column.controls.append(ft.Text("لا توجد ملفات حتى الآن", color="grey"))
            else:
                for fn in current_data.keys():
                    # تصميم الملفات بشكل مستطيل ذو حواف دائرية بارزة باللون الذهبي الفاخر
                    file_card = ft.Container(
                        content=ft.Text(fn, size=18, weight=ft.FontWeight.BOLD, color="#3E2723"),
                        bgcolor="#FFD700",  # لون ذهبي
                        padding=15,
                        border_radius=15,
                        alignment=ft.alignment.center,
                        on_click=lambda e, name=fn: open_detail_view(name),
                        shadow=ft.BoxShadow(blur_radius=5, color=ft.colors.BLACK26)
                    )
                    files_column.controls.append(file_card)
            page.update()

        page.add(
            ft.Text("إدارة الملفات والسجلات الذكية", size=22, weight=ft.FontWeight.BOLD, color="#01579B"),
            file_name_input,
            create_btn,
            ft.Divider(),
            ft.Text("الملفات المحفوظة:", weight=ft.FontWeight.BOLD),
            files_column
        )
        refresh_file_list()

    main_menu_view()

ft.app(target=main)
