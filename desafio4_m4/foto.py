from error import DimensionError


class Foto:
    """Clase que representa una fotografía con dimensiones de ancho y alto.

    Attributes:
        MAX (int): El valor máximo permitido para el ancho y alto de la fotografía.
        __ancho (int): El ancho de la fotografía.
        __alto (int): El alto de la fotografía.
        ruta (str): La ruta de la imagen.
    """

    MAX = 2500

    def __init__(self, ancho: int, alto: int, ruta: str) -> None:
        """Inicializa una instancia de la clase Foto.

        Args:
            ancho (int): El ancho de la fotografía.
            alto (int): El alto de la fotografía.
            ruta (str): La ruta del archivo de imagen.

        Raises:
            DimensionError: Si el ancho o alto están fuera del rango permitido.
        """
        self.__ancho = ancho
        self.__alto = alto
        ruta = ruta

    @property
    def ancho(self) -> int:
        """Obtiene el ancho de la fotografía.

        Returns:
            int: El ancho de la fotografía.
        """
        return self.__ancho

    @ancho.setter
    def ancho(self, ancho: int) -> None:
        """Establece el ancho de la fotografía.

        Args:
            ancho (int): El nuevo ancho de la fotografía.

        Raises:
            DimensionError: Si el nuevo ancho está fuera del rango permitido.
        """
        if ancho < 1 or ancho > Foto.MAX:
            raise DimensionError("Ancho no válido", ancho, Foto.MAX)
        self.__ancho = ancho

    @property
    def alto(self) -> int:
        """Obtiene el alto de la fotografía.

        Returns:
            int: El alto de la fotografía.
        """
        return self.__alto

    @alto.setter
    def alto(self, alto: int) -> None:
        """Establece el alto de la fotografía.

        Args:
            alto (int): El nuevo alto de la fotografía.

        Raises:
            DimensionError: Si el nuevo alto está fuera del rango permitido.
        """
        if alto < 1 or alto > Foto.MAX:
            raise DimensionError("Alto no válido", alto, Foto.MAX)
        else:
            self.__alto = alto


try:
    ruta = input("Ingrese ruta de la imagen: ")
    int_ancho = int(input("Ingrese ancho de la imagen: "))
    int_alto = int(input("Ingrese alto de la imagen: "))
    fotos = Foto(int_ancho, int_alto, ruta)
    print(fotos.alto)
    print(fotos.ancho)
    int_ancho = int(input("Ingrese nuevo ancho de la imagen: "))
    int_alto = int(input("Ingrese nuevo alto de la imagen: "))

    fotos.ancho = int_ancho
    print(fotos.ancho)
    fotos.alto = int_alto
    print(fotos.alto)
except DimensionError as e:
    print(e)
except ValueError:
    print("Ha ocurrido un error al ingresar los valores")
except Exception as e:
    print(f"Ha ocurrido un error inesperado: {e}")
