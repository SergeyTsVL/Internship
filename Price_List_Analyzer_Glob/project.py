import os
import csv
from airium import Airium

file_path = '../Price_List_Analyzer_Glob/Files_for_analysis'
file_html = '../Price_List_Analyzer_Glob/Files_for_analysis/output.html'
list_result = []
class PriceMachine():

    def load_prices(self):
        '''
            Сканирует указанный каталог. Ищет файлы со словом price в названии.
            В файле ищет столбцы с названием товара, ценой и весом.
            Допустимые названия для столбца с товаром:
                товар
                название
                наименование
                продукт
            Допустимые названия для столбца с ценой:
                розница
                цена
            Допустимые названия для столбца с весом (в кг.)
                вес
                масса
                фасовка
        '''
        Product_name = ['товар', 'название', 'наименование', 'продукт']
        Name_with_price = ['розница', 'цена']
        Name_with_weight = ['вес', 'масса', 'фасовка']
        files = os.listdir(file_path)

        for file in files:
            if "price" in file:
                with open(f'{file_path}/{file}', mode="r", encoding='utf-8') as sort_file:
                    for row in csv.reader(sort_file):

                        for i in Product_name:
                            try:
                                index_Product_name = row.index(i)
                            except:
                                None
                        a = row[index_Product_name]

                        for i in Name_with_price:
                            try:
                                index_Name_with_price = row.index(i)
                            except:
                                None
                        try:
                            b = int(row[index_Name_with_price])
                        except:
                            b = row[index_Name_with_price]

                        for i in Name_with_weight:
                            try:
                                index_Name_with_weight = row.index(i)
                            except:
                                None
                        try:
                            c = int(row[index_Name_with_weight])
                        except:
                            c = row[index_Name_with_weight]

                        if a not in Product_name and b not in Name_with_price and c not in Name_with_weight:
                            result = a, b, c, file
                            list_result.append(result)
        list_result.sort(key=lambda x: x[1])
        return list_result

    def export_to_html(self):
        '''
        <!DOCTYPE html>
        <html>
        <head>
            <title>Позиции продуктов</title>
        </head>
        <body>
            <table>
                <tr>
                    <th>Номер</th>
                    <th>Название</th>
                    <th>Цена</th>
                    <th>Фасовка</th>
                    <th>Файл</th>
                    <th>Цена за кг.</th>
                </tr>
        '''
        file = open(f"{file_html}", "w", encoding = 'utf-8')
        a = Airium()
        # Главное преимущество Airium – DOCTYPE уже включен!
        a('<!DOCTYPE html>')
        with ((((a.html())))):
            a.head()
            a.title(_t="Позиции продуктов")
            with a.body():
                with a.table():   # _t="Добро пожаловать на мою страницу!", id="intro"
                    # a = Airium(source_minify=False, source_line_break_character="\n",)
                    with a.tr():
                        a.th(_t="№")
                        a.th(_t="Наименование")
                        a.th(_t="Цена")
                        a.th(_t="Масса")
                        a.th(_t="Файл")
                        pass
            file.write(str(a))

    def find_text():
        '''
        Нолучает текст и возвращает список позиций,
        содержащий этот текст в названии продукта.
        <td 1></td><td Филе пангасиуса б/ш ></td><td 92></td><td 1></td><td price_5.csv></td>
        <td 2></td><td Филе пангасиуса б/ш ></td><td 103></td><td 1></td><td price_4.csv></td>
        <td 3></td><td Ряпушка вял н/р></td><td 119></td><td 1></td><td price_3.csv></td>
        <td 4></td><td Килька п/п ></td><td 130></td><td 1></td><td price_0.csv></td>
        '''
        file = open(f"{file_html}", "a", encoding='utf-8')
        b = Airium(source_minify=True)
        with b.tr():
            y = 0
            for i in list_result:
                y += 1
                b.break_source_line()
                b.td(y)
                b.td(i[0])
                b.td(i[1])
                b.td(i[2])
                b.td(i[3])
            pass
        file.write(str(b))

if __name__ == "__main__":
    PriceMachine.load_prices(file_path)
    PriceMachine.export_to_html(file_html)
    PriceMachine.find_text()