from abc import ABC, abstractmethod


class Display:
    @abstractmethod
    def update(self, temperature: float, humidity: float, pressure: float) -> None:
        raise NotImplemented


class CurrentConditionsDisplay(Display):
    def update(self, temperature: float, humidity: float, pressure: float) -> None:
        # do some thing
        print("Thanks from CurrentConditionsDisplay!")


class StatisticsDisplay(Display):
    def update(self, temperature: float, humidity: float, pressure: float) -> None:
        # do some thing
        print("Thanks from StatisticsDisplay!")


class ForeCastDisplay(Display):
    def update(self, temperature: float, humidity: float, pressure: float) -> None:
        # do some thing
        print("Thanks from ForeCastDisplay!")


class WeatherData:
    __subscribers: list[Display] = []
    __temperature: float
    __humidity: float
    __pressure: float

    def __init__(self, temperature: float, humidity: float, pressure: float) -> None:
        self.__temperature = temperature
        self.__humidity = humidity
        self.__pressure = pressure

    def subscribe(self, subscriber: Display) -> None:
        self.__subscribers.append((subscriber))
        print("Successful subscription!")

    def unsubscribe(self, subscriber: Display) -> None:
        for i, sub in enumerate(self.__subscribers):
            if sub == subscriber:
                del self.__subscribers[i]
                print("Subscription removed successfully!")
                return
        print("Subscription not found!")

    def ___measurementsChanged(self) -> None:
        for subscriber in self.__subscribers:
            subscriber.update(self.__temperature, self.__humidity, self.__pressure)

    def set_temperature(self, temperature: float):
        self.__temperature = temperature
        self.___measurementsChanged()

    def set_humidity(self, humidity: float):
        self.__humidity = humidity
        self.___measurementsChanged()

    def set_pressure(self, pressure: float):
        self.__pressure = pressure
        self.___measurementsChanged()


if __name__ == "__main__":
    publisher = WeatherData(23, 92, 1017)

    current_condition = CurrentConditionsDisplay()
    statistics = StatisticsDisplay()
    forecast = ForeCastDisplay()

    publisher.subscribe(current_condition)
    publisher.subscribe(statistics)
    publisher.subscribe(forecast)

    publisher.set_temperature(22)

    publisher.set_humidity(100)

    publisher.unsubscribe(statistics)

    publisher.set_pressure(1000)
