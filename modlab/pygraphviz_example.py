#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 19 16:58:16 2017

@author: Young
"""

from PIL import Image as im
import pygraphviz as pgv
import matplotlib.pyplot as plt

g = pgv.AGraph(strict=True,directed=True)

# Add node
g.add_node('a') # adds node 'a'

# Add from node list
nodelist=['f','g','h']
g.add_nodes_from(nodelist)

# If node is not string it will convert it to string
g.add_node(1)  # adds node '1'

# Attributes
g.graph_attr['label']='Name of graph'
g.node_attr['shape']='circle'
g.edge_attr['color']='red'

g.add_edge('b','c') # adds edge 'b'-'c' (and also nodes 'b', 'c')


# Draw 
g.draw('/Users/Young/Documents/Capgemini/Learning/Python Development/Project_Test/test.png')

# Save
g.write('/Users/Young/Documents/Capgemini/Learning/Python Development/Project_Test/file.dot')




g = pgv.AGraph(strict=True,directed=True)
g.add_node('Bye', label ='weiofjrgerlg', style = 'filled', fillcolor = 'orange')
g.add_edge('Bye','Data Preparation')

g.layout(prog='dot')
g.draw('/Users/Young/Documents/Capgemini/Learning/Python Development/Project_Test/test.png')

image = im.open('/Users/Young/Documents/Capgemini/Learning/Python Development/Project_Test/test.png')

y_size = np.shape(image)[0]
x_size = np.shape(image)[1]
dpi = 60
plt.figure(figsize = (x_size/dpi, y_size/dpi))
plt.imshow(image, interpolation = 'spline36')


#plt.imshow(image, interpolation = 'bilinear')

g = pgv.AGraph(strict=True,directed=True)
g.add_edges_from([('SAR Data', 'Pre-processing Step 1'), ('Pre-processing Step 1', 'Feature Extraction'), ('Feature Extraction', 'Model Building')])
g.layout(prog='dot')
g.draw('/Users/Young/Documents/Capgemini/Learning/Python Development/Project_Test/test.png')

image = im.open('/Users/Young/Documents/Capgemini/Learning/Python Development/Project_Test/test.png')
#image.show(title = 'Hi')
plt.imshow(image, interpolation = 'spline36')





g = pgv.AGraph(strict=True,directed=True)
g.add_node(0, label ='SAR Data', shape = 'box')#, style = 'filled', fillcolor = 'orange')
g.add_node(1, label = 'Weather Data', shape = 'box')
g.add_node(2, label = 'NFI Data', shape = 'box')
g.add_node(3, label = 'Pre-processing Step 1: Terrain Correction & Calibration')
g.add_node(4, label = 'Pre-processing Step 2: Reprojection')
g.add_node(5, label = 'Pre-processing Step 3: Multi-Temporal Filtering')
g.add_node(6, label = 'Feature Extraction', shape = 'diamond', style = 'rounded')
g.add_node(7, label = 'Exploratory Analysis')
g.add_node(8, label = 'Visualisation')
g.add_node(9, label = 'Model Building')
g.add_node(10, label = 'Results_Evaluation')
g.add_edge(1, 3)
g.add_edge(2, 3)
g.add_edge(0, 3)
g.add_edge(3, 4)
g.add_edge(4, 5)
g.add_edge(5, 6)
g.add_edge(5, 7)
g.add_edge(7, 8)
g.add_edge(7, 6)
g.add_edge(6, 7)
g.add_edge(6, 9)
g.add_edge(9, 10)
g.add_edge(10, 8)
g.layout(prog='dot')

g.draw('/Users/Young/Documents/Capgemini/Learning/Python Development/Project_Test/test.png')
# Save
g.write('/Users/Young/Documents/Capgemini/Learning/Python Development/Project_Test/test.dot')
image = im.open('/Users/Young/Documents/Capgemini/Learning/Python Development/Project_Test/test.png')
image.show(title = 'Hi')


y_size = np.shape(image)[0]
x_size = np.shape(image)[1]
dpi = 60
plt.figure(figsize = (x_size/dpi, y_size/dpi))
plt.imshow(image, interpolation = 'spline36')
