# This script runs before game start and defines the persistent variable classes

label init_classes:

    init python:
        # create persistent flower class
        class Flowers(NoRollback):
            def __init__(self):
                self.flower1 = False
                self.flower2 = False
                self.flower3 = False
                self.flower4 = False

        # create persistent class for unlocked puzzles
        class Puzzles(NoRollback):
            def __init__(self):
                self.loop2 = False
                self.loop3 = False
                self.loop4 = False

        # create persistent class for solved puzzles
        class Solves(NoRollback):
            def __init__(self):
                self.loop2 = False
                self.loop3_1 = False
                self.loop3_2 = False
                self.loop3_3 = False
                self.loop4 = False

        # create persistent class for puzzle hints
        class Hints(NoRollback):
            def __init__(self):
                self.loop2_1 = False
                self.loop2_2 = False
                self.loop2_3 = False
                self.loop3_1 = False
                self.loop3_2 = False
                self.loop3_3 = False
                self.loop4_1 = False
                self.loop4_2 = False
                self.loop4_3 = False

        # create persistent class for solved puzzles
        class MoonGlitches(NoRollback):
            def __init__(self):
                self.glitch1 = False
                self.glitch2 = False
                self.glitch3 = False
                self.glitch4 = False
                self.glitch5 = False
                self.glitch6 = False
                self.glitch7 = False
                self.glitch8 = False
                self.glitch9 = False
                self.glitch10 = False

        # create persistent endings class
        class Endings(NoRollback):
            def __init__(self):
                self.ending1 = False
                self.ending2 = False
                self.ending3 = False

    return