package practicas.bibli;

public class estudiante {
    private String codigo;
    private String nombre;

    public estudiante(String codigo, String nombre) {
        this.codigo = codigo;
        this.nombre = nombre;
    }

    public void mostrarInfo() {
        System.out.println("Estudiante: " + nombre + ", Codigo: " + codigo);
    }
}
