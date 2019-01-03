from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Restaurant, MenuItem

app = Flask(__name__)

engine = create_engine('sqlite:///restaurantmenu.db?check_same_thread=False')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

@app.route('/')
@app.route('/restaurants/')
def showRestaurants():
    return "This page will show all my restaurants"

@app.route('/restaurant/new/')
def newRestaurants():
    return "This page will be used to make a new restaurant"

@app.route('/restaurant/<int:restaurant_id>/edit/')
def editRestaurants(restaurant_id):
    restaurant = session.query(Restaurant).filter_by(id=restaurant_id)
    output = "This page will be used to edit restaurant %s"%restaurant_id
    return output

@app.route('/restaurant/<int:restaurant_id>/delete/')
def deleteRestaurants(restaurant_id):
    restaurant = session.query(Restaurant).filter_by(id=restaurant_id)
    output = "This page will be used to delete restaurant %s"%restaurant_id
    return

@app.route('/restaurant/<int:restaurant_id>/menu/')
def showMenu(restaurant_id):
    restaurant = session.query(Restaurant).filter_by(id=restaurant_id)
    output = "This page will be used to show the menu at restaurant %s"%restaurant_id
    return output

@app.route('/restaurant/<int:restaurant_id>/menu/new/')
def newMenuItem(restaurant_id):
    restaurant = session.query(Restaurant).filter_by(id=restaurant_id)
    output = "This page will be used to create a new restaurant %s"%restaurant_id
    return output

@app.route('/restaurant/<int:restaurant_id>/menu/<int:menu_id>/edit/')
def editMenuItem(restaurant_id, menu_id):
    editedItem = session.query(MenuItem).filter_by(id=menu_id).one()
    output = "This page will be used to edit menu item %s"%menu_id
    return output

@app.route('/restaurant/<int:restaurant_id>/menu/<int:menu_id>/delete/')
def deleteMenuItem(restaurant_id, menu_id):
    itemToDelete = session.query(MenuItem).filter_by(id=menu_id).one()
    return "This page will be used to delete menu item %s"%menu_id



if __name__ == '__main__':
    app.debug = True
    app.run(host = '0.0.0.0', port = 5000)
