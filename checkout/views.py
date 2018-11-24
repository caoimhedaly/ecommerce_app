from django.shortcuts import render, redirect,get_object_or_404, HttpResponse
from products.models import Product
from .forms import MakePaymentForm, OrderForm
from .models import OrderLineItem
from django.conf import settings
from django.contrib import messages
import stripe
 
 
stripe.api_key = settings.STRIPE_SECRET_KEY
# Create your views here.




def get_cart_items_and_total(cart):
    cart_items = []
    # list
    cart_total=0
    # set variable
  
    
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
        
    return {'cart_items':cart_items, 'cart_total':cart_total}
        
    
    
    
    
def show_checkout(request):
    cart = request.session.get('cart', {})
    # get cart from dictionary in session
    
    cart_items_and_total = get_cart_items_and_total(cart)
        
    payment_form = MakePaymentForm()
    order_form= OrderForm()
    
    context= {'order_form':order_form, 'payment_form':payment_form, 'publishable':settings.STRIPE_PUBLISHABLE_KEY}
    
    context.update(cart_items_and_total)
    # add payment form to order form to display in checkout
    
    return render(request, 'checkout/show_checkout.html', context)
    


def submit_payment(request):
    
    cart = request.session.get('cart', {})
    # get the cart details
    cart_items_and_total = get_cart_items_and_total(cart)
    # get the total cost
      
    payment_form = MakePaymentForm(request.POST)
    
    order_form = OrderForm(request.POST, request.FILES)
   
   
    if order_form.is_valid() and payment_form.is_valid():
        
              order=order_form.save()
        #   save the order to the database
   
    
    
    for product_id, quantity in cart.items():
        # loop through key and values in cart items
               line_item= OrderLineItem()
            #   add to line items
               line_item.product_id = product_id
               line_item.quantity = quantity
               line_item.order = order
            #   add to this order
               line_item.save()
        
        # Grab the money and run
    total = cart_items_and_total['cart_total']
    stripe_token=payment_form.cleaned_data['stripe_id']

    try:

            total_in_cent = int(total*100)
            customer = stripe.Charge.create(
                amount=total_in_cent,
                currency="EUR",
                description="Dummy Transaction",
                card=stripe_token,
            )

    except stripe.error.CardError:
            print("Declined")
            messages.error(request, "Your card was declined!")

    if customer.paid:
            print("Paid")
            messages.error(request, "You have successfully paid")




        
               
    del request.session['cart']
    
    # clear the cart
     
    
        
    return redirect('/')
    
# return home