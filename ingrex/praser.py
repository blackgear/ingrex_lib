"Ingrex praser deal with message"
from datetime import datetime, timedelta

class Message(object):
    "Message object"
    def __init__(self, raw_msg):
        self.raw = raw_msg
        self.guid = raw_msg[0]
        self.timestamp = raw_msg[1]
        seconds, millis = divmod(raw_msg[1], 1000)
        time = datetime.fromtimestamp(seconds) + timedelta(milliseconds=millis)
        self.time = time.strftime('%Y/%m/%d %H:%M:%S:%f')[:-3]
        self.text = raw_msg[2]['plext']['text']
        self.type = raw_msg[2]['plext']['plextType']
        self.team = raw_msg[2]['plext']['team']
