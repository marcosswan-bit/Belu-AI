import openai
import base64
from pathlib import Path


def generate_image(prompt: str, size: str = "1024x1024") -> bytes:
    """
    Generate an image using OpenAI's DALL-E API.
    
    Args:
        prompt: Description of the image to generate
        size: Image size (256x256, 512x512, or 1024x1024)
    
    Returns:
        Image bytes
    """
    client = openai.OpenAI()
    
    response = client.images.generate(
        model="dall-e-3",
        prompt=prompt,
        size=size,
        quality="standard",
        n=1
    )
    
    image_url = response.data[0].url
    image_response = client.with_options(default_headers={"User-Agent": "Belu-AI"}).beta.raw(
        method="GET",
        url=image_url
    )
    
    return image_response.content


def save_image(image_data: bytes, filename: str) -> str:
    """
    Save image data to a file.
    
    Args:
        image_data: Image bytes
        filename: Output filename
    
    Returns:
        Path to saved file
    """
    output_path = Path(filename)
    output_path.write_bytes(image_data)
    return str(output_path)


def encode_image_to_base64(image_path: str) -> str:
    """
    Encode an image file to base64.
    
    Args:
        image_path: Path to image file
    
    Returns:
        Base64 encoded image string
    """
    with open(image_path, "rb") as image_file:
        return base64.standard_b64encode(image_file.read()).decode("utf-8")


def analyze_image(image_path: str, prompt: str) -> str:
    """
    Analyze an image using OpenAI's GPT-4 Vision API.
    
    Args:
        image_path: Path to image file
        prompt: Question or prompt about the image
    
    Returns:
        Analysis result
    """
    client = openai.OpenAI()
    
    image_data = encode_image_to_base64(image_path)
    image_extension = Path(image_path).suffix.lower()
    
    media_type_map = {
        ".jpg": "image/jpeg",
        ".jpeg": "image/jpeg",
        ".png": "image/png",
        ".gif": "image/gif",
        ".webp": "image/webp"
    }
    media_type = media_type_map.get(image_extension, "image/jpeg")
    
    message = client.chat.completions.create(
        model="gpt-4-vision-preview",
        messages=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": f"data:{media_type};base64,{image_data}",
                        },
                    },
                    {
                        "type": "text",
                        "text": prompt
                    }
                ],
            }
        ],
        max_tokens=1024,
    )
    
    return message.choices[0].message.content
