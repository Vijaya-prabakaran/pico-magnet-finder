# pico-magnet-finder

## Description
A simple magnet detection project using a reed switch and Raspberry Pi Pico.
When a magnet comes near the reed switch, an LED turns ON.

## Components Used
- Raspberry Pi Pico
- Reed switch
- LED
- 470Ω resistor
- Breadboard
- Magnet
- Jumper wires(if needed)

## Working Principle
The reed switch closes in the presence of a magnetic field.
GP19 is configured with an internal pull-down resistor.
When the switch closes, the pin reads HIGH and the LED connected to GP0 turns ON indicating the presence of magnet.

## Pin Connections
- Reed switch -> GP19 and 3.3V
- LED anode -> GP0
- LED cathode -> negative (–) rail of breadboard
- 470Ω resistor -> Pico GND and negative (–) rail of breadboard

## Code
Written in MicroPython.

## Learning Outcome
- GPIO input handling
- Internal pull-down resistors
- Reed switch operation
