from django.shortcuts import render

def index(request):
    context = {
        'title': 'Store',
    }
    return render(request, 'products/index.html', context)


def products(request):
    context = {
        'title': 'Store - каталог',
        'products': [
            {
            'image': '/static/vendor/img/products/Adidas-hoodie.png',
            'name': 'Худи черного цвета с монограммами adidas Originals',
            'price': 6090,
            'description': 'Мягкая ткань для свитшотов. Стиль и комфорт – это образ жизни.'
            },
            {
            'image': '/static/vendor/img/products/Adidas-hoodie.png',
            'name': 'Худи черного цвета с монограммами adidas Originals',
            'price': 6090,
            'description': 'Мягкая ткань для свитшотов. Стиль и комфорт – это образ жизни.'
            },
            {
            'image': '/static/vendor/img/products/Adidas-hoodie.png',
            'name': 'Худи черного цвета с монограммами adidas Originals',
            'price': 6090,
            'description': 'Мягкая ткань для свитшотов. Стиль и комфорт – это образ жизни.'
            },
        ]
    }
    return render(request, 'products/products.html', context)