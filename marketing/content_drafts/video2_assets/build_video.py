import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from video_lib import build_video, GREEN, WHITE, BG

SEGMENTS = [
    {
        "speech": "Found out you need Making Tax Digital software? Here's what that actually means.",
        "onscreen": "MTD software:\nwhat you\nactually need",
        "bg": GREEN, "fg": WHITE, "size": 84,
    },
    {
        "speech": "Once your date hits, you can't just file once a year anymore. You need software that keeps digital records and sends quarterly updates straight to HMRC.",
        "onscreen": "No more once-a-year\nfiling.\n\nDigital records +\nquarterly updates.",
        "bg": BG, "fg": GREEN, "size": 70,
    },
    {
        "speech": "The three most people use: FreeAgent, good if you're with certain banks, often free. QuickBooks, most widely used, solid for general bookkeeping. Xero, strong if you're a landlord juggling multiple properties.",
        "onscreen": "FreeAgent\nQuickBooks\nXero\n\n(pick based on your\nsituation)",
        "bg": GREEN, "fg": WHITE, "size": 78,
    },
    {
        "speech": "Don't wait until your start date to set this up. Start keeping digital records a few months early, so you're not learning new software under deadline pressure.",
        "onscreen": "Start a few months\nearly.\n\nDon't learn new\nsoftware under\ndeadline pressure.",
        "bg": BG, "fg": GREEN, "size": 64,
    },
    {
        "speech": "I built a free checker that tells you your exact date and links to compatible software. Link in bio. Some of those software links are affiliate links, at no extra cost to you.",
        "onscreen": "Free checker +\nsoftware links\nin bio.\n\n(affiliate links,\nno extra cost)",
        "bg": GREEN, "fg": WHITE, "size": 70,
    },
]

if __name__ == "__main__":
    outdir = os.path.dirname(os.path.abspath(__file__))
    build_video(SEGMENTS, outdir, "video2_whattodo.mp4")
