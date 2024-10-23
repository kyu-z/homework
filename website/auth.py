from flask import Blueprint, render_template, request, flash

auth=Blueprint('auth',__name__)

@auth.route('/shopping_cart',methods=['GET','POST'])
def shopping_cart():
    return render_template("shopping_cart.html", boolean=True)


