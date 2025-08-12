import json
import os
from PIL import Image, ImageDraw

# create output directory if it doesn't exist
categoryName = "axe"
output_dir = categoryName
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

folders = [f"full_simplified_{categoryName}"]

# process first 60 lines one by one
for j in range(1):
    for i in range(60):
        path = f'/Users/anjanathreya/Downloads/{folders[j]}.ndjson'
        lines = open(path,'r').readlines()
        print(f"Processing line {i+1}/60...")
        
        # grab the current line, JSON parse it and fetch the 'drawing' array
        raw_drawing = json.loads(lines[i])['drawing']
        
        # zip x,y coordinates for each point in every polyline
        polylines = [list(zip(polyline[0], polyline[1])) for polyline in raw_drawing]
        
        # make a new image
        pil_img = Image.new("RGB", (256, 256), (255,255,255))
        # get a drawing context
        d = ImageDraw.Draw(pil_img)
        # render each polyline
        for polyline in polylines:
            if len(polyline) > 1:  # need at least 2 points to draw a line
                d.line(polyline, fill=(0, 0, 0), width=2)
        
        # save image
        filename = f"{categoryName}_{i+1:03d}.png"
        filepath = os.path.join(output_dir, filename)
        pil_img.save(filepath)

print(f"Saved {min(60, len(lines))} images to {output_dir} folder")