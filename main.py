class ElectronicDevice:
    """
    Базовый класс для электронных устройств.
    Атрибуты:
    - brand: Бренд устройства (строка).
    - model: Модель устройства (строка).
    - price: Цена устройства (число с плавающей запятой).
    - power_status: Состояние питания устройства (True - включено, False - выключено).
    """
    
    def __init__(self, brand: str, model: str, price: float):
        self._brand = brand  # защищенный атрибут
        self._model = model  # защищенный атрибут
        self.price = price
        self.power_status = False

    def power_on(self) -> None:
        """ Включает устройство. """
        self.power_status = True
        print(f"{self._brand} {self._model} включен.")

    def power_off(self) -> None:
        """ Выключает устройство. """
        self.power_status = False
        print(f"{self._brand} {self._model} выключен.")

    def __str__(self) -> str:
        """ Возвращает строковое представление устройства. """
        return f"Устройство {self._brand} {self._model}, цена: {self.price}"

    def __repr__(self) -> str:
        """ Возвращает строковое представление для отладки. """
        return f"{self.__class__.__name__}(brand={self._brand!r}, model={self._model!r}, price={self.price!r})"


class Smartphone(ElectronicDevice):
    """
    Класс для смартфонов.
    Атрибуты:
    - battery_capacity: Емкость батареи (целое число).
    """
    
    def __init__(self, brand: str, model: str, price: float, battery_capacity: int):
        # Расширяем конструктор базового класса, добавляя емкость батареи
        super().__init__(brand, model, price)
        self.battery_capacity = battery_capacity

    def __str__(self) -> str:
        """ Перегружаем метод для добавления специфичной информации о смартфоне. """
        return f"Смартфон {self._brand} {self._model}, цена: {self.price}, емкость батареи: {self.battery_capacity} мАч"

    def charge(self, amount: int) -> None:
        """ Заряжает батарею на заданное количество единиц. """
        print(f"Смартфон {self._brand} заряжается на {amount} мАч.")


class Laptop(ElectronicDevice):
    """
    Класс для ноутбуков.
    Атрибуты:
    - ram: Объем оперативной памяти (целое число).
    - storage: Объем встроенной памяти (целое число).
    """
    
    def __init__(self, brand: str, model: str, price: float, ram: int, storage: int):
        # Расширяем конструктор базового класса, добавляя оперативную память и память устройства
        super().__init__(brand, model, price)
        self.ram = ram
        self.storage = storage

    def __str__(self) -> str:
        """ Перегружаем метод для добавления специфичной информации о ноутбуке. """
        return f"Ноутбук {self._brand} {self._model}, цена: {self.price}, RAM: {self.ram} ГБ, SSD: {self.storage} ГБ"

    def upgrade_ram(self, additional_ram: int) -> None:
        """
        Увеличивает объем оперативной памяти.
        Перегружаем метод, потому что у ноутбуков часто есть возможность увеличить RAM.
        """
        self.ram += additional_ram
        print(f"Оперативная память увеличена до {self.ram} ГБ.")


# Пример использования классов
if __name__ == "__main__":
    # Создаем объект смартфона
    smartphone = Smartphone("Apple", "iPhone 13", 999.99, 3300)
    print(smartphone)
    smartphone.charge(500)

    # Создаем объект ноутбука
    laptop = Laptop("Dell", "XPS 15", 1500.00, 16, 512)
    print(laptop)
    laptop.upgrade_ram(8)
