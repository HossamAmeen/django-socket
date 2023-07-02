# notification_app/views.py

from rest_framework.decorators import api_view
from rest_framework.response import Response
from notification_app.consumers import NotificationConsumer
from django.shortcuts import render
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync

@api_view(['POST'])
def send_notification(request):
    message = request.data.get('message')
    if message:
        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.group_send)(
            'notifications_group',  # Group name to broadcast the message to
            {
                'type': 'notification.message',
                'message': message,
                "user_id": 1
            }
        )
        
        import json 
        m = json.dumps(message)
        print(type(m))

        return Response({'success': True})
    return Response({'success': False, 'message': 'No message provided.'})


def notification_view(request):
    return render(request, 'notification_app/notification.html')
