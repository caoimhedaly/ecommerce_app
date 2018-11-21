def items_in_cart(request):
   cart= request.session.get('cart', {})
   
   count = 0
   for product, quantity in cart.items():
       count += quantity
       
    #   number of items in cart
   return {'items_in_cart':count}