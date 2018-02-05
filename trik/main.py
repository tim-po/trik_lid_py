import os
import time


def convert_base(num, to_base=10, from_base=10):
    if isinstance(num, str):
        n = int(num, from_base)
    else:
        n = int(num)
    alphabet = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if n < to_base:
        return alphabet[n]
    else:
        return convert_base(n // to_base, to_base) + alphabet[n % to_base]


def enter_i2c_command(type_of_command="set", address="", value=0, mode=""):
    """

    :param type_of_command: Принимает значение get для получения или set
    :param address: Адресс устройства для обращения
    :param value: задаваемое значение в 16ричной системе
    :param mode: w для двухбайтового значения b для однобайтового значения value
    :return: Результат выполнения
    """
    value = convert_base(
        value,
        to_base=16
    )
    result = os.system(
        "i2" + type_of_command + " -y 2 0x48 0x" +
        address + " " +
        value + " " +
        mode
    )
    return result


class Robot:
    pass


class Motors:
    class Motor1:
        port = "M1"
        current_power = 0
        address = "0x14"
        PWM_address = "0x10"
        endocoder_address = "0x30"

    class Motor2:
        port = "M2"
        current_power = 0
        address = "0x15"
        PWM_address = "0x11"
        endocoder_address = "0x31"

    class Motor3:
        port = "M3"
        current_power = 0
        address = "0x16"
        PWM_address = "0x12"
        endocoder_address = "0x32"

    class Motor4:
        port = "M4"
        current_power = 0
        address = "0x17"
        PWM_address = "0x13"
        endocoder_address = "0x33"

    @staticmethod
    def change_power(added_power, motor):
        """
        Изменение скорости вращение двигателя на определнную констату
        :param added_power: Значение, которое нужно добавить к текущей скорости
        :param motor: Класс мотора
        :return:
        """
        motor.current_power += added_power

        enter_i2c_command(
            address=motor.address,
            value=motor.current_power
        )

    @staticmethod
    def set_power(new_power, motor):
        """
        Переопределние скорости вращения двигателя
        :param new_power: Значение, на кототорое нужно изменить текущую скорость
        :param motor: Класс мотора
        :return:
        """
        motor.current_power = new_power

        enter_i2c_command(
            address=motor.address,
            value=motor.current_power
        )

    @staticmethod
    def get_power(motor):
        """
        Изменить значение переменной current_power в классе мотора
        :param motor: Класс мотора
        :return:
        """
        motor.current_power = enter_i2c_command(
            type_of_command="get",
            address=motor.address
        )

    @staticmethod
    def stop_motor(motor):
        """
        Остановить мотор(поставить значение мощности на 0)
        :param motor: Класс мотора
        :return:
        """
        enter_i2c_command(
            address=motor.address
        )


Motor3 = Motors.Motor3
Motors.set_power(100, Motor3)
time.sleep(3)
Motors.stop_motor(Motor3)
