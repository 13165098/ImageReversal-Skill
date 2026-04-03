# 🎛️ Prompt Tuning Guide

Welcome to the tuning guide for the **Image Reversal** skill. While the skill automatically routes and generates high-quality prompts based on standard schemas, you can manually fine-tune the JSON templates (`schemas/`) to influence the final output.

## 1. Modifying the Output Schemas
The AI strictly follows the keys defined in the JSON files under the `schemas/` directory.

- **To emphasize a specific style:** Add a new key in the JSON. For example, if you want the AI to always analyze the *Film Grain* type, add `"film_grain_type": "<string>"` under the `photography` section of the schema.
- **To ignore a dimension:** Simply remove the key from the schema file. The AI will stop analyzing that specific aspect.

## 2. Using the `constraints` Block
The `constraints` section is the most powerful tool for quality control.
- `must_keep`: The AI will prioritize these elements when generating the natural language prompt. If an element is crucial (e.g., "glasses", "mole on left cheek"), ensure it lands here.
- `avoid` and `negative_prompt`: These lists prevent the "AI look". Feel free to expand the `negative_prompt` array in the schema with terms like `"symmetry"`, `"over-saturated"`, or `"depth of field"` (if you want a flat image).

## 3. Controlling the Output Format
If you want the Natural Language Prompt to be formatted differently (e.g., comma-separated tags for Stable Diffusion instead of a cinematic paragraph for Midjourney), simply edit the `Instructions -> Step 3` in the main `SKILL.md` file.

```markdown
// Change this:
<string: Insert a detailed cinematic natural language prompt... typically 100-150 words>

// To this:
<string: Insert a comma-separated list of Danbooru tags, ordered by importance>
```

Happy reverse engineering!