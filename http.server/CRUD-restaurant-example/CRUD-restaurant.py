# set up SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Restaurant, MenuItem

# the following CRUD operations are based on SQLite database
# connect to the restaurantmenu.db
engine = create_engine('sqlite:///restaurantmenu.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind = engine)
session = DBSession() # create a session to interface with the database

#### Type "python" in terminal

#### Create a new row in the database
# 1. newEntry = ClassName(property = "value", ...)
# 2. session.add(newEntry)
# 3. session.commit()

### create a new Restaurant
myFirstRestaurant = Restaurant(name="Pizz Palace")
session.add(myFirstRestaurant) #myFirstRestaurant is now in the staging zone to be committed
session.commit() #myFirstRestaurant is now stored in the database
session.query(Restaurant).all()
### create a cheese pizza menue and add it to the newly created restaurant
cheesepizza = MenuItem(name="Cheese Pizza"
    , description="Made with all natural ingredients and fresh mozzarella"
    , course="Entree", price="$8.99", restaurant=myFirstRestaurant)
session.add(cheesepizza)
session.commit()
session.query(MenuItem).all()

#### Read entries from the database
session.query(Restaurant).all #select * from Restaurant tables

items_stored = session.query(MenuItem).all()
for item in items_stored:
    print(item.name)

#### Update the database
# print all the veggie burgers
veggieBurgers = session.query(MenuItem).filter_by(name='Veggie Burger')
for veggieBurger in veggieBurgers:
    print (veggieBurger.id)
    print (veggieBurger.price)
    print (veggieBurger.restaurant.name)
    print ("\n")

# update the price of one veggie burger with the id of 9
# .one() gives the one object, instead of a list
UrbanVeggieBurger = session.query(MenuItem).filter_by(id=9).one()
print (UrbanVeggieBurger.price)
UrbanVeggieBurger.price = '$2.99'
session.add(UrbanVeggieBurger)
session.commit()

# update the prices for all the veggieBurgers in the database
for veggieBurger in veggieBurgers:
    if veggieBurger.price != '$2.99':
        veggieBurger.price = '$2.99'
        session.add(veggieBurger)
        session.commit()

#### Delete entries from the database
# 1. Find entry
# 2. session.delete(entry)
# 3. session.commit()

# delete the first row
spinach = session.query(MenuItem).filter_by(name='Spinach Ice Cream').first()
print (spinach.restaurant.name)
session.delete(spinach)
session.commit()
# delete the second row
spinach2 = session.query(MenuItem).filter_by(name='Spinach Ice Cream').one()
session.delete(spinach2)
session.commit()
