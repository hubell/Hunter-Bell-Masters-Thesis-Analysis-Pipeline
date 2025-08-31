#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Grouped Visualization Framework
Multi-panel figures for thesis presentation

Hunter Bell
Frankfurt School of Finance & Management
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os
import warnings
warnings.filterwarnings('ignore')

# Import data processing to get real data
from data_processing import load_green_bonds, calculate_bank_portfolios, process_temporal_evolution

# Figure configuration
plt.style.use('seaborn-v0_8-whitegrid')
sns.set_palette("husl")
plt.rcParams['figure.figsize'] = (12, 8)
plt.rcParams['font.size'] = 11
plt.rcParams['font.family'] = 'serif'
plt.rcParams['axes.labelsize'] = 12
plt.rcParams['axes.titlesize'] = 14
plt.rcParams['xtick.labelsize'] = 10
plt.rcParams['ytick.labelsize'] = 10
plt.rcParams['legend.fontsize'] = 10

# Output directory
fig_dir = 'Figures/grouped'
if not os.path.exists(fig_dir):
    os.makedirs(fig_dir)

print("Generating grouped figures...")
print(f"Output directory: {fig_dir}/")

# Figure 1: Portfolio Paradox
print("\nFigure 1: Portfolio Optimization Paradox")

# Load real data
df_bonds = load_green_bonds()
bank_portfolios = calculate_bank_portfolios(df_bonds)

# Combine real portfolio data with framework scores
banks_data = {
    'ICBC': {'Green_Portfolio': bank_portfolios.get('ICBC', {}).get('green_portfolio', 167.5), 
             'Framework_Score': 0.05, 'Region': 'China'},
    'ABC': {'Green_Portfolio': bank_portfolios.get('ABC', {}).get('green_portfolio', 37.3), 
            'Framework_Score': 0.00, 'Region': 'China'},
    'CCB': {'Green_Portfolio': bank_portfolios.get('CCB', {}).get('green_portfolio', 85.7), 
            'Framework_Score': 0.11, 'Region': 'China'},
    'BOC': {'Green_Portfolio': bank_portfolios.get('BOC', {}).get('green_portfolio', 544.6), 
            'Framework_Score': 0.12, 'Region': 'China'},
    'HSBC': {'Green_Portfolio': bank_portfolios.get('HSBC', {}).get('green_portfolio', 4.8), 
             'Framework_Score': 0.78, 'Region': 'UK'},
    'BNP Paribas': {'Green_Portfolio': bank_portfolios.get('BNP Paribas', {}).get('green_portfolio', 19.3), 
                    'Framework_Score': 0.82, 'Region': 'EU'},
    'JPMorgan': {'Green_Portfolio': bank_portfolios.get('JPMorgan', {}).get('green_portfolio', 553.0), 
                 'Framework_Score': 0.65, 'Region': 'US'},
    'Banco do Brasil': {'Green_Portfolio': 38, 'Framework_Score': 0.31, 'Region': 'Brazil'},
    'SBI': {'Green_Portfolio': 62, 'Framework_Score': 0.28, 'Region': 'India'},
    'MUFG': {'Green_Portfolio': 41, 'Framework_Score': 0.71, 'Region': 'Japan'}
}

df_paradox = pd.DataFrame.from_dict(banks_data, orient='index')
df_paradox['Paradox_Ratio'] = df_paradox['Green_Portfolio'] / (df_paradox['Framework_Score'] + 0.01)

fig, ax = plt.subplots(figsize=(14, 10))

region_colors = {
    'China': '#E74C3C', 'EU': '#3498DB', 'US': '#2ECC71',
    'UK': '#9B59B6', 'Brazil': '#F39C12', 'India': '#E67E22', 'Japan': '#1ABC9C'
}

for bank, data in df_paradox.iterrows():
    ax.scatter(data['Framework_Score'], data['Green_Portfolio'], 
              s=300, alpha=0.7, color=region_colors[data['Region']],
              edgecolors='black', linewidth=1.5)
    offset_x = 0.02 if data['Framework_Score'] < 0.5 else -0.02
    offset_y = 15 if data['Green_Portfolio'] < 250 else -15
    ax.annotate(bank, (data['Framework_Score'], data['Green_Portfolio']),
               xytext=(data['Framework_Score'] + offset_x, data['Green_Portfolio'] + offset_y),
               fontsize=9, fontweight='bold')

ax.axvline(x=0.5, color='gray', linestyle='--', alpha=0.5)
ax.axhline(y=200, color='gray', linestyle='--', alpha=0.5)

ax.text(0.15, 50, 'Low Implementation\nLow Adoption', 
        ha='center', va='center', fontsize=11, alpha=0.7, style='italic')
ax.text(0.85, 50, 'Low Implementation\nHigh Adoption', 
        ha='center', va='center', fontsize=11, alpha=0.7, style='italic')
ax.text(0.25, 450, 'High Implementation\nLow Adoption', 
        ha='center', va='center', fontsize=11, alpha=0.7, style='italic')
ax.text(0.75, 450, 'High Implementation\nHigh Adoption', 
        ha='center', va='center', fontsize=11, alpha=0.7, style='italic')

ax.set_xlabel('Framework Adoption Score (0 = None, 1 = Full)', fontsize=12, fontweight='bold')
ax.set_ylabel('Green Portfolio Size (Billion USD)', fontsize=12, fontweight='bold')
ax.set_title('The Portfolio Optimization Paradox:\nImplementation Without Adoption vs. Adoption Without Implementation',
            fontsize=14, fontweight='bold', pad=20)

legend_elements = [plt.scatter([], [], s=200, color=color, alpha=0.7, 
                              edgecolors='black', linewidth=1.5, label=region)
                  for region, color in region_colors.items()]
ax.legend(handles=legend_elements, title='Region', loc='upper right', frameon=True)

ax.grid(True, alpha=0.3)
ax.set_xlim(-0.05, 1.05)
ax.set_ylim(0, 500)

plt.tight_layout()
plt.savefig(os.path.join(fig_dir, 'fig1_portfolio_paradox.png'), dpi=300, bbox_inches='tight')
print(f"✓ Figure 1 saved: {fig_dir}/fig1_portfolio_paradox.png")
plt.close()

# Figure 2: Implementation Gap
print("\nFigure 2: Implementation Gap Analysis")

regulatory_data = {
    'China': {'Type': 'Directive', 'Score': 82.5, 'Volume': 3050},
    'India': {'Type': 'Directive', 'Score': 68.3, 'Volume': 300},
    'Brazil': {'Type': 'Directive', 'Score': 65.7, 'Volume': 170},
    'EU': {'Type': 'Market-Based', 'Score': 57.9, 'Volume': 420},
    'UK': {'Type': 'Market-Based', 'Score': 61.2, 'Volume': 180},
    'US': {'Type': 'Market-Based', 'Score': 52.4, 'Volume': 310},
    'Japan': {'Type': 'Market-Based', 'Score': 59.3, 'Volume': 135},
    'South Korea': {'Type': 'Hybrid', 'Score': 71.8, 'Volume': 95},
    'Singapore': {'Type': 'Hybrid', 'Score': 64.5, 'Volume': 75}
}

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 8))

markets = list(regulatory_data.keys())
scores = [regulatory_data[m]['Score'] for m in markets]
volumes = [regulatory_data[m]['Volume'] for m in markets]
types = [regulatory_data[m]['Type'] for m in markets]

type_colors = {'Directive': '#E74C3C', 'Market-Based': '#3498DB', 'Hybrid': '#2ECC71'}
colors = [type_colors[t] for t in types]

# Plot 1: Implementation Scores
bars1 = ax1.bar(markets, scores, color=colors, alpha=0.7, edgecolor='black', linewidth=1.5)
ax1.set_ylabel('Implementation Effectiveness Score (%)', fontweight='bold')
ax1.set_title('Implementation Effectiveness by Regulatory Mechanism', fontweight='bold', pad=15)
ax1.set_ylim(0, 100)

directive_avg = np.mean([s for s, t in zip(scores, types) if t == 'Directive'])
market_avg = np.mean([s for s, t in zip(scores, types) if t == 'Market-Based'])
ax1.axhline(y=directive_avg, color='#E74C3C', linestyle='--', alpha=0.8, linewidth=2,
           label=f'Directive Avg: {directive_avg:.1f}%')
ax1.axhline(y=market_avg, color='#3498DB', linestyle='--', alpha=0.8, linewidth=2,
           label=f'Market-Based Avg: {market_avg:.1f}%')

for bar, score in zip(bars1, scores):
    height = bar.get_height()
    ax1.text(bar.get_x() + bar.get_width()/2., height + 1,
            f'{score:.1f}', ha='center', va='bottom', fontweight='bold', fontsize=9)

ax1.legend(loc='upper right')
ax1.grid(True, alpha=0.3, axis='y')
ax1.set_xticklabels(markets, rotation=45, ha='right')

# Plot 2: Portfolio Volumes
bars2 = ax2.bar(markets, volumes, color=colors, alpha=0.7, edgecolor='black', linewidth=1.5)
ax2.set_ylabel('Green Finance Portfolio (Billion USD)', fontweight='bold')
ax2.set_title('Green Finance Volume by Market', fontweight='bold', pad=15)

ax2.grid(True, alpha=0.3, axis='y')
ax2.set_xticklabels(markets, rotation=45, ha='right')

plt.tight_layout()
plt.savefig(os.path.join(fig_dir, 'fig2_implementation_gap.png'), dpi=300, bbox_inches='tight')
print(f"✓ Figure 2 saved: {fig_dir}/fig2_implementation_gap.png")
plt.close()

# Figure 3: Temporal Evolution
print("\nFigure 3: Temporal Evolution")

# Get real temporal data
years_list, global_volumes, china_volumes = process_temporal_evolution(df_bonds)
years = np.array(years_list)
global_green_debt = np.array(global_volumes)
china_green_credit = np.array(china_volumes)

# Framework adoption (these remain as reported)
sbti_fis = np.array([0, 2, 3, 5, 8, 12, 28, 52, 89, 127, 150])
nzba_members = np.array([0, 0, 0, 0, 0, 0, 0, 43, 98, 131, 143])

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(14, 12))

# Top panel: Global trends
ax1_twin = ax1.twinx()

line1 = ax1.plot(years, global_green_debt, 'o-', color='#2ECC71', linewidth=3, 
                 markersize=8, label='Global Green Debt')
ax1.set_ylabel('Global Green Debt (Billion USD)', color='#2ECC71', fontweight='bold')
ax1.tick_params(axis='y', labelcolor='#2ECC71')

line2 = ax1_twin.plot(years, sbti_fis, 's-', color='#3498DB', linewidth=2, 
                     markersize=7, label='SBTi FIs', alpha=0.8)
line3 = ax1_twin.plot(years, nzba_members, '^-', color='#9B59B6', linewidth=2, 
                     markersize=7, label='NZBA Members', alpha=0.8)
ax1_twin.set_ylabel('Framework Adoption (Count)', color='#34495E', fontweight='bold')

ax1.set_xlabel('Year', fontweight='bold')
ax1.set_title('Global Climate Finance Evolution: Volume vs. Framework Adoption (2014-2024)', 
             fontweight='bold', pad=15)
ax1.grid(True, alpha=0.3)
ax1.set_xlim(2013.5, 2024.5)

lines = line1 + line2 + line3
labels = [l.get_label() for l in lines]
ax1.legend(lines, labels, loc='upper left')

# Bottom panel: China comparison
ax2.bar(years, china_green_credit, color='#E74C3C', alpha=0.7, 
       edgecolor='black', linewidth=1.5, label='China Green Credit')
ax2.bar(years, global_green_debt - china_green_credit, bottom=china_green_credit,
       color='#95A5A6', alpha=0.7, edgecolor='black', linewidth=1.5, 
       label='Rest of World')

ax2.set_xlabel('Year', fontweight='bold')
ax2.set_ylabel('Volume (Billion USD)', fontweight='bold')
ax2.set_title('China\'s Share of Global Green Finance (2014-2024)', fontweight='bold', pad=15)
ax2.legend(loc='upper left')
ax2.grid(True, alpha=0.3, axis='y')
ax2.set_xlim(2013.5, 2024.5)

plt.tight_layout()
plt.savefig(os.path.join(fig_dir, 'fig3_temporal_evolution.png'), dpi=300, bbox_inches='tight')
print(f"✓ Figure 3 saved: {fig_dir}/fig3_temporal_evolution.png")
plt.close()

# Figure 4: Capacity Constraints
print("\nFigure 4: Capacity Constraints")

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 8))

# Left panel: Capacity Constraints
constraints = ['Technology\nAccess', 'Knowledge\nCapacity', 'Finance\nAccess', 'Development\nPriority']
coefficients = [-2.31, -1.89, -1.45, -0.92]
std_errors = [0.42, 0.38, 0.31, 0.28]

bars1 = ax1.bar(constraints, coefficients, yerr=std_errors, capsize=5,
               color=['#E74C3C', '#3498DB', '#2ECC71', '#F39C12'], 
               alpha=0.7, edgecolor='black', linewidth=1.5)

ax1.set_ylabel('Coefficient Value', fontweight='bold')
ax1.set_title('Capacity Constraints Impact on Implementation', fontweight='bold', pad=15)
ax1.axhline(y=0, color='black', linestyle='-', alpha=0.3)
ax1.grid(True, alpha=0.3, axis='y')

for bar, coef in zip(bars1, coefficients):
    height = bar.get_height()
    ax1.text(bar.get_x() + bar.get_width()/2., height - 0.1,
            f'{coef:.2f}', ha='center', va='top', fontweight='bold', fontsize=10)

# Right panel: Implementation Authenticity
countries = ['China', 'EU', 'India', 'US', 'Brazil']
iai_scores = [0.76, 0.71, 0.66, 0.68, 0.61]
mechanism_types = ['Directive', 'Market-Based', 'Hybrid', 'Market-Based', 'Directive']
colors_iai = ['#E74C3C' if m == 'Directive' else '#3498DB' if m == 'Market-Based' else '#2ECC71' 
              for m in mechanism_types]

bars2 = ax2.bar(countries, iai_scores, color=colors_iai, alpha=0.7, 
               edgecolor='black', linewidth=1.5)

ax2.set_ylabel('Implementation Authenticity Index', fontweight='bold')
ax2.set_title('Implementation Authenticity Index by Country', fontweight='bold', pad=15)
ax2.set_ylim(0, 1)
ax2.axhline(y=0.7, color='gray', linestyle='--', alpha=0.5, label='Threshold')
ax2.grid(True, alpha=0.3, axis='y')

for bar, score in zip(bars2, iai_scores):
    height = bar.get_height()
    ax2.text(bar.get_x() + bar.get_width()/2., height + 0.01,
            f'{score:.2f}', ha='center', va='bottom', fontweight='bold', fontsize=10)

ax2.legend()

plt.tight_layout()
plt.savefig(os.path.join(fig_dir, 'fig4_capacity_constraints.png'), dpi=300, bbox_inches='tight')
print(f"✓ Figure 4 saved: {fig_dir}/fig4_capacity_constraints.png")
plt.close()

# Figure 5: NZBA Paradox
print("\nFigure 5: NZBA Paradox")

fig, ax = plt.subplots(figsize=(14, 10))

banks = ['JPMorgan\nChase', 'Bank of\nAmerica', 'Citigroup', 'Wells\nFargo', 'HSBC',
        'ICBC', 'BOC', 'ABC', 'CCB']
fossil_finance = [40.8, 32.2, 28.9, 24.5, 22.6, 0, 0, 0, 0]

# Use real green finance data
green_finance = [
    bank_portfolios.get('JPMorgan', {}).get('green_portfolio', 553.0),
    bank_portfolios.get('Bank of America', {}).get('green_portfolio', 7.4),
    bank_portfolios.get('Citigroup', {}).get('green_portfolio', 50.3),
    8,  # Wells Fargo not in data
    bank_portfolios.get('HSBC', {}).get('green_portfolio', 4.8),
    bank_portfolios.get('ICBC', {}).get('green_portfolio', 167.5),
    bank_portfolios.get('BOC', {}).get('green_portfolio', 544.6),
    bank_portfolios.get('ABC', {}).get('green_portfolio', 37.3),
    bank_portfolios.get('CCB', {}).get('green_portfolio', 85.7)
]
nzba_member = [True, True, True, True, True, False, False, False, False]

x_pos = np.arange(len(banks))
width = 0.35

bars1 = ax.bar(x_pos - width/2, fossil_finance, width, label='Fossil Fuel Finance',
              color='#E74C3C', alpha=0.7, edgecolor='black', linewidth=1.5)
bars2 = ax.bar(x_pos + width/2, green_finance, width, label='Green Finance',
              color='#2ECC71', alpha=0.7, edgecolor='black', linewidth=1.5)

for i, (bank, member) in enumerate(zip(banks, nzba_member)):
    if member:
        ax.text(i, -15, '✓', ha='center', fontsize=12, fontweight='bold', color='#3498DB')

ax.set_xlabel('Financial Institution', fontweight='bold')
ax.set_ylabel('Finance Volume (Billion USD)', fontweight='bold')
ax.set_title('The NZBA Paradox: Fossil Fuel Financing vs. Green Finance Portfolios',
            fontweight='bold', pad=15)
ax.set_xticks(x_pos)
ax.set_xticklabels(banks)
ax.legend(loc='upper right')

ax.axvline(x=4.5, color='black', linestyle='--', alpha=0.5, linewidth=2)
ax.text(2, 450, 'NZBA Members', ha='center', fontsize=11, fontweight='bold', alpha=0.7)
ax.text(6.5, 450, 'Non-NZBA Chinese Banks', ha='center', fontsize=11, fontweight='bold', alpha=0.7)

ax.set_ylim(0, 500)
ax.grid(True, alpha=0.3, axis='y')

plt.tight_layout()
plt.savefig(os.path.join(fig_dir, 'fig5_nzba_paradox.png'), dpi=300, bbox_inches='tight')
print(f"✓ Figure 5 saved: {fig_dir}/fig5_nzba_paradox.png")
plt.close()

# Figure 6: Voluntary vs Directive
print("\nFigure 6: Regulatory Comparison")

fig, axes = plt.subplots(2, 2, figsize=(15, 12))

# Panel 1: Implementation Effectiveness
ax1 = axes[0, 0]
regulatory_types = ['Directive\n(China)', 'Hybrid\n(India)', 'Mixed\n(Brazil)', 'Market-Based\n(US/EU)']
effectiveness_scores = [82.5, 68.3, 65.7, 57.9]
colors_reg = ['#2E7D32', '#558B2F', '#F57C00', '#C62828']

bars1 = ax1.bar(regulatory_types, effectiveness_scores, color=colors_reg)
ax1.set_ylabel('Implementation Effectiveness (%)', fontsize=12)
ax1.set_title('Implementation Effectiveness by Regulatory Mechanism', fontsize=14, fontweight='bold')
ax1.axhline(y=np.mean(effectiveness_scores), color='gray', linestyle='--', alpha=0.5, label='Average')
ax1.set_ylim([0, 100])

for bar, score in zip(bars1, effectiveness_scores):
    ax1.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 1,
             f'{score:.1f}%', ha='center', va='bottom', fontweight='bold')

# Panel 2: Portfolio Optimization Paradox
ax2 = axes[0, 1]
regions = ['China\nBig 4', 'India\nTop 3', 'Brazil\nTop 3', 'NZBA\nTop 5']
green_volumes = [1692, 78, 115, 150]
framework_adoption = [0.125, 0.33, 0.56, 0.85]

scatter = ax2.scatter(framework_adoption, green_volumes, s=[v*2 for v in green_volumes],
                     c=colors_reg, alpha=0.6, edgecolors='black', linewidths=2)
ax2.set_xlabel('Framework Adoption Rate', fontsize=12)
ax2.set_ylabel('Green Finance Volume (Billion USD)', fontsize=12)
ax2.set_title('The Portfolio Optimization Paradox', fontsize=14, fontweight='bold')

for i, region in enumerate(regions):
    if region == 'China\nBig 4':
        ax2.annotate(region, (framework_adoption[i], green_volumes[i]),
                    xytext=(40, 0), textcoords='offset points', fontsize=12,
                    ha='left', va='center', fontweight='bold')
    elif region in ['India\nTop 3', 'Brazil\nTop 3', 'NZBA\nTop 5']:
        ax2.annotate(region, (framework_adoption[i], green_volumes[i]),
                    xytext=(-15, 15), textcoords='offset points', fontsize=12,
                    ha='right', va='bottom', fontweight='bold')

z = np.polyfit(framework_adoption, green_volumes, 1)
p = np.poly1d(z)
ax2.plot(framework_adoption, p(framework_adoption), "r--", alpha=0.5, label=f'Trend (r=-0.68)')
ax2.legend()
ax2.set_xlim(0, 1.0)
ax2.set_ylim(0, 1900)

# Panel 3: NZBA Members Fossil vs Green
ax3 = axes[1, 0]
banks_nzba = ['JPMorgan', 'BofA', 'Citi', 'Wells Fargo', 'HSBC']
fossil_finance_nzba = [40.8, 32.2, 28.9, 24.5, 22.6]
green_finance_nzba = [12, 15, 10, 8, 35]

x = np.arange(len(banks_nzba))
width = 0.35

bars_fossil = ax3.bar(x - width/2, fossil_finance_nzba, width, label='Fossil Finance', color='#8B0000')
bars_green = ax3.bar(x + width/2, green_finance_nzba, width, label='Green Finance', color='#228B22')

ax3.set_xlabel('NZBA Member Banks', fontsize=12)
ax3.set_ylabel('Finance Volume (Billion USD)', fontsize=12)
ax3.set_title('NZBA Members: Fossil vs Green Finance (2023)', fontsize=14, fontweight='bold')
ax3.set_xticks(x)
ax3.set_xticklabels(banks_nzba, rotation=45, ha='right')
ax3.legend()

# Panel 4: Implementation Gap Decomposition
ax4 = axes[1, 1]
components = ['Pure\nRegulatory', 'Capacity\nInteraction', 'Development\nPriority']
values = [15.2, 7.1, 2.3]
percentages = [62, 29, 9]

bars4 = ax4.bar(components, values, color=['#1565C0', '#7B1FA2', '#C62828'])
ax4.set_ylabel('Contribution to Gap (Percentage Points)', fontsize=12)
ax4.set_title('Implementation Gap Decomposition (24.6pp Total)', fontsize=14, fontweight='bold')

for bar, val, pct in zip(bars4, values, percentages):
    ax4.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.2,
             f'{val:.1f}pp\n({pct}%)', ha='center', va='bottom', fontweight='bold')

ax4.set_ylim(0, 18)

plt.tight_layout()
plt.savefig(os.path.join(fig_dir, 'fig6_voluntary_vs_directive.png'), dpi=300, bbox_inches='tight')
print(f"✓ Figure 6 saved: {fig_dir}/fig6_voluntary_vs_directive.png")
plt.close()

print("\nAll grouped figures generated successfully.")
print(f"Location: {fig_dir}/")