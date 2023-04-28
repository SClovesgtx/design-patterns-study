class WheatherData:

    __temperature: float
    __humidity: float
    __pressure: float

    def __init__(
        self, current_conditions_display, statistics_display, fore_cast_display
    ):
        self.current_conditions_display = current_conditions_display
        self.statistics_display = statistics_display
        self.fore_cast_display = fore_cast_display

    def measurementsChanged(self):
        temp: float = self.__temperature
        humidity: float = self.__humidity
        pressure: float = self.__pressure

        self.current_conditions_display.update(temp, humidity, pressure)
        self.statistics_display.update(temp, humidity, pressure)
        self.fore_cast_display.update(temp, humidity, pressure)
