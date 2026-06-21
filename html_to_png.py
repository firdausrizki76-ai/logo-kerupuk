import os
import asyncio
from playwright.async_api import async_playwright

async def generate_png():
    html_file = r"e:\Kerjaan Abi\Logo kurban\index.html"
    output_png = r"e:\Kerjaan Abi\Logo kurban\Desain_Stiker_CorelDraw.png"
    
    # Format path menjadi URI file
    file_url = f"file:///{html_file.replace(chr(92), '/')}"
    
    print(f"Sedang membaca file HTML: {html_file}")
    print("Membuat gambar PNG Resolusi Tinggi (Super Tajam)...")
    
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        
        # device_scale_factor=3 akan membuat resolusi gambar 3x lebih besar
        # sehingga setara dengan kualitas cetak 300 DPI
        context = await browser.new_context(
            viewport={'width': 2500, 'height': 1800},
            device_scale_factor=3
        )
        page = await context.new_page()
        
        # Buka file HTML
        await page.goto(file_url, wait_until="networkidle")
        
        # Tunggu 2 detik tambahan untuk memastikan semua web-fonts dan emoji sudah dirender
        await page.wait_for_timeout(2000)
        
        # Menyimpan sebagai PNG seluruh halaman
        await page.screenshot(
            path=output_png,
            full_page=True,
            animations="disabled"
        )
        
        await browser.close()
        
    print("="*50)
    print("✅ BERHASIL!")
    print(f"File PNG telah disimpan di:\n{output_png}")
    print("="*50)

if __name__ == "__main__":
    asyncio.run(generate_png())
