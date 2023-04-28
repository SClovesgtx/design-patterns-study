
# Observer

Please, read about observer [here](https://refactoring.guru/pt-br/design-patterns/observer).


!<img src="./imgs/2.png" width="50%" height="50%" />


```mermaid
classDiagram

    Publisher o-- Subscriber
    ConcreteSubscriber1 ..|> Subscriber
    ConcreteSubscriber2 ..|> Subscriber

    class Publisher{
        - subscribers: Subscriber[]
        - mainState
        + subscribe(s: Subscriber)
        + unsubscribe(s: Subscriber)
        + notifySubscriber()
        + mainBusinessLogic()
    }

    class Subscriber{
        + update(context)
    }

    class ConcreteSubscriber1{
        + update(context)
    }

    class ConcreteSubscriber2{
        + update(context)
    }
    <<interface>> Subscriber
```

# Example problem: API Weather-O-Rama

This examples was extract from the book [Head First Design Patterns](https://www.oreilly.com/library/view/head-first-design/0596007124/).

> The weather station will be based on our patent pending WeatherData object, which tracks current weather conditions (temperature, humidity, and pressure). We'd like for you to create an application that initially provides three display elements: current conditions, weather statistics and a simple forecast, all updated in real time as the WeatherData object acquires the most recent measurements.

Here a scheme of the final application:

!<img src="./imgs/1.png" width="50%" height="50%" />

## What we know about the WeatherData?

- The WeatherData class has getter methods for three
measurement values: temperature, humidity and
barometric pressure.
- The measurementsChanged() method is called any
time new weather measurement data is available. (We
don’t know or care how this method is called; we just
know that it is.)
- We need to implement three display elements that
use the weather data: a current conditions display, a
statistics display and a forecast display. These displays
must be updated each time WeatherData has new
measurements.
- The system must be expandable—other developers
can create new custom display elements and users
can add or remove as many display elements as they
want to the application. Currently, we know about
only the initial three display types (current conditions,
statistics and forecast).

Here a diagram of Weather class:

```mermaid
classDiagram
    class WeatherData
    WeatherData : +get_temperature()
    WeatherData : +get_humidity()
    WeatherData : +get_pressure()
    WeatherData : +measurementsChanged()
```

Our job is to implement measurementsChanged()
so that it updates the three displays for current
conditions, weather stats, and forecast.

## API Weather-O-Rama with Observer

```mermaid
classDiagram

    WeatherData o-- Display
    CurrentConditionsDisplay ..|> Display
    StatisticsDisplay ..|> Display
    ForeCastDisplay ..|> Display

    class WeatherData{
        - subscribers: list = Display
        - temperature
        - humidity
        - pressure
        + subscribe(s: Subscriber)
        + unsubscribe(s: Subscriber)
        + measurementsChanged()
    }

    class Display{
        + update(temperature: float, humidity: float, pressure: float)
    }

    class CurrentConditionsDisplay{
        + update(temperature: float, humidity: float, pressure: float)
    }

    class StatisticsDisplay{
        + update(temperature: float, humidity: float, pressure: float)
    }

    class ForeCastDisplay{
        + update(temperature: float, humidity: float, pressure: float)
    }

    <<interface>> Display
```


# Puch Line

> Strive for loosely coupled designs
between objects that interact.

