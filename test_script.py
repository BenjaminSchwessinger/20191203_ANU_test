'''
Author: 

'''

import pandas as pd
import os
import sys

#-----------------------
''' This is gene expression data from Saunders et al. from 2014
      bla bla 
      lfjkjfkdj
    hjhdjsh
'''
data = pd.read_excel('12864_2016_2684_MOESM1_ESM.xlsx', sheet_name = 'Table S20', skiprows = 2, header = 0, index_col="gene_id")
#-----------------------
# Get the gene name from the command line
gene = sys.argv[1]
gene2 = sys.argv[2]

try:
        data.loc[gene]
except:
        print("Please provide a gene name.")
        sys.exit()




# Print the gene expression
print('Expression at 0 dpi: ', data.loc[gene]['0dpi'])
print('Expression at 1 dpi: ', data.loc[gene]['1dpi'])
print('Expression at 2 dpi: ', data.loc[gene]['2dpi'])
print('Expression at 3 dpi: ', data.loc[gene]['3dpi'])
print('Expression at 5 dpi: ', data.loc[gene]['5dpi'])
print('Expression at 7 dpi: ', data.loc[gene]['7dpi'])
print('Expression at 9 dpi: ', data.loc[gene]['9dpi'])
print('Expression at 11 dpi: ', data.loc[gene]['11dpi'])


#Print expression second gene

print('Expression at 0 dpi: ', data.loc[gene2]['0dpi'])
