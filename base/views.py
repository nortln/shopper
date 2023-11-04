from django.shortcuts import render, HttpResponseRedirect, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
import numpy as np


from .models import Catalog, Brand, Product, Cart, Review, Color


def home(request):
    catalog = Catalog.objects.all()
    brands = Brand.objects.all()
    if request.method == "GET":
        ## Category ##
        item_type = request.GET.get("category")
        if item_type and item_type != "All Products":
            catalog_filtered = Catalog.objects.get(title=item_type)
            products = Product.objects.filter(catalog=catalog_filtered)
        else:
            products = Product.objects.all()
        ## Sorting ##
        selected_sort = request.GET.get("sort")
        if selected_sort:
            if selected_sort == "Highest Price":
                products = Product.objects.all().order_by('-price')
            elif selected_sort == "Lowest Price":
                products = Product.objects.all().order_by('price')
            elif selected_sort == "Best Rating":
                products = Product.review_set.order_by("-rating")
            elif selected_sort == "Default":
                products = Product.objects.all()    
        ## Brand ##
        brand_type = request.GET.get("brand")
        if brand_type:    
            brand = Brand.objects.get(brand=brand_type)
            products = Product.objects.filter(brand=brand)
    page = request.GET.get("page")
    paginator = Paginator(products, 8)
    page_obj = paginator.get_page(page)
    end_range = min(page_obj.number + 2, page_obj.paginator.count)
    context = {
        "catalog": catalog,
        "brands": brands,
        "products": page_obj,
        "end_range": end_range,
    }
    return render(request, "index.html", context)


def page(request, page=1):
    catalog = Catalog.objects.all()
    brands = Brand.objects.all()
    if request.method == "GET":
        ## Category ##
        item_type = request.GET.get("category")
        if item_type and item_type != "All Products":
            catalog_filtered = Catalog.objects.get(title=item_type)
            products = Product.objects.filter(catalog=catalog_filtered)
        else:
            products = Product.objects.all()
        ## Sorting ##
        selected_sort = request.GET.get("sort")
        if selected_sort:
            if selected_sort == "Highest Price":
                products = Product.objects.all().order_by('-price')
            elif selected_sort == "Lowest Price":
                products = Product.objects.all().order_by('price')
            elif selected_sort == "Best Rating":
                products = Product.review_set.order_by("-rating")
            elif selected_sort == "Default":
                products = Product.objects.all()
        ## Brand ##
        brand_type = request.GET.get("brand")
        if brand_type:    
            brand = Brand.objects.get(brand=brand_type)
            products = Product.objects.filter(brand=brand)
    paginator = Paginator(products, 8)
    page_obj = paginator.get_page(page)
    end_range = min(page_obj.number + 2, page_obj.paginator.count)

    context = {
        "catalog": catalog,
        "brands": brands,
        "products": page_obj,
        "end_range": end_range,
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


def add_product_page(request):
    if request.user.is_superuser:
        brands = Brand.objects.all()
        catalogs = Catalog.objects.all()
        colors = Color.objects.all()
        
        context = {
            'brands': brands,
            'catalogs': catalogs,
            'colors': colors,
        }
    else: 
        return redirect("home")

    return render(request, "add_product.html", context)

def add_product(request):
    if request.method == "POST":
        title = request.POST['title']
        brand_title = request.POST['brand']
        color_title = request.POST['color']
        catalog_title = request.POST['catalog']
        brand = Brand.objects.get(brand=brand_title)
        color = Color.objects.get(name=color_title)
        catalog = Catalog.objects.get(title=catalog_title)
        price = request.POST['price']
        images = request.FILES
        image_list  = images.getlist('images')
        image = image_list[0]
        image2 = image_list[1]
        image3 = image_list[2]
        image4 = image_list[3]

        product_instance = Product(title=title,
                                   brand=brand,
                                   catalog=catalog,
                                   color=color,
                                   price=price,
                                   image=image,
                                   image2=image2,
                                   image3=image3,
                                   image4=image4
                                   )
        product_instance.save()
    
 
    return redirect("home")

def add_cart(request, pk):
    if request.method == "POST":
        product = Product.objects.get(id=pk)
        cart_products = Cart.product.get_queryset()
        quantity=request.POST["quantity"]
       
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
    

    
@login_required(login_url="auth")
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


def logout_user(request):
    logout(request)
    return redirect("home")
