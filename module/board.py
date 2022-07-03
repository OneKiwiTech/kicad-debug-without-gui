import pcbnew
import os

filename = '/home/vanson/kicad/iMX8M_OneKiwi/iMX8M_OneKiwi.kicad_pcb'
board = pcbnew.LoadBoard(filename)

def get_filename():
    file_name = board.GetFileName()
    base = os.path.basename(file_name)
    name = os.path.splitext(base)[0]
    return name

def get_filename_with_extension():
    file_name = board.GetFileName()
    name = os.path.basename(file_name)
    return name

def get_filename_path():
    file_name = board.GetFileName()
    path = os.path.dirname(file_name)
    return path