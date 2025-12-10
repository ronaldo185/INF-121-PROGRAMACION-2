package practicas.prt32;

import java.util.Scanner;

public class aadivina extends juego {

    protected int numeroAAdivinar;

    public aadivina(int vidas) {
        super(vidas);
    }

    public boolean validaNumero(int n) {
        return n >= 0 && n <= 10;
    }

    public void juega() {
        reiniciaPartida();

        numeroAAdivinar = (int)(Math.random() * 11);
        Scanner sc = new Scanner(System.in);

        System.out.println("\n--- JUEGO ADIVINA NÚMERO ---");
        System.out.println("Adivina un número entre 0 y 10.");

        while (true) {
            int intento = sc.nextInt();


            if (!validaNumero(intento)) {
                System.out.println("Número inválido. Debe estar entre 0 y 10.");
                continue; 
            }

            if (intento == numeroAAdivinar) {
                System.out.println("¡Acertaste!");
                actualizaRecord();
                break;
            } else {
                boolean quedanVidas = quitaVida();
                if (!quedanVidas) break;

                if (intento < numeroAAdivinar)
                    System.out.println("El número es mayor. Intenta otra vez:");
                else
                    System.out.println("El número es menor. Intenta otra vez:");
            }
        }
        sc.close();
    }
}
