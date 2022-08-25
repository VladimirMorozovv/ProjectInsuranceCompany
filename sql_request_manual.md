# 1. Управление справочником клиентов.

- Запрос на добавления физического лица в БД
```
INSERT INTO ClientFL
(FIO, residentialAddress, numberPassport, numberPhone)
VALUES
('Иванов Генадий Павлович', 'г.Санкт-Петербург, ул. Курочкина, д.3, кв.2134', '8923 652344', 89123464050);
```
- Запрос на добавления юридического лица в БД
```
INSERT INTO ClientLegal
(Name, legalAddress, OGRN, numberPhone)
VALUES
    ('ООО Газприм', 'г.Санкт-Петербург, ул. Морская, д.1', '7894567891356', 88005553535);
```
- Запрос на изменение данных физического лица в БД
```
UPDATE ClientFL SET FIO = 'Константинов Евгений Николаевич', residentialAddress = 'г.Санкт-Петербург, ул. Морская, д.8, кв.1',
numberPassport = '8911 428645', numberPhone = '89514267878' WHERE id = 2;
```
- Запрос на изменение данных юридического лица в БД
```
UUPDATE ClientLegal SET Name = 'АО Бишкек', legalAddress = 'г.Санкт-Петербург, ул. Морская, д.8',
OGRN = '8911 428645', numberPhone = '8800451212' WHERE id = 2;
```
- Запрос на удаление данных клиента физического лица в БД
```
DELETE FROM ClientFL
WHERE id=2
```

- Запрос на удаление данных клиента юридического лица в БД
```
DELETE FROM ClientLegal
WHERE id=2
```