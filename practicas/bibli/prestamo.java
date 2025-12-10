package practicas.bibli;
import java.util.Date;

public class prestamo {
    private Date fechaPrestamo;
    private Date fechaDevolucion;
    private estudiante estudiante; 
    private libro libro; 

    public prestamo(estudiante estudiante, libro libro) {
        this.estudiante = estudiante;
        this.libro = libro;
        this.fechaPrestamo = new Date();

        this.fechaDevolucion = new Date(fechaPrestamo.getTime() + 7L*24*60*60*1000);
    }
    public void mostrarInfo() {
        System.out.println("Prestamo de libro: " + libro.getTitulo());
        estudiante.mostrarInfo();
        System.out.println("Fecha de prestamo: " + fechaPrestamo);
        System.out.println("Fecha de devolucion: " + fechaDevolucion);
    }
}