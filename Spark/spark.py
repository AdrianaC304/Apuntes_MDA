from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("KafkaSparkConsumer") \
    .getOrCreate()

# Configura el DataFrame de Spark para consumir datos de Kafka
kafka_df = spark \
    .readStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers", "localhost:9092") \
    .option("subscribe", "tu_topic") \
    .load()

# Procesa los datos según sea necesario
processed_df = kafka_df.selectExpr("CAST(value AS STRING)")

# Imprime el resultado en la consola (puedes ajustar esto según tus necesidades)
query = processed_df \
    .writeStream \
    .outputMode("append") \
    .format("console") \
    .start()

query.awaitTermination()
