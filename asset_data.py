from wad_reader import *

class AssetData:
    def __init__(self, wad_data):
        self.wad_data = wad_data
        self.reader = wad_data.reader
        self.get_lump_index = wad_data.get_lump_index

        self.palletes = self.wad_data.get_lump_data(
            reader_func = self.reader.read_pallete,
            lump_index = self.get_lump_index('PLAYPAL'),
            num_bytes = 256 * 3
        )
        self.pallete_idx = 0
        self.pallete = self.palletes[self.pallete_idx]
