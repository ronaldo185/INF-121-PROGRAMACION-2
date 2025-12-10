package participavi;

import java.util.Date;

public class objeto {
    private String color;
    private boolean rellenado;
    private Date fechaDeCreacion;

    public objeto() {
        this.color = "blanco";
        this.rellenado = false;
        this.fechaDeCreacion = new Date();
    }

    public objeto(String color, boolean rellenado) {
        this.color = color;
        this.rellenado = rellenado;
        this.fechaDeCreacion = new Date();
    }

    public String getColor() {
        return color;
    }

    public void setColor(String color) {
        this.color = color;
    }

    public boolean isRellenado() {
        return rellenado;
    }

    public void setRellenado(boolean rellenado) {
        this.rellenado = rellenado;
    }

    public Date getFechaDeCreacion() {
        return fechaDeCreacion;
    }

    @Override
    public String toString() {
        return "Objeto Geometrico[color=" + color + ", rellenado=" + rellenado + ", fechaDeCreacion=" + fechaDeCreacion + "]";
    }
}
