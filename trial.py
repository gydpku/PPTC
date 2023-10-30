import json
json_path = 'PPT_test_input/Create_new_slides/session_0.json'
def parse_train_json(path):
    turns = []
    with open(path, 'r') as file:
        for line in file:
            data = json.loads(line)
            turn_id, instruction, label_api, base_ppt_path, label_ppt_path, api_lack_label_ppt_path = data['Turn'],data['User instruction'],data['Feasible API sequence'],data['Base File'],data['Label File'],data['API Lack Label File']
            turns.append([turn_id, instruction, label_api, base_ppt_path, label_ppt_path, api_lack_label_ppt_path])
    return turns

def parse_test_json(path):
    turns = []
    with open(path, 'r') as file:
        for line in file:
            data = json.loads(line)
            turn_id, instruction, label_api, reply, pred_api, pred_ppt_path, label_ppt_path, prompt_path = data['Turn'],data['User instruction'],data['Feasible API sequence'],data['Reply'],data['Pred API sequence'],data['Pred File'],data['Label File'],data['Prompt File']
            turns.append([turn_id, instruction, label_api, reply, pred_api, pred_ppt_path, label_ppt_path, prompt_path])
    return turns

turns = parse_train_json(json_path)
print(len(turns))
for x in turns[0]:
    print(x)