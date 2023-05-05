from abc import ABC, abstractmethod
from dataclasses import dataclass, field


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


@dataclass
class WeatherData:
    __subscribers: list[Display] = field(default_factory=list)
    __temperature: float = 0
    __humidity: float = 0
    __pressure: float = 0

    def __init__(
        self,
        temperature: float,
        humidity: float,
        pressure: float,
        subscribers: list[Display] = [],
    ) -> None:
        self.__temperature = temperature
        self.__humidity = humidity
        self.__pressure = pressure
        self.__subscribers = subscribers

    def subscribe(self, subscriber: Display) -> None:
        if subscriber not in self.__subscribers:
            self.__subscribers.append((subscriber))
            print("Successful subscription!")
        else:
            print("This display object is already subscribed!")

    def unsubscribe(self, subscriber: Display) -> None:
        for i, sub in enumerate(self.__subscribers):
            if sub == subscriber:
                del self.__subscribers[i]
                print("Subscription removed successfully!")
                return
        print("Subscription not found!")

    def __notify(self) -> None:
        for subscriber in self.__subscribers:
            subscriber.update(self.__temperature, self.__humidity, self.__pressure)

    @property
    def temperature(self) -> float:
        return self.__temperature

    @temperature.setter
    def temperature(self, temperature: float):
        self.__temperature = temperature
        self.__notify()

    @property
    def humidity(self) -> float:
        return self.__humidity

    @humidity.setter
    def humidity(self, humidity: float):
        self.__humidity = humidity
        self.__notify()

    @property
    def pressure(self) -> float:
        return self.__pressure

    @pressure.setter
    def pressure(self, pressure: float):
        self.__pressure = pressure
        self.__notify()


if __name__ == "__main__":
    publisher = WeatherData(23, 92, 1017)

    current_condition = CurrentConditionsDisplay()
    statistics = StatisticsDisplay()
    forecast = ForeCastDisplay()

    publisher.subscribe(current_condition)
    publisher.subscribe(statistics)
    publisher.subscribe(forecast)

    publisher.temperature = 22

    publisher.humidity = 100

    publisher.unsubscribe(statistics)

    publisher.pressure = 1000
