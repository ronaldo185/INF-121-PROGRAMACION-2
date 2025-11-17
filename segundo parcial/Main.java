package novi;

public class Main {
    public static void main(String[] args) {

        Teleferico t = new Teleferico();


        t.lineas.add(new Linea("Roja"));
        t.lineas.add(new Linea("Amarilla"));
        t.lineas.add(new Linea("Azul"));

        t.agregarCabina("Roja");
        t.agregarCabina("Roja");
        t.agregarCabina("Amarilla");
        t.agregarCabina("Amarilla");
        t.agregarCabina("Azul");
        t.agregarCabina("Azul");

        Persona p1 = new Persona("Ana", 20, 60);
        Persona p2 = new Persona("Luis", 30, 80);
        Persona p3 = new Persona("Carlos", 70, 75);
        Persona p4 = new Persona("Maria", 40, 65);
        Persona p5 = new Persona("Pedro", 24, 90);

        // (a) Agregar personas a cabinas específicas
        t.agregarPersonaCabina(p1, "Roja", 1);
        t.agregarPersonaCabina(p2, "Roja", 1);
        t.agregarPersonaCabina(p3, "Roja", 2);
        t.agregarPersonaCabina(p4, "Amarilla", 1);
        t.agregarPersonaCabina(p5, "Azul", 1);

        // (b) Verificar reglas de abordo
        System.out.println("cumplen reglas? " + t.verificarReglasAbordo());

        // (c) Calcular ingreso total
        float ingreso = t.calcularIngresoTotal();
        System.out.println("Ingreso total: " + ingreso + " Bs");

        // (d) Línea con más ingreso regular
        String lineaMayor = t.lineaConMasIngresoRegular();
        System.out.println("Línea con mayor ingreso regular: " + lineaMayor);
    }
}

