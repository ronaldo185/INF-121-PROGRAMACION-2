package practicas.prt4;

public abstract class empleado {
    protected String nombre;

    public empleado(String nombre) {
        this.nombre = nombre;
    }

    public abstract double CalcularSalarioMensual();

    @Override
    public String toString() {
        return "Nombre: " + nombre;
    }

    public String getNombre() {
        return nombre;
    }
}
