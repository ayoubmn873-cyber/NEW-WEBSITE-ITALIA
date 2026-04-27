"""
Google Imagen 3 — Recipe Image Generator
Generates 2 images per recipe and saves them to the article folders.

Install: pip install google-genai
Run:     python generate_images.py
"""

from google import genai
from google.genai import types
from pathlib import Path

API_KEY = "AIzaSyA5VeamagdX1IuZUxTrpTWS6dO4SYQYWVM"

client = genai.Client(api_key=API_KEY)

RECIPES = [
    {
        "folder": "article-1-shrimp-pasta",
        "images": [
            (
                "image-1.jpg",
                "Shot on iPhone 15 Pro Max, zoomed in close, one single shot — "
                "a massive plate of creamy garlic butter shrimp pasta, perfectly cooked "
                "jumbo shrimp glistening with butter, fresh parsley sprinkled generously on top, "
                "parmesan shavings melting into the rich cream sauce, sitting on parchment paper "
                "on a rustic wooden kitchen counter, warm cozy natural light, steam still rising, "
                "ultra detailed, mouth-watering, real food photography style, vertical 3:4"
            ),
            (
                "image-2.jpg",
                "Shot on iPhone 15 Pro Max, zoomed in close, one single shot — "
                "a fork twirling creamy garlic butter shrimp pasta, one juicy shrimp draped on top "
                "dripping with golden butter sauce, fresh basil leaves scattered around, "
                "rustic wooden table, soft warm bokeh background, cozy kitchen lighting, "
                "ultra detailed, mouth-watering, real food photography style, vertical 3:4"
            ),
        ],
    },
    {
        "folder": "article-2-lava-cake",
        "images": [
            (
                "image-1.jpg",
                "Shot on iPhone 15 Pro Max, zoomed in close, one single shot — "
                "a perfect chocolate lava cake just cut open with a spoon, warm dark chocolate "
                "flowing out dramatically like lava, dusted with powdered sugar, sitting on a dark "
                "slate plate on a rustic wooden kitchen counter, warm cozy candlelight, "
                "steam still rising, vanilla ice cream melting on the side, ultra detailed, "
                "mouth-watering, real food photography style, vertical 3:4"
            ),
            (
                "image-2.jpg",
                "Shot on iPhone 15 Pro Max, zoomed in close, one single shot — "
                "individual chocolate lava cake in a ceramic ramekin, rich chocolate sauce "
                "drizzled over the top, fresh raspberries and a mint leaf garnish, dark moody "
                "background, rustic wooden table, warm golden backlight, steam still rising, "
                "ultra detailed, mouth-watering, real food photography style, vertical 3:4"
            ),
        ],
    },
]


def generate_image(prompt: str, output_path: Path) -> bool:
    print(f"  Generating: {output_path.name} ...")
    try:
        response = client.models.generate_images(
            model="imagen-4.0-generate-001",
            prompt=prompt,
            config=types.GenerateImagesConfig(
                number_of_images=1,
                aspect_ratio="3:4",
                output_mime_type="image/jpeg",
            ),
        )
        image_bytes = response.generated_images[0].image.image_bytes
        output_path.write_bytes(image_bytes)
        print(f"  Saved: {output_path}")
        return True
    except Exception as e:
        print(f"  ERROR: {e}")
        return False


def main():
    print("=" * 55)
    print("  Google Imagen 3 — Recipe Image Generator")
    print("=" * 55)

    base = Path(__file__).parent

    for recipe in RECIPES:
        folder = base / recipe["folder"]
        folder.mkdir(parents=True, exist_ok=True)
        print(f"\nRecipe folder: {folder.name}")

        for filename, prompt in recipe["images"]:
            out = folder / filename
            if out.exists():
                print(f"  Skip (already exists): {filename}")
                continue
            generate_image(prompt, out)

    print("\nDone! All images generated.")


if __name__ == "__main__":
    main()
