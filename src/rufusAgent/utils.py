import json
import re


def save_json(data, filepath):
    """Save dictionary as JSON file."""
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)


def clean_text(text):
    """Remove unwanted characters, excessive spaces, and navigation text."""
    text = re.sub(r'\s+', ' ', text)  # Remove excessive whitespace
    text = text.replace("\u2193", "").replace("\u2019", "'")  # Fix encoding issues
    text = re.sub(r'MIT AdmissionsSkip to content.*?Menu', '', text)  # Remove navigation text
    return text.strip()