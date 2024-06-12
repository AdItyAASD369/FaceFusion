from gradio_client import Client

client = Client("http://127.0.0.1:7860/")
result = client.predict(
                "/Users/adityasantoshdeshmukh/Downloads/a83260ededd887b78794f1569e2ba8da.png",
                "/Users/adityasantoshdeshmukh/Downloads/clip5.mp4",     # str (filepath on your computer (or URL) of file) in 'Input Video' Video component
                True,   # bool  in 'Enhance Face' Checkbox component
                True,   # bool  in 'Enhance Frame' Checkbox component
                api_name="/predict"
)
print(result)


