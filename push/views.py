import json

from django.http import HttpResponse
from django.views.decorators.http import require_POST

import pusher


def json_response(data):
    return HttpResponse(json.dumps(data), content_type='application/json')


@require_POST
def auth(request):
    channel = request.POST.get('channel_name')
    socket_id = request.POST.get('socket_id')

    p = pusher.pusher_from_url()

    auth = p[channel].authenticate(socket_id)
    return json_response(auth)
