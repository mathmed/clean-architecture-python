#!/bin/bash
cd /home/api && PYTHONDONTWRITEBYTECODE=1 && pip install -r requirements.txt && python3 main.py