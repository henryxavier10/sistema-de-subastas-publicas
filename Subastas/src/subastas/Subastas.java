/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package subastas;

import java.util.Scanner;
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
public class Subastas {
    public static int opcion = -1;
    public static String nombre_subastador="";
    public static String nombre_participante="";
    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        // TODO code application logic here
        
       mostrarmenu();
        
    /**
     *
     */
    
    }
    
    public static void mostrarmenu(){ 
            System.out.println("**********************************************************************************************");
            System.out.println("**********************************************************************************************"); 
            System.out.println("***************************BIENVENIDOS A SUBASTAS ON-LINE*************************************");
            System.out.println("**********************************************************************************************");
            System.out.println("**********************************************************************************************");
            while(opcion != 0){
			//Try catch para evitar que el programa termine si hay un error
                    try{
                            System.out.println("Elige opción:\n1.- Ser Subastador" +
                                            "\n2.- Ser Participante de una subasta\n" +
                                            "3.- Ver Resultados\n" +
                                            "0.- Salir");
                            opcion = Integer.parseInt(new Scanner(System.in).nextLine()); 

                            switch(opcion){
                            case 1: 
                                    System.out.println("");
                                    crear_subastador();
                                    break;
                            case 2: 
                                    System.out.println("");
                                    break;
                            case 3: 
                                    System.out.println("");
                                    break;
                            case 0: 
                                    System.out.println("Adios!");
                                    break;
                            default:
                                    System.out.println("Número no reconocido");
                                    break;
                            }

                            System.out.println("\n"); 
                    }catch(Exception e){
                            System.out.println("Error!");
                    }
	}
    }
    
    public static void crear_subastador(){
        System.out.println("**********************************************************************************************");
        System.out.println("**********************************************************************************************"); 
        System.out.println("**************************************SUBASTADOR**********************************************");
        System.out.println("**********************************************************************************************");
        System.out.println("**********************************************************************************************");
        System.out.println("Ingrese su nombre:");
        nombre_subastador= new Scanner(System.in).nextLine();
        Subastador subastador = new Subastador(nombre_subastador);
        System.out.println("nombre de subastador:"+subastador.nombre);
    }
    
}
