import minidrive

try:
    # Set LED1 to high using the LED_out function
    minidrive.LED_out(True, 1)

finally:
    # Cleanup the GPIO
    minidrive.cleanup()
