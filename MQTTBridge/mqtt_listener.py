import paho.mqtt.client as mqtt
from paho.mqtt.client import MQTTv31, MQTTv311

def setup_client(cfg):
    #possibly accept callbacks for connect etc...  or else don't, just let caller add them on client...
    client = mqtt.Client(client_id="mqtt-sub-", clean_session=False, protocol=MQTTv311)
    client.username_pw_set(cfg['mqtt']['username'], password=cfg['mqtt']['password'])
    client.connect(cfg['mqtt']['host'])
    return client