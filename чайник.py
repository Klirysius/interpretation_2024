# Чайник
class Kettle:
    def __init__(self, is_filled=False):
        self.is_filled = is_filled
        self.is_boiled = False

    # Опустошить чайник
    def make_empty(self):
        if self.is_filled:
            self.is_filled = False
            print("ЧАЙНИК опустошён")
        else:
            print("ЧАЙНИК уже был пустым")


# Кран
class Tap:
    def __init__(self):
        self.is_opened = False

    # Открыть кран
    def open(self):
        if not self.is_opened:
            self.is_opened = True
            print("КРАН теперь открыт")
        else:
            print("КРАН уже был открыт")

    # Закрыть кран
    def close(self):
        if self.is_opened:
            self.is_opened = False
            print("КРАН теперь закрыт")
        else:
            print("КРАН уже был закрыт")

    # Заполнить чайник водой
    def fill(self, kettle):
        if self.is_opened:
            kettle.is_filled = True
            print("КРАН наполняет ЧАЙНИК")
            for i in range(3):
                print("Наполнение ЧАЙНИКА")
            print("ЧАЙНИК теперь наполнен")
        else:
            print("КРАН закрыт и не может наполнить ЧАЙНИК")


# Спички
class Matches:
    def __init__(self):
        self.is_lighted = False

    # Зажечь спичку
    def light(self):
        if not self.is_lighted:
            print("СПИЧКА теперь горит")
            self.is_lighted = True
        else:
            print("СПИЧКА уже горит")

    # Потушить спичку
    def put_out(self):
        if self.is_lighted:
            print("СПИЧКА теперь не горит")
            self.is_lighted = False
        else:
            print("СПИЧКА уже не горит")


# Газовая плита
class GasCooker:
    def __init__(self):
        self.is_lighted = False

    # Зажечь плиту
    def light_cooker(self, matches):
        if matches.is_lighted:
            self.is_lighted = True
            print("ГАЗОВАЯ ПЛИТА теперь зажжена")
        else:
            print("СПИЧКА не горит и не может зажечь плиту")

    # Выключить плиту
    def turn_off(self):
        if self.is_lighted:
            self.is_lighted = False
            print("ГАЗОВАЯ ПЛИТА теперь не зажжена")
        else:
            print("ГАЗОВАЯ ПЛИТА уже не зажжена")

    # Нагреть чайник
    def heat_kettle(self, kettle):
        if not kettle.is_filled:
            print("ЧАЙНИК не заполнен")
        elif not self.is_lighted:
            print("ГАЗОВАЯ ПЛИТА не зажжена")
        else:
            print("ЧАЙНИК поставлен на ГАЗОВУЮ ПЛИТУ")
            for i in range(3):
                print("Вода в ЧАЙНИКЕ нагревается")
            kettle.is_boiled = True
            print("Вода в ЧАЙНИКЕ закипела")
            print("ЧАЙНИК не заполнен")


if __name__ == "__main__":
    print("Первый случай:")
    kettle1 = Kettle()  # Чайник пустой
    tap1 = Tap()
    matches1 = Matches()
    gas_cooker1 = GasCooker()

    tap1.open()  # Открыть кран
    tap1.fill(kettle1)  # Заполнить кран
    tap1.close()
    matches1.light()  # Зажечь спичку
    gas_cooker1.light_cooker(matches1)  # Зажечь плиту
    matches1.put_out()  # Потушить спичку
    gas_cooker1.heat_kettle(kettle1)  # Вскипятить чайник
    gas_cooker1.turn_off()  # Выключить плиту

    print("Второй случай(исправлен):")

    kettle2 = Kettle(is_filled=True)  # Чайник уже заполнен
    tap2 = Tap()
    matches2 = Matches()
    gas_cooker2 = GasCooker()

    matches2.light()  # Зажечь спички
    gas_cooker2.light_cooker(matches2)  # Зажечь плиту
    matches2.put_out()
    gas_cooker2.heat_kettle(kettle2)  # Нагреть чайник можно, так как в нём уже была вода
    gas_cooker2.turn_off()
