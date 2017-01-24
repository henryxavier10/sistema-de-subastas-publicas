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
import javax.jms.Session;
import javax.jms.TextMessage;
 
import org.apache.activemq.ActiveMQConnection;
import org.apache.activemq.ActiveMQConnectionFactory;
/**
 *
 * @author henry
 */
public class Publisher {
    private ConnectionFactory connectionFactory;
    private Connection connection;
    private Session session;
    private javax.jms.MessageProducer messageProducer;
    
    
    public void publishMessage(final String message) {
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
                    messageProducer = session.createProducer(destination);
                    // create a TextMessage, there are many more message types
                    TextMessage textMessage = session.createTextMessage(message);
                    // send the message
                    messageProducer.send(textMessage);
                    System.out.println("Publishing Message : " + textMessage);
            } catch (JMSException e) {
                    e.printStackTrace();
            } finally {
                    try {
                            messageProducer.close();
                            session.close();
                            connection.close();
                    } catch (JMSException e) {
                            e.printStackTrace();
                    }
            }
    }
}
