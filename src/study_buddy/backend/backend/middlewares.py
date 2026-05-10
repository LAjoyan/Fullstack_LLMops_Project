from fastapi import FastAPI, Request
from starlette.responses import Response
from starlette.middleware.base import RequestResponseEndpoint
import time
import mlflow


def logging_middleware(app: FastAPI):
    @app.middleware("http")
    async def mlflow_middleware(
        request: Request, call_next: RequestResponseEndpoint
    ) -> Response:
        start_time = time.perf_counter()

        with mlflow.start_run(run_name=f"{request.method} {request.url.path}"):
            response = await call_next(request)
            elapsed_time_seconds = time.perf_counter() - start_time

            mlflow.log_metric("status_code", response.status_code)
            mlflow.log_metric("latency_seconds", elapsed_time_seconds)

            mlflow.log_params(
                {
                    "endpoint": request.url.path,
                    "is_error": response.status_code >= 400,
                }
            )

            mlflow.set_tags(
                {
                    "environment": "dev", # TODO: Change to "prod" when the app is live
                    "endpoint": request.url.path,
                }
            )
        return response