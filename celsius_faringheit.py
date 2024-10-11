class Temperature:
    def __init__(self, celsius):
        self.__celsius = celsius  # Приватная переменная для хранения температуры в Цельсиях

    def to_fahrenheit(self):
        # Преобразование в Фаренгейт
        return (self.__celsius * 9/5) + 32

    def get_celsius(self):
        # Получение температуры в Цельсиях
        return self.__celsius


# Пример использования:
temp = Temperature(25)  # Создаем объект с начальнной температурой 25 градусов Цельсия
fahrenheit = temp.to_fahrenheit()  # Преобразуем в Фаренгейт
celsius = temp.get_celsius()  # Получаем температуру в Цельсиях

print(f"Temperature in Fahrenheit: {fahrenheit}")  # Выводим значение в Фаренгейте
print(f"Temperature in Celsius: {celsius}")        # Выводим значение в Цельсиях