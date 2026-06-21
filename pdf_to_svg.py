import fitz

def convert_pdf_to_svg():
    pdf_path = r"e:\Kerjaan Abi\Logo kurban\Desain_Stiker_CorelDraw.pdf"
    svg_path = r"e:\Kerjaan Abi\Logo kurban\Desain_Stiker_CorelDraw.svg"
    
    # Buka dokumen PDF
    doc = fitz.open(pdf_path)
    
    # Ambil halaman pertama
    page = doc[0]
    
    # Konversi halaman ke format SVG
    svg_content = page.get_svg_image(matrix=fitz.Identity)
    
    # Simpan sebagai file SVG
    with open(svg_path, "w", encoding="utf-8") as f:
        f.write(svg_content)
        
    print(f"Berhasil! File SVG disimpan di: {svg_path}")

if __name__ == "__main__":
    convert_pdf_to_svg()
