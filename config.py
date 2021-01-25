TOKEN = ''
phone_number = ''
address = ''

sticker = '/home/st.gzip'
foto = '/home/visitka.jpg'
foto_special_offer_interior_doors = '/home/dv.jpg'
foto_blinds_promotion = '/home/zh.jpg'


URL = 'https://'

database_file = 'subscrabers'
database_file_sub = 'sub'
db_path = '/home/db.db'

# admins group
admin0 = ''
admin1 = ''
admin2 = ''
admin_all = [admin0, admin2]

# for act1-4 items list
items_list = ["Двері вхідні", "Двері міжкімнатні", "Вікна", "Жалюзі"]

#заглушка
def hello_text(text):
    return f'Вітаємо в Червонограді, {text}! \n'\
           'Салон "Золотий дуб" пропонує: \n'\
            'Вікна \n'\
            'Двері вхідні \n'\
            'Двері міжкімнатні \n'\
            'Ламінат \n'\
            'Жалюзі'
