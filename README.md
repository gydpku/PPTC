# PPTC
Power-Point Task Completion (PPTC) is a benchmark that measures LLMs' task completion performance for PowerPoint software. The benchmark focuses on two basic tasks
within PowerPoint: the creation of new slides and the editing of PPT templates. It simulates the multi-turn dialogue session between the user and the LLM. Each turn consists of a user instruction, a feasible solution that provides the correct solution, and the resulting label output file. To finish the instruction, we use the current instruction, past turns’ instructions (dialogue history), the PPT file content, and the reference API file as the input and prompt the LLM to generate an API sequence as the solution. Then we use the API executor to execute the API sequence and return the user the resulting PPT file (the prediction file) as the LLM’s response.

To evaluate the correctness of the prediction file, we further propose the PPTX-match evaluation system that evaluate the prediction file in two ways: (1) by checking if the objects in
the prediction file satisfy the label position relation and (2) by comparing the content of attributes in the prediction with those in the corresponding attributes in the label file.resulting PPT file. Based on our evaluation system, our evaluation metrics focus on two key aspects: turn and session. For example, turn-based accuracy is the ratio of successfully completed turns to the total number of turns, while session-based accuracy measures the ratio of completed sessions to the overall session count.

This repository contains information about PPTC benchmark, data, code, and the PPTX-Match evaluation system. To evaluate your LLM or LLM-based AI assistant system, you should follow the five main steps below.

# Requirements
Please install these packages first:
```
pip install -r PPT_code/requirements.txt
```

# Registering LLM systems

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
   python3 -m fastchat.serve.openai_api_server --host localhost
   --controller-address 'http://localhost:21007' --port 8000
   ```
You can adjust the 'port id' of openai_api_server (21007), model_worker (21008), and openai_api_server (8000) based on your situation. 

# Generating PPT label file
Now we generate the label PPT files by executing the feasible API sequences and store them into your system. We don't upload them into this epository as they are too large.
You need to execute these codes:
   ```
   python3 PPT_code/main.py --prepare --dataset long
   python3 PPT_code/main.py --prepare --dataset short  
   ```
# Testing your LLM 
To test your LLM in our benchmark, you can execute this code:
   ```
   bash PPT_code/basic_run/run.sh model_name port_id evaluation_name dataset_name 
   ```
```model_name```: For closed-source LLMs, GPT-4's name is 'gpt4', ChatGPT's name is 'turbo', and Davince's name is 'text3'. 
For open-source LLMs, your LLM's name must be consistency with the name you used in step 'Launch the model worker' (e.g., 'vicuna-13b-v1.5-16k').

```port_id```: For closed-source LLMs, you can set it as '0000'. 
For open-source LLMs, you need to use the 'port_id' of openai_api_server (e.g., '8000').

```evaluation_name```: Setting it as 'tf' if you want to assess your LLM in the turn-based evaluation way.
Setting it as 'sess' if you want to assess your LLM in the session-based evaluation way.

```dataset_name```: Setting it as 'short' if you want to assess your LLM in the creating new slides task.
Setting it as 'long' if you want to assess your LLM in the editing PPT template task.

# Evaluating the task completion performance of your LLM
After the test inference process, you can run this code to do evaluation:
```
python PPT_code/main.py --eval --dataset=dataset_name --evaluation_name --model=model_name
```
This process will generate the prediction file by executing the LLM-generated API sequence and assess the prediction file in the PPTX-Match system one by one. Finally, it reports the results of average api cost, average token cost, and average accuracy ('string acc').
