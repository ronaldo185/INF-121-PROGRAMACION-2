package practicas.prt42;

public abstract class figura {
    private String color;

    public figura(String color) {
        this.color = color;
    }

    public void setColor(String color) {
        this.color = color;
    }

    public String getColor() {
        return color;
    }

    public abstract double area();
    public abstract double perimetro();

    @Override
    public String toString() {
        return "Color: " + color;
    }
}
