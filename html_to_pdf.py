import os
import asyncio
import sys

# Script ini membutuhkan package Playwright.
# Jika belum ada, Anda bisa menginstallnya dengan menjalankan perintah di terminal:
# pip install playwright
# playwright install chromium

try:
    from playwright.async_api import async_playwright
except ImportError:
    print("Error: Library Playwright belum terinstall.")
    print("Silakan jalankan perintah berikut di terminal Anda:")
    print("pip install playwright")
    print("playwright install chromium")
    sys.exit(1)

async def generate_pdf():
    html_file = r"e:\Kerjaan Abi\Logo kurban\index.html"
    output_pdf = r"e:\Kerjaan Abi\Logo kurban\Desain_Stiker_CorelDraw.pdf"
    
    # Format path menjadi URI file
    file_url = f"file:///{html_file.replace(chr(92), '/')}"
    
    print(f"Sedang membaca file HTML: {html_file}")
    print("Proses ini akan menyimpan warna background dan grafik...")
    
    async with async_playwright() as p:
        # Meluncurkan Chromium dalam mode tanpa tampilan (headless)
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()
        
        # Buka file HTML
        await page.goto(file_url, wait_until="networkidle")
        
        # Tunggu 2 detik tambahan untuk memastikan semua web-fonts dan emoji sudah dirender
        await page.wait_for_timeout(2000)
        
        # Menyimpan sebagai PDF
        # Lebar dan tinggi dibuat cukup besar (bebas / custom) agar semua stiker muat 
        # dalam satu halaman tanpa terpotong page-break.
        await page.pdf(
            path=output_pdf,
            print_background=True,
            width="2500px",
            height="1800px"
        )
        
        await browser.close()
        
    print("="*50)
    print("✅ BERHASIL!")
    print(f"File PDF telah disimpan di:\n{output_pdf}")
    print("="*50)
    print("Langkah selanjutnya untuk klien Anda:")
    print("1. Buka Corel Draw")
    print("2. Pilih File > Import (Ctrl + I)")
    print("3. Pilih file PDF di atas, lalu import as Text / Curves")
    print("4. Simpan as .cdr")

if __name__ == "__main__":
    asyncio.run(generate_pdf())
