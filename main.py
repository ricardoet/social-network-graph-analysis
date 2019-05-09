import findspark
findspark.init()
import os
os.environ['PYSPARK_SUBMIT_ARGS'] = ' --packages graphframes:graphframes:0.7.0-spark2.4-s_2.11 pyspark-shell'

from pyspark import SparkContext
from functools import reduce
from pyspark.sql.functions import col, lit, when
from pyspark.sql import SQLContext
from graphframes import GraphFrame
#from graphframes import *
import pandas as pd
from pyspark.sql.types import IntegerType

sc = SparkContext("local", "Simple App")
sqlContext = SQLContext(sc)


checkins_df = pd.read_csv("./Dataset/checkins/checkins.txt", sep = '\t')

#Load text file into pandas dataframe and extract vertices
friendship_edges_df = pd.read_csv("./Dataset/edges/edges.txt", sep = '\t')
friendship_vertices = edges_df['0'].drop_duplicates()

#build GraphFrame object of friendship file
friendship_nodes = sqlContext.createDataFrame(friendship_vertices, IntegerType()).toDF("id")
friendship_list_compreh = [(int(x[0]), int(x[1])) for x in friendship_edges_df.values]
friendship_edges = sqlContext.createDataFrame(friendship_list_compreh).toDF("src", "dst")
friendship_graph = GraphFrame(friendship_nodes, friendship_edges)

#Online working example
vertices = sqlContext.createDataFrame([
  ("a", "Alice", 34),
  ("b", "Bob", 36),
  ("c", "Charlie", 30),
  ("d", "David", 29),
  ("e", "Esther", 32),
  ("f", "Fanny", 36),
  ("g", "Gabby", 60)], ["id", "name", "age"])

edges = sqlContext.createDataFrame([
  ("a", "b", "friend"),
  ("b", "c", "follow"),
  ("c", "b", "follow"),
  ("f", "c", "follow"),
  ("e", "f", "follow"),
  ("e", "d", "friend"),
  ("d", "a", "friend"),
  ("a", "e", "friend")
], ["src", "dst", "relationship"])

g = GraphFrame(vertices, edges)
print(g)