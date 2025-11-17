package novi;

import java.util.ArrayList;

public class Linea {
    String color;
    ArrayList<Persona> filaPersonas;
    ArrayList<Cabina> cabinas;
    
    public Linea(String color) {
        this.color = color;
        this.filaPersonas = new ArrayList<>();
        this.cabinas = new ArrayList<>();
    }
    
    public void agregarPersona(Persona p) { filaPersonas.add(p); }
    public void agregarCabina(int nroCab) { cabinas.add(new Cabina(nroCab)); }
    public ArrayList<Cabina> getCabinas() { return cabinas; }
    public String getColor() { return color; }
}