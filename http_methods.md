# 1.Управление справочником клиентов.
Управление справочником клиентов можно разбить на три функции:
### 1. Добавление клиента в справочник.

```
POST /client
```
В зависимости от типа клиента(физ.лицо или юр лицо) тело запроса может быть разным:
###### Если мы хотим добавить  физ. лицо:
```json
{
  "legal": "False",
  "FIO": "Морозов Владимир Васильевич",
  "residentialAddress": "г.Санкт-Петербург, ул.Оптиков, д.34, кв.1",
  "numberPassport": "8741 568578",
  "numberPhone": "89997771122"
}
```
###### Если мы хотим добавить  юр. лицо:
```json
{
  "legal":"True",
  "Name":"АО 'Сбербанк'",
  "legalAddress":"г.Москва, ул.Заречная, д.1",
  "OGRN": "0123456789123",
  "numberPhone": "88342728982"
}
```
Предпологаемый ответ:
```json
{
  "status": "success",
  "text": "Данные успешно внесены в базу"
}
```
***
2. Изменение данных клиента в справочнике.
 ```
PUT /client
```
В зависимости от типа клиента(физ.лицо или юр лицо) тело запроса может быть разным:
###### Если мы хотим изменить физ. лицо:
```json
{
  "legal": "False",
  "id": 2,
  "FIO": "Морозов Владимир Васильевич",
  "residentialAddress": "г.Санкт-Петербург, ул.Оптиков, д.34, кв.1",
  "numberPassport": "8741 568578",
  "numberPhone": 89997771122
}
```
###### Если мы хотим изменить юр. лицо:
```json
{
  "legal":"True",
  "id": 2,
  "Name":"АО 'Сбербанк'",
  "legalAddress":"г.Москва, ул.Заречная, д.1",
  "OGRN": "0123456789123",
  "numberPhone": 88342728982
}
```

Предпологаемый ответ:
```json
{
  "status": "success",
  "text": "Данные успешно изменены"
}
```
***
3. Удаление клиента из справочника.

```
DELETE /client
```
передаем:
```json
{
  "legal": "(True если объект юр.лицо и False если физ.)",
  "id":11
}
```

- legal=(True если объект юр.лицо и False если физ.)
- id=11

преполагаемй ответ
```json
{
  "status": "success",
  "text": "Клиент удален"
}
```
***
# 2. Управление справочником объектов страхования.
1. Добавление объекта в справочник.

```
POST /object
```

```json
{
  "Name": "Toyota Camry",
  "numberPassport": "AAA 485679",
  "idTypeObject": 1
  
}
```

Предпологаемый ответ:
```json
{
  "status": "success",
  "text": "Данные успешно внесены в базу"
}
```
***
2. Изменение данных объекта в справочнике.
 ```
PUT /object
```

```json
{
  "idObjects": 3,
  "Name": "Toyota Camry",
  "numberPassport": "AAA 485679",
  "idTypeObject": 1
  
}
```


Предпологаемый ответ:
```json
{
  "status": "success",
  "text": "Данные успешно изменены"
}
```
***
3. Удаление объекта из справочника.

```
DELETE /object
```
передаем:
```json
{
  "id":11
}
```

- legal=(True если объект юр.лицо и False если физ.)
- id=11

преполагаемй ответ
```json
{
  "status": "success",
  "text": "Клиент удален"
}
```
***

# 3. Управление справочником типов объектов страхования.
1. Добавление типа объекта в справочник.

```
POST /object_type
```

```json
{
  "ObjectType": "Домашнее животное"
  
}
```

Предпологаемый ответ:
```json
{
  "status": "success",
  "text": "Данные успешно внесены в базу"
}
```
***
2. Изменение данных типа объекта в справочнике.
 ```
PUT /object_type
```

```json
{
  "idTypes": 2,
  "ObjectType": "Средства передвижения"
  
}
```


Предпологаемый ответ:
```json
{
  "status": "success",
  "text": "Данные успешно изменены"
}
```
***
3. Удаление типа объекта из справочника.

```
DELETE /object_type
```
передаем:
```json
{
  "id":2
}
```


преполагаемй ответ
```json
{
  "status": "success",
  "text": "Клиент удален"
}
```
***
# 4. Управление конкретным полисом
Управление полисом логично сделать добавив в него функции "Создание" и "Редактирование данных"
- Составление полиса возможно только на основе имеющихся данных о страхователе(клиенте) и объекте страхования.
1. Создание полиса.
 ```
POST /policy
```

```json
{
  "idTypeObject": 2,
  "idFL": "None",
  "idL": 45,
  "idObjects": 67,
  "startDate": "01.09.22",
  "stopDate": "01.09.23",
  "insuranceAmount": 2000000
  
}
```

Предпологаемый ответ:
```json
{
  "status": "success",
  "text": "Полис успешно внесены в базу"
}
```
2. Изменение полиса.
 ```
PUT /policy
```

```json
{
  "policyNumber": 356,
  "idTypeObject": 2,
  "idFL": "None",
  "idL": 45,
  "idObjects": 67,
  "startDate": "01.09.22",
  "stopDate": "01.09.23",
  "insuranceAmount": 2000000
  
}
```

Предпологаемый ответ:
```json
{
  "status": "success",
  "text": "Изменения успешно внесены в полис"
}
```
# 5. Продажа полиса.

Замена статуса полиса по номеру в библиотеке всех полисов.
 ```
PUTCH /policy
```

```json
{
  "policyNumber": 456,
  "status": "sold"
  
}
```


Предпологаемый ответ:
```json
{
  "status": "success",
  "text": "Продажа исполнена"
}
```
***
# 6. Производство страховой выплаты полису.

Добавление в таблицу исполнения выплат.
 ```
POST /payment
```

```json
{
  "paymentDate": "22.04.2021",
  "payoutAmount": "100000",
  "policyNumber": 25
  
}
```


Предпологаемый ответ:
```json
{
  "status": "success",
  "text": "Выплата исполнена"
}
```
***

# 7. Построение отчетов.
Необходимо предоставить 6 разных отчетов, для этого каждому отчету присвоим идентификатор:
Данный идентификатор и будет передаваться в GET запросе.
- Отчет по продажам различных видов полисов за период == report1 
```
GET /report?name=report1&datestart='2021-04-22'&datestop='2022-04-22'
```
- Отчет по страховым выплатам за период == report2 
```
GET /report?name=report2&datestart='2021-04-22'&datestop='2022-04-22'
```
- Отчет о полисах конкретного клиента и сроках их окончания == report3 
```
GET /report?name=report3&clientid=55
```
- Отчет о самых "невыгодных" клиентах с самыми большими выплатами за период == report4 
```
GET /report?name=report4
```

- Отчет об объектах с самой большой суммой страхования == report5 
```
GET /report/?name=report5
```

- Отчет об убыточности/прибыльности компании == report6 
```
GET /report/?name=report6
```
Предпологаемый ответ:
```
файл
```

# 8. Просмотр полисов.
Необходимо реализовать два вида просмотра, для этого присвоим идентификатор каждому из видов для последующей перадачи его в GET запросе.

- Просмотр полисов, которые закачиваются на конкретную дату == viewing1
```
GET /viewing?name=viewing1&date=2020-30-05
```
- Просмотр полисов по объекту страхования == viewing2
```
GET /viewing?name=viewing2&idtype=2
```
Предпологаемый ответ:
```

{
    "2": {
        "idFL": null,
        "idL": 3,
        "idObjects": 3,
        "idTypeObject": 2,
        "insuranceAmount": 50000000,
        "startDate": "Fri, 22 Jul 2022 00:00:00 GMT",
        "stopDate": "Sat, 23 Jul 2022 00:00:00 GMT"
    }
}
```