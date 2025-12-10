package practicas.bibli;


public class horario {
    private String diasApertura;
    private String horaApertura;
    private String horaCierre;

    public horario(String diasApertura, String horaApertura, String horaCierre) {
        this.diasApertura = diasApertura;
        this.horaApertura = horaApertura;
        this.horaCierre = horaCierre;
    }

    public void mostrarHorario() {
        System.out.println("Horario: " + diasApertura + " de " + horaApertura + " a " + horaCierre);
    }
}