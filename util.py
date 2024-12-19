import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def bar_plot(df: pd.DataFrame, 
             col1: str, 
             col2: str, 
             title: str, 
             xlabel: str, 
             ylabel: str):
    plt.figure(figsize=(14, 7))
    sns.barplot(data=df, x=col1, y=col2, palette="magma")
    plt.title(title, fontsize=16)
    plt.xlabel(xlabel, fontsize=14)
    plt.ylabel(ylabel, fontsize=14)
    plt.xticks(rotation=0, ha="center")

    for index, row in df.iterrows():
        plt.text(index, row[col2] + 7, f"{row[col2]:,}", 
                color="black", ha="center", fontsize=12)

    plt.tight_layout()
    plt.show()
    
def box_plot(df: pd.DataFrame, 
             col1: str, 
             col2: str, 
             title: str, 
             xlabel: str, 
             ylabel: str, 
             ordered_levels: list):
    plt.figure(figsize=(14, 7))
    sns.boxplot(x=col1, y=col2, data=df, orient="h", palette="magma", order=ordered_levels)
    plt.title(title, fontsize=16)
    plt.xlabel(xlabel, fontsize=14)
    plt.ylabel(ylabel, fontsize=14)
    plt.xticks(range(10, 50, 5), rotation=0, ha="center")
    plt.tight_layout()
    plt.show()
    
def violin_plot(df: pd.DataFrame, 
                col1: str, 
                col2: str, 
                title: str, 
                xlabel: str, 
                ylabel: str, 
                ordered_levels: list):
    plt.figure(figsize=(14, 7))
    sns.violinplot(x=col1, y=col2, data=df, palette="magma", order=ordered_levels)
    plt.title(title, fontsize=16)
    plt.xlabel(xlabel, fontsize=14)
    plt.ylabel(ylabel, fontsize=14)
    plt.xticks(rotation=0, ha="center")
    plt.tight_layout()
    plt.show()
    
def count_plot(df: pd.DataFrame, 
               col1: str, 
               col2: str, 
               title: str, 
               xlabel: str, 
               ylabel: str, 
               ordered_levels: list, 
               legend_title: str):
    plt.figure(figsize=(14, 7))
    sns.countplot(x=col1, hue=col2, data=df, palette="magma", order=ordered_levels)
    plt.title(title, fontsize=16)
    plt.xlabel(xlabel, fontsize=14)
    plt.ylabel(ylabel, fontsize=14)
    plt.xticks(rotation=0, ha="center")
    plt.legend(title=legend_title)
    plt.tight_layout()
    plt.show()
    
def hist_plot(df: pd.DataFrame, 
              col: str,
              title: str, 
              xlabel: str, 
              ylabel: str,
              xline: int,
              yline: int,
              xlinelabel: str,
              ylinelabel: str):
    plt.figure(figsize=(14, 7))
    sns.histplot(data=df, x=col, bins=50, kde=True, color= "#5B0C84")
    plt.axvline(xline, color="red", linestyle="--", linewidth=1, label=xlinelabel)
    plt.axvline(yline, color="green", linestyle="--", linewidth=1, label=ylinelabel)
    plt.title(title, fontsize=16)
    plt.xlabel(xlabel, fontsize=14)
    plt.ylabel(ylabel, fontsize=14)
    plt.legend()
    plt.xlim(df[col].min(), df[col].max())

    counts, bins, patches = plt.hist(df[col], bins=25, color= "#5B0C84" , alpha=0.7)
    for count, patch in zip(counts, patches):
        if count > 0:
            plt.text(patch.get_x() + patch.get_width() / 2, count, int(count), ha="center", va="bottom", fontsize=8)

    plt.tight_layout()
    plt.show()
    
def correlation_heatmap(df: pd.DataFrame, title: str):
    plt.figure(figsize=(12, 8))
    numerical_cols = df.select_dtypes(include=["int64", "float64"]).columns
    correlation_matrix = df[numerical_cols].corr()
    sns.heatmap(correlation_matrix, annot=True, cmap="magma", fmt=".2f", linewidths=0.5)
    plt.title(title, fontsize=16)
    plt.tight_layout()
    plt.show()