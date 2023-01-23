import pandas as pd
import numpy as np
import math
import ipywidgets as widgets
from ipywidgets import VBox, Label, HBox 
from IPython.display import display


from pandas_profiling import ProfileReport
from pandas.plotting import scatter_matrix

##Seaborn for fancy plots. 
#%matplotlib inline
import matplotlib.pyplot as plt
import seaborn as sns
plt.rcParams["figure.figsize"] = (8,8)





class edaDF:

##########################################################################
### Once connected to the class edaDF, please start by .user_choice() ####
## And enter what type of Data Exploration you would like to perform  ####
##########################################################################

    # Calss Initial constructor to define:
    # self.data
    # self.target
    # self.cat to define Categorical columns
    #self.num to define Numerical columns
    def __init__(self, data, target):
        self.data=data
        self.target=target
        # Identify Categorical, Numerical, Boolean type Columns
        self.cat=self.data.select_dtypes(exclude=[np.number]) # Categorical Columns
        self.num=self.data.select_dtypes(include=[np.number]) # Numerical Columns
        self.bool=self.data.select_dtypes('bool') # Boolean Column, {True, False}
        print('SUCCESSFULLY CONNECTED TO THE EDAdf')
        print('Please start with .user_input()')
        #print('THIS IS A BASIC EXPLORATORY DATA ANALYSIS: ')
    

    # Method 1: Display .info() of data
    def info(self):
        return self.data.info()
    
    # Method 2: Describe the data
    def describe(self):
        return self.data.describe().T
    
    # Method 3: Describe the data
    def Null_Values(self):
        return self.data.isnull().sum()
    
    # Method 4: Display the Target varaiable
    def giveTarget(self):
        return self.target
    
    # Method 5: Diplay Countplots for Categorical Columns
    def countPlots(self):
        n = len((self.cat).columns)
        cols = 2
        figure, ax = plt.subplots(math.ceil(n/cols), cols, figsize=(20,20))
        r = 0
        c = 0
        for col in (self.cat).columns:
            # https://github.com/mwaskom/seaborn/issues/1582
            splot=sns.countplot(data=self.data, x=col, hue=self.target, ax=ax[r][c])
            for p in splot.patches:
                splot.annotate(format(p.get_height(), '.2f'), (p.get_x() + p.get_width() / 2., p.get_height()),  
                        ha = 'center', va = 'center', xytext = (0, 2), textcoords = 'offset points')
            c += 1
            if c == cols:
                r += 1
                c = 0
        plt.tight_layout()
        return figure
    
    # Method 6: Diplay Histplot for the Numerical Columns
    def histPlots(self, kde=True):
        
        n = len((self.num).columns)
        cols = 2
        figure, ax = plt.subplots(math.ceil(n/cols), cols, figsize=(20,20))
        r = 0
        c = 0
        for col in (self.num):
            if (self.num[col]).nunique() == 2:
                print(f'Variable/Column, {col}, has only 2 UNIQUE values, therefore a  horizontal CountPlot is displayed.')
                print('********************************************************************')
                splot=sns.countplot(data=self.data, x=col, hue=self.target, ax=ax[r][c])
                for p in splot.patches:
                    splot.annotate(format(p.get_height(), '.2f'), (p.get_x() + p.get_width() / 2., p.get_height()),  
                        ha = 'center', va = 'center', xytext = (0, 2), textcoords = 'offset points')
                c+=1
                if c== cols:
                    r+=1
                    c=0
            else:
            #print("r:",r,"c:",c)
                sns.histplot(data=self.data, x=col, hue=self.target, kde=True, ax=ax[r][c])
                c += 1
                if c == cols:
                    r += 1
                    c = 0
        plt.tight_layout()
        plt.show()
        return figure

    # Method 7: Diplay Boxplotx for the Numerical Columns to view outliers
    def Boxplot(self):
        for cols in self.num.columns:
            if self.num[cols].nunique()==2:
                print(f'Column/Variable, {cols} will not have a Boxplot as it only has 2 unique values')
                print()
        
        n = len(self.num.columns)
        cols = 2
        figure, ax = plt.subplots(math.ceil(n/cols), cols, figsize=(20,20))
        r = 0
        c = 0
        for col in self.num.columns:
            if self.num[col].nunique() != 2:
                sns.boxplot(data=self.data, x=col, ax=ax[r][c])
                #counter += 1
                c += 1
                if c == cols:
                    r += 1
                    c = 0
        plt.tight_layout()
        plt.show()
        return figure

    # Method 8: Scatter_Matrix for all Numerical Columns
    def Scatterplot(self):
        #scatter_matrix=sns.pairplot(self.num, corner=True)
        attributes=(self.num).columns
        scatter=scatter_matrix((self.data)[attributes], figsize=(20,20), hist_kwds=None)
        plt.tight_layout()
        plt.show()
        return scatter
   
    # Method 9: Correlation between all Numerical Columns
    def correlation(self):
        self.corr=(self.num).corr(method='spearman')
        return self.corr
    
    # Method 10: Find Top 4 Correlations to Target variable
    def TOP4Corr(self):
        corr_matrix=(self.num).corr(method='spearman')
        print(f'Top 3 Correlations to Target:{self.target}, are:')
        return display(corr_matrix[self.target].sort_values(ascending=False).head(4))

    # Method 11: Diplay basic_EDA of dataframe with widget tabs
    def basic_EDA(self):
        out1 = widgets.Output()
        out2 = widgets.Output()
        out3 = widgets.Output()
        out4 = widgets.Output()
        out5 = widgets.Output()
        out6 = widgets.Output()
        out7 = widgets.Output()
        out8 = widgets.Output()
        out9 = widgets.Output()


        tab = widgets.Tab(children = [out1, out2, out3, out4, out5, out6, out7, out8, out9])
        tab.set_title(0, 'Overall Info')
        tab.set_title(1, 'Columns Info')
        tab.set_title(2, 'Describe Data')
        tab.set_title(3, 'Missing_Values')
        tab.set_title(4, 'Categorical Plots')
        tab.set_title(5, 'Numerical Plots')
        tab.set_title(6, 'BoxPlot:Numerical')
        tab.set_title(7, 'ScatterPlot: Numerical')
        tab.set_title(8, 'Correlation: Numerical')
        display(tab)

        with out1:
            display(self.info())

        with out2:
            print('#############################################')
            print()
            print('Number of Categorical Columns:',len((self.cat).columns))
            print(*self.cat, sep=', ')
            print()
            print('#############################################')
            print()
            print('Number of Numerical Columns:',len((self.num).columns))
            print(*self.num, sep=', ')
            print()
            print('#############################################')
            print()
            print('Number of Variables/Columns with only 2 Unique Values:')
            for unik in self.data.columns:
                if self.data[unik].nunique() == 2:
                    display(unik),
            print('#############################################')
            print()
            print('Number of Boolean Columns:',len((self.bool).columns))
            print(*self.bool, sep=', ')
            print()
            print()
            print('#############################################')
            print('Target Variable is set to:',self.target)
            print('#############################################')

        with out3:
            display(self.describe())
        
        with out4:
            display(self.Null_Values())
            
        with out5:
            fig5 = self.countPlots()
            plt.show(fig5)
        
        with out6:
            fig6 = self.histPlots()
            plt.show(fig6)
        
        with out7:
            fig7 = self.Boxplot()
            plt.show(fig7)
        
        with out8:
            print('Realtionship between Numerical Columns')
            fig8 = self.Scatterplot()
                
        with out9:
            fig9 = self.correlation()
            fig10 = self.TOP4Corr()
            display(fig9)
            display(fig10)
    
    # Method 12: User Input on what type of Data Exploration they like to see
    def user_choice(self):
        user_choice = input("Do you want to use BASIC exploration or PANDAS profiling? (BASIC/PANDAS): ")
        # Check user choice between BASIC and PANDAS
        if user_choice == "BASIC":
            self.basic_EDA()
        elif user_choice == "PANDAS":
            user_input=input('Do you want this to show as HTML or within the IDE? (HTML/IDE): ')
            if user_input == 'HTML':
                self.profiling_html()
            elif user_input == 'IDE':
                self.profiling_IDE()
            else:
                print("Invalid choice. Please choose 'HTML' or 'IDE'.")
        else:
            print("Invalid choice. Please choose 'basic' or 'profiling'.")

    # Method 13: Using Pandas_Profiling to generate a report in html.
    def profiling_html(self):
        profile = ProfileReport(self.data)
        profile.to_file("PANDAS_PROFILE_DATA.html")
        print("Data profile has been saved as PANDAS_PROFILE_DATA.html")
        print('###########   InStructionS on Viewing HTML File ############')
        print("YOU CAN OPEN THE HTML FILE USING THE VSC Extention called Open in Browser")
        print("Once installed, right click on file and choose OPEN with HTML Viewer")

    # Method 14: Display Pandas Profile Report within IDE
    def profiling_IDE(self):
        profile_IDE = ProfileReport(self.data)
        display(profile_IDE)