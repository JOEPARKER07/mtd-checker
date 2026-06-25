import subprocess, os
from PIL import Image, ImageDraw, ImageFont
from moviepy import ImageClip, AudioFileClip, concatenate_videoclips

W, H = 1080, 1920
GREEN = (10, 110, 78)
WHITE = (255, 255, 255)
BG = (250, 251, 252)
WARN_BG = (253, 241, 222)
WARN_FG = (154, 91, 0)

FONT_BOLD = "/System/Library/Fonts/Supplemental/Arial Bold.ttf"
FONT_REG = "/System/Library/Fonts/Supplemental/Arial.ttf"

def wrap(draw, text, font, max_width):
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

def make_slide(text, bg, fg, size, path, footer="mtdchecker"):
    img = Image.new("RGB", (W, H), bg)
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype(FONT_BOLD, size)
    lines = wrap(draw, text, font, W - 160)
    line_height = int(size * 1.25)
    total_height = line_height * len(lines)
    y = (H - total_height) // 2
    for line in lines:
        w = draw.textlength(line, font=font)
        x = (W - w) // 2
        draw.text((x, y), line, font=font, fill=fg)
        y += line_height
    foot_font = ImageFont.truetype(FONT_REG, 36)
    fw = draw.textlength(footer, font=foot_font)
    draw.text(((W - fw) // 2, H - 100), footer, font=foot_font, fill=fg)
    img.save(path)

def build_video(segments, outdir, out_name, voice="Daniel"):
    clips = []
    for i, seg in enumerate(segments):
        aiff_path = os.path.join(outdir, f"seg{i}.aiff")
        wav_path = os.path.join(outdir, f"seg{i}.wav")
        img_path = os.path.join(outdir, f"slide{i}.png")

        subprocess.run(["say", "-v", voice, "-o", aiff_path, seg["speech"]], check=True)
        subprocess.run(["afconvert", "-f", "WAVE", "-d", "LEI16", aiff_path, wav_path], check=True)

        make_slide(seg["onscreen"], seg["bg"], seg["fg"], seg["size"], img_path)

        audio = AudioFileClip(wav_path)
        dur = audio.duration + 0.4
        clip = ImageClip(img_path).with_duration(dur).with_audio(audio)
        clips.append(clip)

    final = concatenate_videoclips(clips, method="compose")
    out_path = os.path.join(outdir, out_name)
    final.write_videofile(out_path, fps=30, codec="libx264", audio_codec="aac")
    print("DONE:", out_path)
    return out_path
