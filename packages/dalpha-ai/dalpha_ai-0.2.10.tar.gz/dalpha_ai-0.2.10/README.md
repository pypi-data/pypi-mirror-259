## Core-SDK (Dalpha-ai 라이브러리) 

### Introduction 
- 달파 AI 팀 내부에서 개발한 라이브러리로, 자주 사용되는 AI 모델들을 빠르고 편리하게 사용하는 목적으로 만들어진 python library, package입니다.
- 현재는 Classifier Train & Inference / Zero-Shot Classifier를 지원하며, 추후에는 Clip training / Vector similarity search / Detector 등등을 지원할 예정입니다.

### Update
****v0.2.9****
- start ipynb 및 readme 추가 (준표님~)
- multi-label-classification 관련 에러 수정 (준표님~~)
- monitor accuracy 유효자리 4자리로 변경
- peft 0.7버전대 지원
- augmentation auto crop ratio 0.9 default 값 지정
- image model onnx 관련 에러 수정
- only_backbone, last_embedding 관련 지원 확대
- pipeline에서 pillow image Input 지원
- textclassifier에서 model type bert 지원
- requirements.txt 관련 패키지들 최신 버전으로 고정 (이제 절대 버전 안풀거임)

### Installation

```
#### GPU 
pip install dalpha-ai
#### CPU
pip install dalpha-ai-cpu
```

### QuickStart

`` examples/HowToStart.ipynb ``
