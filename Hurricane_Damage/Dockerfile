FROM python:3.11

RUN pip install Flask==3.0
RUN pip install tensorflow==2.15
RUN pip install pillow==10.3.0

COPY api.py /api.py
COPY lenet-5-modified.keras /lenet-5-modified.keras

CMD ["python", "api.py"]