from kafka import KafkaProducer 
import csv 
producer = KafkaProducer(bootstrap_server='localhost:9092') 

with open('META_stock_data.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        producer.send('your_topic', ','.join(row).encode('utf-8'))
producer.close()