from django.shortcuts import render, HttpResponse
from core.models import Subscription, Order
from django.views.decorators.csrf import csrf_exempt


def index(request):
    
    subscriptions = Subscription.get_table()

    return render(request, 'panel/subscriptions/index.html', {
        'subscriptions': subscriptions
    })


@csrf_exempt
def change_status(request):
    if request.POST:
        subscription = Subscription.objects.get(pk=request.POST.get('id'))
        subscription.status = request.POST.get('status')
        subscription.save()
    return HttpResponse()
