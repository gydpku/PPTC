class API(object):
    def __init__(self, name, parameters, description,
                 parameter_description="", composition_instruction="", example="", api_desc="",
                 type="",
                 implementation=None,
                 ):
        self.name = name
        self.parameters = parameters
        self.description = description
        self.parameter_description = parameter_description
        self.composition_instruction = composition_instruction
        self.example = example
        self.api_desc = api_desc

        # self.implementation = implementation
        # self.type = type

    def __str__(self):
        infos = [f"API: {self.name}{self.parameters}: {self.description}", self.parameter_description, self.composition_instruction, self.example]
        infos = [item for item in infos if item != ""]
        return '\n'.join(infos)

# slide
slide_APIs = [
    API(name="create_slide", parameters="()", description="This API creates a new slide.",api_desc="create a slide"),
    API(name="move_to_previous_slide", parameters="()", description="This API moves to the previous slide.",api_desc="move to previous slide"),
    API(name="move_to_next_slide", parameters="()", description="This API moves to the next slide.",api_desc="move to next slide"),
    API(name="move_to_slide", parameters="(slide_id)", description="This API moves to the slide with given slide id.", 
        parameter_description="It takes one parameter 'slide_id', the ID of the slide to move to as a integer.",api_desc="move to slide x"),
    API(name="set_background_color", parameters="(color)", description="This API sets the background color of the slide.",
        parameter_description="It takes one parameter 'color', the color name to set as a string, such as 'red', 'purple'.",api_desc="background color"),
]

# choose
choose_APIs = [
    API(name="choose_title", parameters="()", description="This API selects the title on the slide.", 
        composition_instruction="You should first call choose_title() before inserting text to or changing font attributes of the title.",api_desc="choose title, name a slide"),
    API(name="choose_content", parameters="()", description="This API select the content on the slide.",  
        composition_instruction="You should first call choose_content() before inserting text to or changing font attributes of the content.",api_desc="choose content, insert text, bullet point"),
    # API(name="choose_textbox", parameters="()", description="This API selects the textbox element on the slide.", 
    #     composition_instruction="You should first call choose_textbox() before inserting text to or changing font attributes of the textbox element.",api_desc="choose textbox"),
    API(name="choose_textbox", parameters="(idx)", description="This API selects the textbox element on the slide.", 
        parameter_description="It takes one parameter, the index of textbox as integer. idx is set to 0 by default, meaning the first textbox.",
        composition_instruction="You should first call choose_textbox() before inserting text to or changing font attributes of the textbox element.",api_desc="choose textbox, insert text,"),
    API(name="choose_picture", parameters="(idx)", description="This API selects the picture element on the slide.", 
        parameter_description="It takes one parameter, the index of textbox as integer. idx is set to 0 by default, meaning the first textbox.",
        composition_instruction="You should first call choose_picture() before changing height, width, rotation of the picture element. You should not call choose_picture() before inserting picture element.",api_desc="picture, image"),
    API(name="choose_chart", parameters="()", description="This API selects the chart element on the slide.", 
        composition_instruction="You should first call choose_chart() before changing the chart. You should not call choose_chart() before inserting chart element.",api_desc="chart"),
    API(name="choose_shape", parameters="(shape_name)", description="This API selects a specific shape by shape name on the slide.", 
        parameter_description="It takes one parameter 'shape_name', the name of the shape to select as a string. \
        shape_name can be chosen from ['rectangle','right_arrow','rounded_rectangle','triangle','callout','cloud','star','circle']", 
        composition_instruction="You should first call choose_shape(shape_name) before you can do operations on the shape. You should not call choose_shape(shape_name) before inserting shape element.",
        api_desc="choose ['rectangle','right_arrow','rounded_rectangle','triangle','callout','cloud','star','circle']"),
    API(name="choose_table", parameters="()", description="This API selects the table element on the slide.",
        composition_instruction="You should first call choose_table() before changing the table. You should not call choose_table() before inserting table element.",api_desc="table, row, column"),
    API(name="choose_table_cell", parameters="(row_id, column_id)", description="This API selects a specific cell in the table by giving row_id and column_id.",
        parameter_description="It takes two parameters, the row id and column id of the cell to select as integers (id starts from 0). Remember the first parameter is row id, the second parameter is column id.",
        composition_instruction="You should first call choose_table_cell(row_id, column_id) before inserting text into a specific cell of the table.",api_desc="table, row, column, cell"),
]

# basic
basic_APIs = [
    API(name="set_width", parameters="(width)", description="This API sets the width of the selected object.",
        parameter_description="It takes one parameter 'width', the width of an object in centimeters as float.",
        composition_instruction="You should first choose an object before you can change the width of it.",api_desc="width of picture and shapes"),
    API(name="set_height", parameters="(height)", description="This API sets the height of the selected object.",
        parameter_description="It takes one parameter 'height', the height of an object in centimeters as float.",
        composition_instruction="You should first choose an object before you can change the height of it",api_desc="height of picture and shapes"),  
    API(name="rotate_element", parameters="(angle)", description="This API rotates the selected element by the specified angle.",
        parameter_description="It takes one parameter 'angle', the angle to rotate clockwise as integer.",
        composition_instruction="You should first choose an object before you can rotate it.",api_desc="rotate"),
    API(name="set_fill_color", parameters="(color)", description="This API sets the fill color of the selected object after the object is chosen.",
        parameter_description="It takes one parameter 'color', the color name to set as a string, such as 'red', 'purple'.",
        composition_instruction="You can set the fill color of content, title or textbox.",api_desc="fill color: red, purple, blue, green, yellow, orange"),
    # ?
    # API(name="align_top_right_corner", parameters="()", description="This API moves the selected object to the top right corner of the slide.",
    #     composition_instruction="You should first choose an object before you can call align_top_right_corner()."),
    # API(name="align_top_left_corner", parameters="()", description="This API moves the selected object to the top left corner of the slide.",
    #     composition_instruction="You should first choose an object before you can call align_top_left_corner()."),
    # API(name="align_bottom_right_corner", parameters="()", description="This API moves the selected object to the bottom right corner of the slide.",
    #     composition_instruction="You should first choose an object before you can call align_bottom_right_corner()."),
    # API(name="align_bottom_left_corner", parameters="()", description="This API moves the selected object to the bottom left corner of the slide.",
    #     composition_instruction="You should first choose an object before you can call align_bottom_left_corner()."),
    # API(name="align_slide_top", parameters="()", description="This API moves the selected object to the top side of the slide.",
    #     composition_instruction="You should first choose an object before you can call align_slide_top()."),
    # API(name="align_slide_bottom", parameters="()", description="This API moves the selected object to the bottom side of the slide.",
    #     composition_instruction="You should first choose an object before you can call align_slide_bottom()."),
    # API(name="align_slide_left", parameters="()", description="This API moves the selected object to the left side of the slide.",
    #     composition_instruction="You should first choose an object before you can call align_slide_left()."),
    # API(name="align_slide_right", parameters="()", description="This API moves the selected object to the right side of the slide.",
    #     composition_instruction="You should first choose an object before you can call align_slide_right()."),
    # API(name="align_slide_center", parameters="()", description="This API moves the selected object to the center of the slide.",
    #     composition_instruction="You should first choose an object before you can call align_slide_center()."),
    # ??
    API(name="set_left", parameters="(left)", description="This API moves and changes the object's position. It sets the x position of the selected object's leftmost point.",
        parameter_description="It takes one parameter, the x position to set.",composition_instruction="You should first choose an object before you can change the left of it",api_desc="move an object, left, middle, center, right"),
    API(name="set_top", parameters="(top)", description="This API moves and changes the object's position. It sets the y position of the selected object's upmost point.",
        parameter_description="It takes one parameter, the y position to set.",composition_instruction="You should first choose an object before you can change the top of it",api_desc="move an object, top, middle, center, bottom"),  
]

# text
text_APIs = [
    API(name="insert_text", parameters="(text)", description="This API inserts text into a text frame (textbox, title, content, table).",api_desc='insert or name text, title, content, table, textbox with given text ""'),
    API(name="insert_bullet_point", parameters="(text)", description="This API inserts a bullet point into the content.",
        parameter_description="It takes one parameter, the text of the bullet point to insert as a string.",api_desc="bullet point"),
    API(name="insert_note", parameters="(text)", description="This API inserts a note onto the slide.",
        parameter_description="It takes one parameter, the note text to insert as a string.",api_desc="note"),
    API(name="insert_textbox", parameters="()", description="This API inserts a textbox onto the slide.",
        composition_instruction="When you need to add a caption or text under/above/left to/right to an object, you can call insert_textbox().",api_desc="textbox"),
    API(name="delete_text", parameters="()", description="This API delete the text part of an object.",
        composition_instruction="You should first choose content or title before you can call delete_text()",api_desc="delete text, change text"),
    API(name="set_font_size", parameters="(font_size)", description="This API sets the size of the font",
        parameter_description="It can take one argument 'font_size', the font size to set as an integer.",api_desc="font size"),
    API(name="set_font_color", parameters="(color)", description="This API sets the color of the font.",
        parameter_description="It takes one parameter 'color', the color name to set as a string, such as 'red', 'purple'.",api_desc="font color: red, purple, blue, green, yellow, orange"),
    API(name="set_font_bold", parameters="()", description="This API sets the font to be bold.",api_desc="bold"),
    API(name="set_font_italic", parameters="()", description="This API sets the font to be italic.",api_desc="italic"),
    API(name="set_font_underline", parameters="()", description="This API sets the font to be underlined.",api_desc="underline, underlined"),
    API(name="set_font_style", parameters="(font_name)", description="This API sets the font style of the selected text.",
        parameter_description="It can take one argument 'font_style', the font name as a string.",api_desc="font style"),
    API(name="set_line_space", parameters="(line_space_level)", description="This API sets the line spacing of the selected text.",
        parameter_description="It can take one argument 'line_space_level', as an integer, default 0.",api_desc="line space"),
    API(name="text_align_left", parameters="()", description="This API aligns the text to left.",api_desc="text align left"), 
    API(name="text_align_center", parameters="()", description="This API aligns the text to center.",api_desc="text align center"), 
    API(name="text_align_right", parameters="()", description="This API aligns the text to right.",api_desc="text align right"),
]

# picture
picture_APIs = [
    API(name="insert_picture", parameters="(picture_name)", description="This API inserts a picture onto the slide.",
        parameter_description="It takes one parameter 'picture_name', the name or description of picture as a string",api_desc="picture, image"), 
]

# shape
shape_APIs = [
    API(name="insert_rectangle", parameters="()", description="This API inserts a rectangle or square shape onto the slide.",api_desc="rectangle, square"),
    API(name="insert_right_arrow", parameters="()", description="This API inserts an arrow shape onto the slide.",api_desc="arrow"),
    API(name="insert_rounded_rectangle", parameters="()", description="This API inserts a rounded rectangle shape onto the slide.",api_desc="rounded rectangle"),
    API(name="insert_triangle", parameters="()", description="This API inserts a triangle shape onto the slide.",api_desc="triangle"),
    API(name="insert_callout", parameters="()", description="This API inserts a callout shape onto the slide.",api_desc="callout"),
    API(name="insert_cloud", parameters="()", description="This API inserts a cloud shape onto the slide.",api_desc="cloud"),
    API(name="insert_star", parameters="()", description="This API inserts a star shape onto the current slide.",api_desc="star"),
    API(name="insert_circle", parameters="()", description="This API inserts a circle or oval shape into the current slide.",api_desc="circle, oval"),
]

# table
table_APIs = [
    API(name="insert_table", parameters="(row_num, col_num)", description="This API inserts a table of row_num rows and col_num columns onto the current slide.",
        parameter_description="It takes two argument, the row number and the column number of the inserted table as integer. Remember the first parameter is row number and the second parameter is column number.",api_desc="table, column, row"),
    API(name="insert_table_row", parameters="(row_data)", description="This API inserts a row (list) of data into the table.",
        parameter_description="It takes one argument, the data to insert as a list of numbers or strings.",
        composition_instruction="You should first call choose_table() before you can call insert_table_row(). The parameter 'row_data' should be a list of strings.",api_desc="insert table, column, row data"),
]

# chart
chart_APIs = [
    API(name="insert_line_chart", parameters="(data, series)", description="This API inserts a line chart onto the slide.",
        parameter_description="It takes two argument, 'data' is a list of numbers and 'series' is a list of strings.",api_desc="line chart"),
    API(name="insert_bar_chart", parameters="(data, series)", description="This API inserts a bar chart onto the slide.",
        parameter_description="It takes two argument, 'data' is a list of numbers and 'series' is a list of strings.",api_desc="bar chart"),
    API(name="insert_pie_chart", parameters="(data, series)", description="This API inserts a pie chart onto the slide.",
        parameter_description="It takes two argument, 'data' is a list of numbers and 'series' is a list of strings.",api_desc="pie chart"),
    API(name="set_chart_title", parameters="(title)", description="This API sets the title of a previously inserted chart.",
        parameter_description="It takes one argument 'title', the title to be set as a string.",api_desc="chart title"),
]

lack_APIs = [
    API(name="seek_assistance", parameters="()", description="This API requests human help when the computer is unsure about the result or lacks the necessary API to fulfill the user's instruction.",api_desc="assistance"),
]

import random
random.seed(42)
def random_permutation(lst):
    shuffled = lst.copy()
    random.shuffle(shuffled)
    return shuffled

def get_all_APIs(args):
    all_apis =  slide_APIs + choose_APIs + basic_APIs + text_APIs + picture_APIs+ shape_APIs + table_APIs + chart_APIs 
    if args.api_update:
        all_apis += update_APIs
        all_apis = random_permutation(all_apis)
    if args.api_lack:
        all_apis = [x for x in all_apis if x.name in original_apis]
        all_apis += lack_APIs
    return all_apis



def get_API_name(apis):
    return [api.name + api.parameters for api in apis]

def get_API_desc(apis):
    return [api.api_desc for api in apis]

def get_must_APIs(args):
    if args.dataset == 'long':
        must_APIs = [slide_APIs[3], text_APIs[0], text_APIs[4], choose_APIs[2]]
    else:
        must_APIs = [slide_APIs[3], text_APIs[0], text_APIs[4], choose_APIs[1], basic_APIs[4], basic_APIs[5]]
    if args.api_lack:
        must_APIs += lack_APIs
    return must_APIs

def api_lack_mask(apis):
    ans = []
    for api in apis:
        if not api.split('(')[0] in original_apis:
            ans.append("seek_assistance()")
        else:
            ans.append(api)
    return ans

# update     

update_APIs = [
    API(name="insert_icon", parameters="(icon_id)", description="This API inserts an icon onto the slide.",parameter_description="It takes one parameter 'icon_id', the ID or name of the icon to insert as a string.", api_desc="icon"),
    API(name="insert_3d_model", parameters="(model_id)", description="This API inserts a 3D model onto the slide.",parameter_description="It takes one parameter 'model_id', the ID or name of the 3D model to insert as a string.", api_desc="3D model"),
    API(name="insert_smart_art_list", parameters="(smart_art_type_id)", description="This API inserts a SmartArt list onto the slide.",parameter_description="It takes one parameter 'smart_art_type_id', the ID or name of the SmartArt list type to insert as a string.", api_desc="SmartArt list"),
    API(name="insert_smart_art_process", parameters="(smart_art_type_id)", description="This API inserts a SmartArt process diagram onto the slide.",parameter_description="It takes one parameter 'smart_art_type_id', the ID or name of the SmartArt process type to insert as a string.", api_desc="SmartArt process"),
    API(name="insert_smart_art_cycle", parameters="(smart_art_type_id)", description="This API inserts a SmartArt cycle diagram onto the slide.",parameter_description="It takes one parameter 'smart_art_type_id', the ID or name of the SmartArt cycle type to insert as a string.", api_desc="SmartArt cycle"),
    API(name="insert_smart_art_pyramid", parameters="(smart_art_type_id)", description="This API inserts a SmartArt pyramid diagram onto the slide.",parameter_description="It takes one parameter 'smart_art_type_id', the ID or name of the SmartArt pyramid type to insert as a string.", api_desc="SmartArt pyramid"),
    API(name="insert_smart_art_relationship", parameters="(smart_art_type_id)", description="This API inserts a SmartArt relationship diagram onto the slide.",parameter_description="It takes one parameter 'smart_art_type_id', the ID or name of the SmartArt relationship type to insert as a string.", api_desc="SmartArt relationship"),
    API(name="insert_link", parameters="(link)", description="This API inserts a hyperlink onto the slide.",parameter_description="It takes one parameter 'link', the URL or path of the hyperlink as a string.", api_desc="hyperlink"),
    API(name="insert_comment", parameters="(comment)", description="This API inserts a comment onto the slide.",parameter_description="It takes one parameter 'comment', the text of the comment to insert as a string.", api_desc="comment"),
    API(name="insert_symbol", parameters="(symbol)", description="This API inserts a symbol onto the slide.",parameter_description="It takes one parameter 'symbol', the symbol character to insert as a string.", api_desc="symbol"),
    API(name="insert_equation", parameters="(equation)", description="This API inserts an equation onto the slide.",parameter_description="It takes one parameter 'equation', the mathematical equation to insert as a string.", api_desc="equation"),
    API(name="insert_audio", parameters="(url)", description="This API inserts an audio file onto the slide.",parameter_description="It takes one parameter 'url', the URL or path of the audio file to insert as a string.", api_desc="audio"),
    API(name="insert_video", parameters="(url)", description="This API inserts a video onto the slide.",parameter_description="It takes one parameter 'url', the URL or path of the video file to insert as a string.", api_desc="video"),
    API(name="insert_transition", parameters="(transition_id)", description="This API sets the slide transition effect for the current slide.",parameter_description="It takes one parameter 'transition_id', the ID or name of the transition effect to set as a string.", api_desc="slide transition"),
    API(name="set_transition_duration", parameters="(time)", description="This API sets the duration of the slide transition effect.",parameter_description="It takes one parameter 'time', the duration of the transition effect in seconds as an integer or float.", api_desc="transition duration"),
    API(name="set_transition_sound", parameters="(url)", description="This API sets the sound for the slide transition effect.",parameter_description="It takes one parameter 'url', the URL or path of the sound file to set for the transition as a string.", api_desc="transition sound"),
    API(name="set_transition_after_time", parameters="(time)", description="This API sets the delay time before the slide transition starts.",parameter_description="It takes one parameter 'time', the delay time in seconds as an integer or float.", api_desc="transition delay"),
    API(name="increase_transition_after_time", parameters="()", description="This API increases the delay time before the slide transition starts.", api_desc="increase transition delay"),
    API(name="decrease_transition_after_time", parameters="()", description="This API decreases the delay time before the slide transition starts.", api_desc="decrease transition delay"),
    API(name="increase_transition_duration", parameters="()", description="This API increases the duration of the slide transition effect.", api_desc="increase transition duration"),
    API(name="decrease_transition_duration", parameters="()", description="This API decreases the duration of the slide transition effect.", api_desc="decrease transition duration"),
    API(name="insert_entrance_animation", parameters="(animation_id)", description="This API adds an entrance animation to the selected object or text on the slide.",parameter_description="It takes one parameter 'animation_id', the ID or name of the entrance animation to apply as a string.", api_desc="entrance animation"),
    API(name="insert_emphasis_animation", parameters="(animation_id)", description="This API adds an emphasis animation to the selected object or text on the slide.",parameter_description="It takes one parameter 'animation_id', the ID or name of the emphasis animation to apply as a string.", api_desc="emphasis animation"),
    API(name="insert_exit_animation", parameters="(animation_id)", description="This API adds an exit animation to the selected object or text on the slide.",parameter_description="It takes one parameter 'animation_id', the ID or name of the exit animation to apply as a string.", api_desc="exit animation"),
    API(name="insert_path_animation", parameters="(animation_id)", description="This API adds a motion path animation to the selected object on the slide.",parameter_description="It takes one parameter 'animation_id', the ID or name of the motion path animation to apply as a string.", api_desc="motion path animation"),
    API(name="delete_animation", parameters="()", description="This API removes any animation applied to the selected object or text on the slide.", api_desc="remove animation"),
    API(name="set_animation_start_time", parameters="(time)", description="This API sets the start time of the animation for the selected object or text on the slide.",parameter_description="It takes one parameter 'time', the start time of the animation in seconds as an integer or float.", api_desc="animation start time"),
    API(name="set_animation_duration", parameters="(time)", description="This API sets the duration of the animation for the selected object or text on the slide.",parameter_description="It takes one parameter 'time', the duration of the animation in seconds as an integer or float.", api_desc="animation duration"),
    API(name="start_record", parameters="()", description="This API starts recording the slide show.", api_desc="start recording slide show"),
    API(name="end_record", parameters="()", description="This API stops recording the slide show.", api_desc="stop recording slide show"),
    API(name="get_screenshot", parameters="()", description="This API captures a screenshot of the current slide.", api_desc="capture slide screenshot"),
    API(name="set_font_crossline", parameters="()", description="This API adds a crossline to the selected font in the text on the slide.", api_desc="add font crossline"),
    API(name="delete_comment", parameters="(comment_id)", description="This API deletes a specific comment from the slide.",parameter_description="It takes one parameter 'comment_id', the ID or name of the comment to delete as a string.", api_desc="delete comment"),
    API(name="play_from_start", parameters="()", description="This API starts playing the slide show from the beginning.", api_desc="play slide show from start"),
    API(name="play_from_current_slide", parameters="()", description="This API starts playing the slide show from the current slide.", api_desc="play slide show from current slide"),
    API(name="play_from_slide", parameters="(slide_id)", description="This API starts playing the slide show from a specific slide.",parameter_description="It takes one parameter 'slide_id', the ID or number of the slide to start playing from as a string or integer.", api_desc="play slide show from specific slide"),
    API(name="insert_hierarchy_chart", parameters="(data, series)", description="This API inserts a hierarchy chart onto the slide.",parameter_description="It takes two parameters, 'data' as a list of numbers and 'series' as a list of strings.", api_desc="hierarchy chart"),
    API(name="insert_statistical_chart", parameters="(data, series)", description="This API inserts a statistical chart onto the slide.",parameter_description="It takes two parameters, 'data' as a list of numbers and 'series' as a list of strings.", api_desc="statistical chart"),
    API(name="insert_scatter_chart", parameters="(data, series)", description="This API inserts a scatter chart onto the slide.",parameter_description="It takes two parameters, 'data' as a list of numbers and 'series' as a list of strings.", api_desc="scatter chart"),
    API(name="insert_combo_chart", parameters="(data, series)", description="This API inserts a combo chart onto the slide.",parameter_description="It takes two parameters, 'data' as a list of numbers and 'series' as a list of strings.", api_desc="combo chart"),
    API(name="insert_map", parameters="()", description="This API inserts a map shape onto the slide.", api_desc="map"),
    API(name="insert_left_arrow", parameters="()", description="This API inserts a left arrow shape onto the slide.", api_desc="left arrow"),
    API(name="insert_down_arrow", parameters="()", description="This API inserts a down arrow shape onto the slide.", api_desc="down arrow"),
    API(name="insert_up_arrow", parameters="()", description="This API inserts an up arrow shape onto the slide.", api_desc="up arrow"),
    API(name="insert_pentagon", parameters="()", description="This API inserts a pentagon shape onto the slide.", api_desc="pentagon"),
    API(name="insert_trapezoid", parameters="()", description="This API inserts a trapezoid shape onto the slide.", api_desc="trapezoid"),
    API(name="insert_smile_face", parameters="()", description="This API inserts a smiley face shape onto the slide.", api_desc="smiley face"),
    API(name="insert_heart_shape", parameters="()", description="This API inserts a heart shape onto the slide.", api_desc="heart shape"),
    API(name="insert_lightening_shape", parameters="()", description="This API inserts a lightning shape onto the slide.", api_desc="lightning shape"),
    API(name="insert_stop_shape", parameters="()", description="This API inserts a stop sign shape onto the slide.", api_desc="stop sign shape"),
#
    API(name="insert_flow_chart", parameters="(flow_chart_type)", description="This API inserts a flow chart shape onto the slide.", parameter_description="It takes one parameter 'flow_chart_type', the type of flow chart shape to insert as a string.", api_desc="flow chart"),
    API(name="insert_moon", parameters="()", description="This API inserts a moon shape onto the slide.", api_desc="moon shape"),
    API(name="insert_sun", parameters="()", description="This API inserts a sun shape onto the slide.", api_desc="sun shape"),
    API(name="insert_ellipse", parameters="()", description="This API inserts an ellipse shape onto the slide.", api_desc="ellipse shape"),
    API(name="group_shapes", parameters="(shape_ids)", description="This API groups multiple shapes on the slide.", parameter_description="It takes one parameter 'shape_ids', a list containing the IDs or names of the shapes to group.", api_desc="group shapes"),
    API(name="ungroup_shapes", parameters="(group_id)", description="This API ungroups a set of grouped shapes on the slide.", parameter_description="It takes one parameter 'group_id', the ID or name of the shape group to ungroup.", api_desc="ungroup shapes"),
    API(name="set_border_color", parameters="(shape_id, color)", description="This API sets the border color of a specific shape.", parameter_description="It takes two parameters, 'shape_id' as the ID or name of the shape and 'color' for the border color.", api_desc="set border color"),
    API(name="lock_shape", parameters="(shape_id)", description="This API locks a specific shape, preventing it from being edited or moved.", parameter_description="It takes one parameter 'shape_id', the ID or name of the shape to lock.", api_desc="lock shape"),
    API(name="unlock_shape", parameters="(shape_id)", description="This API unlocks a specific shape, allowing it to be edited or moved.", parameter_description="It takes one parameter 'shape_id', the ID or name of the shape to unlock.", api_desc="unlock shape"),
    API(name="set_shape_opacity", parameters="(shape_id, opacity)", description="This API sets the opacity of a specific shape.", parameter_description="It takes two parameters, 'shape_id' as the ID or name of the shape and 'opacity' as a value between 0 (transparent) to 1 (opaque).", api_desc="set shape opacity"),
    API(name="send_to_back", parameters="(shape_id)", description="This API sends a specific shape to the back of the slide.", parameter_description="It takes one parameter 'shape_id', the ID or name of the shape to send to the back.", api_desc="send shape to back"),
    API(name="bring_to_front", parameters="(shape_id)", description="This API brings a specific shape to the front of the slide.", parameter_description="It takes one parameter 'shape_id', the ID or name of the shape to bring to the front.", api_desc="bring shape to front"),
    API(name="distribute_horizontally", parameters="(shape_ids)", description="This API distributes shapes equally in horizontal spacing.", parameter_description="It takes one parameter 'shape_ids', a list containing the IDs or names of the shapes to distribute.", api_desc="distribute shapes horizontally"),
    API(name="distribute_vertically", parameters="(shape_ids)", description="This API distributes shapes equally in vertical spacing.", parameter_description="It takes one parameter 'shape_ids', a list containing the IDs or names of the shapes to distribute.", api_desc="distribute shapes vertically"),
    API(name="export_slide_as_image", parameters="(file_name, format)", description="This API exports the current slide as an image in the specified format.", parameter_description="It takes two parameters, 'file_name' as the name of the file to save the image to and 'format' as the desired image format (e.g., 'JPEG', 'PNG').", api_desc="export slide as image"),
    API(name="set_shape_gradient", parameters="(shape_id, gradient_type, colors)", description="This API sets a gradient fill on a shape.", parameter_description="Takes 'shape_id' as the shape's ID or name, 'gradient_type' as the gradient's type (linear, radial, etc.), and 'colors' as a list of colors for the gradient.", api_desc="set shape gradient"),
    API(name="merge_cells", parameters="(table_id, start_row, start_column, end_row, end_column)", description="Merges cells in a table.", parameter_description="Parameters specify the table and the range of cells to merge.", api_desc="merge table cells"),
    API(name="split_cell", parameters="(table_id, row, column)", description="Splits a previously merged cell.", parameter_description="Takes 'table_id' for the table's ID or name and 'row' and 'column' for cell location.", api_desc="split table cell"),
    API(name="set_table_style", parameters="(table_id, style)", description="Applies a style to a table.", parameter_description="Takes 'table_id' for the table's ID or name and 'style' for the style name.", api_desc="set table style"),
    API(name="insert_hyperlink", parameters="(text, link)", description="Inserts a hyperlink onto the slide.", parameter_description="Takes 'text' as the visible text and 'link' as the actual hyperlink.", api_desc="insert hyperlink"),
    API(name="remove_animation", parameters="(shape_id)", description="Removes any animation from a shape.", parameter_description="Takes 'shape_id' for the shape's ID or name.", api_desc="remove animation"),
    API(name="remove_slide_transition", parameters="()", description="Removes any transition effect from the slide.", api_desc="remove slide transition"),
    API(name="play_media", parameters="(media_id)", description="Plays an audio or video clip on the slide.", parameter_description="Takes 'media_id' for the audio or video clip's ID or name.", api_desc="play media"),
    API(name="pause_media", parameters="(media_id)", description="Pauses an audio or video clip on the slide.", parameter_description="Takes 'media_id' for the audio or video clip's ID or name.", api_desc="pause media"),
    API(name="stop_media", parameters="(media_id)", description="Stops an audio or video clip on the slide.", parameter_description="Takes 'media_id' for the audio or video clip's ID or name.", api_desc="stop media"),
    API(name="set_media_volume", parameters="(media_id, volume)", description="Sets the volume for an audio or video clip.", parameter_description="Specifies the media and desired volume (0-100).", api_desc="set media volume"),
    API(name="mute_media", parameters="(media_id)", description="Mutes an audio or video clip.", parameter_description="Takes 'media_id' for the audio or video clip's ID or name.", api_desc="mute media"),
    API(name="unmute_media", parameters="(media_id)", description="Unmutes an audio or video clip.", parameter_description="Takes 'media_id' for the audio or video clip's ID or name.", api_desc="unmute media"),
    API(name="trim_media", parameters="(media_id, start_time, end_time)", description="Trims an audio or video clip's playback range.", parameter_description="Specifies the media and desired start and end times for playback.", api_desc="trim media"),
    API(name="set_slide_master", parameters="(master_id)", description="Applies a slide master layout to the current slide.", parameter_description="Takes 'master_id' as the ID or name of the slide master.", api_desc="set slide master"),
    API(name="duplicate_slide", parameters="()", description="Duplicates the current slide.", api_desc="duplicate slide"),
    API(name="hide_slide", parameters="()", description="Hides the current slide from the slideshow view.", api_desc="hide slide"),
    API(name="unhide_slide", parameters="()", description="Unhides the current slide for the slideshow view.", api_desc="unhide slide"),
    API(name="set_slide_orientation", parameters="(orientation)", description="Sets the slide orientation.", parameter_description="Takes 'orientation' as either 'portrait' or 'landscape'.", api_desc="set slide orientation"),
    API(name="insert_image_gallery", parameters="(image_paths)", description="Inserts a gallery of images onto the slide.", parameter_description="Takes 'image_paths' as a list of paths to the images.", api_desc="insert image gallery"),
    API(name="flip_shape", parameters="(shape_id, direction)", description="Flips a shape horizontally or vertically.", parameter_description="Takes 'shape_id' for the shape's ID or name and 'direction' as either 'horizontal' or 'vertical'.", api_desc="flip shape"),
    API(name="set_slide_looping", parameters="(loop_count)", description="Sets the number of times a slide should loop.", parameter_description="Takes 'loop_count' as the number of loops (0 for infinite).", api_desc="set slide looping"),
    API(name="insert_slide_number", parameters="(position)", description="Inserts slide number at a specified position.", parameter_description="Takes 'position' as the location on the slide (e.g., 'bottom_right').", api_desc="insert slide number"),
    API(name="insert_date_time", parameters="(format, position)", description="Inserts date and time on the slide.", parameter_description="Takes 'format' for date/time format and 'position' as the location.", api_desc="insert date and time"),
    API(name="embed_fonts", parameters="()", description="Embeds the fonts used in the presentation.", api_desc="embed fonts"),
    API(name="optimize_media", parameters="(compression_level)", description="Optimizes embedded media to reduce file size.", parameter_description="Takes 'compression_level' as the desired level of compression.", api_desc="optimize media"),
    API(name="enable_slide_grid", parameters="(grid_spacing)", description="Enables a grid overlay on the slide.", parameter_description="Takes 'grid_spacing' as the distance between grid lines.", api_desc="enable slide grid"),
    API(name="disable_slide_grid", parameters="()", description="Disables the grid overlay on the slide.", api_desc="disable slide grid"),
    API(name="set_slide_grid_color", parameters="(color)", description="Sets the color of the grid overlay on the slide.", parameter_description="Takes 'color' as the desired color value.", api_desc="set slide grid color"),
    API(name="set_text_wrap", parameters="(shape_id, wrap_type)", description="Sets how text wraps inside a shape.", parameter_description="Takes 'shape_id' for the shape's ID or name and 'wrap_type' as the desired wrap setting (e.g., 'square', 'tight').", api_desc="set text wrap"),
    API(name="lock_aspect_ratio", parameters="(shape_id)", description="Locks the aspect ratio of a shape.", parameter_description="Takes 'shape_id' as the shape's ID or name.", api_desc="lock shape aspect ratio"),
    API(name="unlock_aspect_ratio", parameters="(shape_id)", description="Unlocks the aspect ratio of a shape.", parameter_description="Takes 'shape_id' as the shape's ID or name.", api_desc="unlock shape aspect ratio")
]

update_apis = [x.name for x in update_APIs]

original_apis = [
    "move_to_slide",
    "create_slide",
    "choose_title",
    "choose_content",
    "choose_picture",
    "choose_shape",
    "choose_textbox",
    "set_background_color",
    "insert_text",
    "insert_picture",
    "insert_rectangle",
    "insert_right_arrow",
    "insert_line_chart",
    "insert_bar_chart",
    "insert_pie_chart",
    "choose_table",
    "choose_table_cell",
    "insert_table",
    "set_font_color",
    "set_font_size",
    "set_font_bold",
    "set_height",
    "set_width",
    "set_left",
    "set_top",
]

# api_selector
# - get_all_APIs
# - get_selected_APIs
# api_executor

# api update:


# api lack:
