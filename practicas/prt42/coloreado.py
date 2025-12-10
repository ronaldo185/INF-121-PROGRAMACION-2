from abc import ABC, abstractmethod

class Coloreado(ABC):
    @abstractmethod
    def como_colorear(self) -> str:
        pass
