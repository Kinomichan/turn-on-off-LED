#!/usr/bin/env python3

import sys
import subprocess
import psutil
import board
import neopixel

def main():
    args = sys.argv

    if (len(args) > 1):
        ledStatus = args[1]
    else:
        ledStatus = "none"

    scriptName = "/opt/iot-python/soundBar.py"

    pixelPin = board.D18
    numPixels = 10

    scriptPid = isScriptRunning(scriptName)
    if scriptPid > 0 and ledStatus == "on":
        print(f"ledStatus: {ledStatus}")
    elif scriptPid < 0 and ledStatus == "off":
        print(f"ledStatus: {ledStatus}")
    elif scriptPid > 0:
        if killPid(scriptName, scriptPid):
            turnOffLed(pixelPin, numPixels)
        print("ledStatus: off")
    else:
        # turn on LED
        scriptPid = subprocess.Popen(
                [scriptName],
                stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL
        )
        print("ledStatus: on")


def isScriptRunning(scriptName):
    for process in psutil.process_iter(attrs=['pid', 'name', 'cmdline']):
        cmdline = process.info['cmdline']
        if cmdline and scriptName in cmdline:
            return process.info['pid']
    return -1


def killPid(scriptName, scriptPid):
    try:
        print(f"Terminating: {scriptName} (pid = {scriptPid})...")
        process = psutil.Process(scriptPid)
        process.terminate()
        process.wait(timeout=1)
        print(f"Terminated: {scriptName} (pid = {scriptPid})")
        return True
    except psutil.NoSuchProcess:
        print(f"Process not exist: {scriptName} ({pid})")
    except psutil.AccessDenied:
        print(f"Permission denied: scritpName ({pid})")


def turnOffLed(pixelPin, numPixels):
    pixels = neopixel.NeoPixel(pixelPin, numPixels)
    pixels.fill((0, 0, 0))
    pixels.show()


if __name__ == "__main__":
    main()