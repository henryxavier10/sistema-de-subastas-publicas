/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package subastas_participante;

import java.util.Scanner;

/**
 *
 * @author henry
 */
public class Subastas_participante {

    /**
     * @param args the command line arguments
     */
    
    public static int opcion = -1;
    public static String nombre_canal="";
    public static String nombre_participante="";
    
    public static void main(String[] args) {
        // TODO code application logic here
        mostrarmenu();
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
                            System.out.println("Elige opción:\n1.- Resgistrarse en Subasta\n"+
                                            "0.- Salir");
                            opcion = Integer.parseInt(new Scanner(System.in).nextLine()); 

                            switch(opcion){
                            case 1: 
                                    String part="";
                                    System.out.println("");
                                    part=Registrar_participante();
                                    Ver_list_subastas(part);
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
    
    public static String Registrar_participante(){
        System.out.println("**********************************************************************************************");
        System.out.println("**********************************************************************************************"); 
        System.out.println("**************************************REGISTRAR**********************************************");
        System.out.println("**********************************************************************************************");
        System.out.println("**********************************************************************************************");
        
        
        System.out.println("Ingrese su nombre:");
        nombre_participante= new Scanner(System.in).nextLine();
        Participante participante = new Participante(nombre_participante);
        System.out.println("nombre del participante:"+participante.nombre);
        return participante.nombre;
    }
    
    public static void Ver_list_subastas(String p ){
        System.out.println("**********************************************************************************************");
        System.out.println("**********************************************************************************************"); 
        System.out.println("**************************************BIENVENIDO "+p+"**********************************************");
        System.out.println("**********************************************************************************************");
        System.out.println("**********************************************************************************************");
        
        
        System.out.println("Subastas:");
        nombre_participante= new Scanner(System.in).nextLine();
        Participante participante = new Participante(nombre_participante);
        System.out.println("Ingrese la subasta a participar:"+participante.nombre);
        //return participante.nombre;
    }
}


