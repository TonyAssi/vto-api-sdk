# Virtual Try-On API Python SDK
Virtual Try-On API with 3 line of Python code.

<img width="894" alt="vto" src="https://github.com/user-attachments/assets/49118950-e1e0-4c71-8bd6-f454d8fc476c" />

Try out the Web Demo: [![Hugging Face Spaces](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Spaces-blue)](https://huggingface.co/spaces/tonyassi/Virtual-Try-On-Pro)

## Download
**(Option 1)** Download the [.zip file](https://github.com/TonyAssi/vto-api-sdk/archive/refs/heads/main.zip)

**(Option 2)** Use this in the command line
```
git clone https://github.com/TonyAssi/vto-api-sdk.git
```

## Installation
```bash
pip install -r requirements.txt
```

## Quick Start
```python
from vto import VirtualTryOnAPI

vto = VirtualTryOnAPI(api_key="YOUR API KEY")
result = vto.generate(model_image_path="img/kim.jpg", garment_image_path="img/red.jpg", category="one-pieces")
print(result)
```

## Usage
Import
```python
from vto import VirtualTryOnAPI
```

Initialize the SDK
```python
vto = VirtualTryOnAPI(api_key="YOUR_API_KEY")
```

### Synchronous Generation
The synchronous generation will return the final image to you but you'll need to wait for it to finish (~20 seconds) before the code moves on.
```python
result = vto.generate(model_image_path="img/kim.jpg", garment_image_path="img/red.jpg", category="one-pieces")
print(result)
```

### Aynchronous Generation
In aynchronous generation you first start the generation and then it will return the generation_id.
```python
generation_id = vto.run_generation(model_image_path="img/kim.jpg", garment_image_path="img/black.jpg", category="one-pieces")
print(generation_id)
```
Then you need to check the status of the generation with the generation_id.
```python
result = vto.get_status(generation_id)
print(result)
```
The response will be "processing" while it's working. When it's done it'll say "completed" and provide the final image.
