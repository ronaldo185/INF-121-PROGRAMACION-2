package participaiv;

public class Circulo2D {
    // Campos privados
    private double x;
    private double y;
    private double radio;

    // Constructor sin argumentos
    public Circulo2D() {
        this.x = 0;
        this.y = 0;
        this.radio = 1;
    }

    // Constructor con valores especificados
    public Circulo2D(double x, double y, double radio) {
        this.x = x;
        this.y = y;
        this.radio = radio;
    }

    // Métodos get
    public double getX() {
        return x;
    }

    public double getY() {
        return y;
    }

    public double getRadio() {
        return radio;
    }

    // Método para calcular área
    public double getArea() {
        return Math.PI * radio * radio;
    }

    // Método para calcular perímetro
    public double getPerimetro() {
        return 2 * Math.PI * radio;
    }

    // Método para verificar si un punto está dentro del círculo
    public boolean contiene(double px, double py) {
        double distancia = Math.sqrt(Math.pow(px - x, 2) + Math.pow(py - y, 2));
        return distancia <= radio;
    }

    // Método para verificar si otro círculo está completamente dentro
    public boolean contiene(Circulo2D c) {
        double distanciaCentros = Math.sqrt(Math.pow(c.getX() - x, 2) + Math.pow(c.getY() - y, 2));
        return distanciaCentros + c.getRadio() <= radio;
    }

    // Método para verificar si otro círculo se sobrepone
    public boolean sobrepone(Circulo2D c) {
        double distanciaCentros = Math.sqrt(Math.pow(c.getX() - x, 2) + Math.pow(c.getY() - y, 2));
        return distanciaCentros < (radio + c.getRadio()) && !this.contiene(c);
    }
}
