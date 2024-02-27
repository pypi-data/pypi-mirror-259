# Copyright (c) Streamlit Inc. (2018-2022) Snowflake Inc. (2022-2024)
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from __future__ import annotations

from typing import Any, Final, Iterator, MutableMapping

from streamlit import logger as _logger
from streamlit import runtime
from streamlit.runtime.metrics_util import gather_metrics
from streamlit.runtime.state.common import require_valid_user_key
from streamlit.runtime.state.safe_session_state import SafeSessionState
from streamlit.runtime.state.session_state import SessionState
from streamlit.type_util import Key

_LOGGER: Final = _logger.get_logger(__name__)


_state_use_warning_already_displayed: bool = False


def get_session_state() -> SafeSessionState:
    """Get the SessionState object for the current session.

    Note that in streamlit scripts, this function should not be called
    directly. Instead, SessionState objects should be accessed via
    st.session_state.
    """
    global _state_use_warning_already_displayed
    from streamlit.runtime.scriptrunner import get_script_run_ctx

    ctx = get_script_run_ctx()

    # If there is no script run context because the script is run bare, have
    # session state act as an always empty dictionary, and print a warning.
    if ctx is None:
        if not _state_use_warning_already_displayed:
            _state_use_warning_already_displayed = True
            if not runtime.exists():
                _LOGGER.warning(
                    "Session state does not function when running a script without `streamlit run`"
                )
        return SafeSessionState(SessionState(), lambda: None)
    return ctx.session_state


class SessionStateProxy(MutableMapping[Key, Any]):
    """A stateless singleton that proxies `st.session_state` interactions
    to the current script thread's SessionState instance.

    The proxy API differs slightly from SessionState: it does not allow
    callers to get, set, or iterate over "keyless" widgets (that is, widgets
    that were created without a user_key, and have autogenerated keys).
    """

    def __iter__(self) -> Iterator[Any]:
        """Iterator over user state and keyed widget values."""
        # TODO: this is unsafe if fastReruns is true! Let's deprecate/remove.
        return iter(get_session_state().filtered_state)

    def __len__(self) -> int:
        """Number of user state and keyed widget values in session_state."""
        return len(get_session_state().filtered_state)

    def __str__(self) -> str:
        """String representation of user state and keyed widget values."""
        return str(get_session_state().filtered_state)

    def __getitem__(self, key: Key) -> Any:
        """Return the state or widget value with the given key.

        Raises
        ------
        StreamlitAPIException
            If the key is not a valid SessionState user key.
        """
        key = str(key)
        require_valid_user_key(key)
        return get_session_state()[key]

    @gather_metrics("session_state.set_item")
    def __setitem__(self, key: Key, value: Any) -> None:
        """Set the value of the given key.

        Raises
        ------
        StreamlitAPIException
            If the key is not a valid SessionState user key.
        """
        key = str(key)
        require_valid_user_key(key)
        get_session_state()[key] = value

    def __delitem__(self, key: Key) -> None:
        """Delete the value with the given key.

        Raises
        ------
        StreamlitAPIException
            If the key is not a valid SessionState user key.
        """
        key = str(key)
        require_valid_user_key(key)
        del get_session_state()[key]

    def __getattr__(self, key: str) -> Any:
        try:
            return self[key]
        except KeyError:
            raise AttributeError(_missing_attr_error_message(key))

    @gather_metrics("session_state.set_attr")
    def __setattr__(self, key: str, value: Any) -> None:
        self[key] = value

    def __delattr__(self, key: str) -> None:
        try:
            del self[key]
        except KeyError:
            raise AttributeError(_missing_attr_error_message(key))

    def to_dict(self) -> dict[str, Any]:
        """Return a dict containing all session_state and keyed widget values."""
        return get_session_state().filtered_state


def _missing_attr_error_message(attr_name: str) -> str:
    return (
        f'st.session_state has no attribute "{attr_name}". Did you forget to initialize it? '
        f"More info: https://docs.streamlit.io/library/advanced-features/session-state#initialization"
    )
