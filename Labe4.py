if __name__ == "__main__":
    clas Transport:
        # Базовый класс
        def __init__(self, capacity: int, name: str):
            self.capacity = capacity
            self.name = name

        def __str__(self) -> str:
            return f'Транспортное средство "{self.name}"'

        def __repr__(self) -> str:
            return f"Transport(name={self.name!r}, capacity={self.capacity})"

        def road_time(self, distance: float) -> int:
            ... #Считает время в пути


    class Public_transport(Transport):
        def __init__(self, capacity: int, name: str):
            self.type=type

        def __str__(self) -> str:
            return f'Транспортное средство "{self.name}"'

        def __repr__(self) -> str:
            return f"Transport(name={self.name!r}, capacity={self.capacity})"

        def road_time(self, distance: float):
            ... #Считает время в пути пешком, на транспорте, общее

    pass
