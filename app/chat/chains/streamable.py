from queue import Queue
from flask import current_app
from threading import Thread
from app.chat.callbacks.stream import StreamingHandler


class StreamableChain:
    def stream(self, input):
        queue = Queue()
        handler = StreamingHandler(queue)

        def task(app_context):
            app_context.push()
            self(input, callbacks=[handler])

        # execute the chain in a separate thread
        Thread(target=task, args=[current_app.app_context()]).start()

        while True:
            token = queue.get()
            if token is None:
                break

            yield token
