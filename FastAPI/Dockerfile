FROM python:3.8

COPY requirements.txt ./requirements.txt
RUN pip install -r requirements.txt

COPY Movie_Data.csv ./Movie_Data.csv
COPY Movie_Data.py ./Movie_Data.py
COPY Movie_Clusters.py ./Movie_Clusters.py
COPY api.py ./api.py

EXPOSE 8000

CMD ["uvicorn", "api:app", "--host", "0.0.0.0", "--port", "8000"]
