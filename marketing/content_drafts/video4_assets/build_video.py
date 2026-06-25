import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from video_lib import build_video, GREEN, WHITE, BG

SEGMENTS = [
    {
        "speech": "If you rent out a property and don't do anything else self employed, this is still for you.",
        "onscreen": "Landlords:\nMTD applies\nto you too",
        "bg": GREEN, "fg": WHITE, "size": 80,
    },
    {
        "speech": "Making Tax Digital isn't just for the self employed. If you earn rental income, it counts as qualifying income on its own. You don't need a separate business.",
        "onscreen": "Rental income\nalone counts.\n\nNo separate\nbusiness needed.",
        "bg": BG, "fg": GREEN, "size": 70,
    },
    {
        "speech": "Got a self employed side income too? It all gets added together. Twenty thousand pounds in rent plus fifteen thousand freelancing is thirty five thousand combined. That's well over the twenty twenty seven threshold.",
        "onscreen": "£20k rent +\n£15k freelance\n= £35k combined\n\nOver the 2027\nthreshold",
        "bg": GREEN, "fg": WHITE, "size": 68,
    },
    {
        "speech": "Multiple properties? Same deal. All your rental income across all properties counts as one total.",
        "onscreen": "Multiple\nproperties =\nadded together",
        "bg": BG, "fg": GREEN, "size": 80,
    },
    {
        "speech": "Free checker handles all of this automatically. Link in bio.",
        "onscreen": "Free checker.\nDoes the maths\nfor you.\n\nLink in bio.",
        "bg": GREEN, "fg": WHITE, "size": 78,
    },
]

if __name__ == "__main__":
    outdir = os.path.dirname(os.path.abspath(__file__))
    build_video(SEGMENTS, outdir, "video4_landlords.mp4")
