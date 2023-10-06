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
    
    def configure_xticks(self, step, min, max):
        plt.xticks(range(min, max+1, step))

    def configure_yticks(self, step, min, max):
        plt.yticks(range(min, max+1, step))
            

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

    def configure_yticks(self, step, min, max):
        plt.yticks(range(min, max+1, step), rotation=90)

    def regline(self,):
        sns.regplot(data=self.data, x=self.x, y=self.y, scatter=False, ci=False, ax=plt.gca())


class Heatmap:
    def __init__(self, data=None, index=None, columns=None, figsize=(5, 5), cmap='summer', annot=True, fmt='d', linewidths=0.8, xlabel=None, ylabel=None, title=None, square=True, label_position=None):
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
        self.square = square
        self.label_position = label_position


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
            self.label_position = label_position
        plt.xticks(fontsize=x_label_size)
        plt.yticks(fontsize=y_label_size)

        if self.label_position == 'bottom':
            plt.gca().xaxis.tick_bottom()
            plt.gca().xaxis.set_label_position('bottom')
        elif self.label_position == 'top':
            plt.gca().xaxis.tick_top()
            plt.gca().xaxis.set_label_position('top')


class GroupedBarPlot:
    def __init__(self, data1, data2, labels, label1, label2):
        self.data1 = data1
        self.data2 = data2
        self.labels = labels
        self.label1 = label1
        self.label2 = label2

    def set_legend_labels(self, label1, label2):
            self.label1 = label1
            self.label2 = label2

    def create_bar_plot(self, title, xlabel, ylabel, figsize=(12, 6)):

        indices = np.arange(len(self.labels))

        bar_width = 0.35

        fig, ax = plt.subplots(figsize=figsize)
        bars1 = ax.bar(indices - bar_width/2, self.data1, bar_width, label=self.label1)
        bars2 = ax.bar(indices + bar_width/2, self.data2, bar_width, label=self.label2)

        ax.set_xticks(indices)
        ax.set_xticklabels(self.labels, rotation=90)

        ax.set_xlabel(xlabel)
        ax.set_ylabel(ylabel)
        ax.set_title(title)

        ax.legend()


    def adjust_yticks(self, min, max, step):
        plt.yticks(range(min, max+1, step))



class Catplot:
    def __init__(self, data, x, y, jitter=False, size=10):
        self.data = data
        self.x = x
        self.y = y
        self.jitter = jitter
        self.size = size
        self.figure = None
    
    def create_catplot(self, title, figsize = (10,5)):
        self.figure = plt.figure(figsize=figsize)
        sns.catplot(data=self.data, x=self.x, y=self.y, jitter=self.jitter, size=self.size)
        plt.title(title)
        return self.figure
    
    def set_ylim_ticks(self, ylim_min, ylim_max, min, max, step, rotation):
        plt.ylim(ylim_min, ylim_max)
        plt.yticks(range(min, max+1, step))
        plt.xticks(rotation=rotation)


class ScatterPlot:
    def __init__(self, data, x, y, hue = None):
        self.data = data
        self.x = x
        self.y = y
        self.hue = hue
        self.figure = None
    
    def create_scatterplot(self, title, figsize = (10,5)):
        self.figure = plt.figure(figsize=figsize)
        sns.scatterplot(data=self.data, x=self.x, y=self.y, hue=self.hue)
        plt.title(title)
        return self.figure
    
    def set_yticks(self, min, max, step, rotation=None):
        plt.yticks(range(min, max + step, step), rotation=rotation)

    def set_xticks(self, min, max, step, rotation=None):
        plt.xticks(range(min, max + step, step), rotation=rotation)

    

