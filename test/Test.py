
import this
from types import new_class

class Block:
    def Block(prop):
        this(prop)

    def getName(self):
        self.Properties.getName()

    class Properties:
        __n = "default"
        __t = "D"

        def setName(self, name):
            self.__n=name
            return self
        def getName(self):
            return self.__n
        def setTool(self, tool):
            self.__t=tool
            return self
        def build(self):
            print("Saved")
            return self


class Registry:
    def register(Classe):
        print(Classe)

rock = Block.Properties().setName("rock").setTool("PICK").build()

dacite = Block(Block.Properties().setName("dacite").setTool("PICK").build())

Registry.register(dacite.getName())
Registry.register(dacite.Properties.getName())
Registry.register(rock.getName())