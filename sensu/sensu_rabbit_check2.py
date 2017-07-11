#!/usr/bin/env python
import pika, time, sys, boto.ses

server = 'X.X.X.X' 
credentials = pika.PlainCredentials('sensu', 'sensu')

error_message = ''

# rabbitmqctl add_vhost /checkrabbit
# rabbitmqctl set_permissions -p /checkrabbit sensu ".*" ".*" ".*"


# CREATING MESSAGE
def create_one_message():
   try:
        #connection = pika.BlockingConnection(pika.ConnectionParameters(host=server))
        print 1
	connection = pika.BlockingConnection(pika.ConnectionParameters(server,5672,'/checkrabbit',credentials))
        channel = connection.channel()
        print 2
        res = channel.queue_declare(queue='hellomonitor')
        channel.basic_publish(exchange='',routing_key='hellomonitor',body='hello monitor')
        print "sent a 'hello monitor'"
        connection.close()
   except:
        print 'error 1 - sending mail'
	send_mail_error('Creating message error')
        sys.exit()

# QUEUE SIZE
def read_size():
   try:
        connection = pika.BlockingConnection(pika.ConnectionParameters(server,5672,'/checkrabbit',credentials))
        channel = connection.channel()
        res = channel.queue_declare(queue='hellomonitor')
        print 'Messages in queue %d' % res.method.message_count
        connection.close()
        return res.method.message_count
   except:
        print 'error 2 - sending mail'
        send_mail_error('Reading queue error')
        sys.exit()


# CONSUMING MESSAGES
def receive():
   try:
        connection = pika.BlockingConnection(pika.ConnectionParameters(server,5672,'/checkrabbit',credentials))
        channel = connection.channel()
        channel.queue_declare(queue='hellomonitor')
        channel.basic_consume(callback, queue='hellomonitor', no_ack=True)
   except:
        print 'error 3 - sending mail'
        send_mail_error('Consuming messages error')
        sys.exit()


def callback(ch, method, properties, body):
    ch.stop_consuming()

def send_mail_error(error_message):
    #conn = boto.ses.connect_to_region('us-east-1')
    return 0

#MAIN
def main():
        consumer = 0
        create_one_message()
        time.sleep(1)
        consumer = read_size()
        if consumer != 1:
                print 'error introducing consumer'
                print 'error 0 - sending mail'
	        send_mail_error('Creating message more than we expect')
        print consumer
        time.sleep(1)
        receive()
        time.sleep(1)
        consumer = read_size()
        print consumer
        if consumer != 0:
                print 'error consuming'
                print 'error - sending mail'
                send_mail_error('Consuming messages errors')

if __name__ == "__main__":
        main()
