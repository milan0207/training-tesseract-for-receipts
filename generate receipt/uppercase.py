import matplotlib.font_manager

fonts = [f.name for f in matplotlib.font_manager.fontManager.ttflist]
for font in fonts:
    if 'Hypermarket' in font:
        print(font)
