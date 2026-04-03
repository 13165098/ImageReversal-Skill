# Image Reversal Skill 📸🔄

A high-precision Vision-Language Image Reverse Engineering skill designed to extract highly structured JSON metadata and generate production-ready cinematic prompts from any input image.

## 🌟 Overview

The **Image Reversal** skill acts as your personal visual analyst and prompt engineer. It forces the AI to look beyond basic image descriptions and deconstruct the image at a micro-level (pores, lighting setup, depth of field, stray hairs). It then translates this analysis into a strict JSON schema and a high-quality natural language prompt ready for AI image generators.

## ✨ Core Features

- **Micro-level Deconstruction:** Breaks down images into strictly defined dimensions (`subject`, `hair`, `body`, `pose`, `clothing`, `photography`, `background`, `the_vibe`).
- **Dynamic Schema Routing (v2.0):** Automatically detects whether the image is a Portrait, Architecture, or Product, and applies the perfect domain-specific JSON template.
- **Production-Ready Prompts:** Automatically outputs a 100-150 word cinematic English prompt optimized for Midjourney (v6) and Stable Diffusion.
- **Auto-Archiving Workflow (v3.0):** Equipped with a Python script that automatically intercepts the AI's output and saves the JSON and Prompt into organized, timestamped folders in your local `~/Pictures/RIP-Prompts/` directory.
- **Authenticity Control:** Built-in constraints and negative prompts (e.g., avoiding "plastic skin", "3d render") to ensure high-realism and organic outputs.
- **Strict JSON Schema:** Always outputs a predictable, structured JSON format for easy reading and programmatic integration.

## 🚀 Installation & Usage

**For WorkBuddy Users:**

1. Install this skill by copying `SKILL.md` into your local `~/.workbuddy/skills/Image-reversal/` directory.
2. In the WorkBuddy chat, upload an image (preferably high-resolution).
3. Invoke the skill by typing:
   ```text
   @Image reversal
   ```
   *Or use natural language: "Analyze this image using the Image reversal skill."*

## 🎯 Example Output Structure

When you upload an image, the skill will reply with:

1. **A detailed JSON block** capturing facial micro-details, hair dynamics, lighting setup, camera settings, and atmospheric vibes. (Uses `"N/A"` for obscured details to prevent AI hallucination).
2. **A Natural Language Prompt** similar to:
   > *"Ultra-detailed cinematic close-up portrait of a slender young female... [Detailed descriptions of lighting, lens, and subject]... High realism, nostalgic springtime vibe. --ar 2:3 --style raw --v 6.0"*

## 🛠 Ideal Use Cases

- **AI Artists & Creators:** Reverse-engineer stunning reference images to find the perfect prompt formulation.
- **Prompt Engineers:** Standardize the way images are analyzed and converted into text.
- **Photography Enthusiasts:** Analyze lighting setups, camera angles, and depth-of-field choices from existing photos.

## 📸 Showcase

*(Add your images to the `assets/` folder and name them `original_sample.jpg` and `generated_sample.jpg` to display them here!)*

| Original Input Image | AI Generated Result from Extracted Prompt |
| :---: | :---: |
| ![Original Input](assets/original_sample.jpg) | ![Generated Output](assets/generated_sample.jpg) |

## 📚 Documentation & Tuning

Want to customize how the AI analyzes images or formats the prompt? 
Check out our **[Prompt Tuning Guide](docs/prompt_tuning_guide.md)** to learn how to modify schemas and control the output aesthetic.

---
*Built for WorkBuddy AI to empower high-fidelity image-to-text workflows.*