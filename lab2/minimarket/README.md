Mini Market Domain Model
========================

Product 5 3 2 -> PriceTag, Shelf  
PriceTag 3 1 1 -> Product  
Shelf 4 2 1 -> Product  
Aisle 3 2 1 -> Shelf  
Department 3 2 1 -> Aisle  
Store 4 4 2 -> Department, InventoryRecord  
StoreHours 4 1 1 -> Store  
Planogram 3 2 2 -> Product, Shelf  
CartItem 3 3 1 -> Product  
ShoppingCart 3 6 2 -> CartItem, Coupon  
Order 4 4 2 -> ShoppingCart, StockItem  
PaymentSession 4 3 1 -> Order  
Receipt 3 1 1 -> Order  
StockItem 4 5 1 -> Product  
InventoryRecord 3 3 1 -> StockItem  
InventoryAudit 3 3 1 -> InventoryRecord  
WasteReport 3 2 1 -> StockItem  
ReorderRequest 4 3 1 -> Product  
ColdStorageUnit 5 3 1 -> Product  
Customer 4 3 2 -> LoyaltyAccount, Order  
Employee 4 3 1 -> Shift  
Cashier 3 3 1 -> Employee  
SupplierRepresentative 3 2 1 -> Supplier  
Shift 4 1 1 -> Employee  
LoyaltyAccount 4 4 1 -> Reward  
Reward 2 0 1 -> LoyaltyAccount  
Coupon 6 4 1 -> ShoppingCart  
PromotionCampaign 5 3 1 -> Product  
BundleOffer 3 1 1 -> ShoppingCart  
CleaningSchedule 3 3 1 -> Store  
EquipmentMaintenance 3 2 1 -> Store  
TemperatureLog 3 3 1 -> Equipment  
DisplayReset 3 3 1 -> Store  
ShiftRoster 2 2 1 -> Employee  
SecurityIncident 4 3 1 -> Store  
AccessBadge 3 1 1 -> Employee  
CameraFeed 3 2 1 -> SecurityIncident  
LossPreventionCase 4 3 1 -> SecurityIncident  
CustomerFeedback 4 2 1 -> Customer  
ReturnRequest 6 3 2 -> Order, Product  
IssueTicket 4 2 1 -> Customer  
GiftCard 3 3 1 -> Customer  
CommunityEvent 3 1 1 -> Store  
Supplier 3 2 1 -> Product  
PurchaseOrder 4 3 1 -> Supplier  
DeliverySchedule 4 2 1 -> Supplier  
Invoice 3 2 1 -> Supplier  
SupplyContract 3 1 1 -> Supplier  
TrainingModule 4 2 1 -> Employee  
AssessmentResult 5 1 1 -> Employee  
MentorshipSession 4 2 1 -> Employee  

Exceptions (12)
---------------
DuplicateItemException, GiftCardBalanceException, InsufficientStockException, InventoryAuditException, OrderStateException, PaymentAuthorizationException, ProductSpoiledException, QuantityLimitException, ReturnWindowExpiredException, SupplierDelayException, UnauthorizedDiscountException, VoucherExpiredException.


Summary
-------
Classes: 52  
Fields: 184  
Behaviors: 125  
Associations: 58  
Exceptions: 12  
Modules: 11  
Tests: `tests/test_checkout.py`
