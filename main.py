from fastapi import FastAPI
import logging
import sys

app = FastAPI()


@app.get("/")
async def main():
    return "Hello World, this is server."


@app.get("/exception/severe")
async def severe():
    logger.error("This is a Severe Exception")
    return "This is a Severe Exception"


@app.get("/exception/ignore")
async def ignore():
    logger.info("This is an neglectable exception.")
    return "This is an neglectable exception."


logger = logging.getLogger(__name__)
formatter = logging.Formatter(
    fmt="%(asctime)s loglevel=%(levelname)-6s %(funcName)s() L%(lineno)-4d %(message)s"
)
stream_handler = logging.StreamHandler(sys.stdout)
stream_handler.setFormatter(formatter)
logger.handlers = [stream_handler]
logger.setLevel(getattr(logging, "INFO", logging.INFO))
