# # notification_app/consumers.py

# from channels.generic.websocket import AsyncWebsocketConsumer
# from asgiref.sync import async_to_sync
# import json
# import channels.layers


# class NotificationConsumer(AsyncWebsocketConsumer):
#     async def connect(self):
#         self.group_name = 'notifications'
#         await self.channel_layer.group_add(self.group_name, self.channel_name)
#         await self.accept()

#     async def disconnect(self, close_code):
#         await self.channel_layer.group_discard(self.group_name, self.channel_name)

#     async def receive(self, text_data):
#         text_data_json = json.loads(text_data)
#         message = text_data_json['message']
#         await self.send(text_data=json.dumps({'message': message}))

#     @staticmethod
#     def send_notification(message):
#         print("tst252"*20)
#         group_name = 'notifications'
#         channel_layer = channels.layers.get_channel_layer()
#         async_to_sync(channel_layer.group_send)(
#             group_name,
#             {
#                 'type': 'send_notification',
#                 'message': message
#             }
#         )

#     async def send_notification(self, event):
#         print("asd"*20)
#         message = event['message']
#         await self.send(text_data=json.dumps({'message': message}))


from channels.generic.websocket import AsyncWebsocketConsumer


class NotificationConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.channel_layer.group_add('notifications_group', self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard('notifications_group', self.channel_name)

    async def notification_message(self, event):
        message = {"test": event['message'], "user": event['user_id']}
        import json 
        await self.send(text_data=json.dumps(message))
