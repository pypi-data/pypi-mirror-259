import json
import uuid
import gzip
import time
from io import BytesIO
import base64
import websocket
import auth

try:
    import thread
except ImportError:
    import _thread as thread


class MIXIN_WS_API:

    def __init__(self, bot_config, on_message, on_open=None, on_error=None, on_close=None, on_data=None, on_pong=None, on_ping=None):

        jwt_token = auth.generate_authentication_token('GET', '/', '', bot_config['client_id'], bot_config['session_id'], bot_config['private_key'])

        if on_open is None:
            on_open = MIXIN_WS_API.__on_open

        if on_close is None:
            on_close = MIXIN_WS_API.__on_close

        if on_error is None:
            on_error = MIXIN_WS_API.__on_error

        if on_data is None:
            on_data = MIXIN_WS_API.__on_data

        if on_pong is None:
            on_pong = MIXIN_WS_API.__on_pong

        if on_ping is None:
            on_ping = MIXIN_WS_API.__on_ping

        self.ws = websocket.WebSocketApp("wss://mixin-blaze.zeromesh.net/",
                                    on_message=on_message,
                                    on_error=on_error,
                                    on_close=on_close,
                                    header=["Authorization:Bearer " + jwt_token],
                                    subprotocols=["Mixin-Blaze-1"],
                                    on_data=on_data,
                                    on_ping=on_ping,
                                    on_pong=on_pong)

        self.ws.on_open = on_open

    """
    run websocket server forever
    """
    def run(self):
            self.ws.run_forever(ping_interval=10)

    """
    ========================
    WEBSOCKET DEFAULT METHOD
    ========================
    """

    """
    on_open default
    """
    @staticmethod
    def __on_open(ws):

        def run(*args):
            print("ws open at", time.ctime())
            Message = {"id": str(uuid.uuid1()), "action": "LIST_PENDING_MESSAGES"}
            Message_instring = json.dumps(Message)

            fgz = BytesIO()
            gzip_obj = gzip.GzipFile(mode='wb', fileobj=fgz)
            gzip_obj.write(Message_instring.encode())
            gzip_obj.close()
            ws.send(fgz.getvalue(), opcode=websocket.ABNF.OPCODE_BINARY)
            while True:
                time.sleep(1)

        thread.start_new_thread(run, ())

    """
    on_data default
    """
    @staticmethod
    def __on_data(ws, readableString, dataType, continueFlag):
        # print('readableString:', readableString, ', dataType:', dataType, ', continueFlag:', continueFlag)
        return

    @staticmethod
    def __on_pong(ws, data):

        return

    @staticmethod
    def __on_ping(ws, data):
        ws.send(None, opcode=websocket.ABNF.OPCODE_PONG)
        return


    """
    on_close default
    """

    def __on_close(self):
        print('closing at', time.ctime())
    """
    on_error default
    """

    @staticmethod
    def __on_error(ws, error):
        print(error)


    """
    =================
    REPLY USER METHOD
    =================
    """

    """
    generate a standard message base on Mixin Messenger format
    """

    @staticmethod
    def writeMessage(websocketInstance, action, params):

        message = {"id": str(uuid.uuid1()), "action": action, "params": params}
        message_instring = json.dumps(message)

        fgz = BytesIO()
        gzip_obj = gzip.GzipFile(mode='wb', fileobj=fgz)
        gzip_obj.write(message_instring.encode())
        gzip_obj.close()
        websocketInstance.send(fgz.getvalue(), opcode=websocket.ABNF.OPCODE_BINARY)

    """
    when receive a message, must reply to server
    ACKNOWLEDGE_MESSAGE_RECEIPT ack server received message
    """
    @staticmethod
    def send_receipt(websocketInstance, msgid):
        parameter4IncomingMsg = {"message_id": msgid, "status": "READ"}
        Message = {"id": str(uuid.uuid1()), "action": "ACKNOWLEDGE_MESSAGE_RECEIPT", "params": parameter4IncomingMsg}
        Message_instring = json.dumps(Message)
        fgz = BytesIO()
        gzip_obj = gzip.GzipFile(mode='wb', fileobj=fgz)
        gzip_obj.write(Message_instring.encode())
        gzip_obj.close()
        websocketInstance.send(fgz.getvalue(), opcode=websocket.ABNF.OPCODE_BINARY)
        return

    """
    reply a button to user
    """
    @staticmethod
    def sendUserAppButton(websocketInstance, in_conversation_id, to_user_id, realLink, text4Link, colorOfLink="#0084ff"):

        btn = '[{"label":"' + text4Link + '","action":"' + realLink + '","color":"' + colorOfLink + '"}]'

        btn = base64.b64encode(btn.encode('utf-8')).decode(encoding='utf-8')

        params = {"conversation_id": in_conversation_id, "recipient_id": to_user_id, "message_id": str(uuid.uuid4()),
                  "category": "APP_BUTTON_GROUP", "data": btn}
        return MIXIN_WS_API.writeMessage(websocketInstance, "CREATE_MESSAGE", params)

    """
    reply a contact card to user
    """

    @staticmethod
    def sendUserContactCard(websocketInstance, in_conversation_id, to_user_id, to_share_userid):

        btnJson = json.dumps({"user_id": to_share_userid})
        btnJson = base64.b64encode(btnJson.encode('utf-8')).decode('utf-8')
        params = {"conversation_id": in_conversation_id, "recipient_id": to_user_id, "message_id": str(uuid.uuid4()),
                  "category": "PLAIN_CONTACT", "data": btnJson}
        return MIXIN_WS_API.writeMessage(websocketInstance, "CREATE_MESSAGE", params)

    """
    reply a text to user
    """
    @staticmethod
    def sendUserText(websocketInstance, in_conversation_id, to_user_id, textContent):

        textContent = textContent.encode('utf-8')
        textContent = base64.b64encode(textContent).decode(encoding='utf-8')

        params = {"conversation_id": in_conversation_id, "recipient_id": to_user_id, "status": "SENT",
                  "message_id": str(uuid.uuid4()), "category": "PLAIN_TEXT",
                  "data": textContent}
        return MIXIN_WS_API.writeMessage(websocketInstance, "CREATE_MESSAGE", params)

    """
    send user a pay button
    """
    @staticmethod
    def sendUserPayAppButton(webSocketInstance, in_conversation_id, to_user_id, inAssetName, inAssetID, inPayAmount, linkColor="#0CAAF5"):
        payLink = "https://mixin.one/pay?recipient=" + mixin_config.client_id + "&asset=" + inAssetID + "&amount=" + str(
            inPayAmount) + '&trace=' + str(uuid.uuid1()) + '&memo=PRS2CNB'
        btn = '[{"label":"' + inAssetName + '","action":"' + payLink + '","color":"' + linkColor + '"}]'

        btn = base64.b64encode(btn.encode('utf-8')).decode(encoding='utf-8')

        gameEntranceParams = {"conversation_id": in_conversation_id, "recipient_id": to_user_id,
                              "message_id": str(uuid.uuid4()), "category": "APP_BUTTON_GROUP", "data": btn}
        MIXIN_WS_API.writeMessage(webSocketInstance, "CREATE_MESSAGE", gameEntranceParams)

    @staticmethod
    def sendAppCard(websocketInstance, in_conversation_id, to_user_id, asset_id, amount, icon_url, title, description, color="#0080FF", memo=""):
        payLink = "https://mixin.one/pay?recipient=" + to_user_id + "&asset=" + asset_id + "&amount=" + \
                amount + "&trace=" + str(uuid.uuid4()) + "&memo="
        card =  '{"icon_url":"' + icon_url + '","title":"' + title + \
                '","description":"' + description + '","action":"'+ payLink + '"}'
        enCard = base64.b64encode(card.encode('utf-8')).decode(encoding='utf-8')
        params = {"conversation_id": in_conversation_id,  "message_id": str(uuid.uuid4()),
                  "category": "APP_CARD", "status": "SENT", "data": enCard}
        return MIXIN_WS_API.writeMessage(websocketInstance, "CREATE_MESSAGE", params)

    @staticmethod
    def sendAppButtonGroup(websocketInstance, in_conversation_id, to_user_id, buttons):
        buttonsStr = '[' + ','.join(str(btn) for btn in buttons) +']'
        enButtons = base64.b64encode(buttonsStr.encode('utf-8')).decode(encoding='utf-8')
        params = {"conversation_id": in_conversation_id,  "recipient_id": to_user_id,
                "message_id": str(uuid.uuid4()),
                "category": "APP_BUTTON_GROUP", "status": "SENT", "data": enButtons}
        return MIXIN_WS_API.writeMessage(websocketInstance, "CREATE_MESSAGE", params)

    @staticmethod
    def packButton(to_user_id, asset_id, amount, label, color="#FF8000", memo=""):
        payLink = "https://mixin.one/pay?recipient=" + to_user_id + "&asset=" + asset_id + "&amount=" + \
                    amount + "&trace=" + str(uuid.uuid4()) + "&memo="
        button  = '{"label":"' + label + '","color":"' + color + '","action":"' + payLink + '"}'
        return button


