import pymqi

class IBMMQ:
    def __init__(self, qmgr_name, channel_name, conn_name, queue_name):
        self.qmgr_name = qmgr_name
        self.channel_name = channel_name
        self.conn_name = conn_name
        self.queue_name = queue_name
        self.queue_manager = None
        self.queue = None

    def connect(self):
        cd = pymqi.CD()
        cd.ChannelName = self.channel_name
        cd.ConnectionName = self.conn_name

        self.queue_manager = pymqi.QueueManager(None)
        self.queue = pymqi.Queue(self.queue_manager, self.queue_name)

    def send_message(self, message):
        message_options = pymqi.MQMD()
        message_options.Format = pymqi.MQFMT_STRING

        self.queue.put(message, message_options)

    def receive_message(self):
        message = self.queue.get()
        return message

# Variables
qmgr_name = "MQGD"
channel_name = "SSLCHANNEL"
conn_name = "localhost(1414)"
queue_name = "NATURAL.OUTPUT.LOCAL.QUEUE"

ibm_mq = IBMMQ(qmgr_name, channel_name, conn_name, queue_name)
ibm_mq.connect()

# Enviar mensaje
ibm_mq.send_message('Mensaje de prueba')

# Recibir mensaje
mensaje_recibido = ibm_mq.receive_message()
print(mensaje_recibido)