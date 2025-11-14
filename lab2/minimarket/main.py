from __future__ import annotations

from datetime import date, datetime, time, timedelta

from minimarket.checkout.Order import Order
from minimarket.checkout.PaymentSession import PaymentSession
from minimarket.checkout.Receipt import Receipt
from minimarket.checkout.ShoppingCart import ShoppingCart
from minimarket.core.Aisle import Aisle
from minimarket.core.Department import Department
from minimarket.core.Planogram import Planogram
from minimarket.core.PriceTag import PriceTag
from minimarket.core.Product import Product
from minimarket.core.Shelf import Shelf
from minimarket.core.Store import Store
from minimarket.core.StoreHours import StoreHours
from minimarket.inventory.ColdStorageUnit import ColdStorageUnit
from minimarket.inventory.InventoryAudit import InventoryAudit
from minimarket.inventory.InventoryRecord import InventoryRecord
from minimarket.inventory.StockItem import StockItem
from minimarket.inventory.WasteReport import WasteReport
from minimarket.operations.CleaningSchedule import CleaningSchedule
from minimarket.operations.DisplayReset import DisplayReset
from minimarket.operations.EquipmentMaintenance import EquipmentMaintenance
from minimarket.operations.ShiftRoster import ShiftRoster
from minimarket.operations.TemperatureLog import TemperatureLog
from minimarket.people.Cashier import Cashier
from minimarket.people.Customer import Customer
from minimarket.people.Employee import Employee
from minimarket.people.Shift import Shift
from minimarket.people.SupplierRepresentative import SupplierRepresentative
from minimarket.promotions.BundleOffer import BundleOffer
from minimarket.promotions.Coupon import Coupon
from minimarket.promotions.LoyaltyAccount import LoyaltyAccount
from minimarket.promotions.PromotionCampaign import PromotionCampaign
from minimarket.promotions.Reward import Reward
from minimarket.security.AccessBadge import AccessBadge
from minimarket.security.CameraFeed import CameraFeed
from minimarket.security.LossPreventionCase import LossPreventionCase
from minimarket.security.SecurityIncident import SecurityIncident
from minimarket.support.CommunityEvent import CommunityEvent
from minimarket.support.CustomerFeedback import CustomerFeedback
from minimarket.support.GiftCard import GiftCard
from minimarket.support.IssueTicket import IssueTicket
from minimarket.support.ReturnRequest import ReturnRequest
from minimarket.supply.DeliverySchedule import DeliverySchedule
from minimarket.supply.Invoice import Invoice
from minimarket.supply.PurchaseOrder import PurchaseOrder
from minimarket.supply.Supplier import Supplier
from minimarket.supply.SupplyContract import SupplyContract
from minimarket.training.AssessmentResult import AssessmentResult
from minimarket.training.MentorshipSession import MentorshipSession
from minimarket.training.TrainingModule import TrainingModule


def run_demo() -> None:
    # Store layout and catalog
    store = Store(name="Fresh Corner Mini Market")
    produce = Department(name="Produce", manager="Nadia Ellis")
    dairy = Department(name="Dairy", manager="Gleb Antonov")
    store.add_department(produce)
    store.add_department(dairy)

    apple = Product(sku="APL100", name="Red Apple", base_price=0.50, tax_rate=0.08)
    milk = Product(sku="MLK200", name="Whole Milk 1L", base_price=1.20, tax_rate=0.05)
    bread = Product(sku="BRD300", name="Country Bread", base_price=1.80, tax_rate=0.05)

    shelf_fruit = Shelf(code="FR-01", capacity=12, temperature_zone="ambient")
    shelf_chiller = Shelf(code="DY-CHILL", capacity=10, temperature_zone="cold")
    shelf_bakery = Shelf(code="BK-01", capacity=8, temperature_zone="ambient")

    aisle_produce = Aisle(identifier="A1", category="Fresh")
    aisle_produce.add_shelf(shelf_fruit)
    aisle_dairy = Aisle(identifier="B1", category="Chilled")
    aisle_dairy.add_shelf(shelf_chiller)
    aisle_bakery = Aisle(identifier="C1", category="Bakery")
    aisle_bakery.add_shelf(shelf_bakery)

    produce.add_aisle(aisle_produce)
    dairy.add_aisle(aisle_dairy)

    shelf_fruit.add_product(apple)
    shelf_chiller.add_product(milk)
    shelf_bakery.add_product(bread)

    PriceTag(product=apple, display_price=apple.price_with_tax(), last_updated=datetime.now())
    PriceTag(product=milk, display_price=milk.price_with_tax(), last_updated=datetime.now())
    PriceTag(product=bread, display_price=bread.price_with_tax(), last_updated=datetime.now())

    planogram = Planogram(department="Produce")
    planogram.assign_product(apple, shelf_fruit)

    hours = StoreHours(day="Monday", open_time=time(8, 0), close_time=time(22, 0))
    store_open_now = hours.is_open(current_time=time(9, 30))

    # Workforce and operations
    manager = Employee(employee_id="E001", name="Nadia Ellis", role="Manager")
    cashier_employee = Employee(employee_id="E007", name="Roman Petrov", role="Cashier")
    store.hire(manager)
    store.hire(cashier_employee)

    cashier = Cashier(employee=cashier_employee)
    cashier.assign_register("REG-1")

    shift = Shift(
        shift_id="SHIFT-MORNING",
        start=datetime(2025, 5, 5, 8, 0),
        end=datetime(2025, 5, 5, 16, 0),
        area="Front of House",
    )
    cashier_employee.assign_shift(shift.shift_id)

    roster = ShiftRoster(roster_date=date(2025, 5, 5))
    roster.assign("Front of House", cashier_employee)

    cleaning = CleaningSchedule(area="Coolers")
    slot = datetime(2025, 5, 5, 7, 0)
    cleaning.add_slot(slot)
    cleaning.mark_completed(slot)

    maintenance = EquipmentMaintenance(
        equipment_id="REF-01",
        frequency_days=30,
        last_service_date=date(2025, 4, 1),
    )
    next_service = maintenance.schedule_next()

    display_reset = DisplayReset(reset_id="DR-15")
    display_reset.add_item(bread.sku)
    display_reset.add_note("Refreshed bakery end-cap.")

    temp_log = TemperatureLog(probe_id="Cooler-01", threshold=5.0)
    temp_log.record(3.8)
    temp_log.record(5.4)
    cooler_alert = temp_log.is_out_of_range()

    # Inventory management
    stock_apples = StockItem(product=apple, quantity=120, low_stock_threshold=20)
    stock_milk = StockItem(product=milk, quantity=60, low_stock_threshold=15)
    stock_bread = StockItem(product=bread, quantity=35, low_stock_threshold=10)

    record = InventoryRecord(record_id="INV-2025-05-05")
    record.add_item(stock_apples)
    record.add_item(stock_milk)
    record.add_item(stock_bread)
    store.add_inventory_record(record)

    audit = InventoryAudit(audit_id="AUD-17", records=[record])
    audit.record_discrepancy(sku=apple.sku, delta=-2)

    cold_storage = ColdStorageUnit(
        identifier="Cooler-A",
        temperature_c=3.5,
        min_temp=2.0,
        max_temp=5.0,
    )
    cold_storage.add_product(milk)
    cold_storage.log_temperature(4.2)

    waste_report = WasteReport(report_id="WR-01")
    waste_report.add_waste(sku="OLD-BREAD", quantity=3)

    # Supply chain
    supplier = Supplier(name="Green Valley Farms", lead_time_days=2)
    supplier.add_product(apple)
    supplier.add_product(milk)

    rep = SupplierRepresentative(name="Olga Smirnova", supplier_name=supplier.name)
    rep.log_visit(store.name)

    purchase_order = PurchaseOrder(po_number="PO-5521", supplier=supplier)
    purchase_order.add_item(apple.sku, quantity=80, price=0.35)
    purchase_order.add_item(milk.sku, quantity=40, price=0.90)
    purchase_order.mark_received()

    delivery = DeliverySchedule(
        schedule_id="DEL-5521",
        supplier=supplier,
        window_start=datetime(2025, 5, 6, 6, 0),
        window_end=datetime(2025, 5, 6, 8, 0),
    )
    delivery.delay(30)

    invoice = Invoice(invoice_number="INV-5521", amount_due=210.0)
    invoice.record_payment(210.0)

    contract = SupplyContract(contract_id="SC-2025", supplier=supplier, terms="Seasonal produce")
    contract.terminate()

    # Customer experience and loyalty
    loyalty = LoyaltyAccount(account_id="LOY-1001")
    loyalty.add_points(200, "Welcome bonus")
    reward = Reward(name="Free Coffee", cost_points=50, description="Complimentary drink")
    loyalty.redeem_reward(reward)
    loyalty.qualify_for_tier({"bronze": 0, "silver": 100, "gold": 200})

    coupon = Coupon(
        code="SAVE5",
        discount_percentage=5,
        expires_on=date.today(),
        usage_limit=1,
        stackable=False,
    )
    campaign = PromotionCampaign(
        name="Weekend Deals",
        start_date=date.today(),
        end_date=date.today() + timedelta(days=2),
    )
    campaign.add_product(apple)

    bundle = BundleOffer(
        name="Breakfast Combo",
        items_required={bread.sku: 1, milk.sku: 1},
        bundle_price=2.90,
    )

    customer = Customer(name="Lena Markova", loyalty_account=loyalty)
    gift_card = GiftCard(card_number="GC-2025", balance=25.0)
    gift_card.redeem(5.0)
    gift_card.load(10.0)

    feedback = CustomerFeedback(
        feedback_id="FB-01",
        customer_name=customer.name,
        rating=5,
        comment="Store is bright and well stocked.",
    )
    feedback.add_tag("cleanliness")

    issue_ticket = IssueTicket(ticket_id="SUP-12", category="Suggestion")
    issue_ticket.add_message("Please stock more gluten-free breads.")

    community_event = CommunityEvent(event_id="CE-2025", topic="Local farmer tasting")
    community_event.register(customer.name)

    # Checkout flow
    cart = ShoppingCart(max_unique_items=10)
    cart.add_item(apple, 4)
    cart.add_item(milk, 2)
    cart.add_item(bread, 1)
    cart.apply_coupon(coupon)

    order = Order(order_id="ORD-5001", cart=cart)
    order.allocate_stock(stock_apples, 4)
    order.allocate_stock(stock_milk, 2)
    order.allocate_stock(stock_bread, 1)
    order.mark_status("confirmed")

    payment = PaymentSession(session_id="PAY-5001", order=order, amount_due=order.total_due())
    payment.authorize_payment(order.total_due())

    receipt = Receipt(order=order, printed_at=datetime.now(), footnotes=["See you soon!", "Survey ID 9021"])
    summary_line = receipt.summary()

    bundle_applies = bundle.is_applicable(cart)

    return_request = ReturnRequest(
        request_id="RET-01",
        order=order,
        product=apple,
        reason="Bruised apples",
        days_since_purchase=2,
    )
    return_request.approve()

    # Training and development
    training_module = TrainingModule(module_id="TM-FOODSAFE", title="Food Safety Basics", duration_minutes=45)
    training_module.add_requirement("Hair net")

    assessment = AssessmentResult(
        employee_id=cashier_employee.employee_id,
        module_id=training_module.module_id,
        score=0.0,
    )
    assessment.record_attempt(score=92.0, passing_score=85.0)

    mentorship = MentorshipSession(mentor_id=manager.employee_id, mentee_id=cashier_employee.employee_id)
    mentorship.add_topic("Customer empathy")
    mentorship.complete()

    # Security and loss prevention
    badge = AccessBadge(badge_id="BG-01", roles_allowed={"cashier", "manager"})
    badge_access = badge.grant_access(cashier_employee.role.lower())

    incident = SecurityIncident(incident_id="INC-14", description="Bag left unattended")
    incident.escalate("Customer reminded to take bag.")
    incident.close()

    camera = CameraFeed(camera_id="CAM-Entrance")
    camera.record_alert("Unusual motion detected near entrance.")

    loss_case = LossPreventionCase(case_id="LP-04")
    loss_case.add_item(apple.sku, quantity=2)
    loss_case.add_note("Training scenario for new hires.")
    loss_case.close()

    # Output
    print("=== Mini Market Demonstration Scenario ===")
    print(f"Store: {store.name}, open now: {store_open_now}")
    print(f"Departments tracked: {len(store.departments)}, total products mapped: {store.total_products()}")
    print(f"Next maintenance for {maintenance.equipment_id}: {next_service.isoformat()}")
    print(f"Inventory audit summary: {audit.summary()}")
    print(f"Waste units recorded: {waste_report.total_units()}")
    print(f"Campaign active: {campaign.is_active()}, Bundle applicable: {bundle_applies}")
    print(f"Customer tier: {loyalty.tier}, Gift card balance: {gift_card.balance:.2f}")
    print(f"Cart total items: {cart.total_items()}, Amount charged: {order.total_due():.2f}")
    print(f"Payment status: {payment.status}, Remaining balance: {payment.remaining_balance():.2f}")
    print(summary_line)
    print(f"Return request status: {return_request.status}")
    print(f"Assessment passed: {assessment.passed}, Mentorship completed: {mentorship.completed}")
    print(f"Security badge access for cashier: {badge_access}, Incident resolved: {incident.resolved}")
    print(f"Camera status: {camera.status}, Loss case status: {loss_case.status}")
    print(f"Cooler needs attention: {cooler_alert}, Display updates: {display_reset.items_adjusted}")


if __name__ == "__main__":
    run_demo()
