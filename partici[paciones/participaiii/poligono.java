package participaiii;

public class poligono {
    private int n;
    private double lado;
    private double x;
    private double y;

    public poligono() {
        this.n = 3;
        this.lado = 1;
        this.x = 0;
        this.y = 0;
    }

    public poligono(int n, double lado) {
        this.n = n;
        this.lado = lado;
        this.x = 0;
        this.y = 0;
    }

    public poligono(int n, double lado, double x, double y) {
        this.n = n;
        this.lado = lado;
        this.x = x;
        this.y = y;
    }

    public double getPerimetro() {
        return n * lado;
    }

    public double getArea() {
        return (n * Math.pow(lado, 2)) / (4 * Math.tan(Math.PI / n));
    }
}
