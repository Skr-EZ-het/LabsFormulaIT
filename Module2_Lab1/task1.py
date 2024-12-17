import doctest
from abc import ABC, abstractmethod


class Book(ABC):
    """
    Класс, представляющий книгу.

    Атрибуты:
    :param title: Название книги
    :param author: Автор книги
    :param pages: Количество страниц в книге

    Примеры:
    >>> book = Book("Война и мир", "Лев Толстой", 1225)
    """

    def __init__(self, title: str, author: str, pages: int):
        if not isinstance(title, str):
            raise TypeError("Название книги должно быть строкой")
        if not isinstance(author, str):
            raise TypeError("Автор книги должен быть строкой")
        if not isinstance(pages, int) or pages <= 0:
            raise ValueError("Количество страниц должно быть положительным целым числом")

        self.title = title
        self.author = author
        self.pages = pages

    @abstractmethod
    def read_page(self, page: int) -> str:
        """
        Чтение определенной страницы книги.

        :param page: Номер страницы
        :return: Текст страницы

        Примеры:
        >>> book = Book("Война и мир", "Лев Толстой", 1225)
        >>> book.read_page(100)
        """
        ...


class Laptop(ABC):
    """
    Класс, представляющий ноутбук.

    Атрибуты:
    :param brand: Бренд ноутбука
    :param ram: Объем оперативной памяти
    :param ssd: Объем SSD

    Примеры:
    >>> laptop = Laptop("Apple", 16, 512)
    """

    def __init__(self, brand: str, ram: int, ssd: int):
        if not isinstance(brand, str):
            raise TypeError("Бренд должен быть строкой")
        if not isinstance(ram, int) or ram <= 0:
            raise ValueError("Оперативная память должна быть положительным числом")
        if not isinstance(ssd, int) or ssd <= 0:
            raise ValueError("SSD должен быть положительным числом")

        self.brand = brand
        self.ram = ram
        self.ssd = ssd

    @abstractmethod
    def turn_on(self) -> None:
        """
        Включение ноутбука.

        Примеры:
        >>> laptop = Laptop("Apple", 16, 512)
        >>> laptop.turn_on()
        """
        ...


class Car(ABC):
    """
    Класс, представляющий автомобиль.

    Атрибуты:
    :param make: Марка автомобиля
    :param model: Модель автомобиля
    :param year: Год выпуска

    Примеры:
    >>> car = Car("Toyota", "Corolla", 2020)
    """

    def __init__(self, make: str, model: str, year: int):
        if not isinstance(make, str):
            raise TypeError("Марка автомобиля должна быть строкой")
        if not isinstance(model, str):
            raise TypeError("Модель автомобиля должна быть строкой")
        if not isinstance(year, int) or year <= 0:
            raise ValueError("Год выпуска должен быть положительным числом")

        self.make = make
        self.model = model
        self.year = year

    @abstractmethod
    def start_engine(self) -> None:
        """
        Запуск двигателя.

        Примеры:
        >>> car = Car("Toyota", "Corolla", 2020)
        >>> car.start_engine()
        """
        ...
