from fastapi import FastAPI

app = FastAPI(title="Pipeline Launchpad", version="0.1.0")


@app.get("/health")
def health() -> dict[str, str]:
    """Report that the API process is running.

    This route does not check the database. A later check can do that.
    Today it only answers whether the process is up.
    """
    return {"status": "ok"}
