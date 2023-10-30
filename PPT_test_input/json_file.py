import json
import jsonlines
import pdb

set_name='Create_new_slides'#'Edit_PPT_template'#'Create_new_slides'
session_labels={}
#extract_labels
with open("test/short/api_labels.txt", 'r',encoding="utf8") as file:
    content = file.read()
sessions = content.strip().split('\n\n')
for session_id,session in enumerate(sessions):
	session_labels[session_id]=[]
	lines=session.strip().split('\n')
	for line_id,line in enumerate(lines):
		session_labels[session_id].append(line)
#extract_instruction
with open("test/short/instructions.txt", 'r',encoding="utf8") as file:
    content = file.read()

sessions = content.strip().split('\n\n')
for session_id,session in enumerate(sessions):
	lines=session.strip().split('\n')
	for line_id,line in enumerate(lines):
		#pdb.set_trace()
		with jsonlines.open("PPT_test_input/{0}/session_{1}.json".format(set_name,session_id), mode='a') as writer:
			data={'Turn':line_id,'User instruction':line,'Feasible API sequence':session_labels[session_id][line_id],'Base File':f'PPT_Base_File/{set_name}/{session_id}_{line_id}.pptx','Label File':f'PPT_Label_File/{set_name}/{session_id}_{line_id}.pptx','API Lack Base File':f'PPT_Base_File/{set_name}_API_lack/{session_id}_{line_id}.pptx','API Lack Label File':f'PPT_Label_File/{set_name}_API_lack/{session_id}_{line_id}.pptx'}
		#	data=json.dumps(data,separators=(',', ':'))
		#	json_file.write(data + '\n')
			writer.write(data)
			#json.dump(data, json_file,indent=4)