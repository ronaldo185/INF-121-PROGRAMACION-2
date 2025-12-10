package practicas.bibli;
import java.util.ArrayList;


public class SistemaBiblioteca {
    public static void main(String[] args) {
        // Crear horario
        horario horario = new horario("Lunes a Viernes", "08:00", "18:00");

        // Crear biblioteca
        biblioteca biblioteca = new biblioteca("Biblioteca UMSA", horario);

        // Crear autores
        autor autor1 = new autor("Gabriel Garcia Marquez", "Colombiano");
        autor autor2 = new autor("Isabel Allende", "Chilena");
        biblioteca.agregarAutor(autor1);
        biblioteca.agregarAutor(autor2);

        // Crear libros
        ArrayList<pagina> paginasLibro1 = new ArrayList<>();
        libro libro1 = new libro("Cien Años de Soledad", "ISBN001", paginasLibro1);
        libro1.agregarPagina(new pagina(1, "Capítulo 1..."));
        libro1.agregarPagina(new pagina(2, "Capítulo 2..."));
        ArrayList<pagina> paginasLibro2 = new ArrayList<>();
        libro libro2 = new libro("La Casa de los Espíritus", "ISBN002", paginasLibro2);
        libro2.agregarPagina(new pagina(1, "Capítulo 1..."));

        biblioteca.agregarLibro(libro1);
        biblioteca.agregarLibro(libro2);

        // Crear estudiante
        estudiante estudiante = new estudiante("S001", "Juan Perez");

        // Prestar libro
        biblioteca.prestarLibro(estudiante, libro1);

        // Mostrar estado
        biblioteca.mostrarEstado();

        // Cerrar biblioteca
        biblioteca.cerrarBiblioteca();
    }
}
