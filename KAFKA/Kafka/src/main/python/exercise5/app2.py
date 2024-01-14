# app.py
import streamlit as st
from confluent_kafka import Consumer, KafkaException

# Configuración de Kafka
kafka_bootstrap_servers = 'localhost:9092'
kafka_topic = 'your_kafka_topic'

# Configuración del consumidor de Kafka
conf = {
    'bootstrap.servers': kafka_bootstrap_servers,
    'group.id': 'streamlit-consumer-group',
    'auto.offset.reset': 'earliest'  # Puedes ajustar esto según tus necesidades
}

# Crear el consumidor de Kafka
consumer = Consumer(conf)
consumer.subscribe([kafka_topic])

# Configuración de la aplicación Streamlit
st.title('Streamlit Kafka Example')

# Función para consumir mensajes de Kafka
def consume_messages():
    try:
        while True:
            msg = consumer.poll(1.0)  # Esperar durante 1 segundo por nuevos mensajes
            if msg is None:
                continue
            if msg.error():
                if msg.error().code() == KafkaException._PARTITION_EOF:
                    continue
                else:
                    raise KafkaException(msg.error())
            # Procesar el mensaje
            st.write(f"Nuevo mensaje: {msg.value().decode('utf-8')}")
    except KeyboardInterrupt:
        pass
    finally:
        consumer.close()

# Iniciar la función de consumo de mensajes en segundo plano
st.write("Esperando mensajes de Kafka...")
consume_messages()
