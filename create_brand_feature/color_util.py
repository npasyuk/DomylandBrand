from PIL import ImageColor


def brighten(percent, hex):
    rgb_color = ImageColor.getrgb(hex)

    # Изменяем яркость цвета
    new_rgb_color = tuple(int(max(0, min(255, c * (1 + percent / 100)))) for c in rgb_color)

    # Преобразуем RGB-цвет обратно в HEX-цвет
    new_hex_color = '#{:02X}{:02X}{:02X}'.format(*new_rgb_color)
    print(new_hex_color)  # Выводим новый цвет
    return new_hex_color
