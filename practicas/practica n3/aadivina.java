package practicas.prt3;

import java.util.Scanner;

public class aadivina extends juego {

    private int numeroAAdivinar;

    public aadivina(int vidas) {
        super(vidas);
    }

    public void juega() {
        reiniciaPartida();

        numeroAAdivinar = (int)(Math.random() * 11); // 0 a 10
        Scanner sc = new Scanner(System.in);

        System.out.println("Adivina un número entre 0 y 10:");

        while (true) {
            int intento = sc.nextInt();

            if (intento == numeroAAdivinar) {
                System.out.println("¡Acertaste!");
                actualizaRecord();
                break;
            } else {
                boolean quedanVidas = quitaVida();
                if (!quedanVidas) break;

                if (intento < numeroAAdivinar)
                    System.out.println("El número a adivinar es MAYOR. Intenta de nuevo:");
                else
                    System.out.println("El número a adivinar es MENOR. Intenta de nuevo:");
            }
        }
        sc.close();
    }
}
