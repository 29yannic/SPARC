class Mario:
    def jump(self):
        # Code to perform the jumping action
        print("Mario jumps!")
player = Mario()
player.jump()

class Luigi(Mario):
    def invisible(self):
        # Code to make Luigi invisible
        print("Luigi turns invisible!")

luigi = Luigi()
luigi.jump()  # Inherited from Mario class
luigi.invisible()  # Specific to Luigi class
