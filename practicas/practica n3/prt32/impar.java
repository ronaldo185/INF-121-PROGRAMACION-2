package practicas.prt32;

public class impar extends aadivina {

    public impar(int vidas) {
        super(vidas);
    }

    @Override
    public boolean validaNumero(int n) {
        if (n < 0 || n > 10) {
            System.out.println("Número fuera de rango (0–10).");
            return false;
        }

        if (n % 2 == 0) {
            System.out.println("ERROR: Solo se permiten NÚMEROS IMPARES.");
            return false;
        }

        return true;
    }
}
