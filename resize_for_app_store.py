#!/usr/bin/env python3
"""
Resize screenshots to App Store required dimensions
"""

from PIL import Image
import os

def resize_screenshot(input_path, output_dir, sizes):
    """
    Resize a screenshot to multiple App Store sizes

    Args:
        input_path: Path to input screenshot
        output_dir: Directory to save resized screenshots
        sizes: Dict of size names to (width, height) tuples
    """
    img = Image.open(input_path)
    base_name = os.path.splitext(os.path.basename(input_path))[0]

    for size_name, (width, height) in sizes.items():
        # Resize with high-quality Lanczos resampling
        resized = img.resize((width, height), Image.Resampling.LANCZOS)

        # Save with high quality
        output_path = os.path.join(output_dir, f"{base_name}_{size_name}.png")
        resized.save(output_path, quality=95, optimize=True)
        print(f"✅ Created: {output_path} ({width}x{height})")

def main():
    # App Store required sizes
    sizes = {
        '6.7inch': (1290, 2796),  # iPhone 14/15/16 Pro Max
        '6.5inch': (1242, 2688),  # iPhone XS Max through 13 Pro Max
        '5.5inch': (1242, 2208),  # iPhone 6s Plus through 8 Plus
    }

    # Input screenshots
    screenshots = [
        'AppStoreScreenshots/01_tea_selection_marketing.png',
        'AppStoreScreenshots/02_timer_view_marketing.png',
        'AppStoreScreenshots/03_dark_mode_timer_marketing.png',
    ]

    # Create output directory
    output_dir = 'AppStoreScreenshots/Resized'
    os.makedirs(output_dir, exist_ok=True)

    # Resize each screenshot
    for screenshot in screenshots:
        if os.path.exists(screenshot):
            print(f"\n📐 Resizing {os.path.basename(screenshot)}...")
            resize_screenshot(screenshot, output_dir, sizes)
        else:
            print(f"⚠️  Screenshot not found: {screenshot}")

    print("\n✨ All screenshots resized successfully!")
    print(f"📁 Output directory: {output_dir}/")
    print("\n📱 App Store sizes created:")
    print("   - 6.7\" display: 1290 x 2796 pixels")
    print("   - 6.5\" display: 1242 x 2688 pixels")
    print("   - 5.5\" display: 1242 x 2208 pixels")

if __name__ == '__main__':
    main()
