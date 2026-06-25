import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from video_lib import build_video, GREEN, WHITE, BG

SEGMENTS = [
    {
        "speech": "Missed a Making Tax Digital deadline? Here's what actually happens. It's less scary than you think.",
        "onscreen": "MTD penalties:\nthe actual\nnumbers",
        "bg": GREEN, "fg": WHITE, "size": 84,
    },
    {
        "speech": "HMRC uses a points system now, not instant fines. Miss a quarterly update, you get one point. Hit four points, or two if you file annually, that's when a two hundred pound fine kicks in.",
        "onscreen": "1 missed update\n= 1 point\n\n4 points = £200 fine\n(2 if annual)",
        "bg": BG, "fg": GREEN, "size": 68,
    },
    {
        "speech": "Good news: if you're newly joining in the twenty twenty six, twenty seven tax year, there's a soft landing. No penalties for missed quarterly updates that year, while you get used to it.",
        "onscreen": "2026/27 =\nsoft landing year\n\nNo penalties while\nyou adjust",
        "bg": GREEN, "fg": WHITE, "size": 76,
    },
    {
        "speech": "Points also expire automatically twenty four months after the miss, as long as you stay under the threshold. It's designed to be forgiving while you adjust.",
        "onscreen": "Points expire after\n24 months\n\n(if you stay under\nthe threshold)",
        "bg": BG, "fg": GREEN, "size": 68,
    },
    {
        "speech": "Full breakdown, including the official HMRC source, is on my free checker tool. Link in bio.",
        "onscreen": "Full breakdown +\nHMRC source\nin bio.",
        "bg": GREEN, "fg": WHITE, "size": 80,
    },
]

if __name__ == "__main__":
    outdir = os.path.dirname(os.path.abspath(__file__))
    build_video(SEGMENTS, outdir, "video3_penalties.mp4")
