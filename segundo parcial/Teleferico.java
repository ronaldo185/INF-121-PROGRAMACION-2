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
    // a) agregar p[ersona a una cabina de una linea
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
    // b) verificar que las cabinas cumpla las reglas de abordo de todas las lineas
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
   
    // c) calcular ingreso total con las tarifas del ejercicio
    public float calcularIngresoTotal() {
        float total = 0;

        for (Linea l : lineas) {
            for (Cabina c : l.getCabinas()) {
                for (Persona p : c.getPersonas()) {
                    if (p.getEdad() < 25 || p.getEdad() > 60) {
                        total += 1.5f;
                    }
                    else {
                        total += 3f;
                    }
                }
            }
        }

        return total;
    }

    // d) línea con más ingreso SOLO con tarifa regular
    public String lineaConMasIngresoRegular() {
        String lineaMax = "";
        float maxIngreso = 0;

        for (Linea l : lineas) {
            float ingresoLinea = 0;

            for (Cabina c : l.getCabinas()) {
                for (Persona p : c.getPersonas()) {

                    if (p.getEdad() >= 25 && p.getEdad() <= 60) {
                        ingresoLinea += 3f;
                    }

                }
            }

            if (ingresoLinea > maxIngreso) {
                maxIngreso = ingresoLinea;
                lineaMax = l.getColor();
            }
        }

        return lineaMax;
    }
}