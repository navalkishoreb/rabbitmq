from pika import BlockingConnection, ConnectionParameters

with BlockingConnection(ConnectionParameters(host="localhost")) as conn:
    with conn.channel() as channel:
        try:
            channel.basic_publish(exchange="", routing_key="check", body="message to be pushed")
        except ChannelWrongStateError as channel_error:
            print(channel_error)
