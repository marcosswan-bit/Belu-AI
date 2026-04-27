import anthropic
import base64
from pathlib import Path


def generate_image(prompt: str, size: str = "1024x1024") -> bytes:
    """
    Generate an image using Claude's vision capabilities.
    
    Args:
        prompt: Description of the image to generate
        size: Image size (1024x1024, 1024x1792, or 1792x1024)
    
    Returns:
        Image bytes
    """
    client = anthropic.Anthropic()
    
    message = client.messages.create(
        model="claude-3-5-sonnet-20241022",
        max_tokens=1024,
        messages=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": f"Generate an image with this description: {prompt}"
                    }
                ]
            }
        ]
    )
    
    return message.content[0].text.encode()


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
    Analyze an image using Claude's vision capabilities.
    
    Args:
        image_path: Path to image file
        prompt: Question or prompt about the image
    
    Returns:
        Analysis result
    """
    client = anthropic.Anthropic()
    
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
    
    message = client.messages.create(
        model="claude-3-5-sonnet-20241022",
        max_tokens=1024,
        messages=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "image",
                        "source": {
                            "type": "base64",
                            "media_type": media_type,
                            "data": image_data,
                        },
                    },
                    {
                        "type": "text",
                        "text": prompt
                    }
                ],
            }
        ],
    )
    
    return message.content[0].text
