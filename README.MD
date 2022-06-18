Как устроены Flask View? Давайте создадим CRUD веб приложение на flask
используя Flask Views

![Image_alt](https://sun9-east.userapi.com/sun9-75/s/v1/ig2/DyHjvj396e7Ygcmtv81ziGv2M7SWctePjag80cmJjthC9iVltGRjaMgGROKdQOz3pslP9l3HyK-9h9UPfE_R9iiM.jpg?size=1343x745&quality=96&type=album)

- Зависимости

    pip install flask flask-sqlalchemy email-validator flask-wtf

- Структура

    md flask_views & cd flask_views
    md templates static 
    cd static & md css favicon img_404 & cd ..
    cd templates & md flaks_views & cd ..
    for %i in (__init__ forms models views settings) do notepad %i.py
    
    rename req.txt requirements.txt

[Сценарий ролика] (https://youtu.be/iaHeGzg9H08)

- Создадим функцию create_user, конфигурацию и запустим проект
    
    python run.py


- Создадим модель User и объект базы данных db и передадим его в контекст приложения

- Создадим шаблоны 

- Подключим файлы стилей и скриптов bootstrap и свой файл стилей

- Создадим IndexView

- Выведем на главную страницу первую информацию - info

- Добавим favicon

- Добавим страницу 404 и обработчик 

- Переопределим стиль alert

- Стилизуем info

- Подключим файл flash.html к шаблону

- Напишем вьюху создания пользователя CreateUserView

- В IndexView сформируем список пользователей и передадим в шаблон

- Добавим вывод пользователей из базы в index.html

- Создадим первого пользователя, передав нужные параметры в строку поиска

    http://localhost:5667/create/Михаил Терехов/admin@gmail.com

- Создадим еще троих пользователей:

    - Вася Пупкин	vasia@gmail.com
    - Милена Халявина	milenka@gmail.com
    - Александр Бровин	brovin@gmail.com


- Пропишем стили для списка пользователей

- Напишем форму и выведем ее в шаблон

  - Выведем плашки в шаблон flash.html

      {% with messages = get_flashed_messages(with_categories=True) %}
    
      {% if messages %}
      {% for category, message in messages %}
      {{ message }}
      {% endfor %}
      {% endif %} 
      {% endwith %}


- Стилизируем плашки

- Напишем свои стили для плашек

- Создадим DeleteView и добавим удаление в шаблон

- Добавим функционал обновления имени пользователя

[Михаил Терехов 2022]






    



    


