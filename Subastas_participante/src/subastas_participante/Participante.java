/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package subastas_participante;

/**
 *
 * @author henry
 */
public class Participante {
    public String nombre;
    public double valor_oferta;
    public double capital;
    
    public Participante(String nombre) {
        this.nombre = nombre;
    }
    
    public Participante(String nombre, double valor_oferta, double capital) {
        this.nombre = nombre;
        this.valor_oferta = valor_oferta;
        this.capital = capital;
    }

    public double getCapital() {
        return capital;
    }

    public void setCapital(double capital) {
        this.capital = capital;
    }

  

    public String getNombre() {
        return nombre;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }

    public double getValor_oferta() {
        return valor_oferta;
    }

    public void setValor_oferta(double valor_oferta) {
        this.valor_oferta = valor_oferta;
    }
    
}
