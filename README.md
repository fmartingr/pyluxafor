pyluxafor
=========

[![Codacy Badge](https://api.codacy.com/project/badge/Grade/5b9a403e59244ce9a7d6a572dabb3392)](https://www.codacy.com/app/fmartingr/pyluxafor?utm_source=github.com&utm_medium=referral&utm_content=fmartingr/pyluxafor&utm_campaign=badger)

Helper interface and CLI to interact with [luxafor](https://luxafor.com) products.


## Usage

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
