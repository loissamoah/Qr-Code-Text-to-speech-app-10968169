import pyttsx3
import PySimpleGUI as sg


# Define the layout of the PySimpleGUI window
sg.theme_background_color('#F8C0C8')

layout = [[sg.Text('Enter what you want to hear:', background_color=('#F51720'))],
          [sg.InputText(key='-INPUT-' ,background_color=('#F9BDC0'))],
          [sg.Text('Gender:',background_color=('#FBC740')),sg.Radio('Male',background_color=('#E11299'), group_id='gender', default=True, key='-MALE-'),
           sg.Radio('Female', group_id='gender', key='-FEMALE-')],
          [sg.Text('Speed:',background_color=('#A06AB4')), sg.Slider(range=(0.5, 2), orientation='h', size=(30, 20), default_value=1, resolution=0.1, key='-SPEED-')],
          [sg.Text('Volume:',background_color=('#D773A2')), sg.Slider(range=(0, 100), orientation='h', size=(30, 20), default_value=50, key='-VOLUME-')],
          [sg.Button('Speak',button_color=('#FFD743')), sg.Button('Exit', button_color=('#E11299'))]
]
window = sg.Window('Text to Speech', layout)
#events for male voice
while True:
    event,values = window.read()
    if event == sg.WIN_CLOSED or event =='Exit':
        break
    if event =='Speak':
        if values['-MALE-']==True:
            text = values['-INPUT-']
            speed = values['-SPEED-']
            volume = values['-VOLUME-']
            speaker = pyttsx3.init()
            voices = speaker.getProperty('voices')
            speaker.setProperty('voice', voices[0].id)
            speaker.setProperty('rate', speed * 150)  # Speed is 150 words per minute
            speaker.setProperty('volume', volume / 100)
            speaker.say(text)
            speaker.runAndWait()
    
            #for female voice
        if values['-FEMALE-'] ==True:
            text = values['-INPUT-']
            speed = values['-SPEED-']
            volume = values['-VOLUME-']
            speaker = pyttsx3.init()
            voices = speaker.getProperty('voices')
            speaker.setProperty('voice', voices[1].id)
            speaker.setProperty('rate', speed * 150)  # Speed is 150 words per minute
            speaker.setProperty('volume', volume / 100)
            speaker.say(text)
            speaker.runAndWait()

        
