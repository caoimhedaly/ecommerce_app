from django import forms
from .models import Order

class MakePaymentForm(forms.Form):
    # regular form, we have to define its properties

    MONTH_CHOICES = [(i, i,) for i in range(1, 13)]
    YEAR_CHOICES = [(i, i,) for i in range(2018, 2040)]

    credit_card_number = forms.CharField(label='Credit card number', required=False)
    cvv = forms.CharField(label='Security code (CVV)', required=False)
    expiry_month = forms.ChoiceField(label="Month", choices=MONTH_CHOICES, required=False)
    expiry_year = forms.ChoiceField(label="Year", choices=YEAR_CHOICES, required=False)
    stripe_id = forms.CharField(widget=forms.HiddenInput)



class OrderForm(forms.ModelForm):
    # model form, properties are already defined in models
    class Meta:
        model= Order
        fields='__all__'
# take form details from class order model in models.py