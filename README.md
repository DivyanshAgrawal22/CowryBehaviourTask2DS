# Task 2: Behaviourally-Optimised Call Script Analysis

## Project Overview

Analysis of field experiment testing a new decision-support script for call center agents. The aim was to improve customer outcomes when choosing broadband packages through simplified decisions, trust building, and reduced decision regret.

## Objective

Understand how customers define "good" service and evaluate whether the new script systematically changed perceptions or emotional tone, particularly for high-value VOLT customers.

## Dataset

- **Source**: Post-call survey feedback (CDS_25_Task2.xlsx)
- **Size**: 582 initial responses, 422 valid comments after preprocessing
- **Structure**: Treatment/Control groups with VOLT customer segment
- **Temporal Filter**: February responses excluded per brief requirements

## Methodology

### 1. Data Preprocessing (01_data_preprocessing.py)
- Temporal filtering and text cleaning with NLTK
- VOLT/Non-VOLT segmentation  
- Date format standardization and validation

### 2. Topic Modeling (02_topic_modelling.py)
- **Model Competition**: 7 approaches tested (3 LDA + 4 BERTopic)
- **Winner**: BERTopic with MiniLM embeddings (0.627 composite score)
- **LLM Theme Extraction**: Zero-shot classification with DeBERTa-v3-NLI
- **Output**: 7 meaningful topics with 68.5% document coverage

### 3. Sentiment Analysis (03_sentiment_analysis.py)
- **Method**: TextBlob (conservative approach for business interpretation)
- **Classification**: Neutrals added to negatives for business focus
- **Analysis**: Topic-sentiment co-occurrence and treatment effects

### 4. Predictive Modeling (04_modelling_interpretation.py)
- **Algorithm**: Logistic Regression (interpretability over accuracy)
- **Features**: 13 total (7 topic + 3 behavioral + 3 metadata)
- **Performance**: 72.4% accuracy, 0.747 AUC, 93% precision positive

### 5. Behavioral Insights (05_behavioural_insights.py)
- Trust, clarity, and decision ease analysis
- Language pattern extraction by treatment group
- Business recommendations and limitations assessment

## Key Findings

### Treatment Impact
- **Overall Effect**: -0.027 sentiment points (pilot script harm)
- **VOLT Customers**: -0.066 points (38% stronger negative reaction)
- **Non-VOLT Customers**: -0.048 points

### Trust Language Elimination
- **VOLT**: 3.7% to 0% trust language usage
- **Non-VOLT**: 1.1% to 0% trust language usage

### Behavioral Insights
- **Politeness Bias**: "Helpful" mentions predict lower satisfaction
- **Process Issues**: Team handoffs and delays emerge with pilot script
- **Cognitive Dissonance**: VOLT customers report ease but experience complexity

## Business Recommendations

1. **Restore Trust-Building Language**: Add relationship-focused phrases
2. **Streamline VOLT Processes**: Expedited handling for premium customers  
3. **Enhance Agent Training**: Focus on solution-oriented communication
4. **Address Call Management**: Reduce wait times and transfer issues

## Technical Stack

- **Languages**: Python
- **NLP Libraries**: NLTK, TextBlob, BERTopic, scikit-learn
- **ML Libraries**: Transformers, sentence-transformers  
- **Analysis**: pandas, numpy, scipy
- **Visualization**: matplotlib, seaborn, wordcloud

## File Structure

```
├── CDS_25_Task2.xlsx                       # Raw data
├── config.py                               # Configuration parameters
├── utils.py                                # Shared utility functions
├── notebooks
│   ├── 01_data_processing.ipynb            # Data cleaning and filtering
│   ├── 02_topic_modelling.ipynb            # Topic discovery and LLM analysis
│   ├── 03_sentiment_analysis.ipynb         # Sentiment scoring and co-occurrence
│   ├── 04_modelling_interpretation.ipynb   # Predictive modeling
│   └── 05_behavioural_insights.ipynb       # Business insights and recommendations        
├── data/processed/                         # Pipeline intermediate files
└── outputs/figures/                        # Generated visualisations
```

## Key Visualizations

- **executive_summary**: 4-panel dashboard of key findings
- **sentiment_distributions_by_groups**: Treatment effect evidence
- **topic_sentiment_heatmap**: Topic-sentiment relationships
- **feature_importance**: Predictive model insights
- **word_clouds_by_segment**: Language patterns by group

## Limitations

- **Sample Size**: 422 comments limits statistical power
- **Response Bias**: Only customers who chose to comment included
- **Temporal Effects**: February exclusion may affect seasonality
- **Segment Imbalance**: VOLT pilot group smaller than control

## LLM Usage Assessment

**Pros**: Scale, consistency, zero-shot classification capability
**Cons**: Results vary between runs, hallucination risk, limited explainability
**Recommendation**: Use as supplementary analysis, not primary decision basis