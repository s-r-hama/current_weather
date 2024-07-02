## Instructions/Howto


This script that will look for the current weather in your locale using a public API


</br>
</br>





#### To run it locally you need the followling: 

- Python 3.x
- `requests` library (install using `python3 -m pip install requests`) on Mac
- OpenWeatherMap API key : Go to the `https://home.openweathermap.org/api_keys` signup and create your own API key and paste it inside the code.



</br>
</br>




#### Example of python running command to check if it's going to rain or Shine in Paris or any other country or city:

```sh
python current_weather.py rain|shine Country|City

python current_weather.py rain Paris
python current_weather.py shine Paris

```
</br>
</br>


#### Dockerfile

##### 1. To build the image and run the docker image locally:

```sh

docker build -t current_weather .
docker run --rm current_weather rain paris
docker run --rm current_weather shine paris
```

</br>

##### 2. Add image to My Docker Hub registery, the registery for now is public so you can run it anywhere on any Operating system

I applied the following steps to add it to my registery, you need to have an account and need login to push the image, but for pulling image login is not required:
 ```sh

docker tag current_weather:latest snoorrasool/current_weather:v1
docker push snoorrasool/current_weather:v1
```
</br>

#### Docker Hub Local Public Registery

```to pull it from docker hub:```

```sh
docker pull snoorrasool/current_weather:v1
```

run it locally:

```sh
docker run --rm snoorrasool/current_weather:v1 rain paris
docker run --rm snoorrasool/current_weather:v1 shine paris
```

</br>
</br>

#### Makefile

to run the following commands you need to be inside the directory where the Makefile exist , you need to be in the same path level
1. build docker image: 

```sh
make build 
```

2. check if its raining:
```sh 
make run-rain
```

3. check if its shining:
```sh
make run-shine
```



4. check if its raining using docker hub image from my registery

```sh
make run-rain-hub
```

5. check if its raining using docker hub image from my registery
```sh
make run-shine-hub
```
