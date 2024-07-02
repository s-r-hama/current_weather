
FROM python:3.9-slim

WORKDIR /app

COPY current_weather.py /app/
RUN pip install requests
RUN pip install argparse


ENTRYPOINT ["python", "current_weather.py"]

CMD ["python", "current_weather.py"]