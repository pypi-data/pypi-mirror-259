import os

from oauthlib.oauth2 import LegacyApplicationClient, InvalidGrantError
from requests_oauthlib import OAuth2Session

from datazone.constants import Constants
from datazone.core.common.settings import SettingsManager
from datazone.errors.auth import DatazoneInvalidGrantError

os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"


class AuthService:
    @staticmethod
    def login() -> dict:
        profile = SettingsManager.get_profile()
        client = LegacyApplicationClient(client_id=Constants.DEFAULT_OAUTH2_CLIENT_ID)
        session = OAuth2Session(client=client)
        try:
            token = session.fetch_token(
                token_url=profile.token_url,
                username=profile.username,
                password=profile.password,
            )
        except InvalidGrantError:
            raise DatazoneInvalidGrantError(detail="Invalid username or password!")

        SettingsManager.update_profile_token(token=token)

        return token

    @classmethod
    def get_session(cls) -> OAuth2Session:
        profile = SettingsManager.get_profile()
        token = SettingsManager.get_profile_token()
        if token is None:
            print("[bold orange]Token not found, logging in...[/bold orange]")
            token = cls.login()

        def token_updater(new_token):
            SettingsManager.update_profile_token(token=new_token)

        return OAuth2Session(
            client_id=Constants.DEFAULT_OAUTH2_CLIENT_ID,
            token=token,
            auto_refresh_url=profile.token_url,
            token_updater=token_updater,
            auto_refresh_kwargs={"client_id": Constants.DEFAULT_OAUTH2_CLIENT_ID},
        )
