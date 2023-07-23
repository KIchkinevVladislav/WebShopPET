from products.models import Basket


def baskets(request):
    """
    Контекстный процессор
    Добавляем в контекс шаблона доступ к объектам Baskets
    """
    user = request.user
    return {'baskets': Basket.objects.filter(user=user) if user.is_authenticated else []}
