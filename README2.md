<h1> Библиотека для работы c Trik на JavaScript </h1>
<h3> Константы для работы функциями: </h3>

```
  var pi = 3.1415926535897931; 
  cpr = 374; // константа (кол-во сигналов на оборот)
  d = 5.60; // диаметр колеса Трика
  r = d / 2; // радиус колеса
```

<h3> Прямолинейное движение: </h3>

```
var go_straight = function () 
{
    var difference = (encoder_3.read() - encoder_4.read()) * 0.0029;
    motor_3_power = motor_3_power - difference;
    motor_4_power = motor_4_power + difference;
    
    motor_3.setPower(motor_3_power);
    motor_4.setPower(motor_4_power);
    script.wait(5);
}
```
<h3> Прохождение лабиринта: </h3>
![alt text](http://image.ibb.co/bX3Zfn/2018_02_17_0_00_11.png)

Код:
Функция для корректировки движения:
```
regulyator = function()
{
	
	while (true) {
		if (!(brick.sensor(A1).read() > threshold || brick.sensor(A2).read() > threshold))
    {
			break;
		}
		err = brick.sensor(A2).read() - threshold;
		u = err * 10;
		brick.motor(M3).setPower(70 + u);
		
		brick.motor(M4).setPower(70 - u);
		
		script.wait(10);
		
	}
	brick.motor(M1).powerOff();
	brick.motor(M2).powerOff();
	brick.motor(M3).powerOff();
	brick.motor(M4).powerOff();
	
	return;
}
```

Функция для поворота налево:

```
nalevo = function()
{
	
	brick.motor(M3).setPower(100);
	brick.motor(M4).setPower(100);
	
	script.wait(340);
	
	brick.motor(M4).setPower(100);
	
	brick.motor(M3).setPower(-(100));
	
	script.wait(520);
	
	brick.motor(M3).setPower(-(100));
	brick.motor(M4).setPower(-(100));
	
	script.wait(340);
	
	brick.motor(M1).powerOff();
	brick.motor(M2).powerOff();
	brick.motor(M3).powerOff();
	brick.motor(M4).powerOff();
	
	return;
	
}
```
Применения в гланой функции:
```
var main = function()
{
	__interpretation_started_timestamp__ = Date.now();
	
	threshold = 25;
	brick.motor(M3).setPower(100);
	brick.motor(M4).setPower(100);
	
	script.wait(1000);
	
	while (true)
  {
		if (brick.sensor(A2).read() <= threshold + 5 && brick.sensor(A1).read() <= threshold + 5) {
			nalevo();
			
		} else {
			regulyator();
			
		}
		script.wait(0);
		
	}
}
```
