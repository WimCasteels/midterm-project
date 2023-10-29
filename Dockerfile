FROM python:3.9.18-slim



RUN pip install scikit-learn==1.3.0 Flask gunicorn

WORKDIR /app
COPY ["predict.py","model_depth=4_samples=200.bin", "./"]



EXPOSE 9696

ENTRYPOINT ["gunicorn", "--bind=0.0.0.0:9696", "predict:app"]