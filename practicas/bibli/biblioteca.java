package practicas.bibli;

import java.util.ArrayList;

public class biblioteca {
    private String nombre;
    private ArrayList<libro> libros;     
    private ArrayList<autor> autores; 
    private ArrayList<prestamo> prestamos;
    private horario horario;              

    public biblioteca(String nombre, horario horario) {
        this.nombre = nombre;
        this.horario = horario;
        this.libros = new ArrayList<>();
        this.autores = new ArrayList<>();
        this.prestamos = new ArrayList<>();
    }
    // Métodos para agregar libros
    public void agregarLibro(libro libro) {
        libros.add(libro);
    }
    // Métodos para agregar autores
    public void agregarAutor(autor autor) {
        autores.add(autor);
    }
    // Método para prestar libros
    public void prestarLibro(estudiante estudiante, libro libro) {
        prestamo p = new prestamo(estudiante, libro);
        prestamos.add(p);
        System.out.println("Libro prestado exitosamente: " + libro.getTitulo());
    }
    // Método para mostrar el estado de la biblioteca
    public void mostrarEstado() {
        System.out.println("\n--- Biblioteca: " + nombre + " ---");
        horario.mostrarHorario();

        System.out.println("\nLibros disponibles:");
        for (libro l : libros) {
            System.out.println("- " + l.getTitulo());
        }

        System.out.println("\nAutores registrados:");
        for (autor a : autores) {
            a.mostrarInfo();
        }

        System.out.println("\nPrestamos activos:");
        for (prestamo p : prestamos) {
            p.mostrarInfo();
            System.out.println();
        }
    }
    // Método para cerrar la biblioteca
    public void cerrarBiblioteca() {
        prestamos.clear(); 
        System.out.println("La biblioteca " + nombre + " ha cerrado. Todos los prestamos han sido eliminados.");
    }
}
