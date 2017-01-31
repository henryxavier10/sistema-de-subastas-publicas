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
    public static String nombre_subasta="";
    private static Publisher publishersubastador;
    ArrayList<String>
    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        // TODO code application logic here
        
       iniciar_subastador();
        
    /**
     *
     */
    
    }
    
    public static void mostrarmenu(){ 
            while(opcion != 0){
			//Try catch para evitar que el programa termine si hay un error
                    try{
                            System.out.println("**********************************************************************************************");
                            System.out.println("**********************************************************************************************"); 
                            System.out.println("************************************BIENVENIDO "+nombre_subastador+"**********************************************");
                            System.out.println("**********************************************************************************************");
                            System.out.println("**********************************************************************************************");
                        
                            System.out.println("Elige opción:\n1.- Crear subasta" +
                                            "\n2.- Ver subastas" +
                                            "\n0.- Salir");
                            opcion = Integer.parseInt(new Scanner(System.in).nextLine()); 

                            switch(opcion){
                            case 1: 
                                    System.out.println("");
                                    crear_subasta();
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
    
    public static void iniciar_subastador(){
        System.out.println("**********************************************************************************************");
        System.out.println("**********************************************************************************************"); 
        System.out.println("**************************************SUBASTADOR**********************************************");
        System.out.println("**********************************************************************************************");
        System.out.println("**********************************************************************************************");
        System.out.println("Ingrese su nombre:");
        nombre_subastador= new Scanner(System.in).nextLine();
        Subastador subastador = new Subastador(nombre_subastador);
        mostrarmenu();
    }
    
    
    public static void crear_subasta() throws Exception{
        System.out.println("**********************************************************************************************");
        System.out.println("**********************************************************************************************"); 
        System.out.println("**************************************SUBASTA**********************************************");
        System.out.println("**********************************************************************************************");
        System.out.println("**********************************************************************************************");
        System.out.println("Ingrese el nombre de la subasta:");
        nombre_subasta= new Scanner(System.in).nextLine();
        publishersubastador = new Publisher();
        publishersubastador.create(nombre_subastador,"subastas");
        publishersubastador.sendCanal("holaaa");
        mostrarmenu();
    }
}
