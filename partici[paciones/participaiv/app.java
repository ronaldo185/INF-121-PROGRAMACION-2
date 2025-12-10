package participaiv;

public class app {
    public static void main(String[] args) {
        Circulo2D c1 = new Circulo2D(2, 0, 1);

        System.out.println("Círculo c1:");
        System.out.println("Área: " + c1.getArea());
        System.out.println("Perímetro: " + c1.getPerimetro());

        System.out.println("\n¿Contiene el punto (2.5, 0)? " + c1.contiene(2.5, 0));
        System.out.println("¿Contiene el círculo (2, 0, 0.5)? " + c1.contiene(new Circulo2D(2, 0, 0.5)));
        System.out.println("¿Se sobrepone al círculo (0, 0, 2)? " + c1.sobrepone(new Circulo2D(0, 0, 2)));
    }
}
