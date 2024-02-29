# Google-Auth

A Reflex custom component Google Auth.

## Usage

Please go to this [blog post](https://reflex.dev/blog/2023-10-25-implementing-sign-in-with-google#implementing-sign-in-with-google) for how to use the component in a Reflex App.

Below is a short code example that goes to Google for authentication and redirects upon success. It still needs code to handle/store the tokens, etc.

```python
from rxconfig import config

import reflex as rx

from rx_google_auth import google_auth, google_login
from google.auth.transport import requests
from google.oauth2.id_token import verify_oauth2_token

CLIENT_ID = "YOUR_CLIENT_ID"

class State(rx.State):
    """The app state."""

    def on_success(self, id_token: dict):
        print(
            verify_oauth2_token(
                id_token["credential"],
                requests.Request(),
                CLIENT_ID,
            )
        )


def index() -> rx.Component:
    return rx.center(
        rx.theme_panel(),
        rx.vstack(
            rx.heading("Welcome to Reflex!", size="9"),
            rx.text("Test your custom component by editing ", rx.code(filename)),
            google_auth(
                google_login(
                    on_success=State.on_success,
                ),
                client_id=CLIENT_ID,
            ),
            align="center",
            spacing="7",
            font_size="2em",
        ),
        height="100vh",
    )


# Add state and page to the app.
app = rx.App()
app.add_page(index)
```
