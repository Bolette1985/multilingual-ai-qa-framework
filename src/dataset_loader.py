import glob
import os
import json


def load_latest_dataset(dataset_dir="prompts"):
    """
    Loads the most recently created generated dataset file.
    """

    prompt_files = glob.glob(os.path.join(dataset_dir, "generated_*.json"))

    if not prompt_files:
        raise FileNotFoundError("❌ No generated prompt files found")

    latest_file = max(prompt_files, key=os.path.getctime)

    print(f"📂 Using dataset: {latest_file}")

    with open(latest_file, "r", encoding="utf-8") as f:
        data = json.load(f)

    return data, latest_file
