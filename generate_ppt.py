from src import utils
from tqdm import tqdm
from src import ppt_executor, ppt_reader, openai_api, prompt_factor, dataset, api_selection, utils, modeling, evaluate, content_selection
import argparse
import os
from tqdm import tqdm
import jsonlines

def regenerate(ppt_assistant, args):
    set_name = 'Create_new_slides' if args.dataset == 'short' else 'Edit_PPT_template'
    utils.makedir(f'PPT_Pred_File1/{set_name}')
    utils.makedir(f'PPT_test_output1/{set_name}')
    for session_path in utils.sorted_list(f'PPT_test_output/{set_name}'):
        if not session_path.startswith(args.exp_name):
            continue

        sess_id = int(session_path.split('_')[-1].replace('.json',''))
        session = utils.parse_test_json(f'PPT_test_output/{set_name}/{session_path}')
        chat_history = []
        for turn_id, turn in tqdm(enumerate(session)):
            print(f"{sess_id}/{turn_id}")  
            turn_id, instruction, label_api, reply, pred_api, pred_ppt_path, label_ppt_path, prompt_path = turn

            if args.tf:
                base_ppt_path = f"PPT_Base_File/{set_name}/{sess_id}_{turn_id}.pptx"
                api_lack_base_ppt_path = f"PPT_Base_File/{set_name}_API_lack/{sess_id}_{turn_id}.pptx"
                if args.api_lack:
                    ppt_assistant.load_ppt(api_lack_base_ppt_path)
                    label_file = api_lack_label_ppt_path
                else:
                    ppt_assistant.load_ppt(base_ppt_path)
                    label_file = label_ppt_path

                apis = pred_api

                ppt_assistant.api_executor(apis,test=True)
                ppt_executor.save_ppt(f'PPT_Pred_File1/{set_name}/{args.exp_name}_{sess_id}_{turn_id}.pptx')
                
                with jsonlines.open(f"PPT_test_output1/{set_name}/{args.exp_name}_session_{sess_id}.json", mode='a') as writer:
                    data={'Turn':turn_id,'User instruction':instruction,'Feasible API sequence':label_api,'Reply':reply,'Pred API sequence':apis,'Pred File':f'PPT_Pred_File1/{set_name}/{args.exp_name}_{sess_id}_{turn_id}.pptx','Label File':label_file,'Prompt File':f'PPT_Prompt_File/{set_name}/{args.exp_name}_{sess_id}_{turn_id}.txt'}
                    writer.write(data)
            
            elif args.sess:
                base_ppt_path = f"PPT_Base_File/{set_name}/{sess_id}_{turn_id}.pptx"
                api_lack_base_ppt_path = f"PPT_Base_File/{set_name}_API_lack/{sess_id}_{turn_id}.pptx"
                if args.api_lack:
                    if turn_id == 0:
                        ppt_assistant.load_ppt(api_lack_base_ppt_path)
                    label_file = api_lack_label_ppt_path
                else:
                    if turn_id == 0:
                        ppt_assistant.load_ppt(base_ppt_path)
                    label_file = label_ppt_path

                apis = pred_api
                ppt_assistant.api_executor(apis,test=True)
                ppt_executor.save_ppt(f'PPT_Pred_File1/{set_name}/{args.exp_name}_{sess_id}_{turn_id}.pptx')

                with jsonlines.open(f"PPT_test_output1/{set_name}/{args.exp_name}_session_{sess_id}.json", mode='a') as writer:
                    data={'Turn':turn_id,'User instruction':instruction,'Feasible API sequence':label_api,'Reply':reply,'Pred API sequence':apis,'Pred File':f'PPT_Pred_File1/{set_name}/{args.exp_name}_{sess_id}_{turn_id}.pptx','Label File':label_file,'Prompt File':f'PPT_Prompt_File/{set_name}/{args.exp_name}_{sess_id}_{turn_id}.txt'}
                    writer.write(data)



# set_name = 'Create_new_slides'
# for sess_id, session_path in enumerate(utils.sorted_list(f'PPT_test_output/{set_name}')):
#     if not session_path.startswith('tf_up_WizardLM-13b'):
#         continue
#     print(session_path)
#     session = utils.parse_test_json(f'PPT_test_output/{set_name}/{session_path}')
#     for turn_id, turn in tqdm(enumerate(session)):
#         turn_id, instruction, label_api, reply, pred_api, pred_ppt_path, label_ppt_path, prompt_path = turn
#         print(pred_api)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    # PPT assistant
    parser.add_argument("--data_path", default="test", type=str,
                        help="The data path to load the instructions")
    parser.add_argument("--dataset", default="short", type=str,
                        help="short/long")
    parser.add_argument("--model_id", default="None", type=str,
                        help="short/long")
    parser.add_argument("--user_path", default='./PPT_assistant_json/', type=str,
                        help="short/long")
    #/home/v-yiduoguo/PPT_assistant_json/
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
    regenerate(ppt_assistant, args)

    # if args.prepare:
    #     prepare_data(ppt_assistant, args)
    #     exit(0)
    # if args.test:
    #     test(ppt_assistant, args)
    #     exit(0)
    # if args.eval:
    #     # evaluate.check_eval(args)
    #     evaluate.eval(args)
    #     # evaluate.get_error_case(args)
    #     exit(0)