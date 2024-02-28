from __future__ import print_function

import dataclasses
import datetime
import json
import logging
import sys
import threading
import traceback
from time import sleep

import certifi
import urllib3

from ._queue import FullError, Queue

logger = logging.getLogger(__name__)


def _json_serializer(obj):
    if isinstance(obj, (datetime.datetime, datetime.date)):
        return obj.isoformat()
    raise TypeError(f"Type {type(obj)} is not serializable")


def _make_pool():
    opts = {"num_pools": 2, "cert_reqs": "CERT_REQUIRED", "ca_certs": certifi.where()}

    return urllib3.PoolManager(**opts)


_SHUTDOWN = object()
_retry = urllib3.Retry()


def send_event(pool, event, store_api_url):
    event_d = dataclasses.asdict(event)
    # Filter out private properties
    event_d = {k: v for k, v in event_d.items() if not k.startswith("_")}

    response = pool.request(
        "POST",
        store_api_url,
        body=json.dumps(event_d, default=_json_serializer).encode("utf-8"),
        headers={
            "Content-Type": "application/json",
        },
    )
    try:
        if response.status == 429:
            retry_timeout = _retry.get_retry_after(response)

            if retry_timeout is not None:
                return datetime.datetime.utcnow() + datetime.timedelta(seconds=retry_timeout)
    finally:
        response.close()


def spawn_thread(transport):
    def thread():
        disabled_until = None

        # copy to local var in case transport._queue is set to None
        queue = transport.queue

        while 1:
            item = queue.get()
            if item is _SHUTDOWN:
                queue.task_done()
                break

            if disabled_until is not None:
                if datetime.datetime.utcnow() < disabled_until:
                    queue.task_done()
                    continue
                disabled_until = None

            try:
                disabled_until = send_event(transport.pool, item, transport.api_uri)
            except Exception:
                print("Could not send approck event", file=sys.stderr)
                print(traceback.format_exc(), file=sys.stderr)
            finally:
                queue.task_done()
            sleep(0)

    t = threading.Thread(target=thread, daemon=True)
    t.start()


class Transport:
    def __init__(self, api_uri):
        self.api_uri = api_uri
        self.queue = None
        self.pool = _make_pool()

    def start(self):
        if self.queue is None:
            self.queue = Queue(30)
            spawn_thread(self)

    def capture_event(self, event):
        if self.queue is None:
            raise RuntimeError("Transport shut down")
        try:
            self.queue.put_nowait(event)
        except FullError:
            pass

    def close(self):
        if self.queue is not None:
            try:
                self.queue.put_nowait(_SHUTDOWN)
            except FullError:
                pass
            self.queue = None

    def drain_events(self, timeout):
        q = self.queue
        if q is not None:
            with q.all_tasks_done:
                while q.unfinished_tasks:
                    q.all_tasks_done.wait(timeout)

    def __del__(self):
        self.close()
