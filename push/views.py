import json

from django.http import HttpResponse
from django.views.decorators.http import require_POST

import pusher


p = pusher.pusher_from_url()


def json_response(data):
    return HttpResponse(json.dumps(data), content_type='application/json')


@require_POST
def auth(request):
    channel = request.POST.get('channel_name')
    socket_id = request.POST.get('socket_id')

    auth = p[channel].authenticate(socket_id)
    return json_response(auth)


@require_POST
def message(request, channel):
    message = request.POST.get('message')

    p['private-%s' % channel].trigger('message', {
        'message': message,
        'strength': 0.1
    })

    return json_response({'success': True})
