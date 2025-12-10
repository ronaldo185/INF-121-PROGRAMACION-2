package practicas.bibli;

public class autor {

    private String nombre;
    private String nacionalidad;

    public autor(String nombre, String nacionalidad) {
        this.nombre = nombre;
        this.nacionalidad = nacionalidad;
    }

    public void mostrarInfo() {
        System.out.println("Autor: " + nombre + ", Nacionalidad: " + nacionalidad);
    }
}
