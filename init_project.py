#!/usr/bin/env python3
"""CLI script to scaffold the open-runyoro-ai project."""

from pathlib import Path


def create_file(path: Path, content: str = "") -> None:
    """Create a file with the given content, ensuring parent directories exist."""
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content)


def main() -> None:
    root = Path("open-runyoro-ai")

    dirs = [
        root / "data" / "raw",
        root / "data" / "interim",
        root / "data" / "prepared" / "asr",
        root / "data" / "prepared" / "tts" / "speaker_1",
        root / "data" / "prepared" / "llm",
        root / "models" / "checkpoints",
        root / "models" / "final",
        root / "src" / "preprocessing",
        root / "src" / "training",
        root / "src" / "inference",
        root / "src" / "utils",
        root / "scripts",
        root / "config",
        root / "notebooks",
    ]

    for d in dirs:
        d.mkdir(parents=True, exist_ok=True)

    # notebooks placeholder
    create_file(root / "notebooks" / ".gitkeep", "")

    # requirements
    requirements = """torch>=2.2
torchaudio
transformers>=4.40
peft
accelerate
datasets
pdfminer.six
beautifulsoup4
readability-lxml
yt-dlp
pydub
soundfile
whisperx
tqdm
pandas
unidecode
"""
    create_file(root / "requirements.txt", requirements)

    # README
    readme = (
        "# Open Runyoro AI\n"
        "This repository contains the scaffold for the Open Runyoro AI project.\n"
        "It organizes data, models and scripts for speech and language tasks.\n"
        "The files are placeholders to help you get started.\n"
    )
    create_file(root / "README.md", readme)

    # config files
    create_file(root / "config" / "local.yaml", "batch_size: 2\ndevice: mps\n")
    create_file(root / "config" / "cloud.yaml", "batch_size: 8\ndevice: cuda\n")

    py_stubs = {
        "src/preprocessing/__init__.py":
            '"""Package for data preprocessing utilities."""\n\n' "def init_package():\n    pass\n",
        "src/preprocessing/text_cleaner.py":
            '"""Utilities for cleaning and normalizing text."""\n\n' "def clean_text(text):\n    pass\n",
        "src/preprocessing/audio_processor.py":
            '"""Audio processing helpers."""\n\n' "def process_audio(path):\n    pass\n",
        "src/preprocessing/whisper_align.py":
            '"""Interfaces to whisperx for alignment."""\n\n' "def align():\n    pass\n",
        "src/preprocessing/conversation_builder.py":
            '"""Builds conversations from transcripts."""\n\n' "def build_conversation():\n    pass\n",
        "src/training/__init__.py":
            '"""Training scripts and helpers."""\n\n' "def init_package():\n    pass\n",
        "src/training/asr_finetune.py":
            '"""Fine-tune ASR models."""\n\n' "def main():\n    pass\n",
        "src/training/tts_finetune.py":
            '"""Fine-tune TTS models."""\n\n' "def main():\n    pass\n",
        "src/training/llm_lora_train.py":
            '"""Train LLM with LoRA."""\n\n' "def main():\n    pass\n",
        "src/training/evaluation.py":
            '"""Model evaluation utilities."""\n\n' "def evaluate():\n    pass\n",
        "src/inference/__init__.py":
            '"""Inference modules."""\n\n' "def init_package():\n    pass\n",
        "src/inference/voice_handler.py":
            '"""Handle voice input and output."""\n\n' "def handle_voice():\n    pass\n",
        "src/inference/conversation_manager.py":
            '"""Manage user conversations."""\n\n' "def manage_conversation():\n    pass\n",
        "src/utils/__init__.py":
            '"""Miscellaneous utilities."""\n\n' "def init_package():\n    pass\n",
        "src/utils/data_validator.py":
            '"""Validate dataset files."""\n\n' "def validate():\n    pass\n",
        "src/utils/memory_optimizer.py":
            '"""Optimize memory usage."""\n\n' "def optimize():\n    pass\n",
        "scripts/01_download_youtube.py":
            '"""Download audio from YouTube."""\n\n' "def main():\n    pass\n",
        "scripts/02_scrape_bible_text.py":
            '"""Scrape Bible text from sources."""\n\n' "def main():\n    pass\n",
        "scripts/03_align_audio_text.py":
            '"""Align audio with text transcripts."""\n\n' "def main():\n    pass\n",
        "scripts/04_split_manifests.py":
            '"""Split dataset manifests for training."""\n\n' "def main():\n    pass\n",
        "scripts/migrate_to_cloud.py":
            '"""Migrate project assets to cloud storage."""\n\n' "def main():\n    pass\n",
    }

    for rel_path, content in py_stubs.items():
        create_file(root / rel_path, content)

    shell_stubs = {
        "scripts/train_local_asr.sh": "#!/bin/bash\n# Placeholder script for local ASR training\n",
        "scripts/train_local_tts.sh": "#!/bin/bash\n# Placeholder script for local TTS training\n",
        "scripts/train_local_llm.sh": "#!/bin/bash\n# Placeholder script for local LLM training\n",
    }

    for rel_path, content in shell_stubs.items():
        file_path = root / rel_path
        create_file(file_path, content)
        file_path.chmod(0o755)

    print("\u2705 Project scaffold created")


if __name__ == "__main__":
    main()
