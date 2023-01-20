from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from django.shortcuts import render
import razorpay
from django.views.decorators.csrf import csrf_exempt


def home(request):
    if request.method == "POST":
        name = request.POST.get('name')
        amount = 50000

        client = razorpay.Client(
auth=("TEST_KEY", "SECRET_KEY"))
        payment = client.order.create({'amount': amount, 'currency': 'INR',
'payment_capture': '1'})

    return render(request, 'pay_index.html')

@csrf_exempt
def success(request):
    return render(request, "pay_success.html")