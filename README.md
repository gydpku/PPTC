# PPTC
This repository contains information about PPTC benchmark, data, code, and the PPTX-Match evaluation system. 

# Requirements
please install these packages first:
```
pip install -r requirements.txt
```

# Baseline systems

For closed-source LLMs (text-davinci-003, ChatGPT (gpt-3.5-turbo), and GPT-4) and other LLMs that you only have the API access. You first need to fill your API access by following the steps below:

1. open the file src/openai_api.py
2. fill your openai key in line 27~31.

For open-source LLMs (e.g., Llama-2-chat, vicuna and other LLMs at huggingface) and other LLMs that you have the model. We recommend serving your models through the fastchat server. You can follow the steps below. More details are in https://github.com/lm-sys/FastChat. 

1. pip3 install "fschat[model_worker,webui]" 
2. Launch the controller
   ```
   python3 -m fastchat.serve.controller --port 21007
   ```
3. Launch the model worker
   ```
   CUDA_VISIBLE_DEVICES=0 python3 -m fastchat.serve.model_worker --model-path your_model_path  --num-gpus 1
   --controller-address 'http://localhost:21007' --port 21008 --worker-address 'http://localhost:21008'
   ```
'your_model_path' can be 'lmsys/vicuna-13b-v1.5-16k' for Vicuna LLM or the storage path for your LLM. --num-gpus is the number of GPUs used to do inference.

4. Launch the fastcht server
   ```
   python3.9 -m fastchat.serve.openai_api_server --host localhost --controller-address 'http://localhost:21007' --port 8000
   ```
