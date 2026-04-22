from pathlib import Path
from PIL import Image

DATA_DIR = Path("data/ecoset_subset")

CATEGORIES = [
    'ball', 'bed', 'boat', 'book', 'car', 'city',
    'dog', 'fire', 'fish', 'gun', 'horse', 'house',
    'man', 'phone', 'table', 'tree', 'woman'
]

def load_local_ecoset(data_dir: Path = DATA_DIR) -> dict:
    """Load ECOSET images from disk. Returns dict of category -> list of PIL Images."""
    dataset = {}
    for category in CATEGORIES:
        cat_dir = data_dir / category
        images = []
        if cat_dir.exists():
            for img_path in sorted(cat_dir.glob("*.jpg")):
                img = Image.open(img_path).convert("RGB")
                images.append(img)
        dataset[category] = images
        print(f"{category}: {len(images)} images")
    return dataset