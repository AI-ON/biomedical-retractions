from lxml import etree
import argparse
from pyspark import SparkContext, SparkConf


def parse(xml):
	tree = etree.parse(xml)
	root=tree.getroot()
	return root.attrib['article-type']	

if __name__ == "__main__":
	#parser = argparse.ArgumentParser()
	#parser.parse_args()
	conf = SparkConf().setAppName('retractions')
	conf = conf.setMaster("local[*]")
	sc   = SparkContext(conf=conf)
	files= sc.textFile('./files-all.txt')
	files.map(lambda x: str(x)+','+parse(x)).saveAsTextFile('./data/article-types')