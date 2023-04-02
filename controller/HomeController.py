from core.Controller import Controller
from core.Core import Core
from models.Product import Product
from tkinter import messagebox
from models.Brand import Brand
from models.Category import Category
import tkinter as tk
from tkinter import ttk

"""
    Main controller. It will be responsible for program's main screen behavior.
"""
class HomeController(Controller):
    #-----------------------------------------------------------------------
    #        Constructor
    #-----------------------------------------------------------------------
    def __init__(self,root):
        self.homeView = self.loadView("Home",root)
        #self.brand = Brand()
    
    #-----------------------------------------------------------------------
    #        Methods
    #-----------------------------------------------------------------------
    product = Product()
    brand = Brand()
    category = Category()
#DASHBOARD

    def get_sum_product(self):
        return str(self.product.get_sum_product())
    def get_sum_brand(self):
        return str(self.brand.get_sum_brand())
    def get_sum_soldproduct(self):
        return str(self.product.get_sum_product())
    def get_profit(self):
        return str(self.product.get_sum_product())

#ADD_BRAND    
    def btnAdd_Brand(self,entry, tree, contentFrame):
        brand_name_list = []
        brand = self.brand.get_brand_list()
        for i in range(len(brand)):
            brand_name_list.append(brand[i][0])
        response = self.brand.check_add_brand(entry, brand_name_list)
        if response > 1:           
            messagebox.showinfo("Add brand", "Customer successfully added!")
            brand_name = entry.get()
            self.brand.add(brand_name)
        elif response == 0:
            messagebox.showerror("Add brand", "Error while adding customer!")
        else: 
            messagebox.showerror("Add brand", "Brand already exists!")
        entry.delete(0, 'end')
        new_brand_list = self.brand.get_brand_list()
        self.reset_BrandList(tree, new_brand_list, contentFrame)

#DISPLAY_BRAND_LIST
    def showTreeView_BrandList(self, contentFrame, brand_list):
        style = ttk.Style()
        style.configure("Treeview", rowheight=25)
        tree = ttk.Treeview(contentFrame, height=11)
        tree["columns"] = ("brand", "quantity")
        tree.column("#0", width=150, stretch=False)
        tree.column("brand", width=600, stretch=False)
        tree.column("quantity", width=140, stretch=False)
        tree.heading("#0", text="No.")
        tree.heading("brand", text="Brand")
        tree.heading("quantity", text="Quantity")
        tree.place(x= 20, y = 160, width = 970, height = 440)
        for i in range(len(brand_list)):
            tree.insert('', 'end', text=i+1, values=(brand_list[i][0], brand_list[i][1]))
        # Scrollbar
        scrollBar = ttk.Scrollbar(contentFrame, orient="vertical", command=tree.yview)
        scrollBar.place(x=970, y=160, height=440, width = 20)
        tree.configure(yscrollcommand=scrollBar.set)
        return tree
    
    def reset_BrandList(self, tree, brand_list, contentFrame):
        tree.destroy()
        tree = self.showTreeView_BrandList(contentFrame, brand_list)


    def BrandList_added(self, brand_list, brand):
        brand_list.append(brand)
        return brand_list
    
    
    def get_brand_list_added(self):
        brand_list = self.brand.get_brand_list()
        return brand_list   

#ADD_PRODUCT (can linked voi DB):
    def btnAdd_Product(self, fields):
        product = []
        response = self.product.check_add_product(fields)
        if response > 0:           
            messagebox.showinfo("Add brand", "Customer successfully added!")
            for i in range(len(fields)):
                product.append(fields[i].get())
            self.product.add(fields)
 #           self.brand.add(product)
        else: 
            messagebox.showerror("Add brand", "Error while adding customer")
        for i in range(len(fields)):
            fields[i].delete = (0, 'end')

    def clearContent(self, fields):
        for i in range(len(fields)):
            fields[i].delete = (0, 'end')    

    def showTreeView_ProductList(self, contentFrame, product_list):
        style = ttk.Style()
        style.configure("Treeview", rowheight=25)
        tree = ttk.Treeview(contentFrame, height=len(product_list))
        tree["columns"] = ("edit_button", "product", "brand", "category", "length_mm", "width_mm", "height_mm", "mass_kg", "fuel_capacity", "fuel_consumption_100km", "engine_type", "Maximize_Efficiency_kW_minute", "color", "Selling_Price_M", "quantity" )
        tree.column("#0", width=50, stretch=False)
        tree.column("product", width=250, stretch=False)
        tree.column("brand", width=100, stretch=False)
        tree.column("category", width=100, stretch=False)
        tree.column("length_mm", width=100, stretch=False)
        tree.column("width_mm", width=100, stretch=False)
        tree.column("height_mm", width=100, stretch=False)
        tree.column("mass_kg", width=100, stretch=False)
        tree.column("fuel_capacity", width=200, stretch=False)
        tree.column("fuel_consumption_100km", width=200, stretch=False)
        tree.column("engine_type", width=140, stretch=False)
        tree.column("Maximize_Efficiency_kW_minute", width=140, stretch=False)
        tree.column("color", width=140, stretch=False)
        tree.column("Selling_Price_M", width=140, stretch=False)
        tree.column("quantity", width=0, stretch=False)
        tree.heading("#0", text="No.")
        tree.heading("product", text="Product")
        tree.heading("brand", text="Brand")
        tree.heading("category", text="Category")
        tree.heading("length_mm", text="Length (mm)")
        tree.heading("width_mm", text="Width (mm)")
        tree.heading("height_mm", text="Height (mm)")
        tree.heading("mass_kg", text="Mass (kg)")
        tree.heading("fuel_capacity", text="Fuel Capacity (L)")
        tree.heading("fuel_consumption_100km", text="Fuel Consumption (100km)")
        tree.heading("engine_type", text="Engine Type")
        tree.heading("Maximize_Efficiency_kW_minute", text="Maximize Efficiency (kW/minute)")
        tree.heading("color", text="Color")
        tree.heading("Selling_Price_M", text="Selling Price (M)")
        tree.heading("quantity", text="Quantity")
        tree.place(x= 0, y = 0, width = 1000, height = 500)
        for i in range(0, len(product_list)):
            tree.insert('', 'end', text=i+1, values=(product_list[i][0], product_list[i][1], product_list[i][2], product_list[i][3], product_list[i][4], product_list[i][5], product_list[i][6], product_list[i][7], product_list[i][8], product_list[i][9], product_list[i][10], product_list[i][11], product_list[i][12], product_list[i][13]))
            tree.bind("<<TreeviewSelect>>", self.on_select)
        # Scrollbar
        scrollBarY = ttk.Scrollbar(contentFrame, orient="vertical", command=tree.yview)
        scrollBarY.place(x=950, y=0, height=440, width = 20)
        tree.configure(yscrollcommand=scrollBarY.set)
        scrollBarX = ttk.Scrollbar(contentFrame, orient="horizontal", command=tree.xview)
        scrollBarX.place(x=0, y=420, height=20, width = 970)
        tree.configure(xscrollcommand=scrollBarX.set)
        return tree             
    
    """
        @Override
    """
    def main(self):
        self.homeView.main()

    def on_select(self, event):
        selected_item = event.widget.selection()[0]
        values = event.widget.item(selected_item)['values']
        print(values)