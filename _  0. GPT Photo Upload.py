# Photo Upload for ChatGPT's API
# Thomas Messerschmidt


import base64
import requests

# OpenAI API Key
api_key = "YOUR_OPENAI_API_KEY"

# Function to encode the image
def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')

# Path to your image
image_path = "path_to_your_image.jpg"

# Getting the base64 string
base64_image = encode_image(image_path)

headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {api_key}"
}

payload = {
    "model": "gpt-4-vision-preview",
    "messages": [
      {
        "role": "user",
        "content": [
          {
            "type": "text",
            "text": "What’s in this image?"
          },
          {
            "type": "image_url",
            "image_url": {
              "url": f"data:image/jpeg;base64,{base64_image}"
            }
          }
        ]
      }
    ],
    "max_tokens": 300
}

response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=payload)

print(response.json())

#``````````````````````````````
# convert jpg to base64
# convert jpg to base64
# convert jpg to base64

import base64

def convert_image_to_base64(image_path):
    """
    Converts an image to Base64 encoding and saves it to a file.

    Args:
        image_path (str): Path to the image file (JPEG format).

    Returns:
        str: Base64 encoded image as a UTF-8 string.
    """
    with open(image_path, "rb") as img_file:
        base64_string = base64.b64encode(img_file.read()).decode("utf-8")

    # Save the Base64 string to a text file
    with open("base64_image.txt", "w") as output_file:
        output_file.write(base64_string)

    return base64_string

# Example usage:
#image_path = "path/to/your/image.jpg"  # Replace with the actual path to your JPEG image
#base64_encoded_image = convert_image_to_base64(image_path)
#print(f"Base64 image saved to base64_image.txt")
