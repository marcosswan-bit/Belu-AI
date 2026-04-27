from image_generator import generate_image, save_image, analyze_image


def main():
    """Main function to run the AI image creation app."""
    
    print("🎨 Welcome to Belu-AI - Image Generation App")
    print("=" * 50)
    
    # Example 1: Generate an image description
    print("\n1. Generating image from prompt...")
    prompt = "A futuristic city with neon lights and flying cars at night"
    print(f"Prompt: {prompt}")
    
    try:
        image_data = generate_image(prompt)
        filename = save_image(image_data, "generated_image.png")
        print(f"✓ Image saved to: {filename}")
    except Exception as e:
        print(f"Error generating image: {e}")
    
    # Example 2: Analyze an existing image
    print("\n2. Analyzing image...")
    try:
        analysis = analyze_image(
            "generated_image.png",
            "Describe what you see in this image in detail."
        )
        print(f"Analysis: {analysis}")
    except Exception as e:
        print(f"Error analyzing image: {e}")
    
    print("\n" + "=" * 50)
    print("✓ Belu-AI image generation complete!")


if __name__ == "__main__":
    main()
