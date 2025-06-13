"""
Configuration for Cowry Task 2 Analysis
"""

from pathlib import Path

# Project paths
PROJECT_ROOT = Path(__file__).parent
DATA_DIR = PROJECT_ROOT / "data"
PROCESSED_DATA_DIR = PROJECT_ROOT / "data/processed"
OUTPUTS_DIR = PROJECT_ROOT / "outputs"

# Data files
EXCEL_FILE = DATA_DIR / "CDS_25_Task2.xlsx"
CONTROL_SHEET = "C Control"
PILOT_SHEET = "C Pilot"

# Pipeline data files (saved between notebooks)
# CLEANED_DATA = PROCESSED_DATA_DIR / "cleaned_data.csv"
TOPIC_RESULTS = PROCESSED_DATA_DIR / "topic_results.pkl"
SENTIMENT_DATA = PROCESSED_DATA_DIR / "sentiment_data.csv"
FINAL_RESULTS = PROCESSED_DATA_DIR / "final_results.csv"

# Analysis parameters
EXCLUDE_MONTH = 2  # February - as required by the brief
RANDOM_STATE = 42

# Behavioral themes - exact keywords mentioned in brief
BEHAVIORAL_THEMES = {
    'agent_personality': ['friendly', 'helpful', 'polite', 'lovely', 'nice', 'professional'],
    'clarity': ['clear', 'explained', 'understand', 'easy', 'simple', 'straightforward'],
    'reassurance': ['reassured', 'confident', 'trust', 'reliable', 'secure', 'comfortable']
}

# Topic modeling parameters
N_TOPICS = 8
MIN_TOPIC_SIZE = 10

def create_directories():
    """Create necessary directories."""
    DATA_DIR.mkdir(exist_ok=True)
    (DATA_DIR / "processed").mkdir(exist_ok=True)
    OUTPUTS_DIR.mkdir(exist_ok=True)
    (OUTPUTS_DIR / "figures").mkdir(exist_ok=True)

if __name__ == "__main__":
    create_directories()
    print("Project directories created successfully.")