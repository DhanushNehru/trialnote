# TrailNote 🌲🐦

TrailNote is an offline-first CLI tool that helps you identify plants and birds from photos using an open-weight vision-language model (CLIP). It runs entirely locally on your machine with no API keys, ensuring privacy and offline capability when you're preparing for or returning from the outdoors.

## Requirements
- Python 3.8+
- ~2GB of free disk space for the local model (`openai/clip-vit-base-patch32`)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/trailnote.git
   cd trailnote
   ```

2. Install the package (preferably in a virtual environment):
   ```bash
   pip install -e .
   ```

## Usage

### Identify an Image
Use the `identify` command to analyze a photo. The first time you run this, it will download the model (approx 600MB). Subsequent runs will be completely offline.

```bash
trailnote identify path/to/your/photo.jpg
```

**Example Output:**
```
Top 3 Guesses:
1. a bird (Confidence: 85.12%)
2. blue jay (Confidence: 45.33%)
3. an insect (Confidence: 1.05%)

WARNING: This is a guess by an AI model. Verify before touching, eating, or interacting with any plant or animal.
```

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
- **Supported Species**: The current version tests against a hardcoded list of common plants and birds in North America. It may default to generic terms like "a plant" or "a bird" if it doesn't know the specific species.
- **Safety**: **NEVER** use this tool to determine if a plant is edible, safe to touch, or medicinal. Always consult a human expert or authoritative guide. This is a fun, best-effort guess tool.
- **Performance**: Running AI models locally can be resource-intensive. Identification might take 5-30 seconds depending on your CPU/GPU.

## License
MIT License. See `LICENSE` for details.
