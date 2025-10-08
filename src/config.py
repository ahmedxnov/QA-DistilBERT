from pathlib import Path

PROJECT_ROOT = Path(__file__).parent.parent
DATA_PATH = PROJECT_ROOT / "data" / "dev-v1.1.json"
DEFAULT_MODEL = "distilbert-base-uncased-distilled-squad"
DEFAULT_TASK = "question-answering"
DEFAULT_DEVICE = 0  # Use -1 for CPU, 0 or other integers for GPU devices

# Inference Configuration
DEFAULT_BATCH_SIZE = 32  # Optimal batch size based on testing
