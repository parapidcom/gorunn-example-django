from django.templatetags.static import static
from django.http import HttpResponse

def home(request):
    # Ensure the generated URLs in the development server are correct
    favicon_url = static('images/favicon.ico')
    logo_url = static('images/gorunn_logo.png')

    html = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <link rel="icon" href="{favicon_url}" type="image/x-icon">
        <title>Gorunn Django</title>
        <style>
            body, html {{
                height: 100%;
                margin: 0;
                font-family: Arial, sans-serif;
                background-color: #000; /* Sets the background color to black */
                color: #fff;
            }}
            .logo {{
                display: block;
                margin-left: auto;
                margin-right: auto;
                width: 50%;
            }}
            .centered-text {{
                position: absolute;
                top: 50%;
                left: 50%;
                transform: translate(-50%, -50%);
                font-size: 24px;
                text-align: center;
            }}
        </style>
    </head>
    <body>
        <div class="centered-text">
            <img src="{logo_url}" alt="Gorunn Logo" class="logo">
            <div>This Django is running on the Gorunn!</div>
        </div>
    </body>
    </html>
    """

    return HttpResponse(html)
