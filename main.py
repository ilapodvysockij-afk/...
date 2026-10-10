import colorama

def inspect_library():
    print(f"Інтроспекція: colorama (Версія: {getattr(colorama, '__version__', 'N/A')}) ===")
    print("\n[Усі атрибути (dir)]: ", dir(colorama))

    print("\n Атрибути та Методи:")

    components = {
        "Fore": "Клас з ANSI-кодами для зміни кольору тексту (шрифту).",
        "Back": "Клас з ANSI-кодами для зміни кольору тла (фону).",
        "Style": "Клас для зміни стилю тексту (яскравість) та його повного скидання.",
        "init()": "Метод ініціалізації для коректної роботи кольорів у консолі Windows.",
        "deinit()": "Метод для скасування дій init() та повернення стандартних потоків."
    }

    for name, comment in components.items():
        print(f"• {name} — {comment}")

if __name__ == "__main__":
    inspect_library()