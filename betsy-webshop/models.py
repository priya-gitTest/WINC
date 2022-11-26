# Models go here

# Import from peewee
from peewee import *

db = SqliteDatabase("D:\\GITCODE\\WINC\\betsy-webshop\\db\\betsy-webshop.db")

#class BaseModel(Model):
#    class Meta:
#        database = db
               

    
class User(Model):
    user_id = CharField(primary_key=True) # primary key = unique id
    user_first_name = CharField()
    user_last_name = CharField()
    address = TextField()
    user_cc_number = IntegerField()
    user_cc_expiry_date = DateField()
    
    class Meta:
        database = db
        db_table = 'user'

class Tag(Model):
    tag_id = CharField(primary_key=True) # primary key = unique id
    tag_name = CharField(unique=True)
    
    class Meta:
        database = db
        db_table = 'tag'
    
class Products(Model):
    product_id = CharField(primary_key=True) # primary key = unique id
    product_name = CharField(index=True)
    product_description = CharField(index=True)
    product_price_per_unit = DecimalField(max_digits=10, decimal_places=2,auto_round=True)
    product_quantity_in_stock = IntegerField(constraints=[Check('product_quantity_in_stock >= 0')])
    
    class Meta:
        database = db
        db_table = 'products'
        
class Product_Tag(Model):
    pt_product_id = ForeignKeyField(Products, backref='product_tag')
    pt_tag_id = ForeignKeyField(Tag, backref='product_tag')

    class Meta:
        database = db
        db_table = 'product_tag'
        
class User_product(Model):
    user_id = ForeignKeyField(User, backref='user_product')
    product_id = ForeignKeyField(Products, backref='user_product')
    
    class Meta:
        database = db
        db_table = 'user_product'
    
class Sale(Model):
    sale_user_id = ForeignKeyField(User, backref='sale')
    sale_product_id = ForeignKeyField(Products, backref='sale')
    sale_quantity_purchased = IntegerField(constraints=[Check('sale_quantity_purchased >= 0')])
    total_price = DecimalField(max_digits=10, decimal_places=2,auto_round=True)
    sold_on = DateField()

    class Meta:
        database = db
        db_table = 'sale'


def create_DB():
    
    db.create_tables([User, Products])
    #User.create_table()
    #rec1=User(name="Rajesh", age=21)
    #rec1.save()
    #User.create(name="Kiran", age=19)
    
if __name__ == "__main__":
    pass
            