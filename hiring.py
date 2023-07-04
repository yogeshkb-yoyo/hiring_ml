#!/usr/bin/env python
# coding: utf-8

# In[9]:


import pandas as pd
dataset = pd.read_csv("G:\Downloads\internship.csv")
evaluation_metrics = ['Python (out of 3)', 'Machine Learning (out of 3)', 'Natural Language Processing (NLP) (out of 3)', 'Deep Learning (out of 3)']
weights = {'Python (out of 3)': 3, 'Machine Learning (out of 3)': 3, 'Natural Language Processing (NLP) (out of 3)': 3, 'Deep Learning (out of 3)': 3}

def calculate_overall_score(row):
    score = 0
    for metric in evaluation_metrics:
        score += row[metric] * weights[metric]
    return score

dataset['Overall Score'] = dataset.apply(calculate_overall_score, axis=1)
ranked_dataset = dataset.sort_values('Overall Score', ascending=False)
num_positions = 1  
top_interns = ranked_dataset.head(num_positions)

for _, intern in top_interns.iterrows():
    skills = []
    for metric in evaluation_metrics:
        if intern[metric] > 0:
            skills.append(metric.split(' (')[0]) 
    print(f"Offering internship to {intern['Name']} with skills: {', '.join(skills)}")

print(ranked_dataset[['Name', 'Overall Score']])


# In[ ]:




