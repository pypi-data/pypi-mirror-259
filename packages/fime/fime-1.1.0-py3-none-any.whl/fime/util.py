import enum

import browser_cookie3
from loguru import logger
from requests import Session

from fime.config import Config, AuthMethods, Browsers

try:
    from PySide6 import QtCore, QtGui, QtWidgets
except ImportError:
    from PySide2 import QtCore, QtGui, QtWidgets

# noinspection PyUnresolvedReferences
import fime.icons


def get_screen_height(qobject):
    if hasattr(qobject, "screen"):
        return qobject.screen().size().height()
    else:
        logger.info("unable to detect screen height falling back to default value of 1080")
        return 1080


def get_screen_width(qobject):
    if hasattr(qobject, "screen"):
        return qobject.screen().size().width()
    else:
        logger.info("unable to detect screen width falling back to default value of 1920")
        return 1920


def get_icon(icon_name):
    theme_name = icon_name.replace("-light", "")  # respect system theme
    fallback = QtGui.QIcon(f":/icons/{icon_name}").pixmap(256, 256)
    return QtGui.QIcon.fromTheme(theme_name, fallback)


class EditStartedDetector(QtWidgets.QStyledItemDelegate):
    editStarted = QtCore.Signal()
    editFinished = QtCore.Signal()

    def __init__(self, parent=None):
        super().__init__(parent)

    def createEditor(self, parent, option, index):
        editor = super().createEditor(parent, option, index)
        editor.editingFinished.connect(self.editFinished)
        self.editStarted.emit()
        return editor


class Status(enum.Enum):
    PROGRESS = enum.auto()
    OK = enum.auto()
    ERROR = enum.auto()


def add_auth(config: Config, session: Session):
    match config.auth_mode:
        case AuthMethods.TOKEN:
            session.headers["Authorization"] = f"Bearer {config.jira_token}"
        case AuthMethods.COOKIES:
            match config.cookie_source:
                case Browsers.AUTO:
                    cookie_jar = browser_cookie3.load()
                case Browsers.FIREFOX:
                    cookie_jar = browser_cookie3.firefox()
                case Browsers.CHROME:
                    cookie_jar = browser_cookie3.chrome()
                case Browsers.CHROMIUM:
                    cookie_jar = browser_cookie3.chromium()
                case Browsers.EDGE:
                    cookie_jar = browser_cookie3.edge()
                case Browsers.OPERA:
                    cookie_jar = browser_cookie3.opera()
                case _:
                    raise AssertionError("Unknown cookie_source")
            session.cookies = cookie_jar
        case _:
            raise AssertionError("Unknown auth method")
