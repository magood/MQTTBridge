import paho.mqtt.client as mqtt
from paho.mqtt.client import MQTTv31, MQTTv311, MQTT_ERR_NO_CONN, MQTT_ERR_SUCCESS
from time import sleep

def do_publish(client, data):
    client.reconnect()
    """Returns a MQTTMessageInfo class, which can be used to determine whether
    the message has been delivered (using info.is_published()) or to block
    waiting for the message to be delivered (info.wait_for_publish()). The
    message ID and return code of the publish() call can be found at
    info.mid and info.rc."""
    info = client.publish("test", data, qos=1)
    print("Published: {0}, return code: {1} ({2} is success)".format(info.is_published(), info.rc, MQTT_ERR_SUCCESS))

if __name__ == '__main__':
    client = mqtt.Client(client_id="mqtt-sub-", clean_session=False, protocol=MQTTv311)
    client.username_pw_set('', password='')
    client.connect("")

    for i in range(20):
        #client.loop()
        do_publish(client, i)
        #print(client.publish("test", i, qos=1))
        #client.loop()
        sleep(1)
