package practicas.prt3;

public class juego {
    protected int numeroDeVidas;
    protected int record;

    public juego(int numeroDeVidas) {
        this.numeroDeVidas = numeroDeVidas;
        this.record = 0;
    }

    public void reiniciaPartida() {
        System.out.println("Partida reiniciada. Vidas restauradas.");
    }

    public void actualizaRecord() {
        if (record < numeroDeVidas) {
            record = numeroDeVidas;
            System.out.println("Nuevo récord: " + record);
        }
    }

    public boolean quitaVida() {
        numeroDeVidas--;
        if (numeroDeVidas > 0) {
            System.out.println("Te quedan " + numeroDeVidas + " vidas.");
            return true;
        } else {
            System.out.println("No te quedan vidas. ¡Perdiste!");
            return false;
        }
    }
}
