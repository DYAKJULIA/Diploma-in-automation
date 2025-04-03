# Diploma-in-automation
# Дипломная работа. Архитектура фреймворка. Автотесты сервиса "КИНОПОИСК"

### Стек зависимостей:
- pytest
- selenium
- requests
- allure
- config
  
### Структура:

- ### API
	- Clients
		- kinopoisk_client.py
	- Tests
		- test_search_by_title.py
    	- test_search_by_title_2_words.py
  		- test_search_by_id.py
      	- test_search_by_title_with_special_characters
      	- test_invalid_method.py
      	- test_search_empty_query.py

- ### Config
  - settings.py
 - ### UI
   	- Pages
   	  	- base.py
   	  	- autorization.py
   	  	- search.py
   	  	- main.py
	- Tests
  		- conftest.py
  		- test_autorization.py
  		- test_kinopoisk.py
- README.md
- requirements.txt

### Установка и настройка:
1. Склонируйте репозиторий: https://github.com/DYAKJULIA/Diploma-in-automation
2. Установите зависимости
3. Запустите тесты 'pytest'

### Включены тесты:
## UI
При выполнении тестов вручную нажмите на капчу "Я не робот".
## API
При выполнении тестов введите код, который поступит на Ваш номер телефона.

## Контакты:
Автор: Юлия Дьякова
E-mail: fruktaym@gmail.com
