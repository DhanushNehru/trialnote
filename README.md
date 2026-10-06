# TrailNote 🌲🐦

TrailNote is an offline-first CLI tool that helps you identify plants and birds from photos using an open-weight vision-language model (CLIP). It runs entirely locally on your machine with no API keys, ensuring privacy and offline capability when you're preparing for or returning from the outdoors.

## Requirements
- Python 3.8+
- A few GB of free disk space (PyTorch is about 750MB on its own, and the CLIP model `openai/clip-vit-base-patch32` is downloaded on first run)
- A recent `pip` (an old pip can fail while resolving the dependencies)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/DhanushNehru/trialnote.git
   cd trialnote
   ```

2. Install the package (preferably in a virtual environment):
   ```bash
   pip install -e .
   ```

## Usage

### Identify an Image
Use the `identify` command to analyze a photo. The first time you run this, it downloads the model from Hugging Face. After that it runs from the local cache (I checked this with `HF_HUB_OFFLINE=1`).

```bash
trailnote identify path/to/your/photo.jpg
```

**Example Output** (real run on a public-domain photo of an American robin from Wikimedia Commons, "American Robin (28380156288).jpg"):
```
Top 3 Guesses:
1. robin (Confidence: 73.06%)
2. cardinal (Confidence: 18.70%)
3. a bird (Confidence: 5.39%)

WARNING: This is a guess by an AI model. Verify before touching, eating, or interacting with any plant or animal.
```
This one was a decent guess. Don't expect that every time. See Limitations.

### Save to Walk Log
Add the `--log` flag to save the identification to your personal walk log.

```bash
trailnote identify photo.jpg --log
```

### View Walk Log
View previously saved identifications:
```bash
trailnote log
```

### Web Interface
You can also launch a simple web interface to upload photos from your browser:
```bash
trailnote-web
```

## Limitations

- **Accuracy**: This tool uses a small, general-purpose vision model (`openai/clip-vit-base-patch32`). It is *not* a specialized botanist or ornithologist AI. Its accuracy is limited, especially for rare or visually similar species.
- **Supported Species**: The model only scores your photo against a short hardcoded list of about 35 labels (a few trees, flowers and common birds, plus generic ones like "a plant", "a bird", "an insect"). It cannot identify species outside that list and will often pick a generic label or a wrong one. It is not a real species identifier.
- **Safety**: **NEVER** use this tool to determine if a plant is edible, safe to touch, or medicinal. Always consult a human expert or authoritative guide. This is a fun, best-effort guess tool.
- **Performance**: Running AI models locally can be resource-intensive. Identification might take 5-30 seconds depending on your CPU/GPU.

## License
MIT License. See `LICENSE` for details.
