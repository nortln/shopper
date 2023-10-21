from django.shortcuts import render, HttpResponseRedirect, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.core.paginator import Paginator
import numpy as np


from .models import Catalog, Brand, Product, Cart, Review


def home(request):
    catalog = Catalog.objects.all()
    brands = Brand.objects.all()
    products = Product.objects.all()
    page = request.GET.get("page")
    paginator = Paginator(products, 8)
    page_obj = paginator.get_page(page)
    context = {
        "catalog": catalog,
        "brands": brands,
        "products": page_obj,
    }
    return render(request, "index.html", context)


def page(request, page=1):
    catalog = Catalog.objects.all()
    brands = Brand.objects.all()
    products = Product.objects.all()
    paginator = Paginator(products, 8)
    page_obj = paginator.get_page(page)

    context = {
        "catalog": catalog,
        "brands": brands,
        "products": page_obj,
    }

    return render(request, "index.html", context)


def product(request, pk):
    product = get_object_or_404(Product, id=pk)
   
    revie = product.review_set.all()
    review = product.review_set.all()
    reviews = product.review_set.all().order_by('-id')[:4]
    recommended = Product.objects.filter(catalog=product.catalog).exclude(id=pk)
    print(recommended)
    all = []
    
    print(reviews)
    for rate in review:
        all.append(rate.rating)
    
    print(all)
    if all != []:
        average = round(np.mean(all))
        print(average)
    else:
        average = 5

    
    context = {
        "product": product,
        "reviews": reviews[:4],
        "len": len(revie),
        "average": average,
        "recommended": recommended,
    
    }
    return render(request, "product.html", context)


def add_cart(request, pk):
    if request.method == "POST":
        product = Product.objects.get(id=pk)
        cart_products = Cart.product.get_queryset()
        quantity=request.POST["quantity"]
        # if product not in cart_products:
        #     cart = Cart(product=product,
        #     cart.user = request.user
        #     cart_product.quantity += int(request.POST["quantity"])
        #     cart.save()
        try:
            cart_product = Cart.objects.get(user=request.user, product=product)
            cart_product.quantity += int(quantity)
            cart_product.save()
        except Cart.DoesNotExist:
            cart_product = Cart(product=product, quantity=quantity)
            cart_product.user = request.user
            cart_product.save()
    
    return redirect(request.META.get("HTTP_REFERER"))


def update_cart(request, pk):
    product = get_object_or_404(Product, id=pk)
    cart = get_object_or_404(Cart, product=product, user=request.user)
    if request.method == "POST":
        quantity = request.POST["update_cart"]
        cart.quantity = quantity
        cart.save()

    return redirect(request.META.get("HTTP_REFERER"))

def add_review(request, pk):
    product = Product.objects.get(id=pk)

    if request.method == "POST":
        title = request.POST["title"]
        review = request.POST["review"]
        rating = request.POST["rating"]

        reviews = Review(title=title,
                         review=review,
                         rating=rating,
                         product=product,
                         user=request.user)
        reviews.save()

    return HttpResponseRedirect(redirect_to=request.META.get('HTTP_REFERER'))
    

    

def cart(request):
    carts = Cart.objects.filter(user=request.user)
    total_price = []
    for cart in carts:
        total = cart.quantity * cart.product.price
        total_price.append(total)

    total = sum(total_price)

    context = {
        "carts": carts,
        "total": total,
    }
    return render(request, "cart.html", context)



def about(request):
    return render(request, "about.html")

def contact(request):
    return render(request, "contact.html")

def faq(request):
    return render(request, "faq.html")


def personal_info(request):
    return render(request, "personal_info.html")

def payment_choose(request):
    return render(request, "payment-choose.html")

def address(request):
    return render(request, "address.html")

def address_edit(request):
    return render(request, "address-edit.html")


def auth(request):
    return render(request, "auth.html")


def login_user(request):
    if request.method == "POST":
         # email = request.POST["login_email"]
         username = request.POST["login_username"]
         password = request.POST["login_password"]
         
         user = authenticate(request, username=username.lower(), password=password)
         if user is not None:
             login(request, user)
             return redirect("home")
         else:
             return render(request, "auth.html", {"error_message": "Invalid Credentials"})
    return render(request, "auth.html")


def register_user(request):
    if request.method == "POST":
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        username = request.POST["register_username"]
        email = request.POST["register_email"]
        password = request.POST["register_password"]
        confirm_password = request.POST["confirm_password"]
        
        user = User.objects.all()

        if not User.objects.filter(username=username).exists():
            if not User.objects.filter(email=email).exists():
                if confirm_password != password:
                    context = {
                    "register_error_message": "Password must match",
                    }
                    return render(request, "auth.html", context)
                else:
                    user = User()
                    user.username = username.lower()
                    user.first_name = first_name
                    user.last_name = last_name
                    user.email = email
                    user.set_password(password)
                    user.save()
                    login(request, user)
                    return redirect("home")
            else:
                context = {
                    "register_error_message": "Email Already Exists",
                }
                return render(request, "auth.html", context)
        else:
            context = {
                "register_error_message": "Username Already Exists!!",
            }
            return render(request, "auth.html", context)
    
    return render(request, "auth.html")