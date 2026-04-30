import os
from PIL import Image

# הנתיב הראשי של פין 1
root_path = r'C:\PinterestWork\pin1'

def process_all_categories(base_path):
    # עובר על כל התיקיות של הקטגוריות (כמו Bags_1, Dresses וכו')
    for category in os.listdir(base_path):
        category_path = os.path.join(base_path, category)
        
        if os.path.isdir(category_path):
            print(f"--- מתחיל לעבוד על קטגוריה: {category} ---")
            
            # צולל פנימה לתת-תיקיות (כמו 5_1, 7_1)
            for subdir, dirs, files in os.walk(category_path):
                if subdir == category_path:
                    continue
                
                files.sort()
                count = 1
                
                for filename in files:
                    if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.webp')):
                        old_path = os.path.join(subdir, filename)
                        new_name = f"{count}.jpg"
                        new_path = os.path.join(subdir, new_name)
                        
                        try:
                            with Image.open(old_path) as img:
                                rgb_img = img.convert('RGB')
                                rgb_img.save(new_path, 'JPEG', quality=95)
                            
                            if old_path != new_path:
                                os.remove(old_path)
                            count += 1
                        except Exception as e:
                            print(f"שגיאה בתיקייה {subdir} קובץ {filename}: {e}")
            print(f"--- סיימתי קטגוריה: {category} ---")

if __name__ == "__main__":
    process_all_categories(root_path)
    print("\n--- הסתיים בהצלחה! כל pin1 עכשיו בפורמט JPG ומספרים נקיים ---")