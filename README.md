# Pipeline Launchpad

Pipeline Launchpad is a small self-service platform. A data engineer submits a pipeline spec, and the platform returns a standard starter: an Airflow DAG, a dbt project, a Terraform snippet, and CI. This repository is the capstone that builds that platform.

Week 1, Part A runs only the API and an empty Postgres database on your machine. The health check proves the API process is up. It does not talk to the database yet.

## Run locally

From the repository root, with Docker running:

```bash
docker compose up --build
```

Then open [http://localhost:8000/health](http://localhost:8000/health). The response is:

```json
{"status": "ok"}
```

Stop it with `Ctrl+C`, then `docker compose down`.

The Postgres password in `docker-compose.yml` is for this local database only. It is not an AWS or production secret.

## CI

Every push and pull request runs lint, tests, and a Docker image build on GitHub Actions. That check does not deploy anything and does not use AWS credentials.

## Tests

```bash
cd platform
uv sync --group dev
uv run ruff check .
uv run ruff format --check .
uv run pytest
```
