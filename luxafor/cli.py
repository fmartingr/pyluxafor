# -*- coding: utf-8 -*-
import sys

import click

from luxafor import luxafor


def get_luxafor():
    return luxafor.Luxafor()


def convert_hex_to_dec_color(hex_color):
    (red, green, blue) = hex_color[0:2], hex_color[2:4], hex_color[4:6]

    red = int(red, 16)
    green = int(green, 16)
    blue = int(blue, 16)

    return (red, green, blue)


def convert_dec_to_hex_color(red, green, blue):
    colors = (red, green, blue)
    return "".join([
        hex(color).split('x')[1].upper() for color in colors])


@click.group()
def cli():
    pass


@cli.command()
@click.argument('color')
def hex2dec(color):
    hex_color = color.strip('#')

    try:
        red, green, blue = convert_hex_to_dec_color(hex_color)
    except ValueError:
        click.echo('Invalid hexadecimal color: %s' % hex_color, err=True)

    click.echo("%d %d %d" % (red, green, blue))


@cli.command()
@click.argument('red', type=click.IntRange(0, 255))
@click.argument('green', type=click.IntRange(0, 255))
@click.argument('blue', type=click.IntRange(0, 255))
def dec2hex(red, green, blue):
    colors = (red, green, blue)
    if not all((0 <= x <= 255 for x in colors)):
        click.echo("Every color must be between 0 and 255", err=True)
        sys.exit(1)

    click.echo(convert_dec_to_hex_color(red, green, blue))

    return (red, green, blue)


@cli.command()
@click.option('--led', default=luxafor.Leds.ALL)
@click.argument('color')
def set(led, color):
    """Sets the flag with a fixed color."""
    color = convert_hex_to_dec_color(color)

    flag = get_luxafor()

    flag.set_color(*color, led=led)


@cli.command()
@click.option('--led', default=luxafor.Leds.ALL)
@click.option('--speed', default=128, type=click.IntRange(0, 255))
@click.argument('color')
def fade(led, speed, color):
    color = convert_hex_to_dec_color(color)

    flag = get_luxafor()

    flag.fade(*color, led=led, speed=speed)


@cli.command()
@click.option('--led', default=luxafor.Leds.ALL)
@click.option('--speed', default=6, type=click.IntRange(0, 255))
@click.option('--repeat', default=1, type=click.IntRange(1, 255))
@click.argument('color')
def strobe(led, speed, repeat, color):
    color = convert_hex_to_dec_color(color)

    flag = get_luxafor()

    flag.strobe(*color, led=led, speed=speed, repeat=repeat)


@cli.command()
@click.option('--wave', default=1, type=click.IntRange(1, 4))
@click.option('--duration', default=2, type=click.IntRange(1, 255))
@click.option('--repeat', default=1, type=click.IntRange(1, 255))
@click.argument('color')
def wave(wave, duration, repeat, color):
    color = convert_hex_to_dec_color(color)

    flag = get_luxafor()

    flag.wave(*color, wave=wave, duration=duration, repeat=repeat)


@cli.command()
@click.option('--repeat', default=1, type=click.IntRange(1, 255))
@click.argument('pattern', type=click.IntRange(1, 8))
def pattern(repeat, pattern):
    flag = get_luxafor()
    flag.pattern(pattern, repeat)


@cli.command()
def off():
    flag = get_luxafor()
    flag.turn_off()


if __name__ == '__main__':
    cli()
