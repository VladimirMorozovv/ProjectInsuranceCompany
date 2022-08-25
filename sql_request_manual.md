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
# 2. Управление справочником типов объектов страхования
- Запрос на добавление типа объекта в справочник
```
INSERT INTO typesInsuranceObjects
(ObjectType)
VALUES
    ('Транспортное средство');
```
- Запрос на изменение данных типа объекта в справочнике
```
UPDATE typesInsuranceObjects SET ObjectType = 'Автомобиль' WHERE idTypes = 1;
```
- Запрос на удаление данных типа объекта в справочнике
```
DELETE FROM typesInsuranceObjects
WHERE idTypes=2
```

3. Управление справочником объектов страхования
- Запрос на добавление объекта в справочник
```
INSERT INTO objectsInsurance
(Name, numberPassport, idTypeObject)
VALUES
    ('Квартира', '6367487263', 2);
```
- Запрос на изменение данных объекта в справочнике
```
UPDATE objectsInsurance SET Name = 'Квартира', numberPassport = 6367487263, idTypeObject =3 
WHERE idObjects = 3;
```
- Запрос на удаление данных объекта в справочнике
```
DELETE FROM objectsInsurance
WHERE idObjects=2
```
***