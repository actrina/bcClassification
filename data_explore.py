"""
- Load the metadata of the study dataset
- Organize tables
- Data exploration (visualize tables)

Author: A.Padilla
05/ago/2022

"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

pathGeneral = 'E:/CMMD/manifest-1616439774456/'
metadataPath = 'metadata.csv'
metadata = pathGeneral + metadataPath
clinicalDatapath = './files/CMMD_clinicaldata_revision.xlsx'

metadata = pd.read_csv(metadata, index_col=False)
metadata['File Location'] = metadata['Download Timestamp']
metadata = metadata.drop(columns=['File Size', 'Download Timestamp'])

clinical_data = pd.read_excel(clinicalDatapath)

# Count malignant/benign
count01 = clinical_data.groupby(['classification'])['classification'].count()
count02 = clinical_data.groupby(['classification', 'abnormality']).size()
count03 = clinical_data.groupby(['subtype', 'abnormality']).size()

# Generate graphs of statistics
labels = count01.axes[0].values
class_values = [count01.Benign, count01.Malignant]

# Count of malignant/benign
fig, ax = plt.subplots(figsize=(6, 3))


def func(pct, allvals):
    absolute = int(np.round(pct / 100. * np.sum(allvals)))
    return "{:.1f}%\n{:d}".format(pct, absolute)


wedges, texts, autotexts = ax.pie(class_values, 
                                  autopct=lambda pct: func(pct, class_values),
                                  textprops=dict(color="w"))
ax.legend(wedges, labels,
          title="Class",
          loc="center left",
          bbox_to_anchor=(1, 0, 0.5, 1))
plt.setp(autotexts, size=8)
plt.show()

# Abnormality per malignant/beningn
x = np.arange(2)
width = 0.2
both = [count02.Benign.both, count02.Malignant.both]
calcification = [count02.Benign.calcification, count02.Malignant.calcification]
mass = [count02.Benign.mass, count02.Malignant.mass]

fig02, ax2 = plt.subplots(figsize=(6, 6))
ax2.bar(x-0.2, both, width, color='#FF8811')
ax2.bar(x, calcification, width, color='#9DD9D2')
ax2.bar(x+0.2, mass, width, color='#073B3A')
ax2.set_xticks(x, labels=['Benign', 'Malignant'])
ax2.set_xlabel('Classification')
ax2.set_ylabel('Count')
ax2.legend(labels = ['Both', 'Calcification', 'Mass'],
           title='Abnormality')
plt.show()

# Plot per subtype of cancer
labels = ['HER2-enriched', 'Luminal A', 'Luminal B', 'triple negative']
HER = count03['HER2-enriched'].values
lumA = count03['Luminal A'].values
lumB = count03['Luminal B'].values
trip_nega = count03['triple negative'].values

both02 = np.array([HER[0], lumA[0], lumB[0], trip_nega[0]])
calcification02 = np.array([HER[1], lumA[1], lumB[1], trip_nega[1]])
mass02 = np.array([HER[2], lumA[2], lumB[2], trip_nega[2]])
width02 = 0.4

fig03, ax3 = plt.subplots()
ax3.bar(labels, both02, width02, label='Both', color='#FF8811')
ax3.bar(labels, calcification02, width02, label='Calcification', 
        bottom=both02, color='#9DD9D2')
ax3.bar(labels, mass02, width02, label='Mass', 
        bottom=both02+calcification02, color='#073B3A')
ax3.set_ylabel('Count')
ax3.set_xlabel('Subtypes')
ax3.legend(title='Abnormality')
# plt.grid(visible=True, color='0.85')
plt.show()
