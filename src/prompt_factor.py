system_prompt = """You are an AI assistant to help user to operate PowerPoint and editing the contents.
"""
API_list_prompt = """Now, you have access to a list of PowerPoint APIs with the following functions: 
{0}

"""
PPT_content_prompt = """You and user are working together to edit this PPT. User may refer to the content in it. All the contents are:
<Begin of PPT>
{0}<End of PPT>
Currently you are at page {1}
"""
instruction_following_prompt = """Please finish user instruction with the functions you have.
Don't generate instructions beyond what the user has instructed. 
Don't guess what the user may instruct in the next step and generete API for them.
Don't use python loop to call API like 'for i in range(n), ...'. You can only call API once in one line.
Don't use the API that is not in the API list.
Expected input parameters of API () should be numerical values, rather than using 'slide_id' or any other non-numeric input. 
If the user does not specify the page to be modified, you can directly start using the APIs without having to navigate to other pages.

You need to generate code which can finish user instruction. The multiple lines of code must start with <code> and end with </code> such as:
<code>
API();
API();
</code>

For example, if the user instruction is "create a slide", then the answer should be:
<code>
create_slide();
</code>

"""
chat_prompt = """The user and the you take turns making statements. Human statements start with ¬Human¬ and AI assistant statements start with ¬AI¬. Complete the transcript in exactly that format, without commentary.
¬User¬
Hello!
¬AI¬
Hi there! How can I help you?
{0}
¬User¬
{1}
¬AI¬
"""
def get_instruction_to_API_code_prompt(selected_API, ppt_content, chat_history, instruction, ask_less_question=False, current_page=1):
    if ask_less_question:
        instruction += ". You must surround your answer start with <code> and end with </code>."
    prompt = system_prompt +API_list_prompt.format(selected_API) + PPT_content_prompt.format(ppt_content, current_page)+instruction_following_prompt + chat_prompt.format("\n".join(chat_history), instruction)
    return prompt

Information_selection_prompt = """You are an AI assistant for PowerPoint. Your task is to determine the type of information needed to fulfill the user's query. 
Here are the possible types of information the user may be asking for: [text, style, position].
To assist the user, you must output which types of information are required to fulfill the user's request. 
Use the following format to indicate which items are needed:
text=0, style=0, position=0
where 1 means the item is needed, and 0 means it is not needed.
Here is an example of a user query:
'The font size of the content is too small. Please increase it to 20
Highlight the title and the first sentence of the content'
To fulfill this request, the AI assistant would need to modify the font style instead of the words of the content and title.
Therefore, the output would be: text=0, style=1, position=0
Here is another example query:
'Insert the following text into the content part: "Machine learning is an application of artificial intelligence (AI)."
Move the text to the top left corner of the slide.'
To fulfill this request, the AI assistant would need to change the text of the content and know the position to move the text. 
Therefore, the output would be: text=1, style=0, position=1
Here is some hint:
1. You should output without any explanation.
2. When changing the style of the text, content or title, you don't need to change the text itself, so you don't need the text information.
Here is the query:
'{0}'
The output is:\n
"""
Shape_selection_prompt = """You are an AI assistant for PowerPoint. Your task is to determine the type of shape needed to fulfill the user's query. 
Here are the possible types of shape the user may be asking for: [title, content, picture, table, chart, textbox, shape].
To assist the user, you must output which types of shape are required to fulfill the user's request. 
Use the following format to indicate which items are needed: title=1, content=1, picture=0, table=1, chart=0, textbox=1, shape=0
where 1 means the item is needed, and 0 means it is not needed.
Here is an example of a user query:
'The font size of the content is too small. Please increase it to 20
Highlight the title and the first sentence of the content'
To fulfill this request, the AI assistant would need to modify the content and title on the current slide.
Therefore, the output would be: title=1, content=1, picture=0, table=0, chart=0, textbox=1, shape=0
Here is another example query:
'Change the font style of the textbox to Verdana
That seems much better. Add a picture related to machine learning to the slide
create a table'
To fulfill this request, the AI assistant would need to modify the textbox font style, add a picture and table on the current slide. 
Therefore, the output would be: title=0, content=0, picture=1, table=1, chart=0, textbox=1, shape=0
Here is some hint:
1. You should output without any explanation.
2. Anything related to text is related to textbox.
Here is the query:
'{0}'
The output is:\n"""


PPT_content_selection_prompt = """You are an AI assistant for PowerPoint. Your task is to determine what kind of content is necessary to fulfill the user's instruction.
You have an API to extract the content, please call the get_content api with correct parameters to fulfill the user's instruction.
You need to extract the minimum information neecessary to fulfill user's query.

get_content(
    need_text: Indicates whether text information is required. The text information encompasses text in title, content, textbox, table, chart, and shape. This parameter is particularly useful when inserting or modifying text of title, content, textbox, table, chart, and shape, or when information about these objects is essential.
    need_style: Indicates whether style information is required. Style information includes attributes like font type, font size, color, background color, line space, bold, undeline, italic and other visual aspects of objects like rotation. This is useful when changing the appearance of text or objects or when information about an object's appearance is essential.
    need_position: Indicates whether position information is required. The position details encompass an object's height, width, and its left and top positions. This is crucial when moving objects or altering an object's size.
    need_title: Determines if information related to the title is required.
    need_content: Determines if information related to the content is required.
    need_picture: Determines if information related to the picture is required.
    need_table: Determines if information related to the table is required.
    need_chart: Determines if information related to the chart is required.
    need_textbox: Determines if information related to the textbox is required.
    need_shape: Determines if information related to the shapes (rectangle, right arrow, rounded rectangle, triangle, callout, cloud, star, circle) is required.
)
Where the parameters are either 1 (needed) or 0 (not needed).
You should only answer with calling get_content() with the right parameters.

For example:

Instruction: 
Increase the font size of the content to 20. 
Explanation: 
For information, style information (font size) is needed. 
For objects, content is needed.
Answer:
get_content(need_text=1,need_style=1,need_position=0,need_title=0,need_content=1,need_picture=0,need_table=0,need_chart=0,need_textbox=0,need_shape=0)

Instruction: 
Move the picture on slide 2 to right and color the rectangle yellow.
Explanation:
For information, style information (color) and position information (moving objects) are needed.
For objects, shape (rectangle) and picture are needed.
Answer:
get_content(need_text=0,need_style=1,need_position=1,need_title=0,need_content=0,need_picture=1,need_table=0,need_chart=0,need_textbox=0,need_shape=1)

Instruction: 
Change the content to "hello". Insert a table with two rows and two columns. 
Explanation: 
For information, text information (change text in content) is needed. 
For objects, content and table are needed.
Answer:
get_content(need_text=1,need_style=0,need_position=0,need_title=0,need_content=1,need_picture=0,need_table=1,need_chart=0,need_textbox=0,need_shape=0)

Given the instruction, output the Answer without Explanation:
Instruction:
{0}
Answer:"""

# query_decomposition_prompt = """You task is to decompose the user query into a list of atmoic queries that can be done in one step.
# Here are some examples:
# query: Create a new slide and add a title  "Company Profile"
# decomposed query:
# <query>
# Create a new slide
# Add a title  "Company Profile"
# </query>
# query: Change the font style of the title to "Calibri Light" and the font size to 40
# decomposed query:
# <query>
# Change the font style of the title to "Calibri Light"
# Change the font size to 40
# </query>
# query: Move the table to the top left corner of the slide.
# decomposed query:
# <query>
# Move the table to the top left corner of the slide.
# </query>
# query: Create a table with four columns and 2 rows. Insert "Guangdong","Beijing", "Shanghai" and "Hainan" in the first row. Insert "34%", "36%", "20%", "10%" in the second row.
# decomposed query:
# <query>
# Create a table with four columns and 2 rows.
# Insert "Guangdong","Beijing", "Shanghai" and "Hainan" in the first row.
# Insert "34%", "36%", "20%", "10%" in the second row.
# </query>
# query: Create three new slides. And name their titles: "Project Scope", "Project Timeline", and "Project Budget" respectively.
# decomposed query:
# <query>
# Create a slide.
# Name the title "Project Scope".
# Create a slide.
# Name the title "Project Timeline".
# Create a slide.
# Name the title "Project Budget".
# </query>
# Here is some hint:
# Don't generate instructions beyond what the user has instructed. 
# Don't guess what the user may instruct in the next step and generete API for them.
# Here is the real user query, you only need to output the answer without generating new queries or explanations.
# query: {}
# decomposed query:
# <query>"""

# query_decomposition_prompt = """Your task is to decompose user queries into atomic queries that can be done in one step. 
# Examples: 
# Name the title as "Company Profile". Insert the content "Hello"
# <decomposed>
# Insert title "Company Profile".
# Insert content "Hello".
# </decomposed>
# Change the font style of the title to "Calibri Light" and the font size to 40
# <decomposed>
# Change the font style of the title to "Calibri Light".
# Change the font size to 40.
# </decomposed>
# Create a table with four columns and 2 rows. Insert "Guangdong","Beijing", "Shanghai" and "Hainan" in the first row. Insert "34%", "36%", "20%", "10%" in the second row.
# <decomposed>
# Insert a table with four columns and 2 rows.
# Insert "Guangdong","Beijing", "Shanghai" and "Hainan" in the first row.
# Insert "34%", "36%", "20%", "10%" in the second row.
# </decomposed>
# Create three new slides. And name their titles: "Project Scope", "Project Timeline", and "Project Budget" respectively.
# <decomposed>
# Create a slide.
# Insert title "Project Scope".
# Create a slide.
# Insert title "Project Timeline".
# Create a slide.
# Insert title "Project Budget".
# </decomposed>
# Insert a new chart and choose the line chart type with the following data, Fujian, Shanghai, Beijing in the X and 120, 140, 110 in the Y.
# <decomposed>
# Insert a line chart with the following data, Fujian, Shanghai, Beijing in the X and 120, 140, 110 in the Y.
# </decomposed>
# Hints:
# - Only generate instructions based on user's query.
# - Do not predict user's next query.
# - Do not create slide if the user does not ask for it.
# - Do not add instructions if the user does not ask for it, be loyal to the user's query.


# {0}
# <decomposed>"""


### for small
# query_decomposition_prompt = """You are a PPT assistant. Your task is to decompose user queries into small easier steps. 
# Examples: 
# Make all the pictures to slide left on slide 4,5, Change the first textbox to "hello" on slide 2 and insert note "hello".
# <decomposed>
# Make all the pictures to slide left on slide 4.
# Make all the pictures to slide left on slide 5.
# Change the first textbox to "hello" on slide 2.
# Insert note "hello" on slide 2.
# </decomposed>

# Change the font style of the textboxes to "Calibri Light" and the font size to 40 on slide 3, move pictures on first two slides to right.
# <decomposed>
# Change the font style of the textboxes to "Calibri Light" on slide 3.
# Change the font size of textboxes to 40 on slide 3.
# Move pictures to right on slide 0.
# Move pictures to right on slide 1.
# </decomposed>

# Create a table with four columns and 2 rows. Insert "Guangdong","Beijing", "Shanghai" and "Hainan" in the first row. Insert "34%", "36%", "20%", "10%" in the second row.
# <decomposed>
# Insert a table with four columns and 2 rows.
# Insert "Guangdong","Beijing", "Shanghai" and "Hainan" in the first row.
# Insert "34%", "36%", "20%", "10%" in the second row.
# </decomposed>
# Hints:
# - Only generate instructions based on user's query.
# - Do not predict user's next query.
# - Do not create slide if the user does not ask for it.
# - Do not add instructions if the user does not ask for it, be loyal to the user's query.


# {0}
# <decomposed>"""

query_decomposition_prompt = """You are a PPT Assistant. Your main responsibility is to decompose user queries into more straightforward actionable steps. 
You need to decompose instructions to several decomposed instructions. The decomposed instructions should be surrounded by <d> and </d> such as:
<d>
Decomposed Instruction 1
Decomposed Instruction 2
</d>

For example:

Instruction: Move to the second page, create a new slide and insert "hello" to the content on it. Underline it.  
<d>
Move to slide 1.
Create a new slide.
Insert "hello" to the content on the current slide.
Underline the content on the current slide.
</d>

Instruction: Insert "Nice to meet you, too . " to the first textbox on slide 4,5 and "hello." to content on the first two slides. 
<d>
Insert "Nice to meet you, too . " to the first textbox on slide 4.
Insert "Nice to meet you, too . " to the first textbox on slide 4.
Insert "hello." to content on slide 0.
Insert "hello." to content on slide 1.
</d>

Instruction: Create three slides and insert a table with four columns and 2 rows on the third slide. Then Insert "Guangdong","Beijing", "Shanghai" and "Hainan" in the first row. Move all the pictures to slide left.
<d>
Create three slides.
Insert a table with four columns and 2 rows on slide 2.
Insert "Guangdong","Beijing", "Shanghai" and "Hainan" in the first row in the table on slide 2.
Move all the pictures to slide left on slide 2.
</d>

Instruction: Change background color to white, insert a shape of red circle on all slides.
<d>
Change background color to white on all slides.
Insert a red circle all slides.
</d>

Given the following instruction, decompose it:
Instruction: {0}
<d>"""

# For the first column, fill it with "Importance" and set the font size to 18 and the color to light blue.
# make_parallel_prompt = """"""
# make_noisy_prompt = """

instruction_following_prompt2 = """You are an AI assistant to help user to operate PowerPoint and editing the contents.
Given you the user instruction:'{0}', you can complete it based on the following APIs and PPT file content.
Currently you are at page {1}.
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
{2}

All the PPT contents are:
<Begin of PPT>
{3}
<End of PPT>"""

chat_prompt = """The user and the you take turns making statements. Human statements start with ¬Human¬ and AI assistant statements start with ¬AI¬. Complete the transcript in exactly that format, without commentary.
¬User¬
Hello!
¬AI¬
Hi there! How can I help you?
{0}
¬User¬
{1}
¬AI¬
"""

def get_instruction_to_API_code_prompt2(selected_API, ppt_content, chat_history, instruction, ask_less_question=False, current_page=1):
    instruction_line = instruction + ". Surrounding your answer with <code> and </code>." if instruction == "" or instruction[-1]!='.' else instruction + " Surrounding your answer with <code> and </code>."
    prompt = instruction_following_prompt2.format(instruction,current_page,selected_API,ppt_content) + "\n\n" + chat_prompt.format("\n".join(chat_history), instruction_line)
    return prompt