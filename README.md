# [МЕГАХАКАТОН 2023 Хакатон SkillFactory (01.11-02.12.2023)]

- __[Васильцов Олег](https://github.com/BYKEFAL)__ - _fullstack разработчик_;
- __Акерке Есимова__ - _project manager_.

___Команда стала победителем мегахакатона!___ 

В рамках хакатона в течении месяца разработано веб приложение для сервиса "Ётакси":
- Развернут проект Django;
- Основной язык програмирования Python;
- Реализован механизм определения геолокации клиента, с отображение информации для ближайшего города клиента
- В зависимости от локации (города) вовыдится соответствующая информация (автомобили, карты, контакты, и т.д.)
- Сформирована структура базы данных и занесены тестовые данные. (Автомобили, таксопарки, города, водители, менеджеры, отзывы и т.д.) Все необходимы переменные выводятся из базы данных;
- Управление данными осуществляется через админ панель. Для удобства использования интерфес которой был доработан (включены фильтрация, поиск и т.д.)
- Реализована корректная отправка валидных данных из всех форм на сайте с занесением информации в базу данных.
-  Осуществленна интеграция с порталом Битрикс24 с использованием REST API. При подаче заявки на сайте и поледующем занесением информации в базу данных сайта о водителе, даная информация при задействовании скрипта из сигналов и использовании ключа(вебхука) от Битрикс, попадают на портал(базу данных портала) в воронку лидов потенциального Заказчика CRM Битрикс24.
- Инегрирована работа фронтэнд-разработчиков, шаблоны страниц и стили (HTML,CSS,JS), в том  числе для адаптивного отображения страниц для различных устройств.

![Screnshot](https://github.com/BYKEFAL/taxitaxi/blob/main/Сертификат%20megaxakaton%20SkillFactory.png)

### Использование

Сначала клонируйте репозиторий с Github и перейдите в новый каталог:

    $ git clone https://github.com/BYKEFAL/taxitaxi.git
    $ cd taxitaxi
    
Активируйте виртуальное окружение для проекта (пример активации для windows).
    
    $ py -3.10 -m venv venv
    $ venv\scripts\activate

Установить зависимости проекта:

    $ cd etaxi
    $ pip install -r requirements.txt
    
Затем примените миграции:

    $ python manage.py migrate
    
И запустите сервер разработки:

    $ python manage.py runserver
