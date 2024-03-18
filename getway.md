### integrating Razorpay into a Django project for accepting payments:

### Step 1: Initiate the Django Project

```bash
# Install Django
pip install django

# Create Django Project
django-admin startproject dj_razorpay

# Create App
cd dj_razorpay
python manage.py startapp payment
```

### Step 2: Get Razorpay Keys

- Sign up on Razorpay's website and obtain Key ID and Key Secret.

### Step 3: Install Razorpay Package

```bash
# Install Razorpay Package
pip install razorpay
```

### Step 4: Create Views (views.py)

```python
from django.shortcuts import render
import razorpay
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseBadRequest
 
 
# authorize razorpay client with API Keys.
razorpay_client = razorpay.Client(
    auth=(settings.RAZOR_KEY_ID, settings.RAZOR_KEY_SECRET))
 
 
def homepage(request):
    currency = 'INR'
    amount = 20000  # Rs. 200
 
    # Create a Razorpay Order
    razorpay_order = razorpay_client.order.create(dict(amount=amount,
                                                       currency=currency,
                                                       payment_capture='0'))
 
    # order id of newly created order.
    razorpay_order_id = razorpay_order['id']
    callback_url = 'paymenthandler/'
 
    # we need to pass these details to frontend.
    context = {}
    context['razorpay_order_id'] = razorpay_order_id
    context['razorpay_merchant_key'] = settings.RAZOR_KEY_ID
    context['razorpay_amount'] = amount
    context['currency'] = currency
    context['callback_url'] = callback_url
 
    return render(request, 'index.html', context=context)
 
 
# we need to csrf_exempt this url as
# POST request will be made by Razorpay
# and it won't have the csrf token.
@csrf_exempt
def paymenthandler(request):
 
    # only accept POST request.
    if request.method == "POST":
        try:
           
            # get the required parameters from post request.
            payment_id = request.POST.get('razorpay_payment_id', '')
            razorpay_order_id = request.POST.get('razorpay_order_id', '')
            signature = request.POST.get('razorpay_signature', '')
            params_dict = {
                'razorpay_order_id': razorpay_order_id,
                'razorpay_payment_id': payment_id,
                'razorpay_signature': signature
            }
 
            # verify the payment signature.
            result = razorpay_client.utility.verify_payment_signature(
                params_dict)
            if result is not None:
                amount = 20000  # Rs. 200
                try:
 
                    # capture the payemt
                    razorpay_client.payment.capture(payment_id, amount)
 
                    # render success page on successful caputre of payment
                    return render(request, 'paymentsuccess.html')
                except:
 
                    # if there is an error while capturing payment.
                    return render(request, 'paymentfail.html')
            else:
 
                # if signature verification fails.
                return render(request, 'paymentfail.html')
        except:
 
            # if we don't find the required parameters in POST data
            return HttpResponseBadRequest()
    else:
       # if other than POST request is made.
        return HttpResponseBadRequest()
```

### Step 5: Frontend (index.html)

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>GFG</title>
    <style>
       
      * {
        box-sizing: border-box;
        padding: 0px;
        margin: 0px;
        font-family: cursive;
      }
      html,
      body {
        height: 100%;
      }
      body {
        background-color: #f1f5f8;
        display: flex;
        justify-content: center;
        align-items: center;
      }
      .card {
        background-color: white;
        padding: 25px;
        border: 1px solid #bbbbbb;
        border-radius: 5px;
        box-shadow: 1px 1px 10px 0px rgb(0 0 0 / 25%);
      }
      .title {
        text-align: center;
        letter-spacing: 1px;
      }
      .muted {
        color: #8e7f7f;
        display: block;
        margin-bottom: 10px;
        text-align: center;
      }
      .btn_container {
        padding: 20px;
        text-align: center;
      }
      .btn {
        border-radius: 4px;
        cursor: pointer;
        padding: 4px 8px;
        background-color: #ffaaa7;
        color: white;
        font-size: 1.2em;
        font-weight: 600;
        letter-spacing: 1px;
      }
    </style>
  </head>
  <body>
    <div class="card">
      <h1 class="title">Buy Me a Chai ☕</h1>
      <small class="muted"
        >If you like my work, you can support me by donating ₹200</small
      >
      <div class="btn_container">
        <!-- Payment Button -->
        <button class="btn" id="pay-btn">Donate❤️</button>
      </div>
    </div>
  </body>
   
  <!-- Razorpay's Javascript code. -->
  <script src="https://checkout.razorpay.com/v1/checkout.js"></script>
  <script>
    var options = {
       
      // Enter the Key ID generated from the Dashboard
      key: "{{ razorpay_merchant_key }}", 
       
      // Amount is in currency subunits.
      // Default currency is INR. Hence, 
      // 50000 refers to 50000 paise
      amount: "{{ razorpay_amount }}", 
      currency: "{{ currency }}",
       
      // Your/store name.
      name: "Dj Razorpay", 
       
      // Pass the `id` obtained in the response of Step 1
      order_id: "{{ razorpay_order_id }}", 
      callback_url: "{{ callback_url }}",
    };
     
    // initialise razorpay with the options.
    var rzp1 = new Razorpay(options);
     
    // add event listener to the payment button.
    document.getElementById("pay-btn").onclick = function (e) {
      rzp1.open();
      e.preventDefault();
    };
  </script>
</html>
```

### Step 6: URL Mapping (urls.py)

```python
from django.contrib import admin
from django.urls import path
from payment import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('paymenthandler/', views.paymenthandler, name='paymenthandler'),
    path('admin/', admin.site.urls),
]
```

That's it! You've successfully integrated Razorpay into your Django project for accepting payments. Make sure to replace `{{ razorpay_merchant_key }}` with your actual Razorpay Key ID in the frontend template.