import argparse
import sys
import os
from .model import identify_image
from .log import save_log, get_logs

DISCLAIMER = "\nWARNING: This is a guess by an AI model. Verify before touching, eating, or interacting with any plant or animal."

def main():
    parser = argparse.ArgumentParser(description="TrailNote: Offline plant and bird identification.")
    subparsers = parser.add_subparsers(dest="command")

    # identify command
    identify_parser = subparsers.add_parser("identify", help="Identify a plant or bird from an image")
    identify_parser.add_argument("image", help="Path to the image file")
    identify_parser.add_argument("--log", action="store_true", help="Save the identification to your walk log")

    # log command
    log_parser = subparsers.add_parser("log", help="View your walk log")

    args = parser.parse_args()

    if args.command == "identify":
        if not os.path.exists(args.image):
            print(f"Error: File {args.image} not found.")
            sys.exit(1)
        
        print("Loading model and analyzing image... (this might take a moment the first time)")
        try:
            results = identify_image(args.image)
        except Exception as e:
            print(f"Error analyzing image: {e}")
            sys.exit(1)
            
        print("\nTop 3 Guesses:")
        for i, res in enumerate(results[:3], 1):
            print(f"{i}. {res['label']} (Confidence: {res['score']:.2%})")
            
        print(DISCLAIMER)

        if args.log:
            save_log(args.image, results[:3])
            print("\nSaved to walk log.")

    elif args.command == "log":
        logs = get_logs()
        if not logs:
            print("No walk logs found.")
        else:
            for entry in logs:
                print(f"[{entry['date']}] Image: {entry['image']}")
                for i, guess in enumerate(entry['guesses'], 1):
                    print(f"  {i}. {guess['label']} ({guess['score']:.2%})")
                print()
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
