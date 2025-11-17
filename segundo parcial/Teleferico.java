package novi;

import java.util.ArrayList;
public class Teleferico {
    ArrayList<Linea> lineas;
    float cantidadIngresos;
    
    public Teleferico() {
        this.lineas = new ArrayList<>();
        this.cantidadIngresos = 0;
    }
    
    public void agregarPersonaFila(Persona p, String linea) {
        for (Linea l : lineas) {
            if (l.getColor().equals(linea)) {
                l.agregarPersona(p);
                return;
            }
        }
    }
    
    public void agregarCabina(String linea) {
        for (Linea l : lineas) {
            if (l.getColor().equals(linea)) {
                l.agregarCabina(l.getCabinas().size() + 1);
                return;
            }
        }
    }
    
    //a) agregar una persona a la cabina
    public boolean agregarPersonaCabina(Persona p, String lineaColor, int nroCabina) {
        for (Linea l : lineas) {
            if (l.getColor().equals(lineaColor)) {
                for (Cabina c : l.getCabinas()) {
                    if (c.getNroCabina() == nroCabina) {
                        return c.agregarPersona(p);
                    }
                }
            }
        }
        return false;
    }

    // b) verificar que las cabinas cum[plas las reglas de abordo de todas las lineas
    public boolean verificarReglasAbordo() {
        for (Linea l : lineas) {
            for (Cabina c : l.getCabinas()) {
                float pesoTotal = c.getPersonas().stream().map(Persona::getPeso).reduce(0f, Float::sum);
                if (c.getPersonas().size() > 10 || pesoTotal > 850) {
                    return false;
                }
            }
        }
        return true;
    }

    //c) calcular el ingreso total del teleferico
    public float getCantidadIngresos() {
        return cantidadIngresos;
    }

    //d) mostrar la linea con mas ingresos en tarifa regular
    public ArrayList<Linea> getLineas() {
        return lineas;
    }

}