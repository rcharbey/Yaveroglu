#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Jan  8 16:12:31 2018

@author: raphael
"""

import csv
import os

home = os.path.expanduser('~')
remaining_edges = 'Remaining_edges'
input_folder = '%s/GALLERY/three/'% home
output_folder = 'Yaveroglu_files/'

def convert_LEDA(ego):
    nodes = []
    edges = []
    nb_nodes = 0
    nb_edges = 0
    with open(input_folder+ego+'/Graphs/friends.gml','r') as to_read:
        source = -1
        for line in to_read:
            splited_line = line.split(' ')
            if 'id' in splited_line:
                nodes.append(int(splited_line[5]))
                nb_nodes +=1
            if 'source' in splited_line:
                source = int(splited_line[5])
            if 'target' in splited_line:
                edges.append((int(splited_line[5]),source))
                nb_edges +=1
    leda_fname = '{}.gw'.format(ego)
    leda_file = open(output_folder+leda_fname,'w')
    leda_file.write('#header section\n')
    leda_file.write('LEDA.GRAPH\n')
    leda_file.write('int\n')
    leda_file.write('int\n')
    leda_file.write('-2\n')
    leda_file.write('#nodes section\n')
    leda_file.write(str(nb_nodes)+'\n')
    for i in range(nb_nodes):
        leda_file.write('|{{{}}}|\n'.format(i))
    leda_file.write('#edges section\n')
    leda_file.write(str(nb_edges)+'\n')
    for i in range(1,nb_edges+1):
        leda_file.write('{} {} {}\n'.format(edges[i-1][0],edges[i-1][1],0))
        
        
def convert_ndump2(ego):
    ndump2_fname = '{}.ndump2'.format(ego)
    with open(output_folder+ndump2_fname,'w') as to_write:
        csv_w = csv.writer(to_write, delimiter=' ')
        with open('%s/results/positions_per_alters/%s.csv' % (home, ego),'r') as to_read:
            csv_r = csv.reader(to_read, delimiter=';')
            for line in csv_r:
                csv_w.writerow(line)  
  
    
def grab_list_egos():
    list_egos = []
    with open('list_egos.csv', 'r') as to_read:
        csv_r = csv.reader(to_read, delimiter = ';')
        for line in csv_r:
            list_egos.append(line[0])
    return list_egos      

        
def multiple_convert_LEDA(list_egos):
    for ego in list_egos:
        convert_LEDA(ego)
            
            
def multiple_convert_ndump2(list_egos):
    for ego in list_egos:
        convert_ndump2(ego)
            
        
list_egos = grab_list_egos()
#multiple_convert_LEDA(list_egos)
multiple_convert_ndump2(list_egos)

            

            