from dill import dumps, loads
import os
import subprocess
import sys

from .worker import Worker

class Process:
    def __init__(self, target, args=(), kwargs={}, debug=False):
        self.target = target
        self.args = args
        self.kwargs = kwargs
        self.debug = debug

    def start(self):
        self.worker = Worker(self.debug)
        pickled = dumps((self.target, self.args, self.kwargs))
        self.worker.stdin.write(len(pickled).to_bytes(8, byteorder='big'))
        self.worker.stdin.write(pickled)
        self.worker.stdin.flush()

    def join(self):
        result = self.worker.receive()
        del self.worker
        return result

    def is_alive(self):
        return self._process.is_alive()