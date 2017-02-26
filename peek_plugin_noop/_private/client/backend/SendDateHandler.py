from datetime import datetime

from vortex.handler.ModelHandler import ModelHandler

from peek_plugin_noop._private.PluginNames import noopFilt

sendDateFilt = {"key": "sendDate"}
sendDateFilt.update(noopFilt)


class SendDateHandler(ModelHandler):
    def buildModel(self, **kwargs):
        return ["From Server : %s" % datetime.utcnow()]


def makeSendDateHandler():
    return SendDateHandler(sendDateFilt)
