import datetime
import os

def generate_receipt_text(sale_id, cart_items, total_amount, payment_method="Cash/M-Pesa"):
    """Generates a formatted text receipt for Candy Wholesale Enterprises."""
    receipt_lines = []
    receipt_lines.append("=" * 40)
    receipt_lines.append("     CANDY WHOLESALE ENTERPRISES     ")
    receipt_lines.append("        Wholesale & Retail Shop      ")
    receipt_lines.append("        Kisii, Kenya                 ")
    receipt_lines.append("=" * 40)
    receipt_lines.append(f"Receipt No: #{sale_id}")
    receipt_lines.append(f"Date/Time:  {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    receipt_lines.append(f"Payment:    {payment_method}")
    receipt_lines.append("-" * 40)
    receipt_lines.append(f"{'Item':<18} {'Qty':<4} {'Price':<7} {'Total':<7}")
    receipt_lines.append("-" * 40)

    for item in cart_items:
        name = item['name'][:17] # Truncate long names to fit receipt
        qty = item['qty']
        price = item['price']
        subtotal = item['subtotal']
        receipt_lines.append(f"{name:<18} {qty:<4} {price:<7.1f} {subtotal:<7.1f}")

    receipt_lines.append("-" * 40)
    receipt_lines.append(f"TOTAL AMOUNT: Ksh {total_amount:.2f}")
    receipt_lines.append("=" * 40)
    receipt_lines.append("     Thank you for shopping with us!     ")
    receipt_lines.append("       Karibu Tena!                      ")
    receipt_lines.append("=" * 40)

    receipt_content = "\n".join(receipt_lines)
    return receipt_content

def save_and_print_receipt(sale_id, cart_items, total_amount):
    """Saves the receipt as a text file (can be printed or viewed anytime)."""
    receipt_text = generate_receipt_text(sale_id, cart_items, total_amount)
    
    # Ensure a receipts folder exists
    if not os.path.exists("receipts"):
        os.makedirs("receipts")
        
    filename = f"receipts/receipt_{sale_id}.txt"
    with open(filename, "w", encoding="utf-8") as f:
        f.write(receipt_text)
        
    return filename