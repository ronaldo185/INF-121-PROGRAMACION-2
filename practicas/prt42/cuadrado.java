package practicas.prt42;

public class cuadrado extends figura implements coloreado {
    private double lado;

    public cuadrado(double lado, String color) {
        super(color);
        this.lado = lado;
    }

    @Override
    public double area() {
        return lado * lado;
    }

    @Override
    public double perimetro() {
        return 4 * lado;
    }

    @Override
    public String comoColorear() {
        return "Colorear los cuatro lados";
    }

    @Override
    public String toString() {
        return "Cuadrado - " + super.toString() + ", Lado: " + lado;
    }
}
