from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from _cart.cart import Cart
from .models import Category, Product
from django.shortcuts import get_object_or_404


def store(request):
    all_products = Product.objects.all()
    items_per_page = 9
    paginator = Paginator(all_products, items_per_page)
    page = request.GET.get("page")

    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)

    context = {
        "my_products": products,
    }
    return render(request, "store/store.html", context)


def categories(request):
    all_categories = Category.objects.all()
    return {"all_categories": all_categories}


def list_category(request, category_slug=None):
    category = get_object_or_404(Category, slug=category_slug)
    all_products = Product.objects.filter(category=category)
    items_per_page = 10
    paginator = Paginator(all_products, items_per_page)
    page = request.GET.get("page")

    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)

    cart = Cart(request)
    return render(
        request,
        "store/list-category.html",
        {"category": category, "products": products, "cart": cart},
    )


def product_info(request, category_slug=None, product_slug=None):
    category = get_object_or_404(Category, slug=category_slug)
    product = get_object_or_404(Product, slug=product_slug, category=category)
    product_images = product.images.all()
    context = {
        "category": category,
        "product": product,
        "product_images": product_images,
    }
    return render(request, "store/product-info.html", context)
