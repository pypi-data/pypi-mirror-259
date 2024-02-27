import logging
import os
from getpass import getpass
from typing import List, Optional

logger = logging.getLogger(__name__)


class CredentialManager:
    def __init__(
        self,
        file_id: str = "api.key",
        env_names: List[str] = ["MODELON_IMPACT_CLIENT_API_KEY"],
        interactive_help_text: str = "Enter Modelon Impact API key:",
    ):
        self._file_id = file_id
        self._env_names = env_names
        self._interactive_help_text = interactive_help_text

    def get_key_from_env(self) -> Optional[str]:
        for env_name in self._env_names:
            env_value = os.environ.get(env_name)
            if env_value:
                return env_value
        return None

    def _cred_file(self) -> str:
        home_dir = os.path.expanduser("~")
        return os.path.join(home_dir, ".impact", self._file_id)

    def get_key_from_file(self) -> Optional[str]:
        credentials_file = self._cred_file()
        if not os.path.isfile(credentials_file):
            return None

        with open(credentials_file, "r") as credentials:
            return credentials.read().strip()

    def get_key_from_prompt(self) -> str:
        key = getpass(self._interactive_help_text)
        if key == '\x16':
            # This is a getpass Windows bug...
            logger.error("Does not support Ctrl+V on Windows")
            return self.get_key_from_prompt()

        return key

    def write_key_to_file(self, api_key: str) -> None:
        credentials_file = self._cred_file()
        os.makedirs(os.path.dirname(credentials_file), exist_ok=True)
        with open(credentials_file, "w") as credentials:
            credentials.write(str(api_key))

    def get_key(self, interactive: bool = False) -> Optional[str]:
        api_key = self.get_key_from_env() or self.get_key_from_file()
        if api_key or not interactive:
            return api_key

        return self.get_key_from_prompt()
