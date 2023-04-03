import qrcode
import PySimpleGUI as sg

# Define the layout of the PySimpleGUI window

sg.theme_background_color('#E384FF')
layout = [
    [sg.Text('Enter text to encode:',background_color=('#9A208C'))],
    [sg.Input(key='-INPUT-')],
    [sg.Text('QR code size:',background_color=('#E11299')), sg.InputText('300', key='-SIZE-')],
    [sg.Text('QR code color:' ,background_color=('#E7B10A')), sg.InputText('orange', key='-COLOR-')],
    [sg.Button('Generate QR Code' ,button_color=('#FFED00')), sg.Button('Exit',button_color=('#30E3DF') )],
    [sg.Image('', key = 'image_key' )]
]

# Create the PySimpleGUI window
window = sg.Window('QR CODE GENERATOR', layout)

# Run the event loop
while True:
    event, values = window.read()
    # If the user closes the window or clicks the exit button, exit the loop and close the window
    if event == sg.WINDOW_CLOSED or event == 'Exit':
        break
    # If the user clicks the generate QR code button, generate the QR code and display it
    if event == 'Generate QR Code':
        input_text = values['-INPUT-']
        qr_size = int(values['-SIZE-'])
        qr_color = values['-COLOR-']
        if not input_text:
            sg.popup('Please enter text to encode.', title='Error')
        else:
            try:
                qr = qrcode.QRCode(version=None, box_size=10, border=4)
                qr.add_data(input_text)
                qr.make(fit=True)
                qr_img = qr.make_image(fill_color=qr_color, back_color='white').resize((qr_size, qr_size))
                qr_img.save('qr_code.png')
                window['image_key'].update('qr_code.png')
                sg.popup('QR Code generated successfully!', title='Success')
            except:
                sg.popup('Invalid input. Please try again.', title='Error')
        
# Close the PySimpleGUI window
window.close()


 