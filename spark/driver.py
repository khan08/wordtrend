from __future__ import print_function
import sys
sys.path.append(".")
from operator import add
from tweetAPI import dataSource
from trainer.process import get_feature,tokenize
from pyspark import SparkContext, SparkConf


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: wordcount <file>", file=sys.stderr)
        exit(-1)

    conf = SparkConf().setAppName('appName')
    sc = SparkContext(conf=conf)
    result = sc.parallelize(dataSource.getByTime())
    counts = result.map(lambda x:get_feature(tokenize(x.text.encode('utf-8'))))

    output = counts.collect()
    for (word, count) in output:
        print("%s: %i" % (word, count))
