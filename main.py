from src import ppt_executor, ppt_reader, openai_api, prompt_factor, dataset, api_selection, utils, modeling, evaluate, content_selection
import argparse
import os
from tqdm import tqdm
import jsonlines

def prepare_data(ppt_assistant, args):
    instructions, labels = dataset.load_data(args.user_path+args.data_path, args.dataset, args)
    print(f"#Dialogues: {len(instructions)}")
    for idx, dialogue in enumerate(instructions): 
        if args.dataset == 'long':
            ppt_assistant.load_ppt(os.path.join(args.user_path+'long_slides',f'{idx}.pptx'))
        else:
            ppt_assistant.load_ppt(None)
        
        set_name = 'Edit_PPT_template' if args.dataset == 'long' else 'Create_new_slides'
        
        if args.api_lack:
            utils.makedir(args.user_path+f"PPT_Base_File/{set_name}_API_lack/")
            utils.makedir(args.user_path+f"PPT_Label_File/{set_name}_API_lack/")
        else:
            utils.makedir(args.user_path+f"PPT_Base_File/{set_name}/")
            utils.makedir(args.user_path+f"PPT_Label_File/{set_name}/")

        for step, instruction in enumerate(dialogue):     
            instruction = instruction.split("##")[0]
            label_apis = utils.merge_list(labels[idx][:step])

            if args.dataset == 'long':
                ppt_assistant.load_ppt(os.path.join(args.user_path+'long_slides',f'{idx}.pptx'))
            else:
                ppt_assistant.load_ppt(None)
            ppt_assistant.api_executor(label_apis,test=False)
            if args.api_lack:
                ppt_executor.save_ppt(args.user_path+f"PPT_Base_File/{set_name}_API_lack/{idx}_{step}.pptx")
            else:
                ppt_executor.save_ppt(args.user_path+f"PPT_Base_File/{set_name}/{idx}_{step}.pptx")

            ppt_assistant.api_executor(labels[idx][step],test=False)

            if args.api_lack:
                ppt_executor.save_ppt(args.user_path+f"PPT_Label_File/{set_name}_API_lack/{idx}_{step}.pptx")
            else:
                ppt_executor.save_ppt(args.user_path+f"PPT_Label_File/{set_name}/{idx}_{step}.pptx")
            print(f"{idx}/{step} done!")

def test(ppt_assistant, args):
    set_name = 'Create_new_slides' if args.dataset == 'short' else 'Edit_PPT_template'
    utils.makedir(args.user_path+f'PPT_Pred_File/{set_name}')
    utils.makedir(args.user_path+f'PPT_Prompt_File/{set_name}')
    for sess_id, session_path in enumerate(utils.sorted_list(args.user_path+f'PPT_test_input/{set_name}')):
        session = utils.parse_train_json(args.user_path+f'PPT_test_input/{set_name}/{session_path}')
        chat_history = []
        for turn_id, turn in tqdm(enumerate(session)):
            print(f"{sess_id}/{turn_id}")  
            if args.resume:

                if args.tf and os.path.exists(args.user_path+f'PPT_Pred_File/{set_name}/{args.exp_name}_{sess_id}_{turn_id}.pptx'):

                    print('Exists!')
                    continue 
                if args.sess and os.path.exists(args.user_path+f'PPT_Pred_File/{set_name}/{args.exp_name}_{sess_id}_{len(session)-1}.pptx'):
                    print('Exists!')
                    continue 
            turn_id, instruction, label_api, base_ppt_path, label_ppt_path, api_lack_base_ppt_path, api_lack_label_ppt_path = turn
            if turn_id == 0 and args.sess:
                if args.api_lack:
                    ppt_assistant.load_ppt(args.user_path+api_lack_base_ppt_path)
                    label_file = api_lack_label_ppt_path
                else:
                    ppt_assistant.load_ppt(args.user_path+base_ppt_path)
                    label_file = label_ppt_path
            splitted_instruction = instruction.split("##")[0]
            if args.tf:
                if args.api_lack:
                    ppt_assistant.load_ppt(args.user_path+api_lack_base_ppt_path)
                    label_file = api_lack_label_ppt_path
                else:
                    ppt_assistant.load_ppt(args.user_path+base_ppt_path)
                    label_file = label_ppt_path
                ppt_assistant.load_chat_history([x[0] for x in chat_history],[x[1].strip(';').split(';') for x in chat_history])
                prompt, reply = ppt_assistant.chat(splitted_instruction, ppt_path=args.user_path+base_ppt_path, verbose=False)
                apis = utils.parse_api(reply)
                ppt_assistant.api_executor(apis,test=True)
                
                ppt_executor.save_ppt(args.user_path+f'PPT_Pred_File/{set_name}/{args.exp_name}_{sess_id}_{turn_id}.pptx')
                utils.write_lines([prompt],args.user_path+f'PPT_Prompt_File/{set_name}/{args.exp_name}_{sess_id}_{turn_id}.txt')
                #import pdb
                #pdb.set_trace()
                utils.makedir(f"PPT_test_output/{set_name}")
                with jsonlines.open(args.user_path+f"PPT_test_output/{set_name}/{args.exp_name}_session_{sess_id}.json", mode='a') as writer:
                    data={'Turn':turn_id,'User instruction':instruction,'Feasible API sequence':label_api,'Reply':reply,'Pred API sequence':apis,'Pred File':f'PPT_Pred_File/{set_name}/{args.exp_name}_{sess_id}_{turn_id}.pptx','Label File':label_file,'Prompt File':f'PPT_Prompt_File/{set_name}/{args.exp_name}_{sess_id}_{turn_id}.txt'}
                    writer.write(data)
                chat_history.append([splitted_instruction, label_api])
            
            elif args.sess:
                prompt, reply = ppt_assistant.chat(instruction, ppt_path=None, verbose=False)
                apis = utils.parse_api(reply)
                ppt_assistant.api_executor(apis,test=True)

                ppt_executor.save_ppt(args.user_path+f'PPT_Pred_File/{set_name}/{args.exp_name}_{sess_id}_{turn_id}.pptx')
                utils.write_lines([prompt],args.user_path+f'PPT_Prompt_File/{set_name}/{args.exp_name}_{sess_id}_{turn_id}.txt')

                with jsonlines.open(args.user_path+f"PPT_test_output/{set_name}/{args.exp_name}_session_{sess_id}.json", mode='a') as writer:
                    data={'Turn':turn_id,'User instruction':instruction,'Feasible API sequence':label_api,'Reply':reply,'Pred API sequence':apis,'Pred File':f'PPT_Pred_File/{set_name}/{args.exp_name}_{sess_id}_{turn_id}.pptx','Label File':label_file,'Prompt File':f'PPT_Prompt_File/{set_name}/{args.exp_name}_{sess_id}_{turn_id}.txt'}
                    writer.write(data)

def test_planning(ppt_assistant):
    instructions, labels = dataset.load_data(args.data_path, args.dataset)
    f = open(f'test_system/planning_{args.dataset}.txt','a+')
    for idx, dialogue in tqdm(enumerate(instructions)):
        for step, instruction in enumerate(dialogue):
            instruction = instruction.split("##")[0]
            try:
                planned = ppt_assistant.planner(instruction)
                f.write(f'{idx}/{step}\n')
                f.write(instruction+'\n')
                f.write(str(planned)+'\n\n')
                f.flush()
            except:
                pass

def test_api_selection(ppt_assistant):
    instructions, labels = dataset.load_data(args.data_path, args.dataset)
    f = open(f'test_system/api_selection_{args.api_topk}_{args.dataset}.txt','a+')
    cnt = 0
    for idx, dialogue in tqdm(enumerate(instructions)):
        for step, instruction in enumerate(dialogue):
            label_apis = labels[idx][step]
            instruction = instruction.split("##")[0]
            # instructions = ppt_assistant.planner(instruction)
            # selected_apis = []
            # for ins in instructions:
            #     selected_apis.extend(ppt_assistant.api_selector(ins))
            selected_apis = ppt_assistant.api_selector(instruction)
            selected_apis = [x.name for x in selected_apis]
            for xx in label_apis:
                if ('align_slide' in xx.split('(')[0]) or (xx.split('(')[0] in ['set_left','set_right','set_top','set_bottom']) or ('corner' in xx.split('(')[0]):
                    continue
                if not xx.split('(')[0] in selected_apis:
                    f.write(f'{idx}/{step}\n')
                    f.write(instruction+'\n')
                    f.write(xx.split('(')[0]+'\n')
                    f.write(str(selected_apis)+'\n\n')
                    f.flush()
                    cnt += 1
    print(cnt)
    
def test_content_selection(ppt_assistant):
    instructions, labels = dataset.load_data(args.data_path, args.dataset)
    f = open(f'test_system/content_selection_{args.dataset}.txt','a+')
    for idx, dialogue in tqdm(enumerate(instructions)):
        for step, instruction in enumerate(dialogue):
            instruction = instruction.split("##")[0]
            prompt = prompt_factor.PPT_content_selection_prompt.format(instruction)
            reply = openai_api.query_azure_openai(prompt, model='turbo')
            f.write(f'{idx}/{step}\n')
            f.write(instruction+'\n')
            f.write(reply+'\n\n')


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    # PPT assistant
    parser.add_argument("--data_path", default="test", type=str,
                        help="The data path to load the instructions")
    parser.add_argument("--dataset", default="short", type=str,
                        help="short/long")
    parser.add_argument("--model_id", default="None", type=str,
                        help="short/long")
    parser.add_argument("--user_path", default='./PPTC/', type=str,
                        help="the user storage file path ")
    parser.add_argument("--save_path", default="test_pptx_data", type=str,
                        help="the path to save the intermediate ppts.")
    
    # mode
    parser.add_argument("--prepare", default=False, action='store_true',
                        help='whether to prepare the data for the model')
    parser.add_argument("--eval", default=False, action='store_true',
                        help='whether to evaluate the pptx file generated by the model')
    parser.add_argument("--test", default=False, action='store_true',
                        help='whether to test on the instruction data loaded from data_path')
    parser.add_argument("--tf", default=False, action='store_true',
                        help='whether to use teacher forcing mode')
    parser.add_argument("--sess", default=False, action='store_true',
                        help='whether to test from session level')
    parser.add_argument("--resume", default=False, action='store_true',
                        help='whether to continue generation from the last unfinished instruction')
    
    # modeling
    parser.add_argument("--model", default="turbo",type=str,
                        help="turbo/gpt4/text3") 
    parser.add_argument("--planning", default=False, action='store_true',
                        help="whether to apply the planning module") 
    parser.add_argument("--api_selection", default=False, action='store_true',
                        help="whether to apply the api selection module") 
    parser.add_argument("--api_topk", default=10, type=int,
                        help="How many apis to retrieve from the api pool") 
    parser.add_argument("--content_selection", default=False, action='store_true',
                        help="whether to apply the shape selection module") 
    
    # api update/lack
    parser.add_argument("--api_lack", default=False, action='store_true',
                        help='whether to test in the api lack setting')
    parser.add_argument("--api_update", default=False, action='store_true',
                        help='whether to test in the api update setting')
    parser.add_argument("--second", default=False, action='store_true',
                        help='second test')

    parser.add_argument("--robust", default=False, action='store_true',
                        help='whether to test in robust data')
    parser.add_argument("--robust_num", default=0, type=int,
                        help="which robusted data") 
    parser.add_argument("--noisy", default=False, action='store_true',
                        help='whether to test in noisy data')

    args = parser.parse_args()

    args.exp_name = utils.prepare_exp_name(args)
    args.save_path = os.path.join(args.save_path,args.dataset)
    api_selection.prepare_embedding(args)
    ppt_assistant = modeling.PPT_assistant(args)

    # test_content_selection(ppt_assistant)

    if args.prepare:
        prepare_data(ppt_assistant, args)
        exit(0)
    if args.test:
        test(ppt_assistant, args)
        exit(0)
    if args.eval:
        # evaluate.check_eval(args)
        evaluate.eval(args)
        # evaluate.get_error_case(args)
        exit(0)
