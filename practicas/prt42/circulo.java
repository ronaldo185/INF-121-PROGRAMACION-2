package practicas.prt42;

public class circulo extends figura {
    private double radio;

    public circulo(double radio, String color) {
        super(color);
        this.radio = radio;
    }

    @Override
    public double area() {
        return Math.PI * radio * radio;
    }

    @Override
    public double perimetro() {
        return 2 * Math.PI * radio;
    }

    @Override
    public String toString() {
        return "Circulo - " + super.toString() + ", Radio: " + radio;
    }
}
