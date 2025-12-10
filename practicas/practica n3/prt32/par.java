package practicas.prt32;

public class par extends aadivina {

    public par(int vidas) {
        super(vidas);
    }

    @Override
    public boolean validaNumero(int n) {
        if (n < 0 || n > 10) {
            System.out.println("Número fuera de rango (0–10).");
            return false;
        }

        if (n % 2 != 0) {
            System.out.println("ERROR: Solo se permiten NÚMEROS PARES.");
            return false;
        }

        return true;
    }
}
