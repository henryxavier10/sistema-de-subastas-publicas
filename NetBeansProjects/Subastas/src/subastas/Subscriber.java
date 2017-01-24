/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package subastas;
import javax.jms.Connection;
import javax.jms.ConnectionFactory;
import javax.jms.Destination;
import javax.jms.JMSException;
import javax.jms.Message;
import javax.jms.Session;
import javax.jms.TextMessage;
 
import org.apache.activemq.ActiveMQConnection;
import org.apache.activemq.ActiveMQConnectionFactory;
 
/**
 *
 * @author henry
 */
public class Subscriber {
    private ConnectionFactory connectionFactory;
    private Connection connection;
    private Session session;
    private javax.jms.MessageConsumer messageConsumer;
 
    public void consumeMessage() {
	try {
			// get the ConnectionFactory
			// default broker URL is tcp://localhost:61616
			connectionFactory = new ActiveMQConnectionFactory(
					ActiveMQConnection.DEFAULT_BROKER_URL);
			// create a Connection object
			connection = connectionFactory.createConnection();
			// start the connection
			connection.start();
			// create a Session object
			// transaction false
			// auto acknowledgment sent when sending or receiving a message
			session = connection.createSession(false, Session.AUTO_ACKNOWLEDGE);
			// create a destination - Queue or Topic - where message will be
			// sent or received from
			Destination destination = session
					.createTopic("topic");
			// create a Producer who will send the message
			messageConsumer = session.createConsumer(destination);
			// consume message sent by Producer
			Message message = messageConsumer.receive();
			// check whether it is an instance of TextMessage
			// because we have let Producer send TextMessage
			// there may be other message type
			if (message instanceof TextMessage) {
				TextMessage textMessage = (TextMessage) message;
				System.out.println("Got message published by Publisher : "
						+ textMessage);
			} else {
				throw new JMSException("Message must be a type of TextMessage");
			}
		} catch (JMSException e) {
			e.printStackTrace();
		} finally {
			try {
				messageConsumer.close();
				session.close();
				connection.close();
			} catch (JMSException e) {
				e.printStackTrace();
			}
		}
            }
    
}
