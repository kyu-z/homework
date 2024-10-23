from flask import Blueprint, render_template, request, flash, redirect, url_for, jsonify
from .models import Item
from . import db
import json

views=Blueprint('views',__name__)

@views.route('/', methods=['GET','POST'])
def home():
    if request.method == 'POST':
        itemName = request.form.get('itemName')
        if len(itemName) < 2:
            flash('Item name must be more than 1 character.', category='error')
        else:
            new_item = Item(name=itemName)  
            db.session.add(new_item) 
            db.session.commit()  
            flash('Item is added.', category='success')
            return redirect(url_for('views.shopping_cart'))
       
    return render_template('home.html')  

@views.route('/shopping_cart', methods=['GET'])
def shopping_cart():
    items = Item.query.all() 
    print(items)
    return render_template('shopping_cart.html', items=items) 

@views.route('/delete-item',methods=['POST'])
def delete_item():
    item = json.loads(request.data)
    itemId = item['itemId']
    print(f"Attempting to delete item with ID: {itemId}") 

    item_to_delete = Item.query.get(itemId)
    if item_to_delete:
        db.session.delete(item_to_delete) 
        db.session.commit()  
        print(f"Item with ID {itemId} deleted successfully")
        return jsonify({'success': True, 'message': 'Item deleted successfully.'})
    else:
        return jsonify({'success': False, 'message': 'Item not found.'}), 404
