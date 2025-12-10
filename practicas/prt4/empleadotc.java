package practicas.prt4;

public class empleadotc extends empleado {
    private double salarioAnual;

    public empleadotc(String nombre, double salarioAnual) {
        super(nombre);
        this.salarioAnual = salarioAnual;
    }

    @Override
    public double CalcularSalarioMensual() {
        return salarioAnual / 12;
    }

    @Override
    public String toString() {
        return super.toString() + ", Salario Anual: " + salarioAnual +
               ", Salario Mensual: " + CalcularSalarioMensual();
    }
}
