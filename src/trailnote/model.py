from transformers import pipeline
from PIL import Image
import os

# Candidate labels for zero-shot classification to help CLIP narrow down to plants and birds
CANDIDATE_LABELS = [
    "oak tree", "pine tree", "maple tree", "birch tree", "willow tree",
    "poison ivy", "poison oak", "dandelion", "sunflower", "rose", "tulip", "fern", "moss",
    "sparrow", "robin", "blue jay", "cardinal", "crow", "pigeon", "hawk", "eagle", "owl", "woodpecker",
    "duck", "goose", "swan", "hummingbird",
    "a plant", "a bird", "a flower", "a tree", "a weed", "a mushroom", "an insect", "a mammal"
]

def identify_image(image_path: str):
    image = Image.open(image_path)
    # Ensure standard RGB
    if image.mode != "RGB":
        image = image.convert("RGB")
    # Use a small CLIP model that downloads quickly and runs okay on CPU
    classifier = pipeline("zero-shot-image-classification", model="openai/clip-vit-base-patch32")
    results = classifier(image, candidate_labels=CANDIDATE_LABELS)
    return results
