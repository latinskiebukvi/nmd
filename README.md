# nmd

В компании имеется несколько складов с техникой. На каждый склад закреплен сотрудник, отвечающий за принятие и выдачу оборудования по поступающим накладным.
У каждой единицы техники есть инвентарный номер, производитель, страна производства и модель.

Предложить структуру БД для инвентаризации оборудования на складах. Реализовать отображение отчета по остаткам на каждом складе и общем остатке по каждой единице техники.

Результат оформить в виде проекта на github/gitlab. Структуру БД прикрепить в виде pdf в корне репозитория.

```
cd nmd
pip install -r requirements.txt
cd myproject

python manage.py migrate
python manage.py makedata
python manage.py runserver
```
go to 
```
http://127.0.0.1:8000/
```