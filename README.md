
# Test exercise
### Python 3.11, Django 4.2, Django rest framework

### Задача:
1. Реализовать API на DRF, которое на HTTP-запрос GET /weather?city=<city_name>
возвращает краткую информацию о погоде
(Температура, атмосферное давление (мм рт. ст.), скорость ветра в м/с)
   
#### Swagger доступен по ссылке localhost/api/schema/swagger-ui/

* Перед запуском необходимо заполнить .env.dev
для Django Secret Key и OpenWeather Key.

### Запуск (docker):
    1.  docker-compose build
    2.  docker-compose up
    3.  Get - запрос на localhost/api/v1/weather?city=Bishkek
