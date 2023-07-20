from products.models import Basket


def baskets(request):
    # контекстный процессор для отбражения содержания корзины в baskets.html
    user = request.user
    return {'baskets': Basket.objects.filter(user=user) if user.is_authenticated else []}
