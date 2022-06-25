# Консольная утилита для сокращения URL
Простое консольное приложение для сокращения URL-адресов с использованием API сервиса [Bitly](https://bitly.com).


## Установка
Для запуска приложения нужен предустановленный Python версии не ниже 3.8+ (на других версиях не проверялся).
Также в программе используются следующие сторонние библиотеки:
- [requests](https://requests.readthedocs.io/en/latest/)
- [python-dotenv](https://saurabh-kumar.com/python-dotenv/)

Рекомендуется устанавливать зависимости в виртуальном окружении, используя [venv](https://docs.python.org/3/library/venv.html) или любую другую реализацию, например, [virtualenv](https://github.com/pypa/virtualenv).

1. Скопируйте репозиторий в текущий каталог. Воспользуйтесь командой:
```bash
$ git clone https://github.com/igorzakhar/url-shortener-cli.git
```

После этого программа будет скопирована в каталог ```url-shortener-cli```.

2. Создайте и активируйте виртуальное окружение:
```bash
$ cd url-shortener-cli # Переходим в каталог с программой
$ python3 -m venv my_virtual_environment # Создаем виртуальное окружение
$ source my_virtual_environment/bin/activate # Активируем виртуальное окружение
```

3. Установите сторонние библиотеки  из файла зависимостей:
```bash
$ pip install -r requirements.txt # В качестве альтернативы используйте pip3
```
## Подготовка перед запуском

Переименуйте файл ```.env.template``` из данного репозитория в ```.env``` и добавьте токен из сервиса [Bitly](https://bitly.com):
```
BITLY_TOKEN=ваш_токен
```

Для получения токена вам нужно зарегистрироваться в сервисе [Bitly](https://bitly.com/a/sign_up) и сгенерировать токен в настройках своего профиля [Developer settings](https://app.bitly.com/settings/api/).

![](https://github.com/igorzakhar/url-shortener-cli/blob/main/media/bitly_settings.png)

Ссылка на документацию: [Bitly API Documentation](https://dev.bitly.com/).

## Запуск

Примеры запуска приложения:

![](https://github.com/igorzakhar/url-shortener-cli/blob/main/media/screenshot.png)

# Цели проекта

Код написан в учебных целях в рамках курса [Devman](https://dvmn.org/modules).
