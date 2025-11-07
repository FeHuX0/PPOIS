# Minimarket Domain Model

Account 3 3 → Customer, Wallet  
Address 3 2 → Customer, Shipment  
AnalyticsService 3 2 → Order, Product, Customer  
AuthService 3 2 → Customer, Account, SessionManager  
BatchExpirationChecker 3 5 → ProductValidator, Product  
BatchRecord 8 0 → ProductBatchTracker, Product  
Card 3 3 → Customer, PaymentProcessor, Transaction  
Cart 3 3 → Customer, Order, OrderItem, Product  
CashRegister 3 2 → Store, Transaction, Receipt  
Category 3 2 → Product, Store  
Coupon 3 2 → Order, DiscountManager  
Courier 4 2 → Shipment, Address  
CurrencyConverter 3 2 → Transaction, Order  
Customer 3 3 → Account, Cart, Order, Address, Review  
DiscountManager 2 5 → DiscountStrategy, Product, Order  
DiscountStrategy 0 2 → DiscountManager  
EmailService 3 2 → NotificationService, Customer  
ExpirationChecker 1 4 → ProductValidator, Product  
FraudDetector 3 2 → Transaction, Customer, Order  
InventoryAuditor 2 4 → InventoryItem, Warehouse, AuditReportGenerator  
InventoryItem 3 2 → Warehouse, Product, PurchaseOrder  
Invoice 3 2 → Order, Customer, PaymentProcessor  
LoyaltyProgram 3 2 → Customer, Order  
NotificationService 3 2 → NotificationBackend, Customer, Order  
Order 3 3 → Customer, OrderItem, Product, Cart, Invoice, Receipt  
OrderItem 3 2 → Order, Product  
PasswordPolicy 3 2 → Customer, Account  
PaymentProcessor 4 3 → PaymentGateway, Transaction, Card, Wallet  
Product 3 3 → Category, Store, OrderItem, Cart, InventoryItem, BatchRecord  
ProductBatchTracker 2 6 → BatchRecord, Product, InventoryItem  
ProductLabelingSystem 2 4 → LabelGenerator, Product  
ProductRotationManager 2 3 → RotationStrategyHandler, Product, InventoryItem  
ProductValidator 0 2 → Product, ExpirationChecker, BatchExpirationChecker  
PurchaseOrder 3 2 → Supplier, InventoryItem, Warehouse  
QualityAssuranceInspector 2 4 → InspectionCriteria, Product  
QualityController 2 4 → QualityInspection, Product  
Receipt 3 2 → Order, Transaction, CashRegister  
RecommendationEngine 3 2 → Product, Customer, Order  
ReturnManager 3 4 → ReturnPolicy, Order, Customer  
Review 3 2 → Product, Customer  
SearchService 3 2 → Product, Category  
SessionManager 3 2 → Customer, Account  
ShelfLifeCalculator 1 3 → ShelfLifeRule, Product  
Shipment 3 2 → Order, Courier, Address  
SMSService 3 2 → NotificationService, Customer  
StockReplenishmentManager 2 3 → ReplenishmentStrategy, Product, InventoryItem  
Store 3 3 → Vendor, Product, Category, CashRegister  
Supplier 3 2 → PurchaseOrder, Product  
TaxCalculator 3 2 → Order, Product  
TemperatureMonitor 3 4 → TemperatureSensor, TemperatureZone, InventoryItem  
Transaction 3 2 → PaymentProcessor, Card, Wallet, Order  
Vendor 3 2 → Store, Product  
Wallet 3 3 → Customer, Transaction, PaymentProcessor  
Warehouse 3 2 → InventoryItem, PurchaseOrder, ProductBatchTracker  
WasteManagementSystem 2 3 → WasteHandler, Product, InventoryItem  

BulkDiscountStrategy 2 2 → DiscountStrategy, DiscountManager  
DemandForecastStrategy 1 3 → ReplenishmentStrategy, StockReplenishmentManager  
DiscountLabelGenerator 0 2 → LabelGenerator, ProductLabelingSystem  
ExpirationLabelGenerator 0 2 → LabelGenerator, ProductLabelingSystem  
ExpirationPriceRule 2 2 → PriceAdjustmentRule, PriceAdjustmentPolicy  
FEFOStrategy 0 1 → RotationStrategyHandler, ProductRotationManager  
FIFOStrategy 0 1 → RotationStrategyHandler, ProductRotationManager  
LIFOStrategy 0 1 → RotationStrategyHandler, ProductRotationManager  
MinThresholdStrategy 2 3 → ReplenishmentStrategy, StockReplenishmentManager  
OverstockPriceRule 2 2 → PriceAdjustmentRule, PriceAdjustmentPolicy  
PercentageDiscountStrategy 1 2 → DiscountStrategy, DiscountManager  
SeasonalDiscountStrategy 3 2 → DiscountStrategy, DiscountManager  
SeasonalStrategy 1 3 → ReplenishmentStrategy, StockReplenishmentManager  
StandardLabelGenerator 0 2 → LabelGenerator, ProductLabelingSystem  

ComprehensiveInspectionCriteria 2 2 → InspectionCriteria, QualityAssuranceInspector  
PackagingInspection 0 2 → QualityInspection, QualityController  
TemperatureInspectionCriteria 2 2 → InspectionCriteria, QualityAssuranceInspector  
VisualInspection 0 2 → QualityInspection, QualityController  
VisualInspectionCriteria 0 2 → InspectionCriteria, QualityAssuranceInspector  
WeightInspection 1 2 → QualityInspection, QualityController  

ElectronicsReturnPolicy 1 3 → ReturnPolicy, ReturnManager  
PerishableReturnPolicy 0 3 → ReturnPolicy, ReturnManager  
StandardReturnPolicy 2 3 → ReturnPolicy, ReturnManager  

DigitalTemperatureSensor 2 2 → TemperatureSensor, TemperatureMonitor  
TemperatureSensor 0 2 → TemperatureMonitor, TemperatureZone  
TemperatureZone 4 3 → TemperatureMonitor, InventoryItem  

CompostHandler 0 3 → WasteHandler, WasteManagementSystem  
DonationHandler 0 3 → WasteHandler, WasteManagementSystem  
RecyclingHandler 0 3 → WasteHandler, WasteManagementSystem  

BakeryShelfLifeRule 0 2 → ShelfLifeRule, ShelfLifeCalculator  
DairyShelfLifeRule 0 2 → ShelfLifeRule, ShelfLifeCalculator  
MeatShelfLifeRule 0 2 → ShelfLifeRule, ShelfLifeCalculator  
ProduceShelfLifeRule 0 2 → ShelfLifeRule, ShelfLifeCalculator  

DetailedReportGenerator 0 2 → AuditReportGenerator, InventoryAuditor  
SummaryReportGenerator 0 2 → AuditReportGenerator, InventoryAuditor  

AuditReportGenerator 0 2 → InventoryAuditor  
InspectionCriteria 0 2 → QualityAssuranceInspector  
LabelGenerator 0 2 → ProductLabelingSystem  
NotificationBackend 0 1 → NotificationService  
PaymentGateway 0 1 → PaymentProcessor  
PriceAdjustmentRule 0 2 → PriceAdjustmentPolicy  
QualityInspection 0 2 → QualityController  
ReplenishmentStrategy 0 3 → StockReplenishmentManager  
ReturnPolicy 0 3 → ReturnManager  
RotationStrategyHandler 0 1 → ProductRotationManager  
ShelfLifeRule 0 2 → ShelfLifeCalculator  
WasteHandler 0 3 → WasteManagementSystem  

AdjustmentReason → PriceAdjustmentPolicy  
AuditFinding → InventoryAuditor  
AuditType → InventoryAuditor  
InspectionResult → QualityAssuranceInspector  
InspectionType → QualityAssuranceInspector  
LabelType → ProductLabelingSystem  
ProductCategory → ShelfLifeCalculator  
QualityGrade → QualityController  
ReplenishmentTrigger → StockReplenishmentManager  
ReturnReason → ReturnManager  
ReturnStatus → ReturnManager  
RotationStrategy → ProductRotationManager  
StorageCondition → ShelfLifeCalculator  
TemperatureAlert → TemperatureMonitor  
WasteDisposalMethod → WasteManagementSystem  
WasteReason → WasteManagementSystem  

Exceptions (12):

AuthenticationError 0 1 →  
AuthorizationError 0 1 →  
DuplicateOrderError 0 1 →  
FraudDetectedError 0 1 →  
InsufficientFundsError 0 1 →  
InvalidCardError 0 1 →  
InvalidCouponError 0 1 →  
InventorySyncError 0 1 →  
OutOfStockError 0 1 →  
PaymentDeclinedError 0 1 →  
ShippingError 0 1 →  
ValidationError 0 1 →  

Итоги

Поля: 289 Поведения: 130 Ассоциации: 98 Исключения: 12
