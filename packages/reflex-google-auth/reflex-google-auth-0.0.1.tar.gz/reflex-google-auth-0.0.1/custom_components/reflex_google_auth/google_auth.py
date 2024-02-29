"""Reflex custom component GoogleAuth."""

import reflex as rx


class GoogleAuth(rx.Component):
    """GoogleAuth component."""

    # The React library to wrap.
    library = "@react-oauth/google"

    # The React component tag.
    tag = "GoogleOAuthProvider"

    # The Google OAuth Client ID: guide to how to create one at https://reflex.dev/blog/2023-10-25-implementing-sign-in-with-google#create-a-google-oauth-client-id
    client_id: rx.Var[str]


class GoogleLogin(rx.Component):
    """GoogleLogin component."""

    # The React library to wrap.
    library = "@react-oauth/google"

    # The React component tag.
    tag = "GoogleLogin"

    # Event triggers to pass its arguments directly to the Reflex event handler.
    def get_event_triggers(self):
        return {"on_success": lambda data: [data]}


google_auth = GoogleAuth.create
google_login = GoogleLogin.create
