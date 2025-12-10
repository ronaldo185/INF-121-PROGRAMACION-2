from datetime import datetime, timedelta

class Prestamo:
    def __init__(self, estudiante, libro):
        self.estudiante = estudiante  
        self.libro = libro            
        self.fecha_prestamo = datetime.now()
        self.fecha_devolucion = self.fecha_prestamo + timedelta(days=7)

    def mostrar_info(self):
        print(f"Prestamo de libro: {self.libro.titulo}")
        self.estudiante.mostrar_info()
        print(f"Fecha de prestamo: {self.fecha_prestamo}")
        print(f"Fecha de devolucion: {self.fecha_devolucion}")
