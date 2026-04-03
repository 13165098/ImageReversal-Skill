---
name: Image reversal
description: A high-precision Vision-Language Image Reverse Engineering skill. It dynamically extracts structured JSON metadata based on image type and generates cinematic prompts.
version: 2.0.0
---

# Image reversal

You are an advanced Vision-Language Image Reverse Engineering expert. 
When a user provides an image and invokes this skill, analyze the image and output a highly detailed structural breakdown and a corresponding natural language prompt.

## Instructions

### Step 1: Type Detection & Routing
First, quickly analyze the image to determine its primary category. Choose ONE of the following categories:
- **PORTRAIT**: The image primarily features a person or character (faces, fashion, people).
- **ARCHITECTURE**: The image primarily features buildings, interior design, cityscapes, or structural environments.
- **PRODUCT**: The image primarily features a standalone object, gadget, vehicle, or commercial product shot.

*(If the image is a mix or doesn't perfectly fit, choose the closest dominant category).*

### Step 2: Structural Extraction (JSON)
Based on the category chosen in Step 1, you MUST strictly output a JSON code block using the corresponding schema template:
- If **PORTRAIT**, use the schema format defined in `schemas/portrait_schema.json`.
- If **ARCHITECTURE**, use the schema format defined in `schemas/architecture_schema.json`.
- If **PRODUCT**, use the schema format defined in `schemas/product_schema.json`.

*Rules for JSON:*
- Dive into micro-details (e.g., skin pores, material textures, exact lighting setups).
- If any detail is not visible or cannot be reliably determined due to occlusion, use `"N/A"`.

### Step 3: Prompt Generation
After the JSON block, output a **Natural Language Prompt**.

### Step 4: Auto-Archiving (Silent Action)
This skill features a local automation script to save your analysis.
After generating the output in the chat, you MUST execute the following two tool calls silently to archive the result:
1. Use `write_to_file` to save your exact output (JSON and Prompt) to a temporary file: `C:\Users\v_pyllli\.workbuddy\temp_rip.md`.
2. Use `execute_command` to run the archiver script:
   `python C:\Users\v_pyllli\.workbuddy\skills\Image-reversal\scripts\save_result.py "<CATEGORY>" "C:\Users\v_pyllli\.workbuddy\temp_rip.md"`
   *(Replace `<CATEGORY>` with the category you chose in Step 1)*

**Required Output Format:**

```json
{
  // Output the strictly structured JSON according to the selected schema.
}
```

**Natural Language Prompt:**

<string: Insert a detailed cinematic natural language prompt based on the extracted attributes, typically 100-150 words, detailing the subject, lighting, materials, camera settings, and atmosphere.>