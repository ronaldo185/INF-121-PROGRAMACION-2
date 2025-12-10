package practicas.bibli;

import java.util.ArrayList;

public class libro {
    private String titulo;
    private String ISBN;
    private ArrayList<pagina> paginas;


    public libro(String titulo, String ISBN, ArrayList<pagina> paginas) {
        this.titulo = titulo;
        this.ISBN = ISBN;
        this.paginas = paginas;
    }

    public void agregarPagina(pagina pagina) {
        paginas.add(pagina);
    }

    public void leer() {
        System.out.println("Leyendo libro: " + titulo);
        for (pagina p : paginas) {
            p.mostrarPagina();
        }
    }

    public String getTitulo() {
        return titulo;
    }
}
