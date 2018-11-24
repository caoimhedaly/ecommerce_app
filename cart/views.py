from django.shortcuts import render, HttpResponse,get_object_or_404, redirect
from products.models import Product
import json



# Create your views here.


def add_to_cart(request):
    product_id=request.POST['product']
    quantity=int(request.POST['quantity'])
    
    # try to get a session variable cart, if there is none, default 0
    cart= request.session.get('cart', {})
    # cart is a dictionary, product_id is the key and quantity is the value
    cart[product_id] = cart.get(product_id, 0) + quantity
    # new quantity in cart added to original quantity
    request.session['cart'] = cart
    
    return redirect('/')
   
   
def view_cart(request):
    cart = request.session.get('cart', {})
    # get cart from session
    
    cart_total=0
    # set variable
    cart_items = []
    # list
    for product_id, quantity in cart.items():
        product = get_object_or_404(Product, pk=product_id)
    
        cart_items.append({
            'id': product.id,
            'name': product.name,
            'brand': product.brand,
            'sku': product.sku,
            'description': product.description,
            'image': product.image,
            'price': product.price,
            'stock': product.stock,
            'quantity': quantity,
            'total': product.price * quantity
        })    
    
    
        cart_total+=product.price*quantity
        
        # calculate the total proce of all products
    
    return render(request, "cart/view_cart.html", {'cart_items': cart_items, 'cart_total':cart_total})
    

   
def remove_from_cart(request):
    
    product_id = request.POST['product']
    # get product id from post
    
    cart= request.session.get('cart', {})
    # get the cart items from session
    
    del cart[product_id]
    # delete product from cart by id in key value pair
    
    request.session['cart']=cart
    # save the cart again

    return redirect("/cart/view" )
#   go back to current page

      
