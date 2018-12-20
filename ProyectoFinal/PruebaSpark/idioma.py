#
# Licensed to the Apache Software Foundation (ASF) under one or more
# contributor license agreements.  See the NOTICE file distributed with
# this work for additional information regarding copyright ownership.
# The ASF licenses this file to You under the Apache License, Version 2.0
# (the "License"); you may not use this file except in compliance with
# the License.  You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

r"""
 Counts words in UTF8 encoded, '\n' delimited text received from the network every second.
 Usage: network_wordcount.py <hostname> <port>
   <hostname> and <port> describe the TCP server that Spark Streaming would connect to receive data.
 To run this on your local machine, you need to first run a Netcat server
    `$ nc -lk 9999`
 and then run the example
    `$ bin/spark-submit examples/src/main/python/streaming/network_wordcount.py localhost 9999`
"""

from __future__ import print_function
from pyspark.sql.functions import *

import sys
import json

from pyspark import SparkContext
from pyspark.streaming import StreamingContext
from pyspark.sql import SQLContext

if __name__ == "__main__":
	if len(sys.argv) != 3:
		print("Usage: idioma.py <hostname> <port>", file=sys.stderr)
		exit(-1)
	sc = SparkContext(appName="PythonStreamingNetworkWordCount")
	ssc = StreamingContext(sc,20)
	sqlContext = SQLContext(sc)

	lines = ssc.socketTextStream(sys.argv[1], int(sys.argv[2]))

	dstream = lines.map(lambda x: json.loads(x[1])).foreachRDD()
	dataFrame = sqlContext.read.json(dstream)
	dataFrame.show()

	ssc.start()
	ssc.awaitTermination()    
