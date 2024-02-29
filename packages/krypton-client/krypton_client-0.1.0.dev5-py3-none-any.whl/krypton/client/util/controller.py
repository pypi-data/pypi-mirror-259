from krypton.lib.model.exchange import StreamSubscription
from krypton.client.exchange import StreamExchangeClient
from krypton.client.worker import Worker

class Controller:

    def __init__(self, streamsubs: list[StreamSubscription]|None = None):
        self.streamsubs: set[StreamSubscription] = set()
        self.sclients: dict[StreamSubscription, StreamExchangeClient] = {}
        self.workers: dict[StreamSubscription, list[Worker]] = {}
        for stream in streams or []:
            self.add_stream(stream)

    def add_stream(self, stream: Stream) -> Stream:
        if stream not in self.streams:
            self.streams.add(stream)
        return stream

    def remove_stream(self, stream: Stream) -> Stream|None:
        if stream not in self.streams:
            return None
        self.remove_rclient(stream)
        self.remove_sclient(stream)
        self.remove_workers(stream)
        self.streams.remove(stream)
        return stream

    def add_rclient(
            self,
            stream: Stream,
            rclient: RequestClient,
    ) -> RequestClient:
        if stream not in self.streams:
            raise KeyError
        if existing := self.rclients.get(stream):
            return existing
        self.rclients[stream] = rclient
        return rclient

    def remove_rclient(self, stream: Stream) -> RequestClient|None:
        return self.rclients.pop(stream)

    def add_sclient(
            self,
            stream: Stream,
            sclient: StreamClient,
    ) -> StreamClient:
        if stream not in self.streams:
            raise KeyError
        if existing := self.sclients.get(stream):
            return existing
        self.sclients[stream] = sclient
        return sclient

    def remove_sclient(self, stream: Stream) -> StreamClient|None:
        if sclient := self.sclients.pop(stream):
            sclient.end()
        return sclient

    def add_worker(self, stream: Stream, worker: Worker) -> Worker:
        self.workers.setdefault(stream, []).append(worker)
        return worker

    def remove_workers(self, stream: Stream) -> list[Worker]|None:
        if workers := self.workers.pop(stream):
            for worker in workers:
                worker.end()
            return workers
        return None

    def start_stream(self, stream: Stream|None = None):
        if stream and stream not in self.streams:
            raise KeyError
        for stream in [stream] if stream else self.streams:
            if sclient := self.sclients.get(stream):
                sclient.start()
            if workers := self.workers.get(stream):
                for worker in workers:
                    worker.start()

    def end_stream(self, stream: Stream|None = None):
        if stream and stream not in self.streams:
            raise KeyError
        for stream in [stream] if stream else self.streams:
            if sclient := self.sclients.get(stream):
                sclient.end()
            if workers := self.workers.get(stream):
                for worker in workers:
                    worker.end()
