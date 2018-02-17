<h1> Библиотека для работы c Trik на JavaScript </h1>
<h3> Константы для работы функциями: </h3>

```
  var pi = 3.1415926535897931; 
  cpr = 374; // константа (кол-во сигналов на оборот)
  r = 5.6/2; // радиус колеса
  var d = 17.5; // длинна передней оси колес
  
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

<h3> Поворот на заданный угол: </h3>

Если degree>0 поворот против часовой стрелки, иначе поворот по часовой

```
var stear = function(degree)
{

    var n = (2 * pi * d/2)/360 * (Math.abs(degree) - 3);

    eleft = brick.encoder(E3);
    eleft.reset();

    var lim = (n /(2 * pi * r)) * 360;

    var Power1 = 100;

    if(degree<0) // необходимо повернуть по часовой
    {
	    Power1 = - Power1;
    }
    
    brick.motor(M3).setPower(Power1);
    brick.motor(M4).setPower(-Power1);
   
    var el = 0;

    while(el <= lim)
    {
        el = Math.abs(eleft.readRawData());
        script.wait(10);
    }

    brick.motor(M3).powerOff();
    brick.motor(M4).powerOff();
}

```

<h2> </h2>
<h2> Прохождение лабиринта: </h2>
<h2> </h2>

![alt text](http://image.ibb.co/cmmx0n/1.png)

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

<h2> </h2>
<h2> Движение вдоль линии: </h2>
<h2> </h2>

![alt text](http://image.ibb.co/dLQAmS/2.png)

```
alongTheLine = function()
{
	__interpretation_started_timestamp__ = Date.now();
		var k=3;
	
		left = brick.sensor(A1).read();
		right = brick.sensor(A2).read();
	
		while (true) 
		{
			u = k * (brick.sensor(A1).read() - left - (brick.sensor(A2).read() - right));
			brick.motor(M3).setPower(50 + u);
		
			brick.motor(M4).setPower(50 - u);
		
			script.wait(30);
		}
}


