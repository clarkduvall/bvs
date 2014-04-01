from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

@login_required
def home(request, channel='main'):
    return render(request, 'index.html', {
        'PUSHER_KEY': settings.PUSHER_KEY,
        'channel': channel,
        'username': request.user.username
    })
