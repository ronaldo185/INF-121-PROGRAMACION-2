package practicas.bibli;


public class pagina {
    private int numero;
    private String contenido;

    public pagina(int numero, String contenido) {
        this.numero = numero;
        this.contenido = contenido;
    }

    public void mostrarPagina() {
        System.out.println("Pagina " + numero + ": " + contenido);
    }
}