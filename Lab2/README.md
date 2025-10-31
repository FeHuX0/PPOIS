Minimarket Domain Model
Account 4 3 → Wallet, PaymentProcessor, Transaction
BankAccount 5 2 → Client, Payment
CashRegister 6 2 → Payment, Receipt
Client 7 3 → Order, LoyaltyProgram, Payment
Delivery 4 2 → Order, Vehicle
Driver 5 2 → Vehicle, Route
Inventory 6 3 → Product, Warehouse, Supply
Invoice 4 2 → Client, Order
LoyaltyProgram 3 2 → Client
Order 8 4 → Client, Product, Payment, Invoice
Payment 5 3 → Client, Order, BankAccount
Product 6 2 → Category, Supplier
Receipt 4 2 → Payment, Client
Route 4 2 → Delivery, GPSPosition
Supplier 5 3 → Product, Invoice, Warehouse
Warehouse 6 3 → Product, Inventory, Supplier

Exceptions (10):
PaymentDeclinedException 0 1 →
InvalidClientDataException 0 1 →
ProductNotFoundException 0 1 →
InsufficientFundsException 0 1 →
VehicleUnavailableException 0 1 →
OrderNotFoundException 0 1 →
StorageOverflowException 0 1 →
InvalidInvoiceDataException 0 1 →
DriverUnavailableException 0 1 →
AccessDeniedException 0 1 →

Итоги
Поля: 192
Поведения: 176
Ассоциации: 66
Исключения: 12

