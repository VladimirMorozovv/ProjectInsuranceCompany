# 1. Управление справочником клиентов.

- Запрос на добавления физического лица в БД
```sql
INSERT INTO ClientFL
(FIO, residentialAddress, numberPassport, numberPhone)
VALUES
('Иванов Генадий Павлович', 'г.Санкт-Петербург, ул. Курочкина, д.3, кв.2134', '8923 652344', 89123464050);
```
- Запрос на добавления юридического лица в БД
```sql
INSERT INTO ClientLegal
(Name, legalAddress, OGRN, numberPhone)
VALUES
    ('ООО Газприм', 'г.Санкт-Петербург, ул. Морская, д.1', '7894567891356', 88005553535);
```
- Запрос на изменение данных физического лица в БД
```sql
UPDATE ClientFL SET FIO = 'Константинов Евгений Николаевич', residentialAddress = 'г.Санкт-Петербург, ул. Морская, д.8, кв.1',
numberPassport = '8911 428645', numberPhone = '89514267878' WHERE id = 2;
```
- Запрос на изменение данных юридического лица в БД
```sql
UUPDATE ClientLegal SET Name = 'АО Бишкек', legalAddress = 'г.Санкт-Петербург, ул. Морская, д.8',
OGRN = '8911 428645', numberPhone = '8800451212' WHERE id = 2;
```
- Запрос на удаление данных клиента физического лица в БД
```sql
DELETE FROM ClientFL
WHERE id=2
```

- Запрос на удаление данных клиента юридического лица в БД
```sql
DELETE FROM ClientLegal
WHERE id=2
```
***
# 2. Управление справочником типов объектов страхования
- Запрос на добавление типа объекта в справочник
```sql
INSERT INTO typesInsuranceObjects
(ObjectType)
VALUES
    ('Транспортное средство');
```
- Запрос на изменение данных типа объекта в справочнике
```sql
UPDATE typesInsuranceObjects SET ObjectType = 'Автомобиль' WHERE idTypes = 1;
```
- Запрос на удаление данных типа объекта в справочнике
```sql
DELETE FROM typesInsuranceObjects
WHERE idTypes=2
```
***
# 3. Управление справочником объектов страхования
- Запрос на добавление объекта в справочник
```sql
INSERT INTO objectsInsurance
(Name, numberPassport, idTypeObject)
VALUES
    ('Квартира', '6367487263', 2);
```
- Запрос на изменение данных объекта в справочнике
```sql
UPDATE objectsInsurance SET Name = 'Квартира', numberPassport = 6367487263, idTypeObject =3 
WHERE idObjects = 3;
```
- Запрос на удаление данных объекта в справочнике
```sql
DELETE FROM objectsInsurance
WHERE idObjects=2 
```
***
# 4. Управление конкретным полисом

- Запрос на создание нового полиса.
```sql
INSERT INTO insurancePolicyClient
(idTypeObject, idFL, idL, idObjects, startDate, stopDate, insuranceAmount, costInsurance, status)
VALUES
    (1, 2, NULL, 2, '22.07.22', '22.07.23', 2000000, insuranceAmount/100*10, 'atWork');
    
```
***
- Запрос на изменения данных существующего.
```sql 
UPDATE insurancePolicyClient SET idTypeObject =1, idFL = 2, idL = NULL, idObjects = 1, startDate= '23.07.22', stopDate = '23.07.23', insuranceAmount = 2000000
WHERE policyNumber = 1;
```
***
# 5. Продажа полиса
- Запрос на изменение статуса полиса с "atWork" на "sold"
```sql
UPDATE insurancePolicyClient SET status = 'sold'
WHERE policyNumber = 1;
```
***
# 6. Производство страховой выплаты
- Запрос на добавление данных о страховой выплате в таблицу
```sql
INSERT INTO payoutsDirectoryClient
(paymentDate, payoutAmount, policyNumber)
VALUES
    ('21.08.22', 200000, 1)
```
***
# 7. Построение отчета по продажам различных видов полисов за период
- Запрос на формирование таблицы состоящей из типов объектов страхование и сумме каждого проданного полиса по типу.
```sql
SELECT typesInsuranceObjects.ObjectType, SUM(insurancePolicyClient.costInsurance)
FROM typesInsuranceObjects, insurancePolicyClient
WHERE insurancePolicyClient.idTypeObject = typesInsuranceObjects.idTypes and insurancePolicyClient.startDate BETWEEN '2022-04-22' and '2022-08-22'
GROUP BY typesInsuranceObjects.ObjectType;
```
***
# 8. Построение отчета по страховым выплатам за период
- Запрос на значение (сумма выплат) за определенный период 
```sql
SELECT  SUM(payoutAmount)
FROM payoutsDirectoryClient
WHERE paymentDate BETWEEN '2021-04-22' and '2022-12-22'; 
```
***
# 9. Построение отчета о полисах конкретного клиента, и сроках их окончания
- Запрос на таблицу полисов которые принадлежат одному клиенту со столбцами номер полиса и датой его окончания
```sql
SELECT policyNumber, stopDate FROM insurancePolicyClient
WHERE idL=3 and stopDate > CURRENT_DATE(); 
```
# 10. Построение отчета о самых "невыгодных" клиентах с самыми большими выплатами за период
- Запрос на таблицу которая показывает id юр и физ лиц, а так же общую сумму выплаты за все время.
```sql
SELECT idFL,idL, SUM(payoutAmount) as money
FROM insurancePolicyClient, payoutsDirectoryClient
WHERE insurancePolicyClient.policyNumber = payoutsDirectoryClient.policyNumber
GROUP BY idFL, idL order by money DESC LIMIT 10; 
```
# 11. Пстроение отчета об объектах с самой большой сумой страхования.
- Запрос на таблицу которая имеет объекты страхования и сумма страхования на них.
```sql
SELECT objectsInsurance.idObjects, objectsInsurance.Name, objectsInsurance.numberPassport, insurancePolicyClient.insuranceAmount
FROM insurancePolicyClient, objectsInsurance
WHERE objectsInsurance.idObjects = insurancePolicyClient.idObjects
GROUP BY insurancePolicyClient.insuranceAmount, objectsInsurance.Name, objectsInsurance.numberPassport, objectsInsurance.idObjects
ORDER BY insuranceAmount DESC LIMIT 10; 
```

# 12. Построение отчета об убыточности/прибыльности компании.
- Запрос на значение разницы сумм проданных полисов и выплаченных средств.
```sql
SELECT OUTPUT.sum - INPUT.sum AS "Разница между проданнами полисами и выплат страхователям"
FROM (SELECT SUM(costInsurance) sum
      FROM insurancePolicyClient
      WHERE status='sold') OUTPUT,
     (SELECT SUM(payoutAmount) sum
      FROM payoutsDirectoryClient) INPUT;
```
# 13. Просмотр полисов заканчивающихся на конкретную дату.
- Запрос таблицы полисов с условием определенным значением даты.
```sql
 SELECT * FROM insurancePolicyClient
WHERE  stopDate = '2022-07-23 00:00:00' ;
```
# 14. Просмотр полисов по объекту страхования.
- Запрос таблицы полисов с выбранным объектом страхования.
```sql
SELECT * FROM insurancePolicyClient
WHERE  idTypeObject = 2 ;
```