from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
from .models import Category
from .models import Customer
# Create your views here.
def index(request):
    products = None
    categories = Category.get_all_categories()
    # print()
    categoryID = request.GET.get('category')
    if categoryID:
        products = Product.get_all_products_by_category_id(categoryID)
    else:
        products = Product.get_all_products()

    data = {}
    data['products'] = products
    data['categories'] = categories

    
    return render(request, 'index.html' , data)
    # return render(request,'orders/order.html')


def signup(request):
    if request.method == 'GET':
        return render(request, 'signup.html')
    else:
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        password = request.POST.get('password')
        #validation
        error_message = None

        if(not first_name):
            error_message = "First Name Required !!"
        elif len(first_name) < 3:
                error_message = 'First Name should be more than 3 characters'
            

        #saving
        if not error_message:
            customer = Customer(first_name=first_name, last_name=last_name, phone=phone, email=email, password=password)
            customer.register()
        else:
            return HttpResponse(request,'signup.html', {'error': error_message})



