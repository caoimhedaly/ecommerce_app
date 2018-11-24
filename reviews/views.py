from django.shortcuts import render, get_object_or_404, redirect
from .models import Product
from .forms import ReviewForm
from products.views import product_detail

# Create your views here.

def make_review(request, id):
    product = get_object_or_404(Product, pk=id)
   
    
    if request.method == "POST":
        form = ReviewForm(request.POST)
        review=form.save(commit=False)
        # dont save to database
        review.author = request.user
        review.product_id=id
        # author= logged in user
        review.save()
        # finally save to database
        return redirect(product_detail, id=id)
     
    else:
     
        form = ReviewForm()
        return render(request, 'reviews/form.html', {'form':form})
    
   