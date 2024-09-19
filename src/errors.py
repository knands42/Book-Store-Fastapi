from fastapi import FastAPI
from fastapi.responses import JSONResponse

def register_all_errors(app: FastAPI):

    @app.exception_handler(500)
    async def internal_server_error_handler(request, exc):

        return JSONResponse(

            content={
                "message": "Oops! Something went wrong",
                "error_code": "server_error"
            }
        )
