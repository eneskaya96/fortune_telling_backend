#!/bin/bash

celery -A src.worker beat -l INFO