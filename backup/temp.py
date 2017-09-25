import codecs, json
import json

from pyspark import SparkContext, StorageLevel
from argparse import ArgumentParser
from kafka import KafkaConsumer
from kafka import KafkaProducer



def getFieldObj(val, effect_format):
	temp_obj = {}
	temp_obj['key'] = val
	temp_obj['value'] = val
	temp_obj['confidence'] = 1
	provenance = []
	provenance_obj = {
		'source' : effect_format['source'] if 'source' in effect_format else '',
		'method' : 'karma',
		'dateRecorded' : effect_format['dateRecorded'] if 'dateRecorded' in effect_format else ''
	}
	provenance.append(provenance_obj)
	temp_obj['provenance'] = provenance
	return temp_obj

def convertEffectToDIGFormat(input_data):
	i = 0
	output_data = []
	for inp in input_data:
		i = i + 1
		if 	i == 10:
			break
		effect_format = json.loads(inp[1])

		dig_format = {}
		dig_format['_id'] = effect_format['uri']
		dig_format['doc_id'] = effect_format['uri']
		if 'dateRecorded' in effect_format:
			dig_format['timestamp_crawl'] = effect_format['dateRecorded'] + 'Z'
			dig_format['timestamp_index'] = effect_format['dateRecorded'] + 'Z'
		dig_format['raw_content'] = ''

		knowledgeGraph = {}
		for key in effect_format:
			if key not in ['uri','dateRecorded', '@context']:
				field_arr = []
				if isinstance(effect_format[key], list):
					for val in effect_format[key]:
						field_arr.append(getFieldObj(val, effect_format))
				else:
					field_arr.append(getFieldObj(effect_format[key], effect_format))
				knowledgeGraph[key] = field_arr

		dig_format['kg'] = knowledgeGraph
		output_data.append(dig_format)
	return output_data

# parser = ArgumentParser()
# parser.add_argument("-ct", "--consumerTopic", help="Kafka consumer topic name", required=True)
# parser.add_argument("-cs", "--consumerServer", help="Consumer Bootstrap server name", required=True)
# parser.add_argument("-pt", "--producerTopic", help="Kafka producer topic name", required=True)
# parser.add_argument("-ps", "--producerServer", help="Producer Bootstrap server name", required=True)

# args = parser.parse_args()

# consumer_bootstrap_servers = [args.consumerServer]
# consumer = KafkaConsumer(args.consumerTopic, bootstrap_servers=consumer_bootstrap_servers)


sc = SparkContext()
# Read the input data
input_data = sc.sequenceFile("sample").collect()
# outfile = open('sample_json', 'w')

output_data = convertEffectToDIGFormat(input_data)

output_data = json.dumps(output_data)
print output_data
# json.dump(output_data, outfile)
# print output_data
producer = KafkaProducer(bootstrap_servers='localhost:9092',value_serializer=lambda v: json.dumps(v).encode('utf-8'))
producer.send('my-topic', output_data)

# producer.send('my-topic', [{"kg": {"a": [{"confidence": 1, "provenance": [{"source": "isi-twitter/FFFFFFFFF2C0F93A", "dateRecorded": "2017-08-10T10:10:24", "method": "karma"}], "value": "UserName", "key": "UserName"}], "publisher": [{"confidence": 1, "provenance": [{"source": "isi-twitter/FFFFFFFFF2C0F93A", "dateRecorded": "2017-08-10T10:10:24", "method": "karma"}], "value": "isi-twitter", "key": "isi-twitter"}], "name": [{"confidence": 1, "provenance": [{"source": "isi-twitter/FFFFFFFFF2C0F93A", "dateRecorded": "2017-08-10T10:10:24", "method": "karma"}], "value": "TT_Smolin", "key": "TT_Smolin"}], "source": [{"confidence": 1, "provenance": [{"source": "isi-twitter/FFFFFFFFF2C0F93A", "dateRecorded": "2017-08-10T10:10:24", "method": "karma"}], "value": "isi-twitter/FFFFFFFFF2C0F93A", "key": "isi-twitter/FFFFFFFFF2C0F93A"}]}, "timestamp_index": "2017-08-10T10:10:24Z", "raw_content": "", "timestamp_crawl": "2017-08-10T10:10:24Z", "_id": "http://effect.isi.edu/data/username/twitter/TT_Smolin", "doc_id": "http://effect.isi.edu/data/username/twitter/TT_Smolin"}] )


# infile = open('sample_json', 'r')
# input_data = json.load(infile)
# print "input_data = ", input_data