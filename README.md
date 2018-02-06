# Библиотека для работы c Trik
Библоитека для работы с Trik при помощи Python3. 

## I2C
Модуль I2C, предназначенный для работы с аналоговыми датчиками и силовыми двигателями.

### Силовые двигатели

Каждый двигатель - это объект, содержащий несколько полей: port(порт, к которому должен быть подключен двигатель), current_power(текущая мощность двигетля), address(I2C адрес двигателя) и два других.
```class Motor1:
       port = "M1"
       current_power = 0
       address = "0x14"
       PWM_address = "0x10"
       endocoder_address = "0x30"```

Для иницаилизации мотора нужно написать следующий код:
```Motor1 = Motors.Motor1```

Далее для задания мощности мотора необходимо использовать функцию ```Motors.set_power()```, которая принимает значения мощности(от -100 до 100) и список моторов. Для задания мощности 100 для первого мотора необходимо написать следующий код:
```Motors.set_power(100, [Motor1])```

Для остановки мотора нужно использовать функцию ```Motors.stop()```, которая принимает лист из двигателей, например, для остановки Motor1 необходимо написать следующий код:
```Motors.stop([Motor1])```

Также, внизу приведен код, в котором инициализируются и работают на полной мощности в течении 4 секунд 2 мотора:

```from trik.i2c import Motors
import time

Motor1 = Motors.Motor1  # Инициализация мотора 1
Motor2 = Motors.Motor2  # Инициализация мотора 2

Motors.set_power(100, [Motor1, Motor2])  # Установка мощности 100 на оба мотора

time.sleep(4)  # Ожидание 4 секунды

Motors.stop([Motor1, Motor2])  # Остановка(мощность 0) обоих моторов
```