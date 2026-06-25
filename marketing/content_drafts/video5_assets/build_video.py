import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from video_lib import build_video, GREEN, WHITE, BG

SEGMENTS = [
    {
        "speech": "Let's actually do the maths on Making Tax Digital, with a real example.",
        "onscreen": "Let's do\nthe maths",
        "bg": GREEN, "fg": WHITE, "size": 90,
    },
    {
        "speech": "Say you're a sole trader earning eighteen thousand pounds from freelancing, plus fifteen thousand a year renting out a flat.",
        "onscreen": "£18,000\nfreelancing\n\n+\n\n£15,000\nrental income",
        "bg": BG, "fg": GREEN, "size": 70,
    },
    {
        "speech": "HMRC adds those together. Eighteen thousand plus fifteen thousand is thirty three thousand pounds in qualifying income.",
        "onscreen": "£18,000 + £15,000\n=\n£33,000\nqualifying income",
        "bg": GREEN, "fg": WHITE, "size": 70,
    },
    {
        "speech": "That's over the thirty thousand pound threshold, which is assessed on your twenty twenty five, twenty six income. So Making Tax Digital applies to you from the sixth of April, twenty twenty seven.",
        "onscreen": "Over £30k\nthreshold\n\nMTD from\n6 April 2027",
        "bg": BG, "fg": GREEN, "size": 72,
    },
    {
        "speech": "Drop your numbers into the free checker and it does this instantly. Link in bio.",
        "onscreen": "Free. No sign-up.\nNot tax advice.\n\nLink in bio.",
        "bg": GREEN, "fg": WHITE, "size": 78,
    },
]

if __name__ == "__main__":
    outdir = os.path.dirname(os.path.abspath(__file__))
    build_video(SEGMENTS, outdir, "video5_workedexample.mp4")
