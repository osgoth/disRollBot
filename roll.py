import re
from random import randint
from typing import List, Callable, Tuple


def roll(a, b) -> List[int]:
    """Roll adb"""
    return [randint(1, int(b)) for i in range(0, int(a))]


def mods(string) -> int:
    total = 0
    modificators = re.split(r"\s*,\s*", string)
    for mod in modificators:
        total += int(mod.replace(" ", ""))
    return total


def dis_adv(string, rolls, alt_rolls) -> List[int]:
    """Form new list with (dis)advantage"""
    return [
        (max(i, j) if re.match(r"\s*[+]\s*", string) else min(i, j))
        for i, j in zip(rolls, alt_rolls)
    ]


def cast_die(string: str) -> str:

    sects: List[int] = string.split(r":")
    dice: List[int] = re.split(r"\s*d\s*", sects[0])
    rolls: List[int] = roll(dice[0], dice[1])
    fin_rolls = rolls
    total: int = 0
    res: str = f"<{str(rolls)}>"

    for sect in sects:
        if re.match(r"(\s*[+-]\s*\d\s*,?\s*)", sect):
            total = mods(sect)
        elif re.match(r"\s*[+-]\s*", sect):
            alt_rolls = roll(dice[0], dice[1])
            fin_rolls = dis_adv(sect, alt_rolls, rolls)
            res += f"<{str(alt_rolls)}>"
            res += f" => {str(fin_rolls)}"

    total += sum(fin_rolls)

    return f"{res} = `{total}`"


def roll_character(form: str) -> List[int]:
    stats = []
    if re.match(r"\d\s*d\s*\d", form):
        dice = re.split(r"\s*d\s*", form)
        for i in range(6):
            rol = roll(dice[0], dice[1])
            if int(dice[0]) == 3:
                stats.append(sum(rol))
            elif int(dice[0]) == 4:
                stats.append(sum(rol) - min(rol))

    return stats
