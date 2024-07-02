
LOCATION=paris   # Location value can be any country or city you would like to check the weather

build:
	docker build -t current_weather .

run-rain:
	docker run --rm current_weather rain $(LOCATION)

run-shine:
	docker run --rm current_weather shine $(LOCATION)


run-rain-hub:
	docker run --rm snoorrasool/current_weather:v1 rain $(LOCATION)

run-shine-hub:
	docker run --rm snoorrasool/current_weather:v1 shine $(LOCATION)
