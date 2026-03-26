import os
import shutil
import torch
from PIL import Image
from transformers import CLIPProcessor, CLIPModel

def ai_filter_dataset(dataset_dir, noise_dir):
    print("🤖 곧바로 AI(OpenAI CLIP) 등판! 모델을 불러오는 중입니다... (최초 1회 모델 다운로드가 진행될 수 있습니다)")
    
    # 1. 모델 설정 (M1/M2/M3 맥북 엔진 가속 지원 여부 확인)
    device = "mps" if torch.backends.mps.is_available() else "cpu"
    model_id = "openai/clip-vit-base-patch32"
    print(f"🖥️ 사용 디바이스 가속: {device}")

    try:
        model = CLIPModel.from_pretrained(model_id).to(device)
        processor = CLIPProcessor.from_pretrained(model_id)
    except Exception as e:
        print(f"❌ 모델 로드 실패: {e}\n(transformers와 torch 라이브러리가 필요합니다)")
        return

    # 2. 모델에게 던져줄 질문 (Zero-shot 분류 레이블)
    # 0번: 우리가 원하는 실사 사진
    # 1번: 일러스트/그림 노이즈
    # 2번: 글자나 간판이 없는 엉뚱한 풍경/사물 위주 사진
    labels = [
        "A real photo of a street banner, flyer, sign, or poster in the street",
        "A cartoon, vector graphic, digital painting, drawing, or illustration",
        "A photo of a person, animal, interior, or nature landscape without clear signboards or text"
    ]

    os.makedirs(noise_dir, exist_ok=True)
    moved_count = 0
    valid_count = 0

    print(f"🧹 본격적인 AI 필터링을 시작합니다: {dataset_dir} ...")

    for root, _, files in os.walk(dataset_dir):
        # 노이즈 디렉토리 자체는 검사 제외
        if os.path.abspath(root).startswith(os.path.abspath(noise_dir)):
            continue

        for file in files:
            file_path = os.path.join(root, file)
            if file.startswith('.') or not file_path.lower().endswith(('.jpg', '.jpeg', '.png', '.webp')):
                continue

            try:
                # 이미지 열고 RGB 변환
                image = Image.open(file_path).convert("RGB")
                
                # 예측 파이프라인 전송
                inputs = processor(text=labels, images=image, return_tensors="pt", padding=True).to(device)
                outputs = model(**inputs)
                
                # 확률(Softmax) 계산
                logits_per_image = outputs.logits_per_image
                probs = logits_per_image.softmax(dim=1).cpu().detach().numpy()[0]
                
                # 가장 확률이 높은 레이블의 인덱스 추론 (0, 1, 2)
                best_match_idx = probs.argmax()

                if best_match_idx == 0:
                    valid_count += 1
                    # print(f"🟢 [통과] 실사 사진 확인: {file} (확률: {probs[0]*100:.1f}%)")
                else:
                    reason = "일러스트" if best_match_idx == 1 else "무관한 피사체"
                    print(f"🔴 [차단] 노이즈 감지({reason}): {file} (확률: {probs[best_match_idx]*100:.1f}%)")
                    
                    category_folder = os.path.basename(root)
                    target_dir = os.path.join(noise_dir, category_folder)
                    os.makedirs(target_dir, exist_ok=True)
                    
                    shutil.move(file_path, os.path.join(target_dir, file))
                    moved_count += 1
            except Exception as e:
                print(f"⚠️ 에러 발생 파일 건너뜀 ({file}): {e}")

    print("\n===================================")
    print(f"✅ AI 필터링 완료!")
    print(f"살아남은 찐 데이터: {valid_count}장")
    print(f"그림/노이즈로 판단되어 격리된 데이터: {moved_count}장")
    print(f"격리 폴더 위치: {os.path.abspath(noise_dir)}")
    print("격리 폴더를 쓱 보시고 이상이 없으면 폴더째로 삭제해주세요!")
    print("===================================")

if __name__ == "__main__":
    raw_images_path = os.path.abspath("../dataset/raw_images")
    noise_images_path = os.path.abspath("../dataset/noise_images")
    
    if os.path.exists(raw_images_path):
        ai_filter_dataset(raw_images_path, noise_images_path)
    else:
        print(f"❌ 데이터 폴더를 찾을 수 없습니다: {raw_images_path}")
