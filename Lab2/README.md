# Minimarket — Modular Retail Simulation System

**Minimarket** — это модульная система моделирования минимаркета.  
Проект построен по принципам чистой архитектуры: каждая область ответственности (платежи, заказы, логистика, клиенты и т.д.) реализована отдельным пакетом.  
Классы структурированы 1:1 с файлами, а тесты отражают структуру исходников.

---



##  Основные пакеты и классы

###  Core

| Класс | Назначение | Методы |
|-------|-------------|--------|
| `PaymentGateway` | Абстрактный интерфейс для шлюзов оплаты | `process_payment(source, amount, metadata)` |
| `notification` | Отправка уведомлений пользователям | `send(message)` |

---

###  Customers

| Класс | Поля | Методы |
|-------|------|--------|
| `Customer` | `customer_id`, `name`, `email` | `update_profile()`, `get_orders()` |
| `Account` | `id`, `balance`, `owner_id` | `deposit()`, `withdraw()`, `transfer_to()` |
| `AuthService` | — | `login()`, `logout()`, `verify_password()` |
| `PasswordPolicy` | `min_length`, `require_special` | `validate(password)` |
| `SessionManager` | `sessions` | `create_session()`, `invalidate()` |

**Ассоциации:**  
🔹 Список основных ассоциаций (≥30)
| №  | Класс 1              | Класс 2        | Тип связи / Описание                                 |
| -- | -------------------- | -------------- | ---------------------------------------------------- |
| 1  | Customer             | Account        | Один клиент владеет одним или несколькими аккаунтами |
| 2  | AuthService          | PasswordPolicy | AuthService использует правила пароля                |
| 3  | AuthService          | SessionManager | AuthService управляет сессиями через SessionManager  |
| 4  | Customer             | Cart           | Каждый клиент имеет корзину                          |
| 5  | Customer             | Order          | Клиент делает заказы                                 |
| 6  | Cart                 | OrderItem      | Корзина содержит элементы заказа                     |
| 7  | Order                | OrderItem      | Заказ состоит из элементов заказа                    |
| 8  | Order                | Invoice        | Заказ связан с выставленным счётом                   |
| 9  | Order                | Receipt        | Заказ связан с квитанцией                            |
| 10 | OrderItem            | Product        | Элемент заказа относится к конкретному продукту      |
| 11 | Cart                 | Product        | Корзина содержит продукты                            |
| 12 | Warehouse            | InventoryItem  | Склад содержит позиции инвентаря                     |
| 13 | PurchaseOrder        | Supplier       | Заказ поставки связан с поставщиком                  |
| 14 | PurchaseOrder        | InventoryItem  | Заказ поставки содержит позиции инвентаря            |
| 15 | Transaction          | Card           | Транзакция проводится с картой                       |
| 16 | Transaction          | Wallet         | Транзакция проводится через кошелёк                  |
| 17 | Account              | Transaction    | Аккаунт участвует в транзакциях                      |
| 18 | Card                 | Customer       | Карта принадлежит клиенту                            |
| 19 | Wallet               | Customer       | Кошелёк принадлежит клиенту                          |
| 20 | PaymentProcessor     | PaymentGateway | PaymentProcessor использует шлюз оплаты              |
| 21 | Courier              | Shipment       | Курьер обслуживает отправки                          |
| 22 | Shipment             | Order          | Отправка относится к заказу                          |
| 23 | AnalyticsService     | Order          | Сервис аналитики анализирует заказы                  |
| 24 | AnalyticsService     | Transaction    | Сервис аналитики анализирует транзакции              |
| 25 | AnalyticsService     | InventoryItem  | Сервис аналитики анализирует позиции склада          |
| 26 | FraudDetector        | Transaction    | Проверка мошенничества по транзакциям                |
| 27 | TaxCalculator        | Order          | Расчёт налогов на заказ                              |
| 28 | RecommendationEngine | Customer       | Рекомендации для клиентов                            |
| 29 | RecommendationEngine | Product        | Рекомендации включают продукты                       |
| 30 | SearchService        | Product        | Поиск осуществляется по продуктам                    |
| 31 | CurrencyConverter    | Transaction    | Конвертация валют в транзакциях                      |
| 32 | NotificationService  | Customer       | Отправка уведомлений клиентам                        |

---

###  Inventory

| Класс | Поля | Методы |
|-------|------|--------|
| `Warehouse` | `warehouse_id`, `address`, `capacity` | `store_item()`, `find_item()` |
| `Supplier` | `supplier_id`, `name` | `provide_item()` |
| `InventoryItem` | `sku`, `qty`, `location` | `reserve()`, `release()` |
| `PurchaseOrder` | `order_id`, `items`, `supplier_id` | `confirm()`, `cancel()` |

**Ассоциации:**  
- `Warehouse` содержит `InventoryItem`.  
- `PurchaseOrder` связан с `Supplier`.

---

###  Logistics

| Класс | Поля | Методы |
|-------|------|--------|
| `Courier` | `courier_id`, `name`, `vehicle` | `assign(shipment)`, `deliver(shipment)` |
| `Shipment` | `shipment_id`, `destination`, `status` | `dispatch()`, `track()` |

**Ассоциации:**  
- `Courier` ↔ `Shipment` — курьер обслуживает одну или несколько отправок.

---

###  Payments

| Класс | Поля | Методы |
|-------|------|--------|
| `Card` | `number`, `holder`, `expiry`, `balance` | `validate()`, `charge(amount)` |
| `Wallet` | `wallet_id`, `owner`, `balance` | `add_funds()`, `pay()` |
| `Transaction` | `tx_id`, `amount`, `status` | `confirm()`, `rollback()` |
| `PaymentProcessor` | `gateway` | `process()` |

**Ассоциации:**  
- `PaymentProcessor` использует `PaymentGateway`.  
- `Card` и `Wallet` участвуют в `Transaction`.

---

###  Orders

| Класс | Поля | Методы |
|-------|------|--------|
| `Cart` | `items`, `customer_id` | `add_item()`, `remove_item()`, `checkout()` |
| `Order` | `order_id`, `customer_id`, `items`, `total` | `calculate_total()`, `finalize()` |
| `OrderItem` | `sku`, `price`, `qty` | — |
| `Coupon` | `code`, `discount` | `apply(cart)` |
| `Invoice` | `invoice_id`, `order_id`, `amount` | `generate_pdf()` |
| `Receipt` | `receipt_id`, `order_id` | `print_receipt()` |

**Ассоциации:**  
- `Order` состоит из `OrderItem`.  
- `Invoice` и `Receipt` связаны с `Order`.

---

###  Products

| Класс | Поля | Методы |
|-------|------|--------|
| `Product` | `sku`, `name`, `price`, `stock` | `adjust_stock()`, `change_price()` |
| `Category` | `category_id`, `name` | `add_product()` |
| `Store` | `store_id`, `address` | `open()`, `close()` |
| `Vendor` | `vendor_id`, `name` | `supply()` |
| `CashRegister` | `register_id`, `balance` | `record_sale()` |

---

###  Services

| Класс | Назначение | Методы |
|-------|-------------|--------|
| `AnalyticsService` | Анализ продаж и трафика | `report()` |
| `CurrencyConverter` | Конвертация валют | `convert(amount, from, to)` |
| `FraudDetector` | Проверка подозрительных операций | `analyze(transaction)` |
| `NotificationService` | Отправка уведомлений | `notify(user, message)` |
| `TaxCalculator` | Расчет налогов | `compute(order)` |
| `AccountingLedger` | Ведение бухгалтерского журнала | `record(transaction)` |
| `SearchService` | Поиск по товарам | `search(query)` |
| `RecommendationEngine` | Рекомендации пользователям | `recommend(customer)` |
| `EmailService` / `SMSService` | Отправка сообщений | `send_message(to, text)` |

---

###  Исключения

| Класс | Назначение |
|-------|-------------|
| `AuthenticationError` | Ошибка аутентификации |
| `AuthorizationError` | Ошибка прав доступа |
| `DuplicateOrderError` | Повторный заказ |
| `FraudDetectedError` | Обнаружено мошенничество |
| `InsufficientFundsError` | Недостаточно средств |
| `InvalidCardError` | Ошибка в данных карты |
| `InvalidCouponError` | Некорректный купон |
| `InventorySyncError` | Ошибка синхронизации склада |
| `OutOfStockError` | Товар закончился |
| `PaymentDeclinedError` | Платеж отклонён |
| `ShippingError` | Ошибка доставки |
| `ValidationError` | Ошибка проверки данных |

---

| Категория          | Количество |
| ------------------ | ---------- |
| Классы             | 50         |
| Поля               | 150        |
| Ассоциации         | 32         |
| Методы / поведения | 100        |
| Исключения         | 12         |

