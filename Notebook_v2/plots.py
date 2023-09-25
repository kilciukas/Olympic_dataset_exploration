import numpy as np
import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt

class BarPlot:
    def __init__(self, x=None, y=None, data=None):
        self.x = x
        self.y = y
        self.data = data
        self.figure = None
    
    def create_bar_plot(self, palette, title=None, figsize=(15,20)):
        self.figure = plt.figure(figsize=figsize)
        sns.set(style='darkgrid')
        sns.barplot(x=self.x, y=self.y, data=self.data, palette=palette)
        plt.xlabel(self.x)
        plt.ylabel(self.y)
        plt.title(title)
        return self.figure
    
    @staticmethod
    def annotate_bars(barplot, fontsize=10, color='black'):
        for bar in barplot.patches:
            barplot.annotate(f'{bar.get_width():.0f}', (bar.get_width(), bar.get_y() + bar.get_height() / 2),
                             ha='left', va='center', fontsize=fontsize, color=color)
            

class LinePlot:
    def __init__(self, x=None, y=None, data=None):
        self.x = x
        self.y = y
        self.data = data
        self.figure = None
    
    def create_line_plot(self, marker='o', color='green', title=None):
        self.figure = plt.figure(figsize=(10,5))
        sns.lineplot(data=self.data, x=self.x, y=self.y, marker=marker, color=color)
        plt.xlabel(self.x)
        plt.ylabel(self.y)
        plt.title(title)
        
        plt.grid(True, linestyle='--', alpha=0.7)
        return self.figure
    
    def configure_xticks(self, step, min_year, max_year):
        plt.xticks(range(min_year, max_year+1, step), rotation=90)


class Heatmap:
    def __init__(self, data=None, index=None, columns=None, figsize=(5, 5), cmap='summer', annot=True, fmt='d', linewidths=0.5, xlabel=None, ylabel=None, title=None):
        self.data = data
        self.index = index
        self.columns = columns
        self.figsize = figsize
        self.cmap = cmap
        self.annot = annot
        self.fmt = fmt
        self.linewidths = linewidths
        self.xlabel = xlabel
        self.ylabel = ylabel
        self.title = title

    def create_heatmap(self):
        plt.figure(figsize=self.figsize)
        sns.heatmap(self.data, cmap=self.cmap, annot=self.annot, fmt=self.fmt, linewidths=self.linewidths, square=self.square)
        
        if self.xlabel:
            plt.xlabel(self.xlabel)
        if self.ylabel:
            plt.ylabel(self.ylabel)
        if self.title:
            plt.title(self.title)
    
    def configure_labels(self, x_label_size, y_label_size, label_position):
        if label_position:
            self.label_position = label_position  # Set the label position if provided
        plt.xticks(fontsize=x_label_size)
        plt.yticks(fontsize=y_label_size)

        if self.label_position == 'bottom':
            plt.gca().xaxis.tick_bottom()
            plt.gca().xaxis.set_label_position('bottom')
        elif self.label_position == 'top':
            plt.gca().xaxis.tick_top()
            plt.gca().xaxis.set_label_position('top')