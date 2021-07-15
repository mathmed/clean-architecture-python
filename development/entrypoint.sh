#!/bin/bash
cd /home/api \
&& PYTHONDONTWRITEBYTECODE=1 \
&& pip install -r requirements.txt && \ 
export FLASK_APP=main.py && \
export FLASK_ENV=development && \
flask run --host=0.0.0.0