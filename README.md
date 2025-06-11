# Telegram Face Swap Video Bot (SimSwap)

## Requirements
- Ubuntu 20.04+
- Python 3.8+
- (Optional) NVIDIA GPU + CUDA

## Setup
1. Update repos & install deps:
   sudo apt update && sudo apt install git ffmpeg python3-venv -y

2. Clone SimSwap:
   git clone https://github.com/neuralchen/SimSwap
   cp test_video_swapsingle.py face-swap-bot/

3. Download pre-trained models:
   - arcface_checkpoint.tar
   - shape_predictor_68_face_landmarks.dat
   - ms1m_ir50.onnx and inswapper_128.onnx (rename to .onnx)

4. Clone this repo:
   git clone <your_repo_url>
   cd face-swap-bot

5. Install Python deps:
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt

6. Move models into `face-swap-bot/arcface_model/`

7. Start bot:
   python3 main.py

## Usage
1. `/start`
2. Send face photo
3. Send target video
4. Receive swapped video
5. Use `/cancel` to reset

## Notes
- All files auto-deleted after each session
- Videos are sent privately (no public posting)
