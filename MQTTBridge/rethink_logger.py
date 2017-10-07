import rethinkdb as r
from datetime import datetime

conn = None

def float_val(byteString):
    try:
        return float(byteString)
    except ValueError:
        return None

def log(cfg, msgObj, payload_parser = None):
    global conn
    with r.connect(db=cfg['rethinkdb']['db']) as conn:
        if payload_parser:
            msg = payload_parser(msgObj)
        else:
            msg = {
                "topic": msgObj.topic,
                "payloadStr": str(msgObj.payload),
                "payloadNum": float_val(msgObj.payload)
            }
        msg.setdefault('timestamp', r.now())
        result = r.table(cfg['rethinkdb']['msg_table']).insert([msg]).run(conn)
        return result