import json
from django.shortcuts import render
from core.models import Subscription


def index(request):
    shorts = Subscription.objects.filter(contest_id=4)
    for short in shorts:
        short.user_data = json.loads(short.data)

    return render(request, 'panel/shorts/index.html', {
        'shorts': shorts
    })
