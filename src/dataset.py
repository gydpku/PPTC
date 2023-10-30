import os
import json

def load_data(path, dataset, args):
    if args.robust:
        instruction_path = os.path.join(path, dataset, f'robust{args.robust_num}.txt')
    elif args.noisy:
        instruction_path = os.path.join(path, dataset, 'noisy.txt')
    else:
        instruction_path = os.path.join(path, dataset, 'instructions.txt')
    label_path = os.path.join(path, dataset, 'api_labels.txt')

    instructions = []
    labels = []

    with open(instruction_path, 'r') as f:
        lines = f.read()
        dialogues = lines.strip().split('\n\n')
        for dialogue in dialogues:
            ins = dialogue.split('\n')
            ins = [x.strip() for x in ins if x!='']
            instructions.append(ins)
        
    with open(label_path, 'r') as f:
        lines = f.read()
        dialogue_labels = lines.strip().split('\n\n')
        for dialogue_label in dialogue_labels:
            apis = dialogue_label.split('\n')
            api_list = [x.strip(';').split(';') for x in apis]
            labels.append(api_list)
    
    return instructions, labels

def load_data_json(path, dataset):
    instructions = []
    labels = []
    ppt_labels = []

    dir = 'Create_new_slides' if dataset == 'short' else 'Edit_PPT_template'
    read_path = os.path.join(path,dir)
    for json_file in sorted(os.listdir(read_path),key=lambda x:int(x.split('_')[1].split('.')[0])):
        if json_file.endswith('.json'):
            print(json_file)
            text = open(os.path.join(read_path,json_file)).read()
            jsons = text.split('\n')[:-1]
            session_instruction = []
            session_api_label = []
            session_ppt_label = []
            for json_line in jsons:
                parsed_data = json.loads(json_line)

                turn = parsed_data['Turn']
                user_instruction = parsed_data['User instruction']
                api_sequence = parsed_data['Feasible API sequence']
                label_file = parsed_data['Label File']

                print(turn)
                print(user_instruction)
                print(api_sequence)
                print(label_file)

                # turns.append([turn,user_instruction,api_sequence,label_file])

                instructions.append(user_instruction)
                labels.append(api_sequence)

        

if __name__ == '__main__':
    load_data_json("json_file", "long")