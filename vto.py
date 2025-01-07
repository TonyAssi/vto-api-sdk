import requests
import base64
import time

class VirtualTryOnAPI:
    def __init__(self, api_key, base_url="https://vto.face-swap.co"):
        self.api_key = api_key
        self.base_url = base_url

    def encode_image(self, image_path):
        """Convert an image to base64."""
        with open(image_path, "rb") as image_file:
            return f"data:image/jpg;base64,{base64.b64encode(image_file.read()).decode('utf-8')}"

    def run_generation(self, model_image_path, garment_image_path, category="one-pieces"):
        """Run the virtual try-on prediction."""
        model_image_base64 = self.encode_image(model_image_path)
        garment_image_base64 = self.encode_image(garment_image_path)

        response = requests.post(
            f"{self.base_url}/run",
            headers={
                "Authorization": f"Bearer {self.api_key}",
                "Content-Type": "application/json"
            },
            json={
                "model_image": model_image_base64,
                "garment_image": garment_image_base64,
                "category": category,
            },
        )

        if response.status_code == 200:
            data = response.json()
            return data.get("id")
        else:
            raise Exception(f"Error: {response.status_code}, {response.text}")

    def get_status(self, prediction_id):
        response = requests.get(
            f"{self.base_url}/status/{prediction_id}",
            headers={
                "Authorization": f"Bearer {self.api_key}"
            }
        )

        if response.status_code == 200:
            status_data = response.json()
            return status_data
        else:
            raise Exception(f"Error: {response.status_code}, {response.text}")


    def generate(self, model_image_path, garment_image_path, category="one-pieces"):
        generation_id = self.run_generation(model_image_path,garment_image_path,category)

        """Wait for image to finish generating"""
        while True:
            response = requests.get(
                f"{self.base_url}/status/{generation_id }",
                headers={
                    "Authorization": f"Bearer {self.api_key}"
                }
            )

            if response.status_code == 200:
                status_data = response.json()

                if status_data.get("status") == "completed":
                    return status_data['output'][0]
                elif status_data.get("status") == "failed":
                    raise Exception(f"Prediction Failed: {status_data.get('error')}")
            else:
                raise Exception(f"Error: {response.status_code}, {response.text}")

            time.sleep(2)  # Wait 2 seconds before polling again
