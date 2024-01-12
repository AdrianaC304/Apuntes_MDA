from confluent_kafka import Producer

# Configura el productor de Kafka
producer_config = {
    'bootstrap.servers': 'localhost:9092',
}

producer = Producer(producer_config)

# Envia un mensaje al topic 'tu_topic'
topic = 'tu_topic'
message = 'Hola desde el productor Kafka'
producer.produce(topic, message.encode('utf-8'))

# Espera a que se envíen todos los mensajes antes de cerrar el productor
producer.flush()
