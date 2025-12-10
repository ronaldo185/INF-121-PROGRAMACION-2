package practicas.prt4;

public class empleadoth extends empleado {
    private double horasTrabajadas;
    private double tarifaHora;

    public empleadoth(String nombre, double horasTrabajadas, double tarifaHora) {
        super(nombre);
        this.horasTrabajadas = horasTrabajadas;
        this.tarifaHora = tarifaHora;
    }

    @Override
    public double CalcularSalarioMensual() {
        return horasTrabajadas * tarifaHora;
    }

    @Override
    public String toString() {
        return super.toString() + ", Horas Trabajadas: " + horasTrabajadas +
               ", Tarifa por Hora: " + tarifaHora +
               ", Salario Mensual: " + CalcularSalarioMensual();
    }
}
