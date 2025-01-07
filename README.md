# Virtual Try-On API Python SDK
Virtual Try-On API with 3 line of Python code.

<img width="894" alt="vto" src="https://github.com/user-attachments/assets/49118950-e1e0-4c71-8bd6-f454d8fc476c" />

Try out the Web Demo: [![Hugging Face Spaces](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Spaces-blue)](https://huggingface.co/spaces/tonyassi/Virtual-Try-On-Pro)

## Download
**(Option 1)** Download the Github repo .zip file

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
