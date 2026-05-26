FROM python:3.12-slim

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

COPY pyproject.toml ./
COPY apps/api ./apps/api
COPY apps/mcp_server ./apps/mcp_server

RUN pip install --no-cache-dir .

EXPOSE 8001

CMD ["uvicorn", "finsignalhub_mcp_server.main:app", "--host", "0.0.0.0", "--port", "8001"]

