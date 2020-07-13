#!/usr/bin/env python
import os
import sys
import time
import logging
from subprocess import call
from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler

CSS_PATH = '/app/src/static/core/css'
SASS_PATH = '/app/src/static/core/scss'

CSS_PATH = './src/static/core/css'
SASS_PATH = './src/static/core/scss'

SECONDS = []

def on_event(event):
    filename = os.path.basename(event.src_path)
    second = str(int(time.time()))

    if second not in SECONDS:
        print('({} {} changed)'.format(second, filename))

        SECONDS.append(second)

        call([
            'sassc',
            '-t', 'compressed',
            '--sourcemap=auto',
            event.src_path,
            CSS_PATH + '/' + filename.replace('.scss', '.min.css')
        ])

if __name__ == "__main__":
    handler = PatternMatchingEventHandler(patterns=['*.scss'])
    handler.on_modified = on_event

    observer = Observer()
    observer.schedule(handler, SASS_PATH, recursive=True)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
