# pyluxafor

Helper interface and CLI to interact with [luxafor](https://luxafor.com) products.

## Install

```
pip3 install pyluxafor
```

or

```
git clone git@github.com:fmartingr/pyluxafor.git
cd pyluxafor
python3 setup.py install
```

## Using the CLI

Pyluxafor provides the `luxa` command to interact with the USB led in the same way as the library
does, with some helper commands to convert colors between RGB/Hex.

```
# Converts between hexadecimal to decimal color notations
luxa hex2dec 00ff00
luxa dec2hex 255 255 0

# Set a flag with a fixed color
luxa set --led=all #ff0000

# Fade
luxa fade --led=all --speed=10 #00ff00

# Strobe
luxa strobe --led=front --speed=100 --repeat=10 #0000ff

# Wave
luxa wave --wave 3 --duration=100 --repeat=200 #ff0000

# Pattern
luxa pattern --repeat=2 2

# Turns off the luxafor
luxa off

# Using the conversion helpers in one command
luxa set $(luxa dec2hex 255 0 0)
```

## Using as a library

``` python
from luxafor import luxafor

lux = luxafor.Luxafor()

# Led types
luxafor.Leds.ALL
luxafor.Leds.FRONT
luxafor.Leds.BACK
luxafor.Leds.LEDn # Where n is a number from 1 to 6, refer to the class

# Set a basic color
# From: off, yellow, green, blue, magenta, cyan, red, white
lux.set_basic_color('green')

# Set a static color
lux.set_color(<red>, <green>, <blue>, <led>)

# Fade to a color
lux.fade(<red>, <green>, <blue>, <led>, <speed>)

# Strobe
lux.strobe(<red>, <green>, <blue>, <led>, <speed>, <repeat times>)

# Wave
# Wave types:
# 1: Short wave
# 2: Long wave
# 3: Overlapping short wave
# 4: Overlapping long wave
lux.wave(<red>, <green>, <blue>, <led>, <wave type>, <duration>, <repeat times>)

# Enable predefined pattern
# Patterns from 1 to 8
lux.pattern(<pattern number>, <repeat>)

# Turn off the luxafor
lux.turn_off()
```
