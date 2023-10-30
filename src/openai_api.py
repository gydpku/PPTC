import openai
import backoff
import os
import tiktoken
@backoff.on_exception(backoff.expo, openai.error.RateLimitError)
@backoff.on_exception(backoff.expo, openai.error.APIConnectionError)
def completions_with_backoff(**kwargs):
    return openai.Completion.create(**kwargs)

@backoff.on_exception(backoff.expo, openai.error.RateLimitError)
@backoff.on_exception(backoff.expo, openai.error.APIConnectionError)
def chat_with_backoff(**kwargs):
    return openai.ChatCompletion.create(**kwargs)

@backoff.on_exception(backoff.expo, openai.error.RateLimitError)
@backoff.on_exception(backoff.expo, openai.error.APIConnectionError)

def embeddings_with_backoff(**kwargs):

    openai.api_type = "azure"
    openai.api_base = "https://{your name}.openai.azure.com/"
    openai.api_version = "2022-12-01"
    openai.api_key = os.getenv("")
    openai.api_key = "your key"
    return openai.Embedding.create(**kwargs)

openai.api_base = "https://{your name}.openai.azure.com/"
openai.api_key = "your key"

def query_azure_openai(query, model = "vicuna-13b-v1.5-16k",id=None):

    if model == 'text3':
        openai.api_type = "azure"
        openai.api_version = "2023-03-15-preview"
        openai.api_key = os.getenv("")
        response = completions_with_backoff(
            engine="text-davinci-003",
            prompt=query,
            temperature=0,
            max_tokens=1000,
            top_p=0.95,
            frequency_penalty=0,
            presence_penalty=0,
            stop=["<|im_end|>", "¬User¬", "</decomposed>","</query>"]
            )
        return response["choices"][0]["text"]
    
    elif model == 'turbo':
        openai.api_type = "azure"

        openai.api_version = "2023-03-15-preview"
        openai.api_key = os.getenv("")

        prompt = "<|im_start|>system\nYou are a helpful assistant.\n<|im_end|>\n<|im_start|>user\nHello!\n<|im_end|>\n<|im_start|>assistant\nHow can I help you?\n<|im_end|>\n<|im_start|>user\n{0}\n<|im_end|>\n<|im_start|>assistant\n".format(
            query)
        response = completions_with_backoff(
            engine="gpt-35-turbo",
            prompt=prompt,
            temperature=0,
            max_tokens=1000,
            top_p=0.95,
            frequency_penalty=0,
            presence_penalty=0,
            stop=["<|im_end|>", "¬User¬", "</decomposed>","</query>"])
        return response["choices"][0]["text"]

    elif model == 'gpt4':
        openai.api_type = "azure"

        openai.api_version = "2023-03-15-preview"
        openai.api_key = os.getenv("")
        response = chat_with_backoff(
            engine="gpt-4-32k",
            messages=[
                {"role": "system", "content": "You are a helpful AI assistant."},
                {"role": "user", "content": query},
            ],
            temperature=0,
            max_tokens=1000,
            top_p=0.95,
            frequency_penalty=0,
            presence_penalty=0,
            stop=["<|im_end|>", "¬User¬", "</decomposed>","</query>"])
        return response["choices"][0]["message"]["content"]
    else:
        openai.api_key = "EMPTY"
        #if id is not None:
        openai.api_base = "http://localhost:{0}/v1".format(id)
        encoding = tiktoken.encoding_for_model("gpt-3.5-turbo")
        def truncate_text_with_token_count (text, max_tokens):
            # Get the token count using tiktoken
            num_tokens = len(encoding.encode(text))
            # token_count = tiktoken.count_tokens(text)

            if num_tokens > max_tokens:
                # Truncate the text while preserving whole words
                tokens = text.split()
                truncated_tokens = tokens[:max_tokens]
                truncated_text = ' '.join(truncated_tokens)
                return truncated_text
            return text

        truncated_input = query#truncate_text_with_token_count(query, max_context_length)

        completion = openai.ChatCompletion.create(
            model=model,
            messages=[
                {"role": "system", "content": "You are a helpful AI assistant."},
                {"role": "user", "content": truncated_input},
            ],
            temperature=0,
            top_p=0.95,

        )

        try:
            return completion.choices[0].message.content  # response['choices'][0]['message']['content']
        except:
            return ' '


def rewrite(prompt):
        response = chat_with_backoff(
            engine="gpt-4-32k",
            messages=[
                {"role": "system", "content": "You are a helpful AI assistant."},
                {"role": "user", "content": prompt},
            ],
            temperature=0.7,
            max_tokens=200
            )
        return response["choices"][0]["message"]["content"]

if __name__ == "__main__":
    prompts = """You are an AI assistant to help user to operate PowerPoint and editing the contents.
Given you the user instruction:'please create a new slide and give it a dark green background.', you can complete it based on the following APIs and PPT file content.
Currently you are at page 0
Please finish user instruction with the functions you have.
Don't generate instructions beyond what the user has instructed. 
Don't guess what the user may instruct in the next step and generete API for them.
Don't use python loop to call API. You can only call API once in one line.
If the user does not specify the page to be modified, you can directly start using the APIs without having to navigate to other pages.

You need to generate code which can finish user instruction. The multiple lines of code should be surrounded by <code> and </code> such as:
<code>
API();
API();
</code>

For example, if the user instruction is "create a slide", then the answer should be:
<code>
create_slide();
</code>

Now, you have access to a list of PowerPoint APIs with the following functions: 
API: create_slide(): This API creates a new slide.
API: move_to_previous_slide(): This API moves to the previous slide.
API: move_to_next_slide(): This API moves to the next slide.
API: move_to_slide(slide_id): This API moves to the slide with given slide id.
It takes one parameter 'slide_id', the ID of the slide to move to as a integer.
API: set_background_color(color): This API sets the background color of the slide.
It takes one parameter 'color', the color name to set as a string, such as 'red', 'purple'.
API: choose_title(): This API selects the title on the slide.
You should first call choose_title() before inserting text to or changing font attributes of the title.
API: choose_content(): This API select the content on the slide.
You should first call choose_content() before inserting text to or changing font attributes of the content.
API: choose_textbox(idx): This API selects the textbox element on the slide.
It takes one parameter, the index of textbox as integer. idx is set to 0 by default, meaning the first textbox.
You should first call choose_textbox() before inserting text to or changing font attributes of the textbox element.
API: choose_picture(idx): This API selects the picture element on the slide.
It takes one parameter, the index of textbox as integer. idx is set to 0 by default, meaning the first textbox.
You should first call choose_picture() before changing height, width, rotation of the picture element. You should not call choose_picture() before inserting picture element.
API: choose_chart(): This API selects the chart element on the slide.
You should first call choose_chart() before changing the chart. You should not call choose_chart() before inserting chart element.
API: choose_shape(shape_name): This API selects a specific shape by shape name on the slide.
It takes one parameter 'shape_name', the name of the shape to select as a string.         shape_name can be chosen from ['rectangle','right_arrow','rounded_rectangle','triangle','callout','cloud','star','circle']
You should first call choose_shape(shape_name) before you can do operations on the shape. You should not call choose_shape(shape_name) before inserting shape element.
API: choose_table(): This API selects the table element on the slide.
You should first call choose_table() before changing the table. You should not call choose_table() before inserting table element.
API: choose_table_cell(row_id, column_id): This API selects a specific cell in the table by giving row_id and column_id.
It takes two parameters, the row id and column id of the cell to select as integers. Remember the first parameter is row id, the second parameter is column id.
You should first call choose_table_cell(row_id, column_id) before inserting text into a specific cell of the table.
API: set_width(width): This API sets the width of the selected object.
It takes one parameter 'width', the width of an object in centimeters as float.
You should first choose an object before you can change the width of it.
API: set_height(height): This API sets the height of the selected object.
It takes one parameter 'height', the height of an object in centimeters as float.
You should first choose an object before you can change the height of it
API: rotate_element(angle): This API rotates the selected element by the specified angle.
It takes one parameter 'angle', the angle to rotate clockwise as integer.
You should first choose an object before you can rotate it.
API: set_fill_color(color): This API sets the fill color of the selected object after the object is chosen.
It takes one parameter 'color', the color name to set as a string, such as 'red', 'purple'.
You can set the fill color of content, title or textbox.
API: set_left(left): This API moves and changes the object's position. It sets the x position of the selected object's leftmost point.
It takes one parameter, the x position to set.
You should first choose an object before you can change the left of it
API: set_top(top): This API moves and changes the object's position. It sets the y position of the selected object's upmost point.
It takes one parameter, the y position to set.
You should first choose an object before you can change the top of it
API: insert_text(text): This API inserts text into a text frame (textbox, title, content, table).
API: insert_bullet_point(text): This API inserts a bullet point into the content.
It takes one parameter, the text of the bullet point to insert as a string.
API: insert_note(text): This API inserts a note onto the slide.
It takes one parameter, the note text to insert as a string.
API: insert_textbox(): This API inserts a textbox onto the slide.
When you need to add a caption or text under/above/left to/right to an object, you can call insert_textbox().
API: delete_text(): This API delete the text part of an object.
You should first choose content or title before you can call delete_text()
API: set_font_size(font_size): This API sets the size of the font
It can take one argument 'font_size', the font size to set as an integer.
API: set_font_color(color): This API sets the color of the font.
It takes one parameter 'color', the color name to set as a string, such as 'red', 'purple'.
API: set_font_bold(): This API sets the font to be bold.
API: set_font_italic(): This API sets the font to be italic.
API: set_font_underline(): This API sets the font to be underlined.
API: set_font_style(font_name): This API sets the font style of the selected text.
It can take one argument 'font_style', the font name as a string.
API: set_line_space(line_space_level): This API sets the line spacing of the selected text.
It can take one argument 'line_space_level', as an integer, default 0.
API: text_align_left(): This API aligns the text to left.
API: text_align_center(): This API aligns the text to center.
API: text_align_right(): This API aligns the text to right.
API: insert_picture(picture_name): This API inserts a picture onto the slide.
It takes one parameter 'picture_name', the name or description of picture as a string
API: insert_rectangle(): This API inserts a rectangle or square shape onto the slide.
API: insert_right_arrow(): This API inserts an arrow shape onto the slide.
API: insert_rounded_rectangle(): This API inserts a rounded rectangle shape onto the slide.
API: insert_triangle(): This API inserts a triangle shape onto the slide.
API: insert_callout(): This API inserts a callout shape onto the slide.
API: insert_cloud(): This API inserts a cloud shape onto the slide.
API: insert_star(): This API inserts a star shape onto the current slide.
API: insert_circle(): This API inserts a circle or oval shape into the current slide.
API: insert_table(row_num, col_num): This API inserts a table of row_num rows and col_num columns onto the current slide.
It takes two argument, the row number and the column number of the inserted table as integer. Remember the first parameter is row number and the second parameter is column number.
API: insert_table_row(row_data): This API inserts a row (list) of data into the table.
It takes one argument, the data to insert as a list of numbers or strings.
You should first call choose_table() before you can call insert_table_row(). The parameter 'row_data' should be a list of strings.
API: insert_line_chart(data, series): This API inserts a line chart onto the slide.
It takes two argument, 'data' is a list of numbers and 'series' is a list of strings.
API: insert_bar_chart(data, series): This API inserts a bar chart onto the slide.
It takes two argument, 'data' is a list of numbers and 'series' is a list of strings.
API: insert_pie_chart(data, series): This API inserts a pie chart onto the slide.
It takes two argument, 'data' is a list of numbers and 'series' is a list of strings.
API: set_chart_title(title): This API sets the title of a previously inserted chart.
It takes one argument 'title', the title to be set as a string.

All the PPT contents are:
<Begin of PPT>  
There are 1 slides with slide height 6858 and slide width 9144.  
Slide 0 with background color None:  
[Title]  
Size: height=1143, width=8229  
Text:   
  
Font Style: bold=None, italic=None, underline=None, size=None, color=None, fill=None, font style=None, line_space=None, align=None  
Visual Positions: left=457, top=274  
  
[Content]  
Size: height=4525, width=8229  
Text:   
  
Font Style: bold=None, italic=None, underline=None, size=None, color=None, fill=None, font style=None, line_space=None, align=None  
Visual Positions: left=457, top=1600  
  
<End of PPT>"""
    answer = query_azure_openai(prompts, model = "vicuna-13b-v1.5-16k")
    print(answer)
