package practicas.prt4;

import java.util.Scanner;

public class app {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        empleado[] empleados = new empleado[5];

        System.out.println("=== Empleados Tiempo Completo ===");
        for (int i = 0; i < 3; i++) {
            System.out.print("Nombre del empleado " + (i + 1) + ": ");
            String nombre = sc.nextLine();
            System.out.print("Salario anual: ");
            double salarioAnual = sc.nextDouble();
            sc.nextLine(); // limpiar buffer
            empleados[i] = new empleadotc(nombre, salarioAnual);
        }

        System.out.println("\n=== Empleados Tiempo Horario ===");
        for (int i = 3; i < 5; i++) {
            System.out.print("Nombre del empleado " + (i - 2) + ": ");
            String nombre = sc.nextLine();
            System.out.print("Horas trabajadas en el mes: ");
            double horas = sc.nextDouble();
            System.out.print("Tarifa por hora: ");
            double tarifa = sc.nextDouble();
            sc.nextLine(); // limpiar buffer
            empleados[i] = new empleadoth(nombre, horas, tarifa);
        }

        System.out.println("\n=== Lista de Empleados ===");
        for (empleado e : empleados) {
            System.out.println(e.getNombre() + " - Salario Mensual: " + e.CalcularSalarioMensual());
        }

        sc.close();
    }
}
