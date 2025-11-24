import subprocess
from pathlib import Path


if __name__ == '__main__':
    repo_url = "https://github.com/huggingface/transformers"

    if not Path("transformers").exists():
        print("Cloning the Transformers repository...")
        subprocess.run(["git", "clone", repo_url], check=True)
