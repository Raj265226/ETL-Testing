#!/bin/bash

if [ ! -d "venv" ]; then
    echo "Creating virtual environment..."
    python -m venv venv
else
    echo "Using existing virtual environment..."
fi

source venv/Scripts/activate

pip install -r requirements.txt