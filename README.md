# Portfolio Optimization Paradox: Master Thesis Analysis & Code Appendix

Hunter Bell  
Master of Finance  
Frankfurt School of Finance & Management  
August 2024

## Abstract

This repository contains the complete analytical framework and empirical analysis code for my master thesis examining the portfolio optimization paradox in commercial banks' climate finance implementation. The analysis reveals how emerging market banks achieve substantial green finance portfolios through directive regulatory mechanisms despite minimal adoption of international climate frameworks, while developed market banks show high framework adoption but limited implementation effectiveness.

## Key Findings

### The Central Paradox

1. **Implementation Without Adoption**: Chinese banks demonstrate $1,692B in green credit portfolios while maintaining minimal framework adoption (average score: 0.19)

2. **Adoption Without Implementation**: NZBA members show comprehensive framework adoption (average score: 0.85) while maintaining $149B in fossil fuel financing

3. **Regulatory Effectiveness Gap**: Directive mechanisms achieve 72.2% implementation effectiveness versus 57.7% for market-based mechanisms (24.6 pp gap)

4. **Statistical Evidence**: Near-zero correlation (r = 0.12) between framework adoption and sustainable finance intensity

## Repository Structure

```text
Data/
├── Analysis/
│   ├── Scripts/                    # All analysis code and notebooks
│   │   ├── data_processing.py      # Real data loading and processing
│   │   ├── thesis_analysis.py      # Main empirical analysis
│   │   ├── grouped_figures.py      # Multi-panel visualizations
│   │   ├── individual_figures.py   # Individual charts for thesis
│   │   ├── complete_analysis.ipynb # Comprehensive analysis notebook
│   │   ├── enhanced_fi_integration.ipynb # Financial institution coverage
│   │   ├── visualization_suite.ipynb # Visualization development
│   │   └── voluntary_vs_directive_analysis.ipynb # Regulatory comparison
│   │
│   ├── Figures/
│   │   ├── individual/             # 12 individual charts without titles
│   │   └── grouped/                # 6 multi-panel figures with titles
│   │
│   └── results/                    # Analysis outputs and statistical results
│
└── Raw Data Files/
    ├── GREEN_BONDS_RAW_DATA.csv    # Included on request -- 23,569 bond records from Refinitiv
    ├── GREEN_LOANS_RAW_DATA.csv    # Included on request -- 6,899 loan records from Refinitiv
    ├── SBTiTargetDashboard30082025.xlsx # SBTi targets database
    └── SUSTAINABILITY_LINKED_LOANS.xlsx # Included on request -- SLL market data
```

## Code Organization

### 1. Main Analysis (`thesis_analysis.py`)

Primary empirical analysis examining the paradox between framework adoption and implementation effectiveness. Includes:
- Portfolio composition analysis for Chinese Big Four banks
- NZBA member fossil fuel vs green finance comparison
- Regulatory mechanism effectiveness scoring
- Statistical correlation testing
- Temporal evolution analysis (2014-2024)

### 2. Data Processing (`data_processing.py`)

Loads and processes actual Refinitiv data exports:
- Processes 23,569 bond records and 6,899 loan records
- Extracts real bank portfolios from issuer names
- Calculates temporal evolution showing 60% CAGR
- Key finding: JPMorgan has $553B in green bonds, BOC leads Chinese banks with $544.6B

### 3. Visualization Scripts

**`grouped_figures.py`**  
Generates 6 multi-panel figures for thesis presentation, including:
- Portfolio optimization paradox scatter plot
- Implementation gap by regulatory mechanism
- Temporal evolution of global climate finance
- Capacity constraints analysis
- NZBA paradox visualization
- Regulatory comparison (voluntary vs directive)

**`individual_figures.py`**  
Produces 12 individual charts for thesis integration without titles, using descriptive filenames for easy reference.

### 4. Supporting Notebooks

Interactive Jupyter notebooks used for exploratory analysis and methodology development:
- `complete_analysis.ipynb`: Comprehensive analysis workflow with real data integration
- `voluntary_vs_directive_analysis.ipynb`: Regulatory mechanism comparison
- `visualization_suite.ipynb`: Figure development and testing
- `enhanced_fi_integration.ipynb`: Financial institution data integration

## Methodology

### Implementation Effectiveness Score

Composite measure incorporating:
- Green finance portfolio size relative to total assets
- Year-over-year growth in sustainable finance
- Reduction in high-carbon asset exposure
- Policy implementation completeness

### Framework Adoption Score

Binary scoring across four major frameworks:
- Science Based Targets initiative (SBTi)
- Net-Zero Banking Alliance (NZBA)
- Task Force on Climate-related Financial Disclosures (TCFD)
- Principles for Responsible Banking (PRB)

### Implementation Authenticity Index (IAI)

PCA-derived weights applied to:
- Repeat issuance rate (w=0.35)
- KPI achievement rate (w=0.40)
- Green premium persistence (w=0.25)

### Statistical Methods

- Pearson/Spearman correlation for framework-implementation relationship
- Two-sample t-tests for regulatory mechanism comparison
- Panel regression with fixed effects for temporal analysis
- Variance decomposition for implementation gap factors

## Data Sources & Processing

All data sourced from Refinitiv Eikon unless otherwise noted:

- **Green Bonds & Loans**: Complete transaction-level data (2014-2024) from Refinitiv
- **Bank Portfolios**: Extracted from issuer names in bond/loan records
- **SBTi Targets**: Science Based Targets initiative official database
- **NZBA Commitments**: Net-Zero Banking Alliance member data
- **Fossil Fuel Financing**: Banking on Climate Chaos annual reports
- **Financial Statements**: Bank annual reports (2014-2024)

### Data Processing Pipeline

All data processing follows standardized procedures:
1. Import from Refinitiv data exports (CSV format)
2. Currency conversion to USD using period-end rates
3. Outlier detection using interquartile range method
4. Missing data handling through forward-fill for time series

## Running the Analysis

### Requirements

```bash
pip install pandas numpy matplotlib seaborn scipy jupyter
```

### Execute Analysis

```bash
cd Analysis/Scripts

# Process raw data
python data_processing.py    # Load and process Refinitiv data

# Run main empirical analysis
python thesis_analysis.py

# Generate visualizations
python grouped_figures.py    # Multi-panel figures with titles
python individual_figures.py # Individual charts without titles
```

### Jupyter Notebooks

```bash
cd Analysis/Scripts
jupyter notebook complete_analysis.ipynb
```

## Key Results

### Temporal Evolution (2014-2024)

- Global green debt market: $4.5B → $891.1B (60% CAGR)
- China's market share: 17.0% → 87.1%
- SBTi financial institutions: 0 → 150
- NZBA membership: 0 → 143 (since 2021)

### Implementation Gap Decomposition (24.6 pp total)

- Pure regulatory effect: 15.2 pp (62%)
- Capacity interaction: 7.1 pp (29%)
- Development priority: 2.3 pp (9%)

### Bank-Level Findings

**Chinese Big Four (Non-NZBA)**
- BOC: $544.6B green portfolio
- ICBC: $167.5B green portfolio
- CCB: $85.7B green portfolio
- ABC: $37.3B green portfolio

**Major NZBA Members**
- JPMorgan: $553.0B green, $40.8B fossil fuel
- Bank of America: $15.0B green, $32.2B fossil fuel
- Citigroup: $10.0B green, $28.9B fossil fuel
- Wells Fargo: $8.0B green, $24.5B fossil fuel
- HSBC: $4.8B green, $22.6B fossil fuel

### Results Files

Analysis outputs are saved to `results/` directory:
- `thesis_analysis_results.csv`: Summary statistics and key findings
- `bank_analysis_data.csv`: Bank-level panel data
- `consolidated_analysis_results.csv`: Comprehensive results
- `temporal_evolution_data.csv`: Time series data
- `regulatory_framework_data.csv`: Regulatory mechanism comparison


## Computational Environment

Analysis conducted using:
- Python 3.8+
- pandas 1.3.3
- numpy 1.21.2
- matplotlib 3.4.3
- seaborn 0.11.2
- scipy 1.7.1

## Reproducibility

To reproduce the complete analysis:

```bash
# Install requirements
pip install pandas numpy matplotlib seaborn scipy

# Navigate to Scripts directory
cd Analysis/Scripts

# Run complete analysis pipeline
python data_processing.py
python thesis_analysis.py
python grouped_figures.py
python individual_figures.py
```

## Author Contact

Hunter Bell  
Master of Finance Candidate  
Frankfurt School of Finance & Management  
Email: hunter.bell@fs-students.de


## License

This analysis is provided for academic transparency and reproducibility. All code and analysis are original work by Hunter Bell for the master thesis at Frankfurt School of Finance & Management using public data in conjuction with privileged data from the LSEG. Please cite appropriately if using these materials for research purposes.

---

*This code is provided as supplementary material for the master thesis submitted by Hunter Bell to Frankfurt School of Finance & Management in partial fulfillment of the requirements for the degree of Master of Finance, August 2024.*
