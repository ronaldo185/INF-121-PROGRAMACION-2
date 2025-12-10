package participaiii;

public class test {
    public static void main(String[] args) {
        // Crear tres objetos
        poligono pol1 = new poligono();
        poligono pol2 = new poligono(6, 4);
        poligono pol3 = new poligono(10, 4, 5.6, 7.8);

        // Mostrar perímetro y área de cada uno
        System.out.println("Polígono 1:");
        System.out.println("Perímetro: " + pol1.getPerimetro());
        System.out.println("Área: " + pol1.getArea());

        System.out.println("\nPolígono 2:");
        System.out.println("Perímetro: " + pol2.getPerimetro());
        System.out.println("Área: " + pol2.getArea());

        System.out.println("\nPolígono 3:");
        System.out.println("Perímetro: " + pol3.getPerimetro());
        System.out.println("Área: " + pol3.getArea());
    }
}
