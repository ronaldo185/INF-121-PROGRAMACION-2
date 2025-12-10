package participaii;

public class app {

    private boolean estado;
    private String colorLuz;
    private int brillo;

    
    public app(String colorLuz, int brillo) {
        this.estado = false;
        this.colorLuz = colorLuz;
        this.brillo = brillo;
    }

    
    public void encender() {
        estado = true;
        System.out.println("La lámpara está encendida.");
    }

    public void apagar() {
        estado = false;
        System.out.println("La lámpara está apagada.");
    }

    public void ajustarBrillo(int nuevoBrillo) {
        brillo = nuevoBrillo;
        System.out.println("Brillo ajustado a " + brillo);
    }


    public boolean isEncendida() {
        return estado;
    }

    public String getColorLuz() {
        return colorLuz;
    }

    public int getBrillo() {
        return brillo;
    }
}
