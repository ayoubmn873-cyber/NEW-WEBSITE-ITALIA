"""
Sapori d'Italia — Full Image Generator (NEW PROMPT STYLE)
19 total images: hero + 4 categories + 5 articles x2

Run:   python generate_all_images.py
Force: python generate_all_images.py --force   (overwrites existing)
"""

import sys
from pathlib import Path
from google import genai
from google.genai import types

API_KEY = "AIzaSyA5VeamagdX1IuZUxTrpTWS6dO4SYQYWVM"
client  = genai.Client(api_key=API_KEY)
BASE    = Path(__file__).parent
FORCE   = "--force" in sys.argv

# ══════════════════════════════════════════════════════════
#  NEW PROMPT STYLE
#  Editorial Pinterest-viral food photography:
#  overhead or 45° angle, natural window light, linen/marble
# ══════════════════════════════════════════════════════════

def hero_prompt():
    return (
        "Professional food photography wide overhead flat lay, "
        "Italian feast on a rustic aged oak farmhouse table: "
        "a steaming bowl of fresh tagliatelle al ragù bolognese, "
        "golden bruschetta with vibrant red tomatoes and green basil, "
        "elegant tiramisù in a white ceramic dish dusted with dark cocoa, "
        "a thick braised ossobuco on a terracotta plate, "
        "crusty Italian bread, olive oil bottle with herbs, scattered fresh basil, "
        "two glasses of red wine catching warm afternoon light, "
        "Mediterranean linen napkin, wooden spoon, antique silverware, "
        "soft dappled sunlight from a nearby window, cinematic warm tones, "
        "ultra detailed, ultra sharp, 16:9 horizontal"
    )

def shot1(subject: str) -> str:
    """Hero portrait shot — close, centered, beautiful"""
    return (
        f"Pinterest-viral Italian food photography, "
        f"45-degree angle close-up hero shot — {subject}, "
        f"placed on aged white Carrara marble surface, "
        f"soft natural window light casting gentle shadows, "
        f"thin wisps of steam rising, "
        f"shallow depth of field with creamy bokeh background, "
        f"fresh herb garnish, a drizzle of olive oil glistening, "
        f"ultra detailed, mouth-watering, vibrant natural colors, "
        f"professional food stylist composition, 3:4 vertical"
    )

def shot2(subject: str) -> str:
    """Action / detail shot — fork, spoon, bite, cross-section"""
    return (
        f"Dramatic Italian food editorial photography — {subject}, "
        f"rustic wooden Italian farmhouse table background, "
        f"warm golden hour side-lighting creating rich shadows, "
        f"moody atmosphere, film grain texture, "
        f"ultra sharp focus on subject with soft bokeh surroundings, "
        f"restaurant-quality plating, 3:4 vertical"
    )


IMAGES = [

    # ── HERO ────────────────────────────────────────────────────────
    {
        "path":   "hero.jpg",
        "prompt": hero_prompt(),
        "ratio":  "16:9",
    },

    # ── PASTA (Tagliatelle al Ragù) ──────────────────────────────
    {
        "path":   "pasta/image-1.jpg",
        "prompt": shot1(
            "a generous portion of fresh homemade tagliatelle al ragù bolognese, "
            "slow-cooked rich meat sauce with deep burgundy color wrapping every strand, "
            "freshly grated Parmigiano Reggiano cascading generously over the top, "
            "served in an elegant deep ceramic rustic bowl"
        ),
        "ratio":  "3:4",
    },
    {
        "path":   "pasta/image-2.jpg",
        "prompt": shot2(
            "a silver fork elegantly twirling tagliatelle bolognese, "
            "thick sauce clinging to every pasta strand, "
            "parmesan shavings melting in the steam, "
            "dark Italian trattoria background with warm candlelight bokeh"
        ),
        "ratio":  "3:4",
    },

    # ── ANTIPASTI (Bruschetta) ───────────────────────────────────
    {
        "path":   "antipasti/image-1.jpg",
        "prompt": shot1(
            "Italian bruschetta al pomodoro on a dark slate board, "
            "thick golden-toasted sourdough rubbed with garlic, "
            "piled generously with bright diced San Marzano tomatoes, "
            "fresh vibrant green basil leaves, "
            "a glossy drizzle of extra virgin olive oil, coarse sea salt flakes"
        ),
        "ratio":  "3:4",
    },
    {
        "path":   "antipasti/image-2.jpg",
        "prompt": shot2(
            "extreme close-up of bruschetta al pomodoro, "
            "juicy ripe tomato chunks glistening with olive oil, "
            "fresh torn basil, crispy golden bread texture visible underneath, "
            "Italian countryside greenery soft bokeh in background"
        ),
        "ratio":  "3:4",
    },

    # ── DOLCI (Tiramisù) ────────────────────────────────────────
    {
        "path":   "dolci/image-1.jpg",
        "prompt": shot1(
            "classic Italian tiramisù in an elegant white ceramic rectangular dish, "
            "thick creamy mascarpone layer generously dusted with bitter dark cocoa powder, "
            "beautiful layered cross-section visible at the cut edge, "
            "a single espresso cup beside it on white marble, "
            "dusting of cocoa still floating in the air"
        ),
        "ratio":  "3:4",
    },
    {
        "path":   "dolci/image-2.jpg",
        "prompt": shot2(
            "a spoon breaking through the mascarpone cream of tiramisù, "
            "revealing perfect soaked savoiardi layers underneath, "
            "coffee drizzle around the ceramic plate, "
            "fresh mint leaf garnish, warm Italian restaurant candlelight atmosphere"
        ),
        "ratio":  "3:4",
    },

    # ── SECONDI (Ossobuco) ───────────────────────────────────────
    {
        "path":   "secondi/image-1.jpg",
        "prompt": shot1(
            "ossobuco alla milanese — a thick braised veal shank, "
            "rich glossy tomato and white wine braising sauce pooling around it, "
            "bright green gremolata of lemon zest and fresh parsley on top, "
            "served alongside golden saffron risotto alla milanese, "
            "elegant deep ceramic plate"
        ),
        "ratio":  "3:4",
    },
    {
        "path":   "secondi/image-2.jpg",
        "prompt": shot2(
            "close-up cross-section of ossobuco revealing rich bone marrow center, "
            "glistening braising jus, fresh gremolata herbs scattered over the veal, "
            "golden risotto visible alongside, "
            "rustic stone Italian kitchen setting"
        ),
        "ratio":  "3:4",
    },

    # ── ARTICLE: Shrimp Pasta ───────────────────────────────────
    {
        "path":   "article-1-shrimp-pasta/image-1.jpg",
        "prompt": shot1(
            "creamy garlic butter shrimp pasta in a white wide-rim pasta bowl, "
            "plump pink shrimp nestled in silky parmesan cream sauce, "
            "linguine perfectly twirled, fresh chopped parsley scattered on top, "
            "lemon wedge on the side, steam rising"
        ),
        "ratio":  "3:4",
    },
    {
        "path":   "article-1-shrimp-pasta/image-2.jpg",
        "prompt": shot2(
            "close-up of a fork lifting creamy shrimp linguine, "
            "sauce clinging in glossy ribbons, juicy seared shrimp, "
            "parmesan melting into the cream, "
            "dark moody kitchen background"
        ),
        "ratio":  "3:4",
    },

    # ── ARTICLE: Lava Cake ──────────────────────────────────────
    {
        "path":   "article-2-lava-cake/image-1.jpg",
        "prompt": shot1(
            "perfect chocolate lava cake on a white ceramic plate, "
            "dark glossy chocolate exterior, "
            "dusted lightly with powdered sugar, "
            "a scoop of vanilla gelato melting beside it, "
            "warm molten chocolate just starting to ooze from the center"
        ),
        "ratio":  "3:4",
    },
    {
        "path":   "article-2-lava-cake/image-2.jpg",
        "prompt": shot2(
            "a spoon cutting into a chocolate lava cake, "
            "hot liquid dark chocolate flowing dramatically onto the white plate, "
            "steam rising from the molten center, "
            "vanilla ice cream melting nearby, "
            "dark dramatic background with warm spotlight"
        ),
        "ratio":  "3:4",
    },

    # ── ARTICLE: Spaghetti Carbonara ────────────────────────────
    {
        "path":   "spaghetti-carbonara/image-1.jpg",
        "prompt": shot1(
            "authentic Roman spaghetti carbonara in a terracotta pasta bowl, "
            "silky glossy egg and Pecorino sauce coating every spaghetti strand, "
            "crispy golden guanciale lardons on top, "
            "generous freshly cracked black pepper, "
            "no cream — pure and elegant"
        ),
        "ratio":  "3:4",
    },
    {
        "path":   "spaghetti-carbonara/image-2.jpg",
        "prompt": shot2(
            "close-up of spaghetti carbonara being lifted with tongs, "
            "silky sauce stretching in golden threads, "
            "crispy guanciale pieces visible, cracked black pepper, "
            "authentic Roman trattoria atmosphere in background"
        ),
        "ratio":  "3:4",
    },

    # ── ARTICLE: Pizza Dough ────────────────────────────────────
    {
        "path":   "homemade-pizza-dough/image-1.jpg",
        "prompt": shot1(
            "freshly baked Neapolitan pizza on a dark pizza peel, "
            "perfectly charred leopard-spot crust, "
            "San Marzano tomato sauce, fresh torn mozzarella di bufala, "
            "fresh basil leaves wilting in the heat, "
            "light drizzle of olive oil, "
            "rustic Italian pizzeria setting"
        ),
        "ratio":  "3:4",
    },
    {
        "path":   "homemade-pizza-dough/image-2.jpg",
        "prompt": shot2(
            "hands stretching homemade pizza dough showing perfect gluten structure, "
            "flour-dusted hands pulling the dough wide and thin, "
            "dough translucent at the center showing elasticity, "
            "rustic kitchen with flour on wooden surface"
        ),
        "ratio":  "3:4",
    },

    # ── ARTICLE: Tiramisu ───────────────────────────────────────
    {
        "path":   "classic-tiramisu/image-1.jpg",
        "prompt": shot1(
            "a perfect individual portion of classic Italian tiramisù on a white plate, "
            "thick creamy mascarpone layer with a velvety cocoa-dusted top, "
            "clean sliced edge showing perfect alternating layers of cream and espresso savoiardi, "
            "an espresso cup and coffee beans beside it"
        ),
        "ratio":  "3:4",
    },
    {
        "path":   "classic-tiramisu/image-2.jpg",
        "prompt": shot2(
            "a dessert fork cutting through tiramisù revealing the perfect layered cross-section, "
            "mascarpone cream and coffee-soaked savoiardi layers visible, "
            "dark cocoa dusting on top, "
            "Italian restaurant warm candlelight background"
        ),
        "ratio":  "3:4",
    },

    # ── ARTICLE: Cacio e Pepe ───────────────────────────────────
    {
        "path":   "cacio-e-pepe-recipe/image-1.jpg",
        "prompt": shot1(
            "authentic Roman cacio e pepe pasta in a rustic ceramic bowl, "
            "silky tonnarelli pasta coated in creamy Pecorino Romano sauce, "
            "generous amounts of freshly cracked coarse black pepper speckling every strand, "
            "wisps of steam rising, no extra toppings — pure minimalist elegance"
        ),
        "ratio":  "3:4",
    },
    {
        "path":   "cacio-e-pepe-recipe/image-2.jpg",
        "prompt": shot2(
            "close-up of tonnarelli cacio e pepe being twirled on a fork, "
            "creamy Pecorino sauce stretching in silky threads, "
            "cracked black pepper visible on every strand, "
            "dark Roman trattoria atmosphere in background"
        ),
        "ratio":  "3:4",
    },

    # ── ARTICLE: Panna Cotta ────────────────────────────────────
    {
        "path":   "panna-cotta-recipe/image-1.jpg",
        "prompt": shot1(
            "elegant Italian panna cotta unmolded on a white ceramic plate, "
            "perfectly smooth ivory cream dome, "
            "vibrant ruby-red strawberry coulis pooling around the base, "
            "fresh whole strawberries and mint leaf garnish, "
            "translucent wobble texture visible — ultra refined, restaurant-quality"
        ),
        "ratio":  "3:4",
    },
    {
        "path":   "panna-cotta-recipe/image-2.jpg",
        "prompt": shot2(
            "a spoon breaking into silky panna cotta revealing its perfect creamy center, "
            "strawberry coulis flowing over the cut edge, "
            "fresh berries scattered around on white marble, "
            "warm soft Italian dessert bar lighting in background"
        ),
        "ratio":  "3:4",
    },

    # ── ARTICLE: Arancini ───────────────────────────────────────
    {
        "path":   "arancini-recipe/image-1.jpg",
        "prompt": shot1(
            "Sicilian arancini on a rustic wooden board, "
            "three golden-fried rice balls with perfectly crispy breadcrumb exterior, "
            "one cut open revealing molten mozzarella and rich ragu filling inside, "
            "fresh basil leaf garnish, marinara dipping sauce in small bowl beside them"
        ),
        "ratio":  "3:4",
    },
    {
        "path":   "arancini-recipe/image-2.jpg",
        "prompt": shot2(
            "close-up cross-section of an arancino split open, "
            "melted mozzarella stretching dramatically from the golden rice ball, "
            "rich meat filling visible in the center, "
            "crispy golden-orange breadcrumb crust detail, "
            "Sicilian market warm lighting atmosphere"
        ),
        "ratio":  "3:4",
    },

    # ── ARTICLE: Pasta Amatriciana ──────────────────────────────
    {
        "path":   "pasta-amatriciana-recipe/image-1.jpg",
        "prompt": shot1(
            "authentic pasta all'amatriciana in a deep ceramic pasta bowl, "
            "bucatini pasta coated in vibrant deep-red San Marzano tomato sauce, "
            "crispy golden guanciale lardons on top, "
            "shavings of sharp Pecorino Romano cheese, "
            "a hint of red chili flakes — pure Roman tradition"
        ),
        "ratio":  "3:4",
    },
    {
        "path":   "pasta-amatriciana-recipe/image-2.jpg",
        "prompt": shot2(
            "close-up of bucatini all'amatriciana being lifted with tongs, "
            "rich tomato sauce clinging dramatically, "
            "crispy guanciale and Pecorino shavings visible, "
            "dark atmospheric Roman trattoria in background"
        ),
        "ratio":  "3:4",
    },

    # ── ARTICLE: Chicken Piccata ────────────────────────────────
    {
        "path":   "chicken-piccata-recipe/image-1.jpg",
        "prompt": shot1(
            "chicken piccata on an elegant white ceramic plate, "
            "golden pan-seared chicken cutlets in bright lemony butter caper sauce, "
            "sauce glistening with melted butter and white wine, "
            "briny green capers and fresh thin lemon slices throughout, "
            "fresh flat-leaf parsley sprinkled over top"
        ),
        "ratio":  "3:4",
    },
    {
        "path":   "chicken-piccata-recipe/image-2.jpg",
        "prompt": shot2(
            "a fork cutting into golden chicken piccata cutlet, "
            "lemon butter caper sauce pooling around tender chicken, "
            "capers and lemon zest visible in the sauce, "
            "warm Italian bistro evening light in background"
        ),
        "ratio":  "3:4",
    },

    # ── ARTICLE: Italian Wedding Soup ───────────────────────────
    {
        "path":   "italian-wedding-soup-recipe/image-1.jpg",
        "prompt": shot1(
            "steaming bowl of Italian wedding soup in a wide white ceramic bowl, "
            "golden rich broth with tender mini meatballs, "
            "curly escarole greens, small acini di pepe pasta, "
            "dusting of Parmigiano Reggiano on top, "
            "crusty Italian bread slice on the side, "
            "steam rising dramatically from the hot broth"
        ),
        "ratio":  "3:4",
    },
    {
        "path":   "italian-wedding-soup-recipe/image-2.jpg",
        "prompt": shot2(
            "close-up of a soup spoon lifting Italian wedding soup, "
            "tender mini meatball and escarole greens visible, "
            "golden broth shimmering under warm light, "
            "cozy Italian home kitchen atmosphere in background"
        ),
        "ratio":  "3:4",
    },

    # ── ARTICLE: Homemade Gnocchi ───────────────────────────────
    {
        "path":   "homemade-gnocchi-recipe/image-1.jpg",
        "prompt": shot1(
            "homemade potato gnocchi in a rustic ceramic bowl, "
            "pillowy soft gnocchi with fork-ridged texture, "
            "tossed in rich golden butter and fresh sage sauce, "
            "Parmigiano shavings melting over them, "
            "one gnocco halved to show its light fluffy interior"
        ),
        "ratio":  "3:4",
    },
    {
        "path":   "homemade-gnocchi-recipe/image-2.jpg",
        "prompt": shot2(
            "hands rolling fresh homemade gnocchi on a flour-dusted wooden board, "
            "perfect ridged gnocchi shapes being formed with a fork, "
            "soft potato dough texture visible, "
            "rustic Italian kitchen warm morning light streaming through window"
        ),
        "ratio":  "3:4",
    },

    # ── ARTICLE: Italian Focaccia ───────────────────────────────
    {
        "path":   "italian-focaccia-recipe/image-1.jpg",
        "prompt": shot1(
            "Ligurian focaccia on a dark baking sheet, "
            "golden dimpled surface glistening with extra virgin olive oil, "
            "coarse flaky sea salt and fresh rosemary sprigs pressed into dimples, "
            "perfectly airy and chewy interior visible at the cut edge, "
            "beautiful golden-brown crust"
        ),
        "ratio":  "3:4",
    },
    {
        "path":   "italian-focaccia-recipe/image-2.jpg",
        "prompt": shot2(
            "a hand tearing a piece of golden focaccia, "
            "showing the open airy crumb interior with large bubbles, "
            "olive oil glistening on the crust surface, "
            "rosemary and sea salt visible, Italian bakery morning atmosphere"
        ),
        "ratio":  "3:4",
    },

    # ── ARTICLE: Semifreddo ─────────────────────────────────────
    {
        "path":   "semifreddo-recipe/image-1.jpg",
        "prompt": shot1(
            "Italian semifreddo sliced on an elegant white plate, "
            "beautiful frozen dessert with creamy nougat and toasted almonds, "
            "drizzled with dark chocolate sauce and honey, "
            "a dusting of cocoa powder, "
            "one slice showing the perfect frozen mousse interior — light and airy"
        ),
        "ratio":  "3:4",
    },
    {
        "path":   "semifreddo-recipe/image-2.jpg",
        "prompt": shot2(
            "close-up of a spoon cutting into semifreddo, "
            "creamy frozen interior with toasted hazelnut pieces, "
            "chocolate drizzle over white plate, "
            "elegant Italian gelato bar marble counter background"
        ),
        "ratio":  "3:4",
    },

    # ── ARTICLE: Ribollita ──────────────────────────────────────
    {
        "path":   "ribollita-recipe/image-1.jpg",
        "prompt": shot1(
            "Tuscan ribollita in a rustic terracotta crock, "
            "thick hearty bean and vegetable stew with dark lacinato kale, "
            "chunks of stale bread soaked and integrated into the rich stew, "
            "a drizzle of deep green Tuscan extra virgin olive oil on top, "
            "steam rising, served with crusty bread on the side"
        ),
        "ratio":  "3:4",
    },
    {
        "path":   "ribollita-recipe/image-2.jpg",
        "prompt": shot2(
            "close-up of a ladle scooping Tuscan ribollita, "
            "thick chunky bean soup with kale and bread visible, "
            "olive oil gleaming on the surface, "
            "rustic Tuscan farmhouse kitchen atmosphere in background"
        ),
        "ratio":  "3:4",
    },

]


def generate(prompt: str, out: Path, ratio: str) -> bool:
    print(f"  Generating: {out.relative_to(BASE)} ...")
    try:
        response = client.models.generate_images(
            model="imagen-4.0-generate-001",
            prompt=prompt,
            config=types.GenerateImagesConfig(
                number_of_images=1,
                aspect_ratio=ratio,
                output_mime_type="image/jpeg",
            ),
        )
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_bytes(response.generated_images[0].image.image_bytes)
        print(f"  SAVED: {out.name}")
        return True
    except Exception as e:
        print(f"  ERROR [{out.name}]: {e}")
        return False


def main():
    print("=" * 55)
    print("  Sapori d'Italia - Image Generator (New Prompts)")
    print(f"  Total: {len(IMAGES)} images | Force: {FORCE}")
    print("=" * 55)

    ok = err = skip = 0
    for item in IMAGES:
        out = BASE / item["path"]
        if out.exists() and not FORCE:
            print(f"  SKIP (exists): {item['path']}")
            skip += 1
            continue
        if generate(item["prompt"], out, item["ratio"]):
            ok += 1
        else:
            err += 1

    print(f"\nDone: {ok} generated | {skip} skipped | {err} errors")
    if FORCE:
        print("(--force mode: all existing images were overwritten)")


if __name__ == "__main__":
    main()
