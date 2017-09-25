#### Petrol Station
#- Create `Station` and `Car` classes
#- `Station`
#  - gas_amount
#  - refill(car) -> decreases the gasAmount by the capacity of the car and increases the cars gas_amount
#- `Car`
#  - gas_amount
#  - capacity
#  - create constructor for `Car` where:
#    - initialize gas_amount -> 0
#    - initialize capacity -> 100

class Station(object):
  gas_amount = 1000

  def refill(self, car):
    self.gas_amount -= car.capacity
    car.gas_amount += car.capacity
    

class Car(object):
  def __init__(self, gas_amount, capacity):
    self.gas_amount = gas_amount
    self.capacity = capacity

car = Car(0, 100)
station = Station()
station.refill(car)
print(car.gas_amount)
print(station.gas_amount)
  