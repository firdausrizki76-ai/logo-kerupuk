import os
from PIL import Image, ImageDraw, ImageFont

def process_stickers():
    # Paths
    original_path = r'e:\Kerjaan Abi\Logo kurban\stiker_kurban_14pcs_F4_BW (1).png'
    output_png = r'e:\Kerjaan Abi\Logo kurban\stiker_kurban_14pcs_A4_BW.png'
    output_pdf = r'e:\Kerjaan Abi\Logo kurban\stiker_kurban_14pcs_A4_BW.pdf'
    
    # 1. Load the original image
    print("Loading original image...")
    im = Image.open(original_path)
    
    # 2. Crop the first sticker (box: x1=156, y1=82, x2=1167, y2=555)
    print("Cropping base sticker...")
    sticker = im.crop((156, 82, 1167, 555)).convert('RGB')
    s_w, s_h = sticker.size # 1011 x 473
    
    # 3. Erase old text and write new text "Idul Adha 1447 H"
    print("Modifying text in sticker banner...")
    draw = ImageDraw.Draw(sticker)
    
    # Erase area: x=455..885, y=380..465 (relative to sticker)
    # The banner background color is around (43, 43, 43)
    draw.rectangle([455, 380, 885, 465], fill=(43, 43, 43))
    
    # Load Segoe Script Bold font
    font_path = r'C:\Windows\Fonts\segoescb.ttf'
    font_size = 40
    try:
        font = ImageFont.truetype(font_path, font_size)
    except IOError:
        print("Warning: Segoe Script Bold not found, falling back to Lucida Handwriting")
        try:
            font = ImageFont.truetype(r'C:\Windows\Fonts\LHANDW.TTF', font_size - 2)
        except IOError:
            print("Warning: Lucida Handwriting not found, using default font")
            font = ImageFont.load_default()
            
    text = 'Idul Adha 1447 H'
    
    # Center text in space x=450..890, y=380..465
    try:
        bbox = draw.textbbox((0, 0), text, font=font)
        tw = bbox[2] - bbox[0]
        th = bbox[3] - bbox[1]
    except AttributeError:
        tw, th = draw.textsize(text, font=font)
        
    cx = 450 + (890 - 450) // 2
    cy = 380 + (465 - 380) // 2
    
    # Draw text in white
    draw.text((cx - tw // 2, cy - th // 2 - 2), text, fill=(255, 255, 255), font=font)
    
    # 4. Create new white A4 image (2480 x 3508 pixels)
    print("Creating A4 canvas (2480 x 3508)...")
    a4_im = Image.new('RGB', (2480, 3508), color=(255, 255, 255))
    
    # Layout 14 stickers in 2x7 grid
    # Horizontal spacing
    gap_x = 150
    margin_x = (2480 - 2 * s_w - gap_x) // 2 # (2480 - 2022 - 150) // 2 = 154
    
    # Vertical spacing
    gap_y = 20
    margin_y = (3508 - 7 * s_h - 6 * gap_y) // 2 # (3508 - 3311 - 120) // 2 = 38
    
    print(f"Layout geometry: margin_x={margin_x}, gap_x={gap_x}, margin_y={margin_y}, gap_y={gap_y}")
    
    # Paste stickers
    for row in range(7):
        y_pos = margin_y + row * (s_h + gap_y)
        for col in range(2):
            x_pos = margin_x + col * (s_w + gap_x)
            a4_im.paste(sticker, (x_pos, y_pos))
            
    # 5. Save the output files with 300 DPI resolution
    print("Saving PNG file...")
    a4_im.save(output_png, 'PNG', dpi=(300, 300))
    
    print("Saving PDF file...")
    a4_im.save(output_pdf, 'PDF', resolution=300.0)
    
    print("Done! Files saved successfully:")
    print(f" - PNG: {output_png}")
    print(f" - PDF: {output_pdf}")

if __name__ == '__main__':
    process_stickers()
