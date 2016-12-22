from __future__ import print_function
import sys
sys.path.append(".")
from operator import add
from tweetAPI import dataSource

from pyspark import SparkContext, SparkConf


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: wordcount <file>", file=sys.stderr)
        exit(-1)

    conf = SparkConf().setAppName('appName')
    sc = SparkContext(conf=conf)
    sc.addPyFile('dist/wordTrend-1.0-py2.7.egg')
    result = sc.parallelize(dataSource.getByTime())

    counts = result.flatMap(lambda x:x.text.encode('utf-8'))\
                   .flatMap(lambda x: x.split(' ')) \
                   .map(lambda x: (x, 1)) \
                   .reduceByKey(add)

    output = counts.collect()
    for (word, count) in output:
        print("%s: %i" % (word, count))
