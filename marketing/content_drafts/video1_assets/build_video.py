import subprocess, os
from PIL import Image, ImageDraw, ImageFont
from moviepy import ImageClip, AudioFileClip, concatenate_videoclips

W, H = 1080, 1920
GREEN = (10, 110, 78)
WHITE = (255, 255, 255)
BG = (250, 251, 252)

FONT_BOLD = "/System/Library/Fonts/Supplemental/Arial Bold.ttf"
FONT_REG = "/System/Library/Fonts/Supplemental/Arial.ttf"

SEGMENTS = [
    {
        "speech": "If you're self employed in the U.K. and don't know this date, you need to.",
        "onscreen": "MTD is coming.\nDo you know\nyour date?",
        "bg": GREEN, "fg": WHITE, "size": 90,
    },
    {
        "speech": "Making Tax Digital is replacing the old Self Assessment return for self employed people and landlords. It's rolling out in stages, and most people have no idea which stage applies to them.",
        "onscreen": "MTD replaces the\nold tax return.\nIt's rolling out\nin stages.",
        "bg": BG, "fg": GREEN, "size": 72,
    },
    {
        "speech": "Let's check an example. Thirty five thousand pounds in self employment income means Making Tax Digital applies to you from the sixth of April, twenty twenty seven.",
        "onscreen": "£35,000 self-employed\nincome =\n\nMTD from\n6 April 2027",
        "bg": GREEN, "fg": WHITE, "size": 80,
    },
    {
        "speech": "It combines self employment and rental income, so add them together if you have both. Fifty thousand pounds from twenty twenty six. Thirty thousand from twenty twenty seven. Twenty thousand from twenty twenty eight.",
        "onscreen": "£50k -> April 2026\n£30k -> April 2027\n£20k -> April 2028\n\n(self-employment +\nproperty, combined)",
        "bg": BG, "fg": GREEN, "size": 64,
    },
    {
        "speech": "Takes ten seconds, no sign up. Link in bio. Free tool, not tax advice.",
        "onscreen": "Free tool.\nNo sign-up.\n\nLink in bio.",
        "bg": GREEN, "fg": WHITE, "size": 90,
    },
]

def wrap_and_draw(draw, text, font, fg, max_width):
    lines = []
    for raw_line in text.split("\n"):
        if raw_line == "":
            lines.append("")
            continue
        words = raw_line.split(" ")
        cur = ""
        for w in words:
            test = (cur + " " + w).strip()
            if draw.textlength(test, font=font) <= max_width:
                cur = test
            else:
                lines.append(cur)
                cur = w
        lines.append(cur)
    return lines

def make_slide(text, bg, fg, size, path):
    img = Image.new("RGB", (W, H), bg)
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype(FONT_BOLD, size)
    lines = wrap_and_draw(draw, text, font, fg, W - 160)
    line_height = int(size * 1.25)
    total_height = line_height * len(lines)
    y = (H - total_height) // 2
    for line in lines:
        w = draw.textlength(line, font=font)
        x = (W - w) // 2
        draw.text((x, y), line, font=font, fill=fg)
        y += line_height
    # small footer brand
    foot_font = ImageFont.truetype(FONT_REG, 36)
    foot_text = "mtdchecker"
    fw = draw.textlength(foot_text, font=foot_font)
    draw.text(((W - fw) // 2, H - 100), foot_text, font=foot_font, fill=fg)
    img.save(path)

def main():
    clips = []
    outdir = os.path.dirname(os.path.abspath(__file__))
    for i, seg in enumerate(SEGMENTS):
        aiff_path = os.path.join(outdir, f"seg{i}.aiff")
        wav_path = os.path.join(outdir, f"seg{i}.wav")
        img_path = os.path.join(outdir, f"slide{i}.png")

        subprocess.run(["say", "-v", "Daniel", "-o", aiff_path, seg["speech"]], check=True)
        subprocess.run(["afconvert", "-f", "WAVE", "-d", "LEI16", aiff_path, wav_path], check=True)

        make_slide(seg["onscreen"], seg["bg"], seg["fg"], seg["size"], img_path)

        audio = AudioFileClip(wav_path)
        # pad 0.4s at end of each segment for breathing room
        dur = audio.duration + 0.4
        clip = ImageClip(img_path).with_duration(dur).with_audio(audio)
        clips.append(clip)

    final = concatenate_videoclips(clips, method="compose")
    out_path = os.path.join(outdir, "video1_amiaffected.mp4")
    final.write_videofile(out_path, fps=30, codec="libx264", audio_codec="aac")
    print("DONE:", out_path)

if __name__ == "__main__":
    main()
