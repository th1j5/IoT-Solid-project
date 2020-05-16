import socket
import ttn
import TTN
import base64


# ttn MQTT client stuff
app_id = "iot_and_solid"
access_key = "ttn-account-v2.RF_3PIv_yBvAUSJejbM4yehHl9d3OKRjVaqdiqmhYzI"
device_id = "the_stupid_blue_board"


# client and server data
client_ipv6 = '2001:db8::1'
client_port = 0

server_ip6 = '2a02:1811:e50b:9100:ba27:ebff:fe60:525b'
server_port = 5683

SS = socket.socket(socket.AF_INET6, socket.SOCK_DGRAM)
SS.bind(('2a02:1811:e50b:9100:ba27:ebff:fe60:525b',5535))

def get_hex_bytes(payload):
    message_hex = base64.b64decode(payload).hex()
    return message_hex

def hex_to_utf8(hex_string):
    utf8_string = bytes.fromhex(hex_string).decode("utf-8")
    return utf8_string

def uplink_callback_Server(msg, client):
    dest = (server_ip6,server_port) # bestemming server address nog implementeren

    if msg.port == 1:
        print("uplink")
        payload = bytes.fromhex(get_hex_bytes(msg.payload_raw))
    else:
        payload = 0
    SS.sendto(payload,dest)

    
def connect_callback(res, client):
    if (res):
        print("connection succeeded")
    else:
        print("connection failed succesfully")

def close_callback(res, client):
    if (res):
        print("connection closed succesfully")
    else:
        print("connection closed unexpectedly")
    

# downlink ophalen en doorsturen naar simulatie bordje
handler = ttn.HandlerClient(app_id, access_key)

app = handler.application()
app.set_payload_format('Custom')
print(app.get())



mqtt_client = handler.data()
mqtt_client.set_uplink_callback(uplink_callback_Server) # aanpassen naar client wanneer klaar bent met testen
mqtt_client.set_connect_callback(connect_callback)
mqtt_client.set_close_callback(close_callback)
mqtt_client.connect()
print("MQTT connected")

print("start TTN Proxy server")
while True:
    data = SS.recvfrom(1024)
    #print("connection established with %s" % (address))
    Payload = {'fport':2, 'payload': str(data[0].hex())}
    TTN.SimulateUplink(Payload)

print("connection ended")
mqtt_client.close()
