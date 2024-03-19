from django.shortcuts import render
import razorpay

def initiate_payment(request):
    if request.method == "POST":
        amount = int(request.POST["amount"]) * 100  # amount in paisa
        client = razorpay.Client(auth=("YOUR_KEY_ID", "YOUR_KEY_SECRET"))

        payment = client.order.create({'amount': amount, 'currency': 'INR', 'payment_capture': '1'})

        return render(request, "payments/checkout.html", {"payment": payment})
    return render(request, "payments/pay.html")

def complete_payment(request):
    if request.method == "POST":
        return render(request, "payments/success.html")
    return render(request, "payments/failure.html")
