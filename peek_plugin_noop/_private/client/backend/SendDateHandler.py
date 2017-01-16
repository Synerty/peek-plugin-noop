from datetime import datetime

from vortex.handler.ModelHandler import ModelHandler

sendDateFilt = {"plugin": "peek_plugin_noop",
                "key": "sendDate"}


class SendDateHandler(ModelHandler):
    def buildModel(self, **kwargs):
        return ["From Server : %s" % datetime.utcnow()]


def makeSendDateHandler():
    return SendDateHandler(sendDateFilt)
