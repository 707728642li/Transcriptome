#!/usr/bin/env python
# coding: utf-8

import os
import pandas as pd
import sys

in1 = pd.read_table(sys.argv[1],header=None,dtype='object',skiprows=1)
in2 = pd.read_table(sys.argv[2],header=None,dtype='object',skiprows=1)
print('Reading files successfully!')
in1['position'] = in1[0].str[:]+'_'+in1[1].str[:]+'_'+in1[2].str[:]+'_'+in1[3].str[:]
in2['position'] = in2[0].str[:]+'_'+in2[1].str[:]+'_'+in2[2].str[:]+'_'+in2[3].str[:]

in_total = pd.merge(in1[['position',6]],in2[['position',6]],on='position',how='outer').fillna('0.0')
print('Combine files successfully!')
in_total['6_x'] = in_total['6_x'].astype('float')
in_total['6_y'] = in_total['6_y'].astype('float')
in_total['meth'] = in_total.iloc[:,1:].mean(axis=1)
in_total.drop(columns=in_total.columns[1:3],inplace=True)
print('Calculate successfully!')
position = in_total.position.str[:].str.split('_',expand=True)
position['meth']=in_total.meth
position.to_csv('mean_'+sys.argv[1].split('.')[0]+'_'+sys.argv[2].split('.')[0]+'.txt',sep='\t',index=False,header=False)
print('Write file successfully!/n filename: mean_'+sys.argv[1].split('.')[0]+'_'+sys.argv[2].split('.')[0]+'.txt ')




