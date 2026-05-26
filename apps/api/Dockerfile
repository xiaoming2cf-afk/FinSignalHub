FROM python:3.12-slim

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

COPY pyproject.toml ./
COPY apps/api ./apps/api
COPY apps/mcp_server ./apps/mcp_server

RUN pip install --no-cache-dir .

EXPOSE 8000

CMD ["uvicorn", "finsignalhub_api.main:app", "--host", "0.0.0.0", "--port", "8000"]

