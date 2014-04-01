import json

from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.views.decorators.http import require_POST

import pusher


p = pusher.pusher_from_url()


def json_response(data):
    return HttpResponse(json.dumps(data), content_type='application/json')


@login_required
@require_POST
def auth(request):
    channel = request.POST.get('channel_name')
    socket_id = request.POST.get('socket_id')

    # We could check permissions here to see if the user should have access to
    # a certain channel.

    auth = p[channel].authenticate(socket_id)
    return json_response(auth)


@login_required
@require_POST
def message(request, channel):
    progress = request.POST.get('progress')
    p['private-%s' % channel].trigger('message', {
        'username': request.user.username,
        'progress': progress
    })

    return json_response({'success': True})
