from .board import board

def get_footprints():
    footprints = board.GetFootprints()
    print('Reference')
    for footprint in footprints:
        reference = str(footprint.GetReference())
        print('\t%s' %reference)