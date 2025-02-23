print("starting of neopixel flashing ")          # just checking printing output

from machine import Pin
from neopixel import NeoPixel
import time

# Pin configuration
btn = Pin(0, Pin.IN, Pin.PULL_UP)  # Built-in boot button on ESP32-S3
pin = Pin(48, Pin.OUT)             # Pin connected to the NeoPixel (use 48 for your setup)
neo = NeoPixel(pin, 1)             # Create NeoPixel driver for 1 pixel



# Interrupt Service Routine (ISR) for button press
def button_isr(pin):
    
    while(btn.value()==0):
        continue
       

# Attach the ISR to the button pin
btn.irq(trigger=Pin.IRQ_FALLING, handler=button_isr)

# Main loop
while True:
    while(btn.value()==1):  # Flash NeoPixel only if the button is not pressed
        neo[0] = (255, 0, 0)  # Set the first pixel to red
        neo.write()           # Write data to the pixel
        print("Red")
        time.sleep(0.4)

        neo[0] = (0, 255, 0)  # Set the first pixel to green
        neo.write()           # Write data to the pixel
        print("Green")
        time.sleep(0.4)
        neo[0] = (0, 0, 255)  # Set the first pixel to green
        neo.write()           # Write data to the pixel
        print("Blue")
        time.sleep(0.4)

