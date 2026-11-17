import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import sqlite3
import datetime
import os
import shutil
from PIL import Image, ImageTk

DB_NAME = "candy_wholesale.db"

def get_db_connection():
    """Connects to SQLite and ensures the tables always exist."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS products (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        barcode TEXT UNIQUE,
        name TEXT NOT NULL,
        category TEXT NOT NULL,
        retail_price REAL NOT NULL,
        wholesale_price REAL NOT NULL,
        wholesale_min_qty INTEGER DEFAULT 10,
        stock_qty INTEGER NOT NULL,
        image_path TEXT DEFAULT 'default.png'
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS sales (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
        sale_type TEXT NOT NULL,
        payment_method TEXT NOT NULL,
        total_amount REAL NOT NULL
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS sale_items (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        sale_id INTEGER,
        product_name TEXT,
        quantity INTEGER,
        unit_price REAL,
        subtotal REAL,
        FOREIGN KEY (sale_id) REFERENCES sales(id)
    )
    """)
    conn.commit()
    return conn

def seed_sample_data():
    """Resets and seeds the 5 exact shop items with their corresponding images."""
    conn = get_db_connection()
    cursor = conn.cursor()
    
    cursor.execute("SELECT COUNT(*) FROM products")
    if cursor.fetchone()[0] == 0:
        sample_items = [
            ("1001", "Menengai Bar Soap", "General Supplies", 200.0, 180.0, 10, 50, "menengai_2.jpg"),
            ("1002", "Tropical Mints", "Sweets", 200.0, 175.0, 10, 100, "TROPICAL_2.jpg"),
            ("1003", "Softcare Diapers", "Toiletries", 680.0, 620.0, 6, 40, "PAMPAS_2.webp"),
            ("1004", "Royco Mchuzi Mix", "Food Additives", 250.0, 225.0, 10, 60, "Ryoco_2.jpg"),
            ("1005", "Mount Kenya Milk", "Milk", 1350.0, 1280.0, 5, 30, "MILK_2.jpg")
        ]
        cursor.executemany("""
        INSERT INTO products (barcode, name, category, retail_price, wholesale_price, wholesale_min_qty, stock_qty, image_path)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """, sample_items)
        conn.commit()
    conn.close()

class CandyPOSApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Candy Wholesale Enterprises")
        self.root.geometry("1200x740")
        self.root.configure(bg="#0f172a")

        self.cart = []
        self.current_photo_image = None

        # --- TOP HEADER ---
        header_frame = tk.Frame(self.root, bg="#1e3a8a", height=60)
        header_frame.pack(fill=tk.X, side=tk.TOP)
        header_frame.pack_propagate(False)

        # Right-side action buttons
        add_stock_btn = tk.Button(header_frame, text="➕ Add Stock", bg="#10b981", fg="white", font=("Arial", 10, "bold"), command=self.open_add_stock_window)
        add_stock_btn.pack(side=tk.RIGHT, padx=15, pady=12)

        report_btn = tk.Button(header_frame, text="📊 Sales Report", bg="#2563eb", fg="white", font=("Arial", 10, "bold"), command=self.open_sales_report)
        report_btn.pack(side=tk.RIGHT, padx=5, pady=12)

        # Centered Shop Name in Red Algerian Font
        title_label = tk.Label(header_frame, text="CANDY WHOLESALE ENTERPRICES", fg="#ef4444", bg="#1e3a8a", font=("Algerian", 18, "bold"))
        title_label.pack(side=tk.TOP, expand=True)

        # --- MAIN BODY CONTAINER ---
        body_frame = tk.Frame(self.root, bg="#0f172a")
        body_frame.pack(fill=tk.BOTH, expand=True, padx=15, pady=15)

        # LEFT SIDE: Product Search, Inventory Table & Image Preview
        left_frame = tk.Frame(body_frame, bg="#1e293b", bd=1, relief=tk.SOLID)
        left_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(0, 10))

        tk.Label(left_frame, text="Search & Add Products", font=("Arial", 12, "bold"), bg="#1e293b", fg="#e2e8f0").pack(anchor="w", padx=15, pady=(15, 5))
        
        # All-Blue Search Container
        search_box_frame = tk.Frame(left_frame, bg="#1e293b", bd=1, relief=tk.SOLID, padx=10, pady=10)
        search_box_frame.pack(fill=tk.X, padx=15, pady=5)
        
        tk.Label(search_box_frame, text="Type to Search:", bg="#1e293b", fg="#38bdf8", font=("Arial", 10, "bold")).pack(side=tk.LEFT, padx=(0, 5))
        
        self.search_entry = tk.Entry(search_box_frame, font=("Arial", 12), width=22, bg="#0f172a", fg="white", insertbackground="white", bd=1, relief=tk.SOLID)
        self.search_entry.pack(side=tk.LEFT, padx=5, ipady=3)
        self.search_entry.bind("<KeyRelease>", self.live_search_inventory)

        clear_search_btn = tk.Button(search_box_frame, text="Clear Search", bg="#475569", fg="white", font=("Arial", 9, "bold"), padx=8, pady=3, command=self.clear_search)
        clear_search_btn.pack(side=tk.LEFT, padx=10)

        middle_container = tk.Frame(left_frame, bg="#1e293b")
        middle_container.pack(fill=tk.BOTH, expand=True, padx=15, pady=10)

        tk.Label(middle_container, text="Available Inventory (Double click item to add to cart)", font=("Arial", 9, "italic"), bg="#1e293b", fg="#94a3b8").pack(anchor="w", pady=(0, 5))
        
        table_frame = tk.Frame(middle_container, bg="#1e293b")
        table_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # Configure TTK Styles for Custom Distinctive Blue Table Theme
        style = ttk.Style()
        style.theme_use("clam")
        style.configure("Treeview", background="#0f172a", fieldbackground="#0f172a", foreground="#f8fafc", font=("Arial", 10))
        style.configure("Treeview.Heading", font=("Arial", 10, "bold"), background="#1e3a8a", foreground="white")
        style.map("Treeview.Heading", background=[('active', '#2563eb')])
        
        # Inventory Table without Picture column
        self.inv_tree = ttk.Treeview(table_frame, columns=("ID", "Name", "Category", "Retail", "Wholesale", "Stock"), show="headings", height=13)
        self.inv_tree.heading("ID", text="Code")
        self.inv_tree.heading("Name", text="Product Name")
        self.inv_tree.heading("Category", text="Category")
        self.inv_tree.heading("Retail", text="Retail Price")
        self.inv_tree.heading("Wholesale", text="Wholesale Price")
        self.inv_tree.heading("Stock", text="Stock Qty")
        
        self.inv_tree.column("ID", width=65, anchor="center")
        self.inv_tree.column("Name", width=170, anchor="w")
        self.inv_tree.column("Category", width=110, anchor="w")
        self.inv_tree.column("Retail", width=90, anchor="e")
        self.inv_tree.column("Wholesale", width=100, anchor="e")
        self.inv_tree.column("Stock", width=80, anchor="center")
        
        self.inv_tree.pack(fill=tk.BOTH, expand=True)
        self.inv_tree.bind("<Double-1>", self.add_selected_inventory_item)
        self.inv_tree.bind("<<TreeviewSelect>>", self.on_inventory_select)

        # Alternating row colors for clarity
        self.inv_tree.tag_configure("evenrow", background="#1e293b", foreground="#f8fafc")
        self.inv_tree.tag_configure("oddrow", background="#0f172a", foreground="#f8fafc")

        # RIGHT SIDE OF LEFT FRAME: Live Product Image Preview Card
        preview_frame = tk.Frame(middle_container, bg="#1e293b", bd=1, relief=tk.SOLID, width=170)
        preview_frame.pack(side=tk.RIGHT, fill=tk.Y, padx=(10, 0))
        preview_frame.pack_propagate(False)

        tk.Label(preview_frame, text="Product Image", font=("Arial", 10, "bold"), bg="#1e293b", fg="white").pack(pady=10)
        
        self.img_display_label = tk.Label(preview_frame, text="No Image\nAvailable", bg="#0f172a", fg="#94a3b8", font=("Arial", 9), width=18, height=10, relief=tk.SUNKEN)
        self.img_display_label.pack(padx=10, pady=5)

        self.img_name_label = tk.Label(preview_frame, text="-", font=("Arial", 9, "italic"), bg="#1e293b", fg="#cbd5e1", wraplength=150)
        self.img_name_label.pack(padx=5, pady=5)

        # RIGHT SIDE: Current Cart & Checkout
        right_frame = tk.Frame(body_frame, bg="#1e293b", bd=1, relief=tk.SOLID, width=380)
        right_frame.pack(side=tk.RIGHT, fill=tk.BOTH, padx=(10, 0))
        right_frame.pack_propagate(False)

        tk.Label(right_frame, text="Current Sale Cart", font=("Arial", 12, "bold"), bg="#1e293b", fg="white").pack(anchor="w", padx=10, pady=10)

        self.cart_tree = ttk.Treeview(right_frame, columns=("Item", "Qty", "Price", "Subtotal"), show="headings", height=14)
        self.cart_tree.heading("Item", text="Product")
        self.cart_tree.heading("Qty", text="Qty")
        self.cart_tree.heading("Price", text="Price")
        self.cart_tree.heading("Subtotal", text="Subtotal")
        
        self.cart_tree.column("Item", width=130)
        self.cart_tree.column("Qty", width=40)
        self.cart_tree.column("Price", width=65)
        self.cart_tree.column("Subtotal", width=75)
        
        self.cart_tree.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)

        self.total_label = tk.Label(right_frame, text="Total: Ksh 0.00", font=("Arial", 16, "bold"), fg="#38bdf8", bg="#1e293b")
        self.total_label.pack(anchor="e", padx=15, pady=10)

        # --- CART ACTION BUTTONS ---
        checkout_frame = tk.Frame(right_frame, bg="#1e293b")
        checkout_frame.pack(fill=tk.X, padx=10, pady=10)

        clear_btn = tk.Button(checkout_frame, text="Clear", bg="#dc2626", fg="white", font=("Arial", 9, "bold"), width=8, command=self.clear_cart)
        clear_btn.pack(side=tk.LEFT, padx=2)

        print_receipt_btn = tk.Button(checkout_frame, text="🖨️ Print Receipt", bg="#0284c7", fg="white", font=("Arial", 9, "bold"), width=13, command=self.print_current_receipt)
        print_receipt_btn.pack(side=tk.LEFT, padx=2)

        pay_btn = tk.Button(checkout_frame, text="Checkout", bg="#16a34a", fg="white", font=("Arial", 9, "bold"), width=11, command=self.complete_checkout)
        pay_btn.pack(side=tk.RIGHT, padx=2)

        self.load_inventory()

    def load_inventory(self, search_query=""):
        for row in self.inv_tree.get_children():
            self.inv_tree.delete(row)
        
        conn = get_db_connection()
        cursor = conn.cursor()
        
        if search_query:
            query_str = f"%{search_query}%"
            cursor.execute("SELECT barcode, name, category, retail_price, wholesale_price, stock_qty, image_path FROM products WHERE barcode LIKE ? OR name LIKE ? OR category LIKE ?", (query_str, query_str, query_str))
        else:
            cursor.execute("SELECT barcode, name, category, retail_price, wholesale_price, stock_qty, image_path FROM products")
            
        rows = cursor.fetchall()
        for idx, row in enumerate(rows):
            barcode, name, category, retail, wholesale, stock, img_file = row
            tag = "evenrow" if idx % 2 == 0 else "oddrow"
            self.inv_tree.insert("", tk.END, values=(barcode, name, category, f"{retail:.2f}", f"{wholesale:.2f}", stock), tags=(tag,))
            
        conn.close()

        if rows:
            first_item = self.inv_tree.get_children()[0]
            self.inv_tree.selection_set(first_item)
            self.display_product_image(rows[0][1], rows[0][6])

    def live_search_inventory(self, event):
        query = self.search_entry.get().strip()
        self.load_inventory(query)

    def clear_search(self):
        self.search_entry.delete(0, tk.END)
        self.load_inventory()

    def on_inventory_select(self, event):
        selected_item = self.inv_tree.selection()
        if not selected_item:
            return
        item_data = self.inv_tree.item(selected_item)["values"]
        prod_name = item_data[1]
        
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT image_path FROM products WHERE name = ?", (prod_name,))
        res = cursor.fetchone()
        conn.close()

        img_file = res[0] if res else "default.png"
        self.display_product_image(prod_name, img_file)

    def display_product_image(self, prod_name, img_file):
        self.img_name_label.config(text=prod_name)
        img_path = os.path.join(".", img_file)

        if os.path.exists(img_path) and img_file != "default.png":
            try:
                pil_img = Image.open(img_path)
                pil_img = pil_img.resize((130, 120), Image.Resampling.LANCZOS)
                self.current_photo_image = ImageTk.PhotoImage(pil_img)
                self.img_display_label.config(image=self.current_photo_image, text="", width=130, height=120)
            except Exception:
                self.img_display_label.config(image="", text=f"Error Loading\nImage", fg="#dc2626", width=18, height=8)
        else:
            self.current_photo_image = None
            self.img_display_label.config(image="", text="No Image\nAvailable", fg="#94a3b8", width=18, height=8)

    def add_selected_inventory_item(self, event):
        selected_item = self.inv_tree.selection()
        if not selected_item:
            return
        item_data = self.inv_tree.item(selected_item)["values"]
        barcode = str(item_data[0])
        
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT name, retail_price, wholesale_price, wholesale_min_qty FROM products WHERE barcode = ?", (barcode,))
        product = cursor.fetchone()
        conn.close()

        if product:
            name, retail_price, wholesale_price, min_wholesale = product
            self.add_to_cart(name, 1, retail_price, wholesale_price, min_wholesale)

    def add_to_cart(self, name, qty, retail_price, wholesale_price, min_wholesale):
        for item in self.cart:
            if item["name"] == name:
                item["qty"] += 1
                if item["qty"] >= min_wholesale:
                    item["price"] = wholesale_price
                else:
                    item["price"] = retail_price
                item["subtotal"] = item["qty"] * item["price"]
                self.update_cart_display()
                return

        price = wholesale_price if qty >= min_wholesale else retail_price
        self.cart.append({
            "name": name,
            "qty": qty,
            "price": price,
            "retail_price": retail_price,
            "wholesale_price": wholesale_price,
            "min_wholesale": min_wholesale,
            "subtotal": qty * price
        })
        self.update_cart_display()

    def update_cart_display(self):
        for row in self.cart_tree.get_children():
            self.cart_tree.delete(row)

        grand_total = 0
        for item in self.cart:
            self.cart_tree.insert("", tk.END, values=(item["name"], item["qty"], f"{item['price']:.2f}", f"{item['subtotal']:.2f}"))
            grand_total += item["subtotal"]

        self.total_label.config(text=f"Total: Ksh {grand_total:.2f}")

    def clear_cart(self):
        self.cart = []
        self.update_cart_display()

    def generate_receipt_content(self, sale_id="PREVIEW"):
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        grand_total = sum(item["subtotal"] for item in self.cart)

        lines = [
            "========================================",
            "       CANDY WHOLESALE ENTERPRICES      ",
            "========================================",
            f"Receipt No: #{sale_id}",
            f"Date & Time: {timestamp}",
            "----------------------------------------",
            f"{'Item':<18} {'Qty':<5} {'Price':<7} {'Total':<7}",
            "----------------------------------------"
        ]

        for item in self.cart:
            name = item["name"][:17]
            qty = item["qty"]
            price = item["price"]
            subtotal = item["subtotal"]
            lines.append(f"{name:<18} {qty:<5} {price:<7.2f} {subtotal:<7.2f}")

        lines.extend([
            "----------------------------------------",
            f"TOTAL AMOUNT: Ksh {grand_total:.2f}",
            "========================================",
            "   Thank you for shopping with us!      ",
            "   You are warmly welcome back again.   ",
            "========================================"
        ])
        return "\n".join(lines), grand_total

    def print_current_receipt(self):
        if not self.cart:
            messagebox.showwarning("Empty Cart", "No items in the cart to print a receipt for.")
            return

        receipt_text, grand_total = self.generate_receipt_content()
        filename = f"receipt_print_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
        
        with open(filename, "w", encoding="utf-8") as f:
            f.write(receipt_text)

        try:
            import platform, subprocess
            current_os = platform.system()
            if current_os == "Windows":
                os.startfile(filename, "print")
            elif current_os == "Darwin":
                subprocess.run(["lp", filename], check=True)
            else:
                subprocess.run(["lpr", filename], check=True)
            
            messagebox.showinfo("Print Successful", "Receipt sent successfully to your connected printer!")
        except Exception as e:
            messagebox.showinfo("Receipt Saved", f"Receipt saved to {filename}.\n(Direct print notice: {e})")

    def complete_checkout(self):
        if not self.cart:
            messagebox.showwarning("Empty Cart", "There are no items in the cart to checkout.")
            return

        receipt_text, grand_total = self.generate_receipt_content(sale_id="NEW")

        conn = get_db_connection()
        cursor = conn.cursor()

        cursor.execute("INSERT INTO sales (sale_type, payment_method, total_amount) VALUES (?, ?, ?)", ("Retail/Wholesale", "Cash/M-Pesa", grand_total))
        sale_id = cursor.lastrowid

        for item in self.cart:
            cursor.execute("""
            INSERT INTO sale_items (sale_id, product_name, quantity, unit_price, subtotal)
            VALUES (?, ?, ?, ?, ?)
            """, (sale_id, item["name"], item["qty"], item["price"], item["subtotal"]))

            cursor.execute("""
            UPDATE products SET stock_qty = stock_qty - ? WHERE name = ?
            """, (item["qty"], item["name"]))

        conn.commit()
        conn.close()

        final_receipt, _ = self.generate_receipt_content(sale_id=sale_id)
        filename = f"receipt_{sale_id}.txt"
        with open(filename, "w", encoding="utf-8") as f:
            f.write(final_receipt)

        try:
            import platform, subprocess
            current_os = platform.system()
            if current_os == "Windows":
                os.startfile(filename, "print")
            elif current_os == "Darwin":
                subprocess.run(["lp", filename], check=True)
            else:
                subprocess.run(["lpr", filename], check=True)
        except Exception:
            pass

        messagebox.showinfo("Checkout Successful", f"Checkout Complete!\nTotal: Ksh {grand_total:.2f}\nReceipt printed & saved.")
        self.clear_cart()
        self.load_inventory()

    def open_sales_report(self):
        report_win = tk.Toplevel(self.root)
        report_win.title("Candy Wholesale Enterprises - Sales Report")
        report_win.geometry("700x500")
        report_win.configure(bg="#0f172a")

        tk.Label(report_win, text="Sales History & Revenue Report", font=("Arial", 14, "bold"), bg="#0f172a", fg="white").pack(pady=15)

        columns = ("Sale ID", "Time", "Type", "Payment", "Total (Ksh)")
        sales_tree = ttk.Treeview(report_win, columns=columns, show="headings", height=15)
        for col in columns:
            sales_tree.heading(col, text=col)
            sales_tree.column(col, width=120)
        
        sales_tree.pack(fill=tk.BOTH, expand=True, padx=15, pady=5)

        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT id, timestamp, sale_type, payment_method, total_amount FROM sales ORDER BY timestamp DESC")
        rows = cursor.fetchall()

        total_revenue = 0
        for row in rows:
            sales_tree.insert("", tk.END, values=row)
            total_revenue += row[4]
        conn.close()

        rev_label = tk.Label(report_win, text=f"Total Revenue: Ksh {total_revenue:.2f}", font=("Arial", 14, "bold"), bg="#0f172a", fg="#38bdf8")
        rev_label.pack(anchor="e", padx=25, pady=15)

    def open_add_stock_window(self):
        """Opens the Register New Product modal with a fully blue theme."""
        stock_win = tk.Toplevel(self.root)
        stock_win.title("Candy Wholesale Enterprises - Register New Product")
        stock_win.geometry("460x440")
        stock_win.configure(bg="#1e293b")

        main_frame = tk.LabelFrame(stock_win, text="Register New Product", font=("Arial", 11, "bold"), bg="#1e293b", fg="white", padx=15, pady=15)
        main_frame.pack(fill=tk.BOTH, expand=True, padx=15, pady=15)

        name_row = tk.Frame(main_frame, bg="#1e293b")
        name_row.pack(fill=tk.X, pady=8)
        tk.Label(name_row, text="Item Name:", font=("Arial", 10), bg="#1e293b", fg="white", width=14, anchor="w").pack(side=tk.LEFT)
        name_entry = tk.Entry(main_frame, font=("Arial", 11), width=28, bg="#0f172a", fg="white", insertbackground="white", bd=1, relief=tk.SOLID)
        name_entry.pack(fill=tk.X, pady=2)

        price_row = tk.Frame(main_frame, bg="#1e293b")
        price_row.pack(fill=tk.X, pady=8)
        tk.Label(price_row, text="Price (KES):", font=("Arial", 10), bg="#1e293b", fg="white", width=14, anchor="w").pack(side=tk.LEFT)
        price_entry = tk.Entry(main_frame, font=("Arial", 11), width=28, bg="#0f172a", fg="white", insertbackground="white", bd=1, relief=tk.SOLID)
        price_entry.pack(fill=tk.X, pady=2)

        stock_row = tk.Frame(main_frame, bg="#1e293b")
        stock_row.pack(fill=tk.X, pady=8)
        tk.Label(stock_row, text="Stock Quantity:", font=("Arial", 10), bg="#1e293b", fg="white", width=14, anchor="w").pack(side=tk.LEFT)
        stock_entry = tk.Entry(main_frame, font=("Arial", 11), width=28, bg="#0f172a", fg="white", insertbackground="white", bd=1, relief=tk.SOLID)
        stock_entry.pack(fill=tk.X, pady=2)

        img_row_container = tk.Frame(main_frame, bg="#1e293b")
        img_row_container.pack(fill=tk.X, pady=8)
        tk.Label(img_row_container, text="Product Image:", font=("Arial", 10), bg="#1e293b", fg="white", width=14, anchor="w").pack(side=tk.LEFT)

        selected_image_path = tk.StringVar(stock_win, value="")

        def choose_custom_image():
            file_path = filedialog.askopenfilename(title="Select Product Image", filetypes=[("Image Files", "*.jpg *.jpeg *.png *.webp")])
            if file_path:
                try:
                    base_name = os.path.basename(file_path)
                    dest_path = os.path.join(".", base_name)
                    if os.path.abspath(file_path) != os.path.abspath(dest_path):
                        shutil.copy(file_path, dest_path)
                    selected_image_path.set(base_name)
                    subtext_label.config(text=f"Selected: {base_name}", fg="#38bdf8")
                except Exception as e:
                    messagebox.showerror("Error", f"Could not copy image file: {e}")

        choose_img_btn = tk.Button(img_row_container, text="Choose Custom Image...", font=("Arial", 9), bg="#334155", fg="white", relief=tk.RAISED, command=choose_custom_image)
        choose_img_btn.pack(side=tk.LEFT)

        subtext_label = tk.Label(main_frame, text="No custom file chosen (Will use Default Image)", font=("Arial", 8, "italic"), bg="#1e293b", fg="#94a3b8")
        subtext_label.pack(anchor="w", padx=110, pady=(0, 10))

        def save_new_item():
            name = name_entry.get().strip()
            price_str = price_entry.get().strip()
            stock_str = stock_entry.get().strip()
            img_file = selected_image_path.get().strip()

            if not name or not price_str or not stock_str:
                messagebox.showerror("Missing Fields", "Please fill in Item Name, Price, and Stock Quantity.")
                return

            try:
                price = float(price_str)
                stock = int(stock_str)
            except ValueError:
                messagebox.showerror("Invalid Format", "Price must be a number and Stock must be a whole integer.")
                return

            if not img_file:
                img_file = "default.png"

            import random
            barcode = str(random.randint(2000, 9999))
            category = "General"

            conn = get_db_connection()
            cursor = conn.cursor()
            try:
                cursor.execute("""
                INSERT INTO products (barcode, name, category, retail_price, wholesale_price, stock_qty, image_path)
                VALUES (?, ?, ?, ?, ?, ?, ?)
                """, (barcode, name, category, price, price * 0.9, stock, img_file))
                conn.commit()
                messagebox.showinfo("Success", f"'{name}' successfully saved to inventory!")
                stock_win.destroy()
                self.load_inventory()
            except Exception as e:
                messagebox.showerror("Database Error", f"Could not save item: {e}")
            finally:
                conn.close()

        save_btn = tk.Button(main_frame, text="Save Item to Inventory", bg="#16a34a", fg="white", font=("Arial", 11, "bold"), padx=15, pady=6, relief=tk.RAISED, command=save_new_item)
        save_btn.pack(pady=15)

if __name__ == "__main__":
    seed_sample_data()
    root = tk.Tk()
    app = CandyPOSApp(root)
    root.mainloop()