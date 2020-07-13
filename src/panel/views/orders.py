from django.shortcuts import render
from core.models import Order, Product

def index(request):
    orders = Order.objects.all().order_by('-id')
    products = [{'id': str(product.id), 'name': product.name}
        for product in Product.objects.all()]
    statuses = [{'id': '1', 'name': 'Aguardando pagamento'},
        {'id': '3', 'name': 'Aprovado'}]
    dias = [{'id': '-1', 'name': 'dia não escolhido'},
        {'id': '04', 'name': '04'}, {'id': '05', 'name': '05'},
        {'id': '06', 'name': '06'}]

    _filter = {}
    for key in request.GET:
        if request.GET[key]:
            _filter[key] = request.GET[key]

    if 'product' in request.GET:
        if request.GET['product']:
            orders = orders.filter(product_id=int(request.GET['product']))

    if 'dia' in request.GET:
        if request.GET['dia']:
            if request.GET['dia'] == '-1':
                orders = orders.filter(data_desejada__isnull=True)
            else:
                orders = orders.filter(data_desejada=request.GET['dia'])

    if 'status' in request.GET:
        if request.GET['status'] == '3':
            orders = orders.filter(status__in=[3, 4])
        else:
            if request.GET['status']:
                orders = orders.filter(status=int(request.GET['status']))

    return render(request, 'panel/orders/index.html', {
        'orders': orders,
        'total': len(orders),
        'products': products,
        'statuses': statuses,
        'dias': dias,
        'filter': _filter
    })


def order(request, order_id):
    order = Order.objects.get(pk=order_id)
    return render(request, 'panel/orders/order.html', {
        'order': order
    })
