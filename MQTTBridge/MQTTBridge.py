import yaml
import click
import mqtt_listener as mq
import rethink_logger as rl

cfg = None

@click.group()
def cli():
    pass

def debug_message(client, userdata, msg):
    click.echo("RECIEVED: topic {}, payload {}".format(msg.topic, str(msg.payload)))

def log_message(client, userdata, msg):
    click.echo("Saving " + msg.topic+" "+str(msg.payload))
    global cfg
    result = rl.log(cfg, msg)
    click.echo("{} records inserted.".format(result['inserted']))

@cli.command('listen')
def listen():
    click.echo("Listening to MQTT Stream...")
    client = mq.setup_client(cfg)
    client.on_message = debug_message
    client.loop_forever()

@cli.command('log')
def log():
    click.echo("Shoveling MQTT Stream to DB...")
    client = mq.setup_client(cfg)
    client.on_message = log_message
    client.loop_forever()

#run this like: python MQTTBridge.py log
if __name__ == '__main__':
    click.echo("MQTTBridge starting up...")
    with open("config.yml", 'r') as ymlfile:
        cfg = yaml.load(ymlfile)
    if cfg is None:
        raise RuntimeError("config.yml file not found or not valid")
    cli()
