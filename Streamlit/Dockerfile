FROM python:3.8

COPY requirements.txt ./requirements.txt
RUN pip install -r requirements.txt

COPY app.py ./app.py

EXPOSE 8501

CMD ["streamlit", "run", "app.py"]