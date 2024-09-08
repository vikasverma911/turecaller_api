from channels.consumer import SyncConsumer, AsyncConsumer
from channels.exceptions import StopConsumer
from time import sleep
import asyncio


class MySyncConsumer(SyncConsumer):
  def websocket_connect(self, event):
    print('Websocket Connected...', event)
    self.send({
        'type': 'websocket.accept',
    })

  def websocket_receive(self, event):
    print('Message received from Client', event)
    print(event['text'])
    for i in range(10):
      self.send({
          'type': 'websocket.send',
          'text': str(i)
      })
      sleep(1)

  def websocket_disconnect(self, event):
    print('Websocket Disconnected...', event)
    raise StopConsumer()
