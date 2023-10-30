from src import utils
from tqdm import tqdm
from src import api_doc
# def remove_dup(dataset):
#     set_name = 'Create_new_slides' if dataset == 'short' else 'Edit_PPT_template'
#     for session_path in utils.sorted_list(f'PPT_test_output/{set_name}'):
#         sess_id = int(session_path.split('_')[-1].replace('.json',''))
#         input_session = open(f'PPT_test_input/Create_new_slides/session_{sess_id}.json').read().split('\n')
#         # print(sess_id)
#         session = open(f'PPT_test_output/{set_name}/{session_path}').read().split('\n')
#         # print(len(session)-1)
#         # print(len(input_session)-1)
#         if (len(session)-1) % (len(input_session)-1) != 0:
#             print(session_path)
        

# remove_dup('short')

all_apis = api_doc.slide_APIs + api_doc.choose_APIs + api_doc.basic_APIs + api_doc.text_APIs + api_doc.picture_APIs+ api_doc.shape_APIs + api_doc.table_APIs + api_doc.chart_APIs 
all_apis = [x.name for x in all_apis]
set_name = 'Create_new_slides'


def check(pred):
    for x in pred:
        strx = x.split('(')[0]
        if not strx in all_apis:
            return 0
    return 1

def check_trigger(pred, label):
    if 'insert_table_row' in '\n'.join(pred) and 'choose_table_cell' in label:
        return 1
    if 'insert_table_row' in label and 'choose_table_cell' in '\n'.join(pred):  
        return 1
    return 0

for model in ['Baichuan-13b','Baichuan-13B-Chat','Llama-2-13b-chat-hf','WizardLM-13b']:
    cnt = 0
    print(model)
    for sess_id, session_path in enumerate(utils.sorted_list(f'PPT_test_output/{set_name}')):
        if not session_path.startswith(f'tf_lack_{model}'):
            continue
        # print(session_path)
        session = utils.parse_test_json(f'PPT_test_output/{set_name}/{session_path}')
        
        for turn_id, turn in enumerate(session):
            turn_id, instruction, label_api, reply, pred_api, pred_ppt_path, label_ppt_path, prompt_path = turn
            if ('insert_table_row' in '\n'.join(pred_api)) or ('choose_table_cell' in '\n'.join(pred_api)):
                if not check(pred_api):
                    continue
                if not check_trigger(pred_api, label_api):
                    continue
                print(pred_api)
                print(label_api)
                print('')
                cnt += 1
    print(cnt)

# tf
# Baichuan-13B-Chat
# 1
# Llama-2-13b-chat-hf
# 4
# WizardLM-13b
# 0

# robusttf
# Baichuan-13B-Chat
# 1
# Llama-2-13b-chat-hf
# 3.5
# WizardLM-13b
# 0

# robust0tf
# Baichuan-13B-Chat
# 1
# Llama-2-13b-chat-hf
# 3
# WizardLM-13b
# 0

# robust1tf
# Baichuan-13B-Chat
# 1
# Llama-2-13b-chat-hf
# 4
# WizardLM-13b
# 0

# robust2tf
# Baichuan-13B-Chat
# 1
# Llama-2-13b-chat-hf
# 3
# WizardLM-13b
# 0

# robust3tf
# Baichuan-13B-Chat
# 1
# Llama-2-13b-chat-hf
# 4
# WizardLM-13b
# 0

# noisytf
# Baichuan-13B-Chat
# 1
# Llama-2-13b-chat-hf
# 5
# WizardLM-13b
# 0

# up_tf
# Baichuan-13B-Chat
# 0
# Llama-2-13b-chat-hf
# 0
# WizardLM-13b
# 1

# lack_tf
# Baichuan-13B-Chat
# 1
# Llama-2-13b-chat-hf
# 0
# WizardLM-13b
# 2