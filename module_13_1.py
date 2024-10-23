        # Задача "Асинхронные силачи": Необходимо сделать имитацию соревнований по поднятию шаров Атласа. Напишите
# асинхронную функцию start_strongman(name, power), где name - имя силача, power - его подъёмная мощность. Реализуйте
# следующую логику в функции: В начале работы должна выводиться строка - 'Силач <имя силача> начал соревнования.'
# После должна выводиться строка - 'Силач <имя силача> поднял <номер шара>' с задержкой обратно пропорциональной его
# силе power. Для каждого участника количество шаров одинаковое - 5. В конце поднятия всех шаров должна выводится
# строка 'Силач <имя силача> закончил соревнования.


import asyncio


async def start_strongman(name, power):
    number_of_balls = 5
    print(f'Силач {name} начал соревнования.')
    for i in range(1,  number_of_balls+1):
        await asyncio.sleep(1/power)
        print(f'Силач {name} поднял {i} шар')
    print(f'Силач {name} закончил соревнования.')


# Также напишите асинхронную функцию start_tournament, в которой создаются 3 задачи для функций start_strongman.
# Имена(name) и силу(power) для вызовов функции start_strongman можете выбрать самостоятельно. После поставьте каждую
# задачу в ожидание (await).


async def start_tournament():
    task_1 = asyncio.create_task(start_strongman('Pasha', 3))
    task_2 = asyncio.create_task(start_strongman('Denis', 4))
    task_3 = asyncio.create_task(start_strongman('Apollon', 5))
    await task_1
    await task_2
    await task_3

# Запустите асинхронную функцию start_tournament методом run.

asyncio.run(start_tournament())





