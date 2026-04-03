import os
import sys
import time

def main():
    if len(sys.argv) < 3:
        print("Usage: python save_result.py <category> <content_file_path>")
        return
    
    category = sys.argv[1].strip().upper()
    content_file = sys.argv[2].strip()

    try:
        with open(content_file, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        print(f"Error reading {content_file}: {e}")
        sys.exit(1)

    json_content = ""
    prompt_content = ""
    
    # Simple extraction logic
    if "```json" in content:
        parts = content.split("```json")
        if "```" in parts[1]:
            json_content = parts[1].split("```")[0].strip()
    
    if "**Natural Language Prompt:**" in content:
        prompt_content = content.split("**Natural Language Prompt:**")[1].strip()
    elif "Natural Language Prompt:" in content:
        prompt_content = content.split("Natural Language Prompt:")[1].strip()

    # Define target local directory (e.g., Pictures/RIP-Prompts)
    base_dir = os.path.expanduser("~/Pictures/RIP-Prompts")
    timestamp = time.strftime("%Y%m%d_%H%M%S")
    target_dir = os.path.join(base_dir, f"{timestamp}_{category}")
    
    os.makedirs(target_dir, exist_ok=True)

    # Save JSON
    if json_content:
        with open(os.path.join(target_dir, "analysis.json"), 'w', encoding='utf-8') as f:
            f.write(json_content)
    else:
        with open(os.path.join(target_dir, "analysis.json"), 'w', encoding='utf-8') as f:
            f.write('{"error": "Could not parse JSON block from output."}')
    
    # Save Prompt
    if prompt_content:
        with open(os.path.join(target_dir, "prompt.txt"), 'w', encoding='utf-8') as f:
            f.write(prompt_content)
    else:
        with open(os.path.join(target_dir, "prompt.txt"), 'w', encoding='utf-8') as f:
            f.write(content) # Fallback: write everything if prompt parsing fails

    print(f"✅ Successfully archived to: {target_dir}")
    
    # Cleanup temporary file
    try:
        os.remove(content_file)
    except:
        pass

if __name__ == "__main__":
    main()
