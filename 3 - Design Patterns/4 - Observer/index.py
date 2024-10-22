from abc import ABC, abstractmethod

class Observer(ABC):
    @abstractmethod
    def update(self, temperature: float, humidity: float, pressure: float):
        pass

class CurrentConditionsDisplay(Observer):
    def update(self, temperature: float, humidity: float, pressure: float):
        print(f"Current conditions: {temperature}°C, {humidity}% humidity, {pressure} hPa")

class StatisticsDisplay(Observer):
    def __init__(self):
        self.temperatures = []
        self.humidities = []
        self.pressures = []

    def update(self, temperature: float, humidity: float, pressure: float):
        self.temperatures.append(temperature)
        self.humidities.append(humidity)
        self.pressures.append(pressure)
        avg_temp = sum(self.temperatures) / len(self.temperatures)
        avg_hum = sum(self.humidities) / len(self.humidities)
        avg_press = sum(self.pressures) / len(self.pressures)
        print(f"AVG Temperature: {avg_temp:.2f}°C\nAVG Humidity: {avg_hum:.2f}%\nAVG Pressure: {avg_press:.2f}hPa")

class Subject(ABC):
    @abstractmethod
    def register_observer(self, observer: Observer):
        pass

    @abstractmethod
    def remove_observer(self, observer: Observer):
        pass

    @abstractmethod
    def notify_observers(self):
        pass

class WeatherStation(Subject):
    def __init__(self):
        self.observers = []
        self.temperature = 0
        self.humidity = 0
        self.pressure = 0

    def register_observer(self, observer: Observer):
        self.observers.append(observer)

    def remove_observer(self, observer: Observer):
        self.observers.remove(observer)

    def notify_observers(self):
        for observer in self.observers:
            observer.update(self.temperature, self.humidity, self.pressure)

    def set_weather_data(self, temperature: float, humidity: float, pressure: float):
        self.temperature = temperature
        self.humidity = humidity
        self.pressure = pressure
        self.notify_observers()

if __name__ == "__main__":
    weather_station = WeatherStation()

    current_display = CurrentConditionsDisplay()
    stats_display = StatisticsDisplay()

    weather_station.register_observer(current_display)
    weather_station.register_observer(stats_display)

    weather_station.set_weather_data(25.3, 65, 1013)
    weather_station.set_weather_data(26.1, 62.5, 1012)
    weather_station.set_weather_data(26.5, 60, 1010)