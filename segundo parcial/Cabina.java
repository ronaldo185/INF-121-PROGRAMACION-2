package novi;

import java.util.ArrayList;

public class Cabina {
    int nroCabina;
    ArrayList<Persona> personasAbordo;

    int MAX_PERSONAS = 10;
    float MAX_PESO = 850;
    
    public Cabina(int nroCabina) {
        this.nroCabina = nroCabina;
        this.personasAbordo = new ArrayList<>();
    }
    
    public boolean agregarPersona(Persona p) {
        if (personasAbordo.size() >= MAX_PERSONAS) return false;
        float pesoTotal = personasAbordo.stream().map(Persona::getPeso).reduce(0f, Float::sum);
        if (pesoTotal + p.getPeso() > MAX_PESO) return false;
        personasAbordo.add(p);
        return true;
    }
    
    public ArrayList<Persona> getPersonas() { return personasAbordo; }
    public int getNroCabina() { return nroCabina; }
}
