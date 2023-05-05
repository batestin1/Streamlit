#!/bin/bash


if [ -d "pip" ]; then
    pip install -q -r pip/*.txt
fi

while true
do
    STREAMLIT_DEBUG=1 streamlit run script/main.py
    sleep 2
done

