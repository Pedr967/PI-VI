import paho.mqtt.client as mqtt

# Configurações do Broker
broker = "test.mosquitto.org"
porta = 1883 
topico = "siChat/mqtt"

# Função que será chamada quando uma nova mensagem for recebida
def on_menssage(client,userData,flags,message):
    print(f"Nova mensagem recebida: {message.payload.decode('utf-8')}")
    
# Função que será chamada quando uma nova mensagem for recebida
def on_connect(client,userData,flags,rc):
    print(f"Conectado ao Broker com código de resultado {rc}")
    # Inscrever-se 
    client.subscribe(topico)

# Criar ciente MQTT
client = mqtt.Client()

#Definir callback de conexão
client.on_connect = on_connect

# Definir callback para recebimento de mensagens
client.on_message = on_menssage

# Conectar ao Broker
client.connect(broker, porta, 60)

# Iniciar o loop de rede para processar mensagens 
client.loop_forever()