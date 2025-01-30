import logging
import os
from fastapi import Request
from fastapi.responses import JSONResponse
from fastapi import  Request,HTTPException 

import traceback


def setup_logger(
    logger_name="app",
    log_folder="storage/logs",
    log_file="app.log",
    log_level=logging.DEBUG,
):
    """
    Sets up a logger with both file and console handlers.

    Args:
        logger_name (str): The name of the logger.
        log_folder (str): The folder where the log file will be stored.
        log_file (str): The name of the log file.
        log_level (int): The logging level (e.g., logging.DEBUG, logging.INFO).

    Returns:
        logging.Logger: Configured logger instance.
    """
    # Create a logger
    logger = logging.getLogger(logger_name)
    logger.setLevel(log_level)

    # Ensure the storage folder exists
    os.makedirs(log_folder, exist_ok=True)
    log_file_path = os.path.join(log_folder, log_file)

    # Create a file handler and set the level
    file_handler = logging.FileHandler(log_file_path)
    file_handler.setLevel(log_level)

    # Create a console handler and set the level
    console_handler = logging.StreamHandler()
    console_handler.setLevel(log_level)

    # Create a formatter
    formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )
    file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)

    # Add handlers to the logger
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger

error_logger=setup_logger(logger_name="error",log_file="error.log")
async def log_errors(request:Request, call_next):
    """
    Middleware to log syntax errors and request data for unhandled exceptions.
    """
    try:
        response = await call_next(request)
        return response
    except HTTPException as http_ex:
        # Log HTTP Exceptions separately
        error_logger.error(
            f"HTTPException: {http_ex.detail}\n"
            f"Path: {request.url.path}\n"
            f"Method: {request.method}\n"
            f"Headers: {dict(request.headers)}"
        )
        raise
    except Exception as ex:
        # Capture and log full stack trace for unhandled exceptions
        error_logger.error(
            f"Unhandled Exception:\n"
            f"Path: {request.url.path}\n"
            f"Method: {request.method}\n"
            f"Headers: {dict(request.headers)}\n"
            f"Body: {await request.body()}\n"
            f"Error: {str(ex)}\n"
            f"Traceback:\n{traceback.format_exc()}"
        )
        return JSONResponse(
            status_code=500,
            content={"message": "An internal server error occurred."},
        )