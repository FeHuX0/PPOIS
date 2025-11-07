# Minimarket Domain Model

## Core Classes

**Account** 3 3 → Customer, Wallet  
**Address** 4 1 → Customer, Shipment  
**AnalyticsService** 2 3 → Order, Product, Customer  
**AuthService** 2 2 → Customer, Account, SessionManager  
**AuthenticationError** 0 1 →  
**AuthorizationError** 0 1 →  
**BatchExpirationChecker** 3 5 → ProductValidator, Product  
**BatchRecord** 8 0 → ProductBatchTracker, Product  
**Card** 3 2 → Customer, PaymentProcessor, Transaction  
**Cart** 3 4 → Customer, Order, OrderItem, Product  
**CashRegister** 2 2 → Store, Transaction, Receipt  
**Category** 2 2 → Product, Store  
**Coupon** 3 2 → Order, DiscountManager  
**Courier** 2 2 → Shipment, Address  
**CurrencyConverter** 2 2 → Transaction, Order  
**Customer** 3 3 → Account, Cart, Order, Address, Review  
**DiscountManager** 2 5 → DiscountStrategy, Product, Order  
**DiscountStrategy** 0 2 → DiscountManager  
**DuplicateOrderError** 0 1 →  
**EmailService** 2 2 → NotificationService, Customer  
**ExpirationChecker** 1 4 → ProductValidator, Product  
**FraudDetectedError** 0 1 →  
**FraudDetector** 2 3 → Transaction, Customer, Order  
**InsufficientFundsError** 0 1 →  
**InventoryAuditor** 2 4 → InventoryItem, Warehouse, AuditReportGenerator  
**InventoryItem** 3 2 → Warehouse, Product, PurchaseOrder  
**Invoice** 3 2 → Order, Customer, PaymentProcessor  
**InvalidCardError** 0 1 →  
**InvalidCouponError** 0 1 →  
**InventorySyncError** 0 1 →  
**LoyaltyProgram** 3 3 → Customer, Order  
**NotificationService** 2 3 → NotificationBackend, Customer, Order  
**Order** 3 3 → Customer, OrderItem, Product, Cart, Invoice, Receipt  
**OrderItem** 4 2 → Order, Product  
**OutOfStockError** 0 1 →  
**PasswordPolicy** 2 2 → Customer, Account  
**PaymentDeclinedError** 0 1 →  
**PaymentProcessor** 2 3 → PaymentGateway, Transaction, Card, Wallet  
**Product** 3 3 → Category, Store, OrderItem, Cart, InventoryItem, BatchRecord  
**ProductBatchTracker** 2 6 → BatchRecord, Product, InventoryItem  
**ProductLabelingSystem** 2 4 → LabelGenerator, Product  
**ProductRotationManager** 2 3 → RotationStrategyHandler, Product, InventoryItem  
**ProductValidator** 0 2 → Product, ExpirationChecker, BatchExpirationChecker  
**PurchaseOrder** 3 2 → Supplier, InventoryItem, Warehouse  
**QualityAssuranceInspector** 2 4 → InspectionCriteria, Product  
**QualityController** 2 4 → QualityInspection, Product  
**Receipt** 3 2 → Order, Transaction, CashRegister  
**RecommendationEngine** 2 3 → Product, Customer, Order  
**ReturnManager** 2 4 → ReturnPolicy, Order, Customer  
**Review** 3 2 → Product, Customer  
**SearchService** 2 2 → Product, Category  
**SessionManager** 2 3 → Customer, Account  
**ShelfLifeCalculator** 1 3 → ShelfLifeRule, Product  
**ShippingError** 0 1 →  
**Shipment** 3 2 → Order, Courier, Address  
**SMSService** 2 2 → NotificationService, Customer  
**StockReplenishmentManager** 2 3 → ReplenishmentStrategy, Product, InventoryItem  
**Store** 3 3 → Vendor, Product, Category, CashRegister  
**Supplier** 2 2 → PurchaseOrder, Product  
**TaxCalculator** 2 2 → Order, Product  
**TemperatureMonitor** 2 4 → TemperatureSensor, TemperatureZone, InventoryItem  
**Transaction** 4 2 → PaymentProcessor, Card, Wallet, Order  
**ValidationError** 0 1 →  
**Vendor** 2 2 → Store, Product  
**Wallet** 3 3 → Customer, Transaction, PaymentProcessor  
**Warehouse** 3 2 → InventoryItem, PurchaseOrder, ProductBatchTracker  
**WasteManagementSystem** 2 3 → WasteHandler, Product, InventoryItem  

## Strategy Pattern Classes

**BulkDiscountStrategy** 2 2 → DiscountStrategy, DiscountManager  
**DemandForecastStrategy** 1 3 → ReplenishmentStrategy, StockReplenishmentManager  
**DiscountLabelGenerator** 0 2 → LabelGenerator, ProductLabelingSystem  
**ExpirationLabelGenerator** 0 2 → LabelGenerator, ProductLabelingSystem  
**ExpirationPriceRule** 2 2 → PriceAdjustmentRule, PriceAdjustmentPolicy  
**FEFOStrategy** 0 1 → RotationStrategyHandler, ProductRotationManager  
**FIFOStrategy** 0 1 → RotationStrategyHandler, ProductRotationManager  
**LIFOStrategy** 0 1 → RotationStrategyHandler, ProductRotationManager  
**MinThresholdStrategy** 2 3 → ReplenishmentStrategy, StockReplenishmentManager  
**OverstockPriceRule** 2 2 → PriceAdjustmentRule, PriceAdjustmentPolicy  
**PercentageDiscountStrategy** 1 2 → DiscountStrategy, DiscountManager  
**SeasonalDiscountStrategy** 3 2 → DiscountStrategy, DiscountManager  
**SeasonalStrategy** 1 3 → ReplenishmentStrategy, StockReplenishmentManager  
**StandardLabelGenerator** 0 2 → LabelGenerator, ProductLabelingSystem  

## Quality Control Classes

**ComprehensiveInspectionCriteria** 2 2 → InspectionCriteria, QualityAssuranceInspector  
**PackagingInspection** 2 2 → QualityInspection, QualityController  
**TemperatureInspectionCriteria** 2 2 → InspectionCriteria, QualityAssuranceInspector  
**VisualInspection** 2 2 → QualityInspection, QualityController  
**VisualInspectionCriteria** 0 2 → InspectionCriteria, QualityAssuranceInspector  
**WeightInspection** 2 2 → QualityInspection, QualityController  

## Return Management Classes

**ElectronicsReturnPolicy** 2 3 → ReturnPolicy, ReturnManager  
**PerishableReturnPolicy** 2 3 → ReturnPolicy, ReturnManager  
**StandardReturnPolicy** 2 3 → ReturnPolicy, ReturnManager  

## Temperature Monitoring Classes

**DigitalTemperatureSensor** 2 2 → TemperatureSensor, TemperatureMonitor  
**TemperatureSensor** 0 2 → TemperatureMonitor, TemperatureZone  
**TemperatureZone** 3 3 → TemperatureMonitor, InventoryItem  

## Waste Management Classes

**CompostHandler** 0 3 → WasteHandler, WasteManagementSystem  
**DonationHandler** 0 3 → WasteHandler, WasteManagementSystem  
**RecyclingHandler** 0 3 → WasteHandler, WasteManagementSystem  

## Shelf Life Calculation Classes

**BakeryShelfLifeRule** 0 2 → ShelfLifeRule, ShelfLifeCalculator  
**DairyShelfLifeRule** 0 2 → ShelfLifeRule, ShelfLifeCalculator  
**MeatShelfLifeRule** 0 2 → ShelfLifeRule, ShelfLifeCalculator  
**ProduceShelfLifeRule** 0 2 → ShelfLifeRule, ShelfLifeCalculator  

## Audit Classes

**DetailedReportGenerator** 0 2 → AuditReportGenerator, InventoryAuditor  
**SummaryReportGenerator** 0 2 → AuditReportGenerator, InventoryAuditor  

## Abstract Base Classes

**AuditReportGenerator** 0 2 → InventoryAuditor  
**InspectionCriteria** 0 2 → QualityAssuranceInspector  
**LabelGenerator** 0 2 → ProductLabelingSystem  
**NotificationBackend** 0 1 → NotificationService  
**PaymentGateway** 0 1 → PaymentProcessor  
**PriceAdjustmentRule** 0 2 → PriceAdjustmentPolicy  
**QualityInspection** 0 2 → QualityController  
**ReplenishmentStrategy** 0 3 → StockReplenishmentManager  
**ReturnPolicy** 0 3 → ReturnManager  
**RotationStrategyHandler** 0 1 → ProductRotationManager  
**ShelfLifeRule** 0 2 → ShelfLifeCalculator  
**TemperatureSensor** 0 2 → TemperatureMonitor  
**WasteHandler** 0 3 → WasteManagementSystem  

## Enums

**AdjustmentReason** → PriceAdjustmentPolicy  
**AuditFinding** → InventoryAuditor  
**AuditType** → InventoryAuditor  
**InspectionResult** → QualityAssuranceInspector  
**InspectionType** → QualityAssuranceInspector  
**LabelType** → ProductLabelingSystem  
**ProductCategory** → ShelfLifeCalculator  
**QualityGrade** → QualityController  
**ReplenishmentTrigger** → StockReplenishmentManager  
**ReturnReason** → ReturnManager  
**ReturnStatus** → ReturnManager  
**RotationStrategy** → ProductRotationManager  
**StorageCondition** → ShelfLifeCalculator  
**TemperatureAlert** → TemperatureMonitor  
**WasteDisposalMethod** → WasteManagementSystem  
**WasteReason** → WasteManagementSystem  

## Exceptions (12)

**AuthenticationError** 0 1 →  
**AuthorizationError** 0 1 →  
**DuplicateOrderError** 0 1 →  
**FraudDetectedError** 0 1 →  
**InsufficientFundsError** 0 1 →  
**InvalidCardError** 0 1 →  
**InvalidCouponError** 0 1 →  
**InventorySyncError** 0 1 →  
**OutOfStockError** 0 1 →  
**PaymentDeclinedError** 0 1 →  
**ShippingError** 0 1 →  
**ValidationError** 0 1 →  

## Statistics

**Total Classes:** 120+  
**Total Fields:** ~350+  
**Total Methods:** ~200+  
**Total Associations:** ~150+  
**Total Exceptions:** 12  

## Architecture Principles

Все классы следуют принципам SOLID:

- **Single Responsibility Principle (SRP)**: Каждый класс имеет одну ответственность
- **Open/Closed Principle (OCP)**: Классы открыты для расширения через наследование и композицию
- **Liskov Substitution Principle (LSP)**: Подклассы могут заменять базовые классы
- **Interface Segregation Principle (ISP)**: Интерфейсы разделены на специфичные абстракции
- **Dependency Inversion Principle (DIP)**: Зависимости от абстракций, а не от конкретных реализаций

## Design Patterns Used

- **Strategy Pattern**: DiscountStrategy, ReplenishmentStrategy, RotationStrategyHandler, PriceAdjustmentRule, WasteHandler, InspectionCriteria, ShelfLifeRule, LabelGenerator, AuditReportGenerator
- **Factory Pattern**: LabelGenerator implementations
- **Template Method Pattern**: ProductValidator, QualityInspection
- **Observer Pattern**: TemperatureMonitor, NotificationService
- **Facade Pattern**: PaymentProcessor, NotificationService

## Module Structure

```
src/minimarket/
├── core/           # Базовые абстракции
├── customers/      # Управление клиентами
├── errors/         # Исключения
├── inventory/      # Управление складом и инвентарем
├── logistics/      # Логистика и доставка
├── misc/           # Вспомогательные классы
├── orders/         # Управление заказами
├── payments/       # Платежи и транзакции
├── products/       # Продукты и валидация
└── services/       # Бизнес-сервисы
```

## Key Features

### Product Management
- Проверка срока годности (ExpirationChecker, BatchExpirationChecker)
- Расчет срока годности (ShelfLifeCalculator)
- Валидация продуктов (ProductValidator)
- Маркировка продуктов (ProductLabelingSystem)

### Inventory Management
- Ротация продуктов (ProductRotationManager - FIFO/LIFO/FEFO)
- Отслеживание партий (ProductBatchTracker)
- Пополнение запасов (StockReplenishmentManager)
- Аудит инвентаризации (InventoryAuditor)
- Управление отходами (WasteManagementSystem)
- Мониторинг температуры (TemperatureMonitor)

### Pricing & Discounts
- Управление скидками (DiscountManager)
- Корректировка цен (PriceAdjustmentPolicy)
- Налоговые расчеты (TaxCalculator)

### Quality Control
- Контроль качества (QualityController)
- Инспекция качества (QualityAssuranceInspector)

### Order Management
- Корзина покупок (Cart)
- Заказы (Order)
- Возвраты (ReturnManager)

### Customer Management
- Клиенты (Customer)
- Аутентификация (AuthService)
- Программа лояльности (LoyaltyProgram)

### Payment Processing
- Обработка платежей (PaymentProcessor)
- Транзакции (Transaction)
- Кошельки и карты (Wallet, Card)

### Services
- Аналитика (AnalyticsService)
- Рекомендации (RecommendationEngine)
- Поиск (SearchService)
- Уведомления (NotificationService)
- Обнаружение мошенничества (FraudDetector)


