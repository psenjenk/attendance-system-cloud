import os
from PIL import Image
from pathlib import Path

def optimize_image(image_path, quality=85, max_size=(1920, 1080)):
    """Optimize an image file."""
    try:
        img = Image.open(image_path)
        
        # Resize if larger than max_size
        if img.size[0] > max_size[0] or img.size[1] > max_size[1]:
            img.thumbnail(max_size, Image.LANCZOS)
        
        # Convert to RGB if necessary
        if img.mode in ('RGBA', 'LA') or (img.mode == 'P' and 'transparency' in img.info):
            background = Image.new('RGB', img.size, (255, 255, 255))
            background.paste(img, mask=img.split()[-1])
            img = background
        
        # Save optimized image
        output_path = image_path
        img.save(output_path, 'JPEG', quality=quality, optimize=True)
        print(f"Optimized: {image_path}")
        
        # Get file size before and after
        original_size = os.path.getsize(image_path)
        optimized_size = os.path.getsize(output_path)
        saved = (original_size - optimized_size) / original_size * 100
        print(f"Saved: {saved:.1f}%")
        
    except Exception as e:
        print(f"Error processing {image_path}: {str(e)}")

def main():
    # Define image directories
    image_dirs = ['static/images']
    
    # Supported image extensions
    extensions = ('.jpg', '.jpeg', '.png')
    
    # Process all images
    for directory in image_dirs:
        for root, _, files in os.walk(directory):
            for file in files:
                if file.lower().endswith(extensions):
                    image_path = os.path.join(root, file)
                    optimize_image(image_path)

if __name__ == '__main__':
    main() 