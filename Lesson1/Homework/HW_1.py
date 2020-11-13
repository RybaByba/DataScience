# TASK5 Користувач вводить 2 букви. Визначити на яких місцях алфафіту вони стоять, і скільки мідж ними знаходиться букв.


def get_letter():
    let = input('введіть будь-яку прописну літеру англійського алфавіту >>> ')
    while len(let) != 1 or (ord(let) not in range(97, 123)):
        let = input('Літера введена ен коректно. Введіть будь-яку прописну літеру англійського алфавіту >>> ')

    return let


let1 = get_letter()
let2 = get_letter()

if ord(let1) and ord(let2) in range(97, 123):
    print(f"літера, \"{let1}\", має номер в ASCI коді ", ord(let1))
    print(f"літера, \"{let2}\", має номер в ASCI коді ", ord(let2))
    print(f"літера, \"{let1}\", в англійському алфавіті має номер", ord(let1) - 96)
    print(f"літера, \"{let2}\", в англійському алфавіті має номер", ord(let2) - 96)

    if ord(let1) == ord(let2):
        print(f"між літерою, \"{let1}\", та літерою, \"{let2}\", не має відстані. Ви вказали одну і ту саму літеру.")
    elif ord(let1) > ord(let2):
        distance = abs((ord(let1) - ord(let2)) - 1)
        print(f"між літерою, \"{let1}\", та літерою, \"{let2}\", відстань, {distance}, символи(ів)")
    else:
        distance = abs((ord(let1) - ord(let2)) + 1)
        print(f"між літерою, \"{let1}\", та літерою, \"{let2}\", відстань, {distance}, символи(ів)")

else:
    print('літери введено не коректно')



