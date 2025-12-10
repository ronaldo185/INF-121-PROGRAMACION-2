package participavi;

import java.util.Scanner;

public class app {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.print("Ingrese el lado1 del triángulo: ");
        double l1 = sc.nextDouble();
        System.out.print("Ingrese el lado2 del triángulo: ");
        double l2 = sc.nextDouble();
        System.out.print("Ingrese el lado3 del triángulo: ");
        double l3 = sc.nextDouble();

        sc.nextLine(); 
        System.out.print("Ingrese el color del triángulo: ");
        String color = sc.nextLine();

        System.out.print("¿Está rellenado? (true/false): ");
        boolean rellenado = sc.nextBoolean();


        triaangulo t = new triaangulo(l1, l2, l3);
        t.setColor(color);
        t.setRellenado(rellenado);


        System.out.println("\n" + t.toString());
        System.out.println("Área: " + t.getArea());
        System.out.println("Perímetro: " + t.getPerimetro());
        System.out.println("Color: " + t.getColor());
        System.out.println("Rellenado: " + t.isRellenado());

        sc.close();
    }
}
