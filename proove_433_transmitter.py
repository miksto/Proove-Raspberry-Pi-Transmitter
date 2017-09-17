#!/usr/bin/env python

import time
import sys

class tx():
   def __init__(self, pi, gpio, repeats=6, bits=32, syncHigh=250, syncLow=2750, pauseHigh=250, pauseLow=10500, oneHigh=250, oneLow=250, zeroHigh=250, zeroLow=1500):
      import pigpio
      self.pi = pi
      self.gpio = gpio
      self.repeats = repeats
      self.bits = bits
      self.syncHigh = syncHigh
      self.syncLow = syncLow
      self.pauseHigh = pauseHigh
      self.pauseLow = pauseLow
      self.oneHigh = oneHigh
      self.oneLow = oneLow
      self.zeroHigh = zeroHigh
      self.zeroLow = zeroLow

      self._make_waves()

      pi.set_mode(gpio, pigpio.OUTPUT)

   def _make_waves(self):
      import pigpio
      """
      Generates the basic waveforms needed to transmit codes.
      """
      wf = []
      wf.append(pigpio.pulse(1<<self.gpio, 0, self.syncHigh))
      wf.append(pigpio.pulse(0, 1<<self.gpio, self.syncLow))
      self.pi.wave_add_generic(wf)
      self._syncWave = self.pi.wave_create()

      wf = []
      wf.append(pigpio.pulse(1<<self.gpio, 0, self.pauseHigh))
      wf.append(pigpio.pulse(0, 1<<self.gpio, self.pauseLow))
      self.pi.wave_add_generic(wf)
      self._pauseWave = self.pi.wave_create()

      wf = []
      wf.append(pigpio.pulse(1<<self.gpio, 0, self.oneHigh))
      wf.append(pigpio.pulse(0, 1<<self.gpio, self.oneLow))
      self.pi.wave_add_generic(wf)
      self._oneWave = self.pi.wave_create()

      wf = []
      wf.append(pigpio.pulse(1<<self.gpio, 0, self.zeroHigh))
      wf.append(pigpio.pulse(0, 1<<self.gpio, self.zeroLow))
      self.pi.wave_add_generic(wf)
      self._zeroWave = self.pi.wave_create()

   def send(self, code):
      """
      Transmitts the code self.repeats number of times.
      """
      chain = [255, 0] # begin loop
      chain += [self._syncWave]

      bit = (1<<(self.bits-1))
      for i in range(self.bits):
         if code & bit:
            chain += [self._oneWave, self._zeroWave]
         else:
            chain += [self._zeroWave, self._oneWave]
         bit = bit >> 1

      chain += [self._pauseWave]

      chain += [255, 1, self.repeats, 0] # end of loop. Repeat self.repeats time

      self.pi.wave_chain(chain)

      while self.pi.wave_tx_busy():
         time.sleep(0.1)


   def destroy(self):
      """
      Cancels the wireless code transmitter.
      """
      self.pi.wave_delete(self._pauseWave)
      self.pi.wave_delete(self._syncWave)
      self.pi.wave_delete(self._oneWave)
      self.pi.wave_delete(self._zeroWave)

      self.pi.stop()

if __name__ == "__main__":

   import sys
   import time
   import pigpio

   TX = 22

   args = len(sys.argv)

   if args > 1:
      pi = pigpio.pi()
      tx = tx(pi, gpio=TX)

      for i in range(args-1):
         command = int(sys.argv[i+1], 2)
         tx.send(command)

      tx.destroy()
   else:
      print("Provide the command you want to send like: \"./proove_433_transmitter.py 00101010001001010010110001110000\"")
