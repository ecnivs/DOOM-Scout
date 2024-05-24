from settings import *

class ViewRenderer:
    def __init__(self, engine):
        self.engine = engine
        self.wad_data = engine.wad_data
        self.player = engine.player

        self.seg = None
        self.rw_angle1 = None

    def update(self):
        pass

    def classify_segment(self, segment, x1, x2, rw_angle1):
        self.seg = segment
        self.rw_angle1 = rw_angle1

        if x1 == x2:
            return None

        back_sector = segment.back_sector
        front_sector = segment.front_sector

        # handle solid walls
        if back_sector is None:
            self.clip_solid_walls(x1, x2)
            return None
