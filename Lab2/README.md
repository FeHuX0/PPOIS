# Minimarket — Modular Retail Simulation System

**Minimarket** — это модульная система моделирования минимаркета.  
Проект построен по принципам чистой архитектуры: каждая область ответственности (платежи, заказы, логистика, клиенты и т.д.) реализована отдельным пакетом.  
Классы структурированы 1:1 с файлами, а тесты отражают структуру исходников.

---

## Архитектура проекта

src/
├── minimarket/
│ ├── core/ # Базовые интерфейсы и абстракции
│ ├── customers/ # Клиенты, аккаунты, сессии
│ ├── errors/ # Кастомные исключения
│ ├── inventory/ # Склад, поставщики, инвентарь
│ ├── logistics/ # Доставка и курьеры
│ ├── misc/ # Мелкие сущности (адрес, отзывы)
│ ├── orders/ # Корзина, заказ, чек
│ ├── payments/ # Карты, транзакции, процессоры
│ ├── products/ # Товары, категории, магазины
│ └── services/ # Сервисы аналитики, налогов, уведомлений
└── tests/ # Unit и integration тесты


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
- `Customer` ↔ `Account` — один клиент владеет одним или несколькими аккаунтами.  
- `AuthService` использует `PasswordPolicy` и `SessionManager`.

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

##  Ассоциации (UML-образно)

Customer ──┬──> Account ───> Transaction
└──> Cart ───> Order ───> Invoice
Product ───> InventoryItem ───> Warehouse
Shipment <── Courier
PaymentProcessor ───> PaymentGateway
