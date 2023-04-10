import openai
import requests
import os

from io import BytesIO
from PIL import Image

openai.api_key = os.environ.get("OPENAI_API_KEY")

def get_image(prompt, size_x:int = 256, size_y:int = 256):

    response = openai.Image.create(
        prompt=prompt,
        n=1,
        size=f"{size_x}x{size_y}"
    )
    return response['data'][0]['url']
