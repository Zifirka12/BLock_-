Домашка 14.1 Введение в ООП

Создал классы 
Product
 и 
Category
.

Для класса 
Product
 определил следующие свойства:

название (
name
),
описание (
description
),
цена (
price
),
количество в наличии (
quantity
).

Для класса 
Category
 определил следующие свойства:

название (
name
),
описание (
description
),
список товаров категории (
products
).

Для этих двух классов добавил инициализацию так, чтобы каждый параметр был передан при создании объекта и сохранен.

Также для класса 
Category
 добавил два атрибута класса. Доступ к этим атрибутам должен быть у каждого объекта класса, и в них должна храниться общая информация для всех объектов. Эти атрибуты хранят в себе количество категорий и количество товаров.

Атрибуты класса должны заполняться автоматически при инициализации нового объекта.

Здесь нет необходимости считать количество на складе, можно посчитать длину списка с товарами.

Написал тесты для классов, которые проверяют:

корректность инициализации объектов класса 
Category
,

корректность инициализации объектов класса 
Product
,

подсчет количества продуктов,

подсчет количества категорий.