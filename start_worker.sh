#!/bin/bash

celery --app=src.worker worker --queues fortune:beat_queue,fortune:create_fortune_queue -l INFO --without-heartbeat --without-gossip --without-mingle