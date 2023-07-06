FROM python:3.10-slim
WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
EXPOSE 4000
EXPOSE 8501

CMD flask run --host=0.0.0.0 --port=4000 ; streamlit run Cadastrar.py