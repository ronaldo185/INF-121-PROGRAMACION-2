package practicas.prt42;

import java.util.Random;

public class app {
    public static void main(String[] args) {
        Random rand = new Random();
        figura[] figuras = new figura[5];
        String[] colores = {"Rojo", "Azul", "Verde", "Amarillo", "Naranja"};

        for (int i = 0; i < figuras.length; i++) {
            int tipo = rand.nextInt(2) + 1; // 1=Cuadrado, 2=Circulo
            String color = colores[rand.nextInt(colores.length)];

            if (tipo == 1) {
                double lado = 1 + rand.nextDouble() * 9; // lado 1 a 10
                figuras[i] = new cuadrado(lado, color);
            } else {
                double radio = 1 + rand.nextDouble() * 5; // radio 1 a 6
                figuras[i] = new circulo(radio, color);
            }
        }

        System.out.println("=== Lista de Figuras ===");
        for (figura f : figuras) {
            System.out.println(f);
            System.out.printf("Área: %.2f\n", f.area());
            System.out.printf("Perímetro: %.2f\n", f.perimetro());

            // Polimorfismo + instanceof para detectar si implementa la interfaz
            if (f instanceof coloreado  ) {
                coloreado c = (coloreado) f;
                System.out.println("Método comoColorear(): " + c.comoColorear());
            }

            System.out.println("---------------------------");
        }
    }
}
