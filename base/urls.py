from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("page/<int:page>", views.page, name="home"),
    path("product/<int:pk>", views.product, name="product"),
    path("about", views.about, name="about"),
    path("contact", views.contact, name="contact"),
    path("faq", views.faq, name="faq"),
    path("cart", views.cart, name="cart"),
    path("add_cart/<int:pk>", views.add_cart, name="add_cart"),
    path("update_cart/<int:pk>", views.update_cart, name="update_cart"),
    path("add_review/<int:pk>", views.add_review, name="add_review"),
    path("personal-info", views.personal_info, name="personal-info"),
    path("payment-choose", views.payment_choose, name="payment-choose"),
    path("address", views.address, name="address"),
    path("address-edit", views.address_edit, name="address-edit"),
    path("auth", views.auth, name="auth"),
    path("register", views.register_user, name="register"),
    path("login", views.login_user, name="login"),
]

