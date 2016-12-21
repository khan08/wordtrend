from __future__ import print_function

import sys
from operator import add
from tweetAPI import dataSource

from pyspark.sql import SparkSession


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: wordcount <file>", file=sys.stderr)
        exit(-1)

    spark = SparkSession\
        .builder\
        .appName("PythonWordCount")\
        .getOrCreate()

    result = spark.parallelize(dataSource.getByTime())

    counts = result.flatMap(lambda x:x.text)\
                   .flatMap(lambda x: x.split(' ')) \
                   .map(lambda x: (x, 1)) \
                   .reduceByKey(add)
    output = counts.collect()
    for (word, count) in output:
        print("%s: %i" % (word, count))

    spark.stop()