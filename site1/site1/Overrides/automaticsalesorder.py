import frappe
def automaticsales(doc,method):
    sales_order = frappe.new_doc("Sales Order")
    sales_order.customer = doc.customer
    sales_order.transaction_date = doc.transaction_date
    sales_order.delivery_date = doc.valid_till 
    for item in doc.items:
        sales_order.append("items", {
            "item_code": item.item_code,
            "qty": item.qty,
            "rate": item.rate
        })
        
    sales_order.insert()
    sales_order.submit()
    frappe.msgprint(f"Sales Order {sales_order.name} created automatically.")