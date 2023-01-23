# Intro to Machine Learning_Assignment 1

Repository for assignment 1 in the Intro to Machine Learning course. 

## Overview

This assignment has two parts:
 - Creating an EDA class to do some semi-automated data exploration. 
 - Creating a predictive tree-based model that is well fitted, using a pipeline. 

The specific details of each part are in the respective .ipynb files. When complete, publish your repository to GitHub and submit the link to the both parts of the assignment dropboxes on Moodle. The EDA file will be peer evaluated by your classmates, and the predictive modelling file will be peer evaluated by me.

## Part 1 - EDA

The first task is to create a python utility file that contains a class that performs common data exploration steps in bulk. 

For this part, please:
 - Modify the class in the ml_utils.py file to create an EDA process that is useful for you.
 - In modifying the utils file, also update the comments, so your file is properly documented.  
 - Modify the eda_example.ipynb file to demonstrate your EDA.
 - In the eda_example file, change/add text boxes to add whatever explaination your EDA needs. E.g. if you added the ability to choose between a histogram and a PDF being printed, explain how that works.

The end goal here is that someone should be able to clone your copy of this repository, open the "eda_example.ipynb" file, click "Run All" and have the EDA process happen.

## Part 2 - Predictive Modelling with Trees

For this part, you need to create a predictive model using a tree-based model, and in doing so, aim for accuracy by limiting the overfitting of the model.

This is very similar to the modelling we've done previously, the one big change is that now we want to implement some steps to combat overfitting. The steps you choose are up to you, some things like editing hyperparameters or implementing pruning may be useful.