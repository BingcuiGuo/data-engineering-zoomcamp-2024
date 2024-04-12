from pyspark.sql import SparkSession

# Create SparkSession
spark = SparkSession.builder \
    .appName('YourSparkJob') \
    .getOrCreate()

# Read from Kafka topic
df = spark \
    .readStream \
    .format('kafka') \
    .option('kafka.bootstrap.servers', 'localhost:9092') \
    .option('subscribe', 'your_topic') \
    .load()

# Perform necessary transformations/aggregations
# Example:
# processed_df = df.selectExpr("CAST(key AS STRING)", "CAST(value AS STRING)")

# Write processed data to sink (e.g., console, file, database)
# Example:
# query = processed_df \
#     .writeStream \
#     .outputMode('append') \
#     .format('console') \
#     .start()

# query.awaitTermination()

# Stop SparkSession
spark.stop()
