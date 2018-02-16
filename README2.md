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
![alt text]((http://image.ibb.co/bX3Zfn/2018_02_17_0_00_11.png)
