class ElectronicDevice:
    """
    Базовый класс для всех электронных устройств.

    Атрибуты:
        - brand (str): Бренд устройства.
        - model (str): Модель устройства.
        - price (float): Цена устройства.
        - power_status (bool): Состояние включения устройства (вкл/выкл).
    """

    def __init__(self, brand: str, model: str, price: float):
        self._brand = brand  # Инкапсуляция для защиты данных от прямого изменения
        self._model = model  # Инкапсуляция для защиты данных от прямого изменения
        self.price = price
        self.power_status = False  # По умолчанию устройство выключено

    def power_on(self) -> None:
        """Включает устройство."""
        self.power_status = True
        print(f"{self._brand} {self._model} включен.")

    def power_off(self) -> None:
        """Выключает устройство."""
        self.power_status = False
        print(f"{self._brand} {self._model} выключен.")

    def __str__(self) -> str:
        return f"{self._brand} {self._model}, цена: {self.price}"

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(brand={self._brand!r}, model={self._model!r}, price={self.price!r})"


class Smartphone(ElectronicDevice):
    """
    Класс для смартфонов. Наследует атрибуты и методы базового класса ElectronicDevice.

    Дополнительные атрибуты:
        - battery_capacity (int): Емкость батареи в мА·ч.
    """

    def __init__(self, brand: str, model: str, price: float, battery_capacity: int):
        super().__init__(brand, model, price)
        self.battery_capacity = battery_capacity

    def charge(self) -> None:
        """Зарядка смартфона."""
        print(f"Смартфон {self._brand} {self._model} заряжается.")

    def __str__(self) -> str:
        return f"Смартфон {self._brand} {self._model}, цена: {self.price}, емкость батареи: {self.battery_capacity} мА·ч"


class Laptop(ElectronicDevice):
    """
    Класс для ноутбуков. Наследует атрибуты и методы базового класса ElectronicDevice.

    Дополнительные атрибуты:
        - ram (int): Объем оперативной памяти в ГБ.
        - storage (int): Объем хранилища в ГБ.
    """

    def __init__(self, brand: str, model: str, price: float, ram: int, storage: int):
        super().__init__(brand, model, price)
        self.ram = ram
        self.storage = storage

    def upgrade_ram(self, additional_ram: int) -> None:
        """
        Увеличивает объем оперативной памяти.

        Причина перегрузки метода: В ноутбуках может быть возможность увеличить объем ОЗУ, чего нет у смартфонов.
        """
        self.ram += additional_ram
        print(f"Объем ОЗУ в {self._brand} {self._model} увеличен до {self.ram} ГБ.")

    def __str__(self) -> str:
        return f"Ноутбук {self._brand} {self._model}, цена: {self.price}, ОЗУ: {self.ram} ГБ, хранилище: {self.storage} ГБ"
