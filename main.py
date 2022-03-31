import urllib.request
from fastapi import FastAPI, HTTPException
from PIL import Image
from fastapi.responses import Response
import io
import logging
logging.basicConfig(level=logging.ERROR)
app = FastAPI()


@app.get("/resize/")
def resize(url: str, height: int, width: int):
    if url is None or height is None or width is None:
        raise HTTPException(status_code=404, detail="parameters are missing!")

    try:
        file_bytes = urllib.request.urlopen(url)
        image = Image.open(io.BytesIO(file_bytes.read()))
        resize_image = image.resize((height, width))
        bytes_image = io.BytesIO()
        resize_image.save(bytes_image, format='PNG')
        return Response(content=bytes_image.getvalue(), media_type="image/png")
    except Exception as e:
        logging.error(e)
        # fallback image
        image = Image.open('fallback.png')
        bytes_image = io.BytesIO()
        image.save(bytes_image, format='PNG')
        return Response(content=bytes_image.getvalue(), media_type="image/png")
