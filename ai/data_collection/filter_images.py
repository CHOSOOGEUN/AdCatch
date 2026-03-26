import os
from PIL import Image

def clean_dataset(dataset_dir, min_width=300, min_height=300):
    print(f"🧹 데이터셋 노이즈 필터링 시작: {dataset_dir}")
    removed_count = 0
    valid_count = 0

    for root, _, files in os.walk(dataset_dir):
        for file in files:
            file_path = os.path.join(root, file)
            
            # macOS 숨김 파일 등 제외
            if file.startswith('.') or file_path.endswith('.txt'):
                continue

            try:
                # 1. 파일이 정상적인 이미지인지 검사
                with Image.open(file_path) as img:
                    img.verify()
                
                # 2. 이미지 크기 검사 (해상도가 너무 작으면 삭제)
                with Image.open(file_path) as img:
                    width, height = img.size
                    
                    if width < min_width or height < min_height:
                        print(f"🗑️ 삭제됨 (선명도/크기 미달 - {width}x{height}): {file_path}")
                        os.remove(file_path)
                        removed_count += 1
                    else:
                        valid_count += 1
                        
            except Exception as e:
                # 열리지 않거나 깨진 이미지 삭제
                print(f"💥 삭제됨 (손상된 파일): {file_path} - {e}")
                try:
                    os.remove(file_path)
                    removed_count += 1
                except:
                    pass

    print("\n===================================")
    print(f"✅ 노이즈 필터링 완료!")
    print(f"유지된 정상(사용 가능) 이미지 수: {valid_count}장")
    print(f"삭제된 찌꺼기/노이즈 이미지 수: {removed_count}장")
    print("===================================")

if __name__ == "__main__":
    # raw_images 경로
    raw_images_path = os.path.abspath("../dataset/raw_images")
    if os.path.exists(raw_images_path):
        # 가로, 세로 중 하나라도 200 픽셀보다 작으면 삭제
        clean_dataset(raw_images_path, min_width=200, min_height=200)
    else:
        print(f"❌ 데이터 폴더를 찾을 수 없습니다: {raw_images_path}")
