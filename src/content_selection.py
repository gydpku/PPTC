from .openai_api import *
from .prompt_factor import *

def select_information_type(query,args):
    prompt = Information_selection_prompt.format(query)
    answer = query_azure_openai(prompt,args.model)
    try:
        return parse_answer(answer)
    except:
        return [1, 1, 1]

def select_shape_type(query,args):
    prompt = Shape_selection_prompt.format(query)
    answer = query_azure_openai(prompt,args.model)
    try:
        return parse_answer(answer)
    except:
        return [1, 1, 1, 1, 1, 1, 1]

def parse_answer(answer):
    answer = answer.strip()
    answer = answer.split(',')
    answer = [int(i.split('=')[1]) for i in answer]
    return answer


if __name__ == '__main__':
    while 1:
        query = input("Please input your query: ")

        shape_list = ['PLACEHOLDER', 'PLACEHOLDER', 'PICTURE', 'TABLE', 'CHART', 'TEXT_BOX', 'AUTO_SHAPE']
        selected_shape_type = select_shape_type(query)
        print(selected_shape_type)
        need_shape_list = [shape_list[i] for i in range(len(shape_list)) if selected_shape_type[i] == 1]

        need_text, need_style, need_position = select_information_type(query)

        print(f"Need Shape: {need_shape_list}")
        print(f"Need Text: {need_text}")
        print(f"Need Style: {need_style}")
        print(f"Need Position: {need_position}")
    # get_contents_v2(slide_id_list=None, need_text=need_text, need_style=need_style, need_position=need_position, need_shape_list=need_shape_list)
