"""
    dustfractals.py – simple text based dust fractals
    Copyright (C) 2022 skymandr

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""
from random import randint
from typing import Optional, List, Tuple

DUST = '#'
SPACE = '.'


def collision(pos: Tuple[int, int], cave: List[str]) -> bool:
    return (
        cave[pos[1]][pos[0]] == DUST
        or (
            pos[1] + 1 < len(cave)
            and cave[pos[1] + 1][pos[0]] == DUST
        )
        or (
            pos[1] - 1 >= 0
            and cave[pos[1] - 1][pos[0]] == DUST
        )
        or (
            pos[0] + 1 < len(cave[0])
            and cave[pos[1]][pos[0] + 1] == DUST
        )
        or (
            pos[0] - 1 >= 0
            and cave[pos[1]][pos[0] - 1] == DUST
        )
    )


def make_dust_fractal(
    width: int,
    height: int,
    size: int,
    seeds: Optional[List[Tuple[int, int]]] = None,
) -> str:
    if height < 1 or width < 1:
        raise ValueError("Width and height must be positive integers!")

    cave = [[SPACE] * width for _ in range(height)]

    if seeds is None:
        seeds = [(width // 2, height // 2)]
    for seed in seeds:
        seed = (seed[0] % width, seed[1] % height)
        cave[seed[1]][seed[0]] = DUST

    for i in range(size):
        edge = randint(0, 3)
        if (edge % 2) == 1:
            pos = (
                randint(0, width - 1),
                (edge // 2) * (height - 1),
            )
        else:
            pos = (
                (edge // 2) * (width - 1),
                randint(0, height - 1),
            )
        while not collision(pos, cave):
            pos = (
                (pos[0] + randint(-1, 1)) % width,
                (pos[1] + randint(-1, 1)) % height,
            )
        cave[pos[1]][pos[0]] = DUST

    return cave


def print_dust_fractal(
    width: int,
    height: int,
    size: int,
    seeds: Optional[List[Tuple[int, int]]] = None,
) -> None:
    cave = '\n'.join(''.join(r) for r in make_dust_fractal(
        width,
        height,
        size,
        seeds,
    ))
    print(cave)
