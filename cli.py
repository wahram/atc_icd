from math import floor

def progress(max, pos):
    percentage = (pos / max) * 100
    progress = floor(percentage)
    print('[' + ('=' * progress) + (' ' * (100 - progress)) + '] %3.2f%%' % percentage)