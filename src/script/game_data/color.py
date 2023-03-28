COLORS = (
    "black",
    "gray",
    "light_gray",
    "white",
    "brown",
    "red",
    "orange",
    "yellow",
    "lime",
    "green",
    "light_blue",
    "cyan",
    "blue",
    "purple",
    "magenta",
    "pink",
)

for color in COLORS:
    globals()[color.upper()] = color

del color