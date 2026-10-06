import gradio as gr
from .model import identify_image
from .log import save_log

DISCLAIMER = "WARNING: This is a guess by an AI model. Verify before touching, eating, or interacting with any plant or animal."

def analyze(image, save_to_log):
    if image is None:
        return "No image provided.", ""
    
    try:
        results = identify_image(image)
        
        output = "Top 3 Guesses:\n"
        for i, res in enumerate(results[:3], 1):
            output += f"{i}. {res['label']} (Confidence: {res['score']:.2%})\n"
            
        output += f"\n{DISCLAIMER}"
        
        if save_to_log:
            save_log(image, results[:3])
            output += "\n\nSaved to walk log."
            
        return output
    except Exception as e:
        return f"Error analyzing image: {e}"

def launch_web():
    demo = gr.Interface(
        fn=analyze,
        inputs=[
            gr.Image(type="filepath", label="Upload Photo"),
            gr.Checkbox(label="Save to Walk Log")
        ],
        outputs=gr.Textbox(label="Identification Results", lines=8),
        title="TrailNote 🌲🐦",
        description="Offline-first plant and bird identification tool."
    )
    demo.launch(inbrowser=True)

if __name__ == "__main__":
    launch_web()
