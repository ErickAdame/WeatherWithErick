
import pandas as pd
from pptx import Presentation
from pptx.util import Pt
from pptx.dml.color import RGBColor

from pptx.compat import BytesIO
from pptx.enum.shapes import PP_PLACEHOLDER, PROG_ID
from pptx.media import SPEAKER_IMAGE_BYTES, Video
from pptx.opc.constants import CONTENT_TYPE as CT
from pptx.oxml.ns import qn
from pptx.oxml.shapes.graphfrm import CT_GraphicalObjectFrame
from pptx.oxml.shapes.picture import CT_Picture
from pptx.oxml.simpletypes import ST_Direction
from pptx.shapes.autoshape import AutoShapeType, Shape
from pptx.shapes.base import BaseShape
from pptx.shapes.connector import Connector
from pptx.shapes.freeform import FreeformBuilder
from pptx.shapes.graphfrm import GraphicFrame
from pptx.shapes.group import GroupShape
from pptx.shapes.picture import Movie, Picture
from pptx.enum.text import PP_ALIGN

powerpoint_file_path = "/Users/erick/Desktop/Graphics_Templates/email_template.pptx"



csv_file_path = "/Users/erick/Desktop/day_part_data.csv"
csv_file_path2 = "/Users/erick/Desktop/city_high_and Lows.csv"


# Set the slide index and text box index of the PowerPoint slide to update
 # REMINDER: Slide index is 0-based, so slide 7 corresponds to index 6
slide_index = 0
slide_index2 = 1

#READ THE DATA
data = pd.read_csv(csv_file_path)
data2 = pd.read_csv(csv_file_path2)



#DAYPART TEMPS
daypart1_value = str(data.iloc[1, 2])
daypart2_value = str(data.iloc[1, 2])
daypart3_value = str(data.iloc[1, 4])
daypart4_value = str(data.iloc[1, 5])
daypart5_value = str(data.iloc[1, 6])

daypart6_value = str(data.iloc[3, 2])
daypart7_value = str(data.iloc[3, 3])
daypart8_value = str(data.iloc[3, 4])
daypart9_value = str(data.iloc[3, 5])
daypart10_value = str(data.iloc[3,6])

daypart11_value= str(data2.iloc[20,2])
daypart12_value = str(data2.iloc[20,3])

daypart13_value = str(data2.iloc[15,2])
daypart14_value = str(data2.iloc[15,3])


#DAYPART WEATHER
daypart1_weather = str(data.iloc[0,1])
daypart2_weather = str(data.iloc[0,2])
daypart3_weather = str(data.iloc[0,3])
daypart4_weather = str(data.iloc[0,4])
daypart5_weather = str(data.iloc[0,5])

daypart6_weather = str(data.iloc[2,2])
daypart7_weather = str(data.iloc[2,3])
daypart8_weather = str(data.iloc[2,4])
daypart9_weather = str(data.iloc[2,5])
daypart10_weather = str(data.iloc[2,6])

daya_weather = str(data2.iloc[20,4])
dayb_weather = str(data2.iloc[15,4])

#IMAGE MAPPING
# Define the base directory for the image files
base_directory = "/Users/erick/Desktop/Weather_Graphics/Simple Weather Icons/weather_icons/"

# Define the dictionary mapping weather values to image file paths
weather_image_mapping = {
    "sky is clear": "Sun 3.png",
    "moderate rain": "Rain.png",
    "light rain": "Rain + Sun.png",
    "overcast clouds": "Cloud.png",
    "scattered clouds": "Sun & Clouds.png",
    "broken clouds": "Sun & Clouds.png",
    "few clouds": "Sun 3.png",
    "heavy intensity rain": "Thunderstorm & Sun.png",
    "clear sky": "Sun 3.png",
    "partly cloudy": "Sun & Clouds.png",
    "sunny": "Sun 3.png",
    "patchy rain possible": "Rain + Sun.png",
    "heavy rain": "Thunderstorm & Sun.png",
    "thunderstorm with rain": "Thunderstorm & Sun.png",
    "thunderstorm with heavy rain": "Thunderstorm 2.png"

    # Add more mappings for other weather conditions
}

daypart1_image_file = base_directory + weather_image_mapping.get(daypart1_weather, "Wind.png")
daypart2_image_file = base_directory + weather_image_mapping.get(daypart2_weather, "Wind.png")
daypart3_image_file = base_directory + weather_image_mapping.get(daypart3_weather, "Wind.png")
daypart4_image_file = base_directory + weather_image_mapping.get(daypart4_weather, "Wind.png")
daypart5_image_file = base_directory + weather_image_mapping.get(daypart5_weather, "Wind.png")
daypart6_image_file = base_directory + weather_image_mapping.get(daypart6_weather, "Wind.png")
daypart7_image_file = base_directory + weather_image_mapping.get(daypart7_weather, "Wind.png")
daypart8_image_file = base_directory + weather_image_mapping.get(daypart8_weather, "Wind.png")
daypart9_image_file = base_directory + weather_image_mapping.get(daypart9_weather, "Wind.png")
daypart10_image_file = base_directory + weather_image_mapping.get(daypart10_weather, "Wind.png")
day_image_file = base_directory + weather_image_mapping.get(daya_weather, "Wind.png")
dayb_image_file = base_directory + weather_image_mapping.get(dayb_weather, "Wind.png")





# SLIDE NUMBER 1 BEGINS HERE **************************
presentation = Presentation(powerpoint_file_path)

slide = presentation.slides[slide_index]

daypart1 = 4  # Textbox index is 0-based, so textbox 9 corresponds to index 8
textboxa = slide.shapes[daypart1].text_frame

daypart2 = 7  # Textbox index is 0-based, so textbox 9 corresponds to index 8
textboxb = slide.shapes[daypart2].text_frame

daypart3 = 10  # Textbox index is 0-based, so textbox 9 corresponds to index 8
textboxc = slide.shapes[daypart3].text_frame

daypart4 = 13  # Textbox index is 0-based, so textbox 9 corresponds to index 8
textboxd = slide.shapes[daypart4].text_frame

daypart5 = 16  # Textbox index is 0-based, so textbox 9 corresponds to index 8
textboxe = slide.shapes[daypart5].text_frame

daypart11 = 21  # Textbox index is 0-based, so textbox 9 corresponds to index 8
textboxf = slide.shapes[daypart11].text_frame

daypart12 = 22  # Textbox index is 0-based, so textbox 9 corresponds to index 8
textboxg = slide.shapes[daypart12].text_frame

#CLEAR TEXT, ADD NEW VALUES
textboxa.clear()
textboxa.text = daypart1_value
textboxb.clear()
textboxb.text = daypart2_value
textboxc.clear()
textboxc.text = daypart3_value
textboxd.clear()
textboxd.text = daypart4_value
textboxe.clear()
textboxe.text = daypart5_value
textboxf.clear()
textboxf.text = daypart11_value
textboxg.clear()
textboxg.text = daypart12_value


#FORMATTING NEW TEXT


for paragraph in textboxa.paragraphs:
    for run in paragraph.runs:
        run.font.size = Pt(48)  # Set font size to 48 points
        run.font.color.rgb = RGBColor(255, 255, 255)
        run.font.bold = False  
    paragraph.alignment = PP_ALIGN.CENTER

for paragraph in textboxb.paragraphs:
    for run in paragraph.runs:
        run.font.size = Pt(48)  # Set font size to 48 points
        run.font.color.rgb = RGBColor(255, 255, 255)
        run.font.bold = False  
    paragraph.alignment = PP_ALIGN.CENTER

for paragraph in textboxc.paragraphs:
    for run in paragraph.runs:
        run.font.size = Pt(48)  # Set font size to 48 points
        run.font.color.rgb = RGBColor(255, 255, 255)
        run.font.bold = False  
    paragraph.alignment = PP_ALIGN.CENTER

for paragraph in textboxd.paragraphs:
    for run in paragraph.runs:
        run.font.size = Pt(48)  # Set font size to 48 points
        run.font.color.rgb = RGBColor(255, 255, 255)
        run.font.bold = False  
    paragraph.alignment = PP_ALIGN.CENTER

for paragraph in textboxe.paragraphs:
    for run in paragraph.runs:
        run.font.size = Pt(48)  # Set font size to 48 points
        run.font.color.rgb = RGBColor(255, 255, 255)
        run.font.bold = False  
    paragraph.alignment = PP_ALIGN.CENTER

for paragraph in textboxf.paragraphs:
    for run in paragraph.runs:
        run.font.size = Pt(54)  # Set font size to 48 points
        run.font.color.rgb = RGBColor(255, 255, 255)
        run.font.bold = False  
    paragraph.alignment = PP_ALIGN.CENTER

for paragraph in textboxg.paragraphs:
    for run in paragraph.runs:
        run.font.size = Pt(54)  # Set font size to 48 points
        run.font.color.rgb = RGBColor(255, 255, 255)
        run.font.bold = False  
    paragraph.alignment = PP_ALIGN.CENTER

#presentation = Presentation(powerpoint_file_path)

for slide in presentation.slides:
    for shape in slide.shapes:
        if shape.name == "daypart1_icon":
            shape.element.getparent().remove(shape.element)
            slide.shapes.add_picture(daypart1_image_file, shape.left, shape.top, shape.width, shape.height)
        elif shape.name == "daypart2_icon":
            shape.element.getparent().remove(shape.element)
            slide.shapes.add_picture(daypart2_image_file, shape.left, shape.top, shape.width, shape.height)
        elif shape.name == "daypart3_icon":
            shape.element.getparent().remove(shape.element)
            slide.shapes.add_picture(daypart3_image_file, shape.left, shape.top, shape.width, shape.height)
        elif shape.name == "daypart4_icon":
            shape.element.getparent().remove(shape.element)
            slide.shapes.add_picture(daypart4_image_file, shape.left, shape.top, shape.width, shape.height)
        elif shape.name == "daypart5_icon":
            shape.element.getparent().remove(shape.element)
            slide.shapes.add_picture(daypart5_image_file, shape.left, shape.top, shape.width, shape.height)
        elif shape.name == "day_icon":
            shape.element.getparent().remove(shape.element)
            slide.shapes.add_picture(day_image_file, shape.left, shape.top, shape.width, shape.height)

# SLIDE NUMBER TWO BEGINS HERE

slide = presentation.slides[slide_index2]

daypart6 = 4  # Textbox index is 0-based, so textbox 9 corresponds to index 8
textboxa = slide.shapes[daypart6].text_frame

daypart7 = 7  # Textbox index is 0-based, so textbox 9 corresponds to index 8
textboxb = slide.shapes[daypart7].text_frame

daypart8 = 10  # Textbox index is 0-based, so textbox 9 corresponds to index 8
textboxc = slide.shapes[daypart8].text_frame

daypart9 = 13  # Textbox index is 0-based, so textbox 9 corresponds to index 8
textboxd = slide.shapes[daypart9].text_frame

daypart10 = 16  # Textbox index is 0-based, so textbox 9 corresponds to index 8
textboxe = slide.shapes[daypart10].text_frame

daypart13 = 21  # Textbox index is 0-based, so textbox 9 corresponds to index 8
textboxf = slide.shapes[daypart13].text_frame

daypart14 = 22  # Textbox index is 0-based, so textbox 9 corresponds to index 8
textboxg = slide.shapes[daypart14].text_frame

#CLEAR TEXT, ADD NEW VALUES
textboxa.clear()
textboxa.text = daypart6_value
textboxb.clear()
textboxb.text = daypart7_value
textboxc.clear()
textboxc.text = daypart8_value
textboxd.clear()
textboxd.text = daypart9_value
textboxe.clear()
textboxe.text = daypart10_value
textboxf.clear()
textboxf.text = daypart13_value
textboxg.clear()
textboxg.text = daypart14_value


#FORMATTING NEW TEXT


for paragraph in textboxa.paragraphs:
    for run in paragraph.runs:
        run.font.size = Pt(48)  # Set font size to 48 points
        run.font.color.rgb = RGBColor(255, 255, 255)
        run.font.bold = False  
    paragraph.alignment = PP_ALIGN.CENTER

for paragraph in textboxb.paragraphs:
    for run in paragraph.runs:
        run.font.size = Pt(48)  # Set font size to 48 points
        run.font.color.rgb = RGBColor(255, 255, 255)
        run.font.bold = False  
    paragraph.alignment = PP_ALIGN.CENTER

for paragraph in textboxc.paragraphs:
    for run in paragraph.runs:
        run.font.size = Pt(48)  # Set font size to 48 points
        run.font.color.rgb = RGBColor(255, 255, 255)
        run.font.bold = False  
    paragraph.alignment = PP_ALIGN.CENTER

for paragraph in textboxd.paragraphs:
    for run in paragraph.runs:
        run.font.size = Pt(48)  # Set font size to 48 points
        run.font.color.rgb = RGBColor(255, 255, 255)
        run.font.bold = False  
    paragraph.alignment = PP_ALIGN.CENTER

for paragraph in textboxe.paragraphs:
    for run in paragraph.runs:
        run.font.size = Pt(48)  # Set font size to 48 points
        run.font.color.rgb = RGBColor(255, 255, 255)
        run.font.bold = False  
    paragraph.alignment = PP_ALIGN.CENTER

for paragraph in textboxf.paragraphs:
    for run in paragraph.runs:
        run.font.size = Pt(54)  # Set font size to 48 points
        run.font.color.rgb = RGBColor(255, 255, 255)
        run.font.bold = False  
    paragraph.alignment = PP_ALIGN.CENTER

for paragraph in textboxg.paragraphs:
    for run in paragraph.runs:
        run.font.size = Pt(54)  # Set font size to 48 points
        run.font.color.rgb = RGBColor(255, 255, 255)
        run.font.bold = False  
    paragraph.alignment = PP_ALIGN.CENTER

#presentation = Presentation(powerpoint_file_path)

for slide in presentation.slides:
    for shape in slide.shapes:
        if shape.name == "daypart6_icon":
            shape.element.getparent().remove(shape.element)
            slide.shapes.add_picture(daypart6_image_file, shape.left, shape.top, shape.width, shape.height)
        elif shape.name == "daypart7_icon":
            shape.element.getparent().remove(shape.element)
            slide.shapes.add_picture(daypart7_image_file, shape.left, shape.top, shape.width, shape.height)
        elif shape.name == "daypart8_icon":
            shape.element.getparent().remove(shape.element)
            slide.shapes.add_picture(daypart8_image_file, shape.left, shape.top, shape.width, shape.height)
        elif shape.name == "daypart9_icon":
            shape.element.getparent().remove(shape.element)
            slide.shapes.add_picture(daypart9_image_file, shape.left, shape.top, shape.width, shape.height)
        elif shape.name == "daypart10_icon":
            shape.element.getparent().remove(shape.element)
            slide.shapes.add_picture(daypart10_image_file, shape.left, shape.top, shape.width, shape.height)
        elif shape.name == "dayb_icon":
            shape.element.getparent().remove(shape.element)
            slide.shapes.add_picture(dayb_image_file, shape.left, shape.top, shape.width, shape.height)



#THIS UPDATES THE PRESENTATION
updated_powerpoint_file_path = "/Users/erick/Desktop/Wx Email Graphics.pptx"
presentation.save(updated_powerpoint_file_path)