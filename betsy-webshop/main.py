__winc_id__ = "d7b474e9b3a54d23bca54879a4f1855b"
__human_name__ = "Betsy Webshop"

from models import *
import os
from os import path as ospath
from datetime import datetime
from peewee import fn, SqliteDatabase

def delete_database():
    """
    Delete the Database, if it exists
    """
    #Delete the DB if it exits
    db_path = "D:\\GITCODE\\WINC\\betsy-webshop\\db\\betsy-webshop.db"
    if os.path.exists(db_path) == True:
        os.remove(db_path)
        
def populate_test_database():
    """
    Fill the Test Data
    """
    db.connect()
    print("Database Connected -->")
    
    db.create_tables([User, Tag, Products, User_product, Sale,Product_Tag])
    print("Tables Created -->")
    
    User.create(user_id=1, user_first_name='Ann', user_last_name='Arbor',address='4,Wellington Street, New York 201212, USA ',user_cc_number='1232323232323232',user_cc_expiry_date='12/12/2023')
    User.create(user_id=2, user_first_name='Rick', user_last_name='Jones',address='5,Travel Street, Texas 343454, USA ',user_cc_number='2222323232323232',user_cc_expiry_date='12/09/2023')
    
    Tag.create(tag_id='T1',tag_name='flower')
    Tag.create(tag_id='T2',tag_name='spice')
    Tag.create(tag_id='T3',tag_name='fragrant')
    
    Products.create(product_id=202,product_name='Jasmine Garland', product_description='White fragrant flower decoration',product_price_per_unit=2.09, product_quantity_in_stock=2)
    Products.create(product_id=203,product_name='Rose Garland', product_description='Red fragrant flower decoration',product_price_per_unit=4.49, product_quantity_in_stock=4)
    Products.create(product_id=204,product_name='Lily Garland', product_description='Pink fragrant flower decoration',product_price_per_unit=5.49, product_quantity_in_stock=5)
    Products.create(product_id=206,product_name='Cardamom Garland', product_description='Fragrant spice decoration',product_price_per_unit=8.49, product_quantity_in_stock=50)
    
    Product_Tag.create(pt_product_id=202,pt_tag_id='T1')
    Product_Tag.create(pt_product_id=202,pt_tag_id='T3')
    Product_Tag.create(pt_product_id=203,pt_tag_id='T1')
    Product_Tag.create(pt_product_id=203,pt_tag_id='T3')
    Product_Tag.create(pt_product_id=204,pt_tag_id='T1')
    Product_Tag.create(pt_product_id=204,pt_tag_id='T3')
    Product_Tag.create(pt_product_id=206,pt_tag_id='T2')
    Product_Tag.create(pt_product_id=206,pt_tag_id='T3')
    
    User_product.create(user_id=1,product_id=202)
    User_product.create(user_id=1,product_id=203)
    User_product.create(user_id=2,product_id=204)
    User_product.create(user_id=2,product_id=206)
    
    
    db.close()
    print("Database Created")
         

def search(term):
    """
    Search the product Name/ Description for a given term.
    """
    term = term.lower()
    search_query_result = (Products
                    .select()
                    .where(Products.product_name.contains(term) | Products.product_description.contains(term)))

    if search_query_result:
        print(f'\nResults search term : {term} -->')
        for product in search_query_result:
            print(f"- {product.product_name}")
    else:
        print('\nNo products found for the given search term.')


def list_user_products(user_id):
    """
    View the products of a given user.
    """
    user = User.get_by_id(user_id)
    user_product_list_query_result = (Products
                               .select(Products.product_name)
                               .join(User_product)
                               .where(User_product.user_id ==user_id))
    
    #User_product.select().where(User_product.user_id == user_id)
    if user_product_list_query_result:
        print(f"\n{user.user_first_name} {user.user_last_name}'s Product List  -->")
        for product in user_product_list_query_result:
            print(f"- {product.product_name}")
    else:
        print(f"\nNo user found for: {user_id}")


def list_products_per_tag(tag_id):
    """
    View all products for a given tag.
    """
    tag = Tag.get_by_id(tag_id)
    products_list_per_tag_query_result = (Products
                                   .select(Products.product_name)
                                   .join(Product_Tag)
                                   .where(Product_Tag.pt_tag_id == tag_id))
    if products_list_per_tag_query_result:
        print(f"\nProducts found for tag: {tag.tag_name} -->")
        for product in products_list_per_tag_query_result:
            print(f"- {product.product_name}")
    else: 
        print(f"\nNo products are found with tag: {tag_id}")


def add_product_to_catalog(user_id, product):
    """
    Add the product to the catalog
    """
    
    Products.create(product_id = product['product_id'],product_name = product['product_name'], product_description = product['product_description'], product_price_per_unit=product['product_price_per_unit'], product_quantity_in_stock=product['product_quantity_in_stock'])
    User_product.create(user_id= user_id ,product_id =  product['product_id'] )
    
    list_user_products(user_id)
    

def update_stock(product_id, new_quantity):
    """
    Update the product stock
    """
    product = Products.get_by_id(product_id)
    old_stock = product.product_quantity_in_stock
    product.product_quantity_in_stock = new_quantity
    product.save()
    print(f"\n{product.product_name} --> Old Stock : {str(old_stock)} . New stock :  {str(product.product_quantity_in_stock)}.")


def purchase_product(product_id, buyer_id, quantity):
    """
    Make a sale entry
    """
    product = Products.get_by_id(product_id)
    current_quantity = product.product_quantity_in_stock
    buyer = User.get_by_id(buyer_id)
       

    if quantity >= current_quantity:
        print(f"\nThere isnt enough {product.product_name} in stock.")
        return

    total_price = round(product.product_price_per_unit * quantity, 2)

    sale = Sale.create(
        sale_user_id = buyer_id,
        sale_product_id = product_id,
        sale_quantity_purchased = quantity,
        total_price = total_price,
        sold_on = datetime.now()
    )

    print(f"\nBuyer : {buyer.user_first_name} { buyer.user_last_name} bought {str(quantity)} of {product.product_name } at a total price of: €{str(total_price) } on { str(sale.sold_on) }.")

    new_quantity = product.product_quantity_in_stock - quantity

    update_stock(product.product_id, new_quantity)



def remove_product(product_id):
    """
    Remove a product from the catalog
    """
    product = Products.get_by_id(product_id)

    print(f"\nRemoving {product.product_name} from the catalog.")
    product.delete_instance()
    
def main():
    
    delete_database()
    #populate_test_database()    
    
    #search('flwer')    
    #list_user_products(2)
    #list_products_per_tag('T1')
    #add_product_to_catalog(2,{'product_id':205,'product_name':'Marigold Garland', 'product_description':'Yellow flower decoration','product_price_per_unit':1.04, 'product_quantity_in_stock':6})
    #update_stock(203,7)
    #purchase_product(203,1,2)
    #remove_product(203)
   
    
if __name__ == "__main__":       
    main()