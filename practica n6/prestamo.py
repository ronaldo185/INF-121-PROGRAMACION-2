from datetime import datetime, timedelta


class Prestamo:
    def __init__(self, estudiante, libro):
        self.estudiante = estudiante
        self.libro = libro
        self.fecha_prestamo = datetime.now()
        self.fecha_devolucion = self.fecha_prestamo + timedelta(days=7)


    def mostrar_info(self) -> None:
        titulo = self.libro.get_titulo() if hasattr(self.libro, 'get_titulo') else getattr(self.libro, 'titulo', str(self.libro))
        print(f"\nPrestamo de libro: {titulo}")
        if hasattr(self.estudiante, 'mostrar_info'):
            self.estudiante.mostrar_info()
        else:
            print(self.estudiante)
        print("Fecha de prestamo:", self.fecha_prestamo)
        print("Fecha de devolucion:", self.fecha_devolucion)