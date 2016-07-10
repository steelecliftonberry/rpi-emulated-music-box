#!/usr/bin/env python

class SignalLevel:
    Low, High = range(2)

class SignalTransition:
    Falling, Rising = range(2)

class SchmittTrigger:
    def __init__(self, lower_threshold, upper_threshold, output_level=SignalLevel.Low):
        self.lower_threshold = lower_threshold
        self.upper_threshold = upper_threshold
        self.output_level = output_level

    def update(self, voltage):
        transition = None
        if self.output_level == SignalLevel.Low and voltage >= self.upper_threshold:
            self.output_level = SignalLevel.High
            transition = SignalTransition.Rising
        elif self.output_level == SignalLevel.High and voltage <= self.lower_threshold:
            self.output_level = SignalLevel.Low
            transition = SignalTransition.Falling
        return transition

    def level(self):
        return self.output_level

if __name__ == '__main__':
    trig = SchmittTrigger(100, 200)
    for level in range(0, 300, 25):
        old = trig.level()
        trans = trig.update(level)
        print("{0} {1} -> {2}".format(old, level, trans))

    for level in range(300, 0, -25):
        old = trig.level()
        trans = trig.update(level)
        print("{0} {1} -> {2}".format(old, level, trans))

