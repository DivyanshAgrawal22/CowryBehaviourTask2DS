"""
Utility functions shared across multiple notebooks
"""

import pandas as pd
import numpy as np
import pickle
import os
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')

# ============================================================================
# PIPELINE FUNCTIONS
# ============================================================================

def save_processed_data(df: pd.DataFrame, name: str):
    """Save processed data for next notebooks"""
    os.makedirs('../data/processed', exist_ok=True)
    filepath = f'../data/processed/{name}'
    
    if name.endswith('.csv'):
        df.to_csv(filepath, index=False)
    elif name.endswith('.pkl'):
        with open(filepath, 'wb') as f:
            pickle.dump(df, f)
    
    print(f"Saved processed data: {filepath}")

def load_processed_data(name: str):
    """Load processed data from previous notebooks"""
    filepath = f'../data/processed/{name}'
    try:
        if name.endswith('.csv'):
            df = pd.read_csv(filepath)
        elif name.endswith('.pkl'):
            with open(filepath, 'rb') as f:
                df = pickle.load(f)
        
        print(f"Loaded processed data: {filepath}")
        return df
    except FileNotFoundError:
        print(f"Processed data not found: {filepath}")
        return None

# ============================================================================
# VISUALIZATION
# ============================================================================

def setup_plotting_style():
    """Set up consistent plotting style"""
    plt.style.use('seaborn-v0_8-whitegrid')
    sns.set_palette("Set2")
    plt.rcParams.update({
        'figure.figsize': (12, 8), 'font.size': 11,
        'axes.titlesize': 14, 'axes.labelsize': 12
    })

def save_figure(name: str, dpi: int = 300):
    """Save figure to outputs folder"""
    os.makedirs('../outputs/figures', exist_ok=True)
    filepath = f'../outputs/figures/{name}.png'
    plt.savefig(filepath, dpi=dpi, bbox_inches='tight', facecolor='white')
    print(f"Saved: {filepath}")

def print_section_header(title: str):
    """Print formatted section header"""
    print(f"\n{'='*60}")
    print(f"{title.upper()}")
    print(f"{'='*60}")

# ============================================================================
# STATISTICAL ANALYSIS
# ============================================================================

def statistical_comparison(group1, group2, metric_name):
    """Compare two groups statistically"""
    from scipy import stats
    
    # Remove NaN values
    group1_clean = [x for x in group1 if not pd.isna(x)]
    group2_clean = [x for x in group2 if not pd.isna(x)]
    
    # T-test for numerical data
    statistic, p_value = stats.ttest_ind(group1_clean, group2_clean)
    
    # Effect size (Cohen's d)
    pooled_std = np.sqrt(((len(group1_clean) - 1) * np.var(group1_clean, ddof=1) + 
                         (len(group2_clean) - 1) * np.var(group2_clean, ddof=1)) / 
                        (len(group1_clean) + len(group2_clean) - 2))
    
    cohens_d = (np.mean(group1_clean) - np.mean(group2_clean)) / pooled_std
    
    result = {
        'metric': metric_name,
        'group1_mean': np.mean(group1_clean),
        'group2_mean': np.mean(group2_clean),
        'statistic': statistic,
        'p_value': p_value,
        'cohens_d': cohens_d,
        'significant': p_value < 0.05
    }
    
    return result

def print_summary_stats(df, group_col, metric_col):
    """Print summary statistics by group"""
    summary = df.groupby(group_col)[metric_col].agg(['count', 'mean', 'std']).round(3)
    print(f"\nSummary Statistics for {metric_col}:")
    print(summary)
    return summary