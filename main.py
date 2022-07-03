from module.board import *
from module.footprint import get_footprints

def main():
    name = get_filename()
    full_name = get_filename_with_extension()
    pcb_path = get_filename_path()

    print('pcb name: %s' % name)
    print('full name: %s' % full_name)
    print('pcb path: %s' % pcb_path)

    get_footprints()
    
if __name__ == "__main__":
    main()

