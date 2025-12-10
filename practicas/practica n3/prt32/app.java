package practicas.prt32;

public class app {
    public static void main(String[] args) {

        aadivina juego1 = new aadivina(3);
        par juego2 = new par(3);
        impar juego3 = new impar(3);


        juego1.juega();
        juego2.juega();
        juego3.juega();
    }
}
