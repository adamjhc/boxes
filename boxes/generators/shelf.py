from boxes import *

class Shelf(Boxes):
    """Simple Shelf: three pieces joined by two finger joints"""

    ui_group = "Box"

    def __init__(self) -> None:
        Boxes.__init__(self)
        self.buildArgParser("x", "y", "h", "outside")
        self.addSettingsArgs(edges.FingerJointSettings)

    def render(self):
        x, y, h = self.x, self.y, self.h
        t = self.thickness

        if self.outside:
            x = self.adjustSize(x, False)
            y = self.adjustSize(y, False)

        self.rectangularWall(h, y, "eFee", move="up")
        self.rectangularWall(h, y, "eFee", move="up")
        self.rectangularWall(x, y, "efef")
