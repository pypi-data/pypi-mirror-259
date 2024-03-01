from fime.util import get_icon

try:
    from PySide6 import QtCore, QtGui, QtWidgets
except ImportError:
    from PySide2 import QtCore, QtGui, QtWidgets

from fime.config import Config, AuthMethods, Browsers

AUTH_METHODS_PRESENTATION = {
    AuthMethods.TOKEN: "Jira Access Token",
    AuthMethods.COOKIES: "Browser Cookies",
}

AUTH_METHODS_VALUE = {v: k for k, v in AUTH_METHODS_PRESENTATION.items()}

class Settings(QtWidgets.QDialog):
    def __init__(self, config: Config, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.setWindowTitle("Settings")

        self.config = config

        caption_label = QtWidgets.QLabel()
        caption_label.setText("Settings")
        caption_label.setAlignment(QtCore.Qt.AlignHCenter)

        settings_layout = QtWidgets.QGridLayout()

        jira_url_label = QtWidgets.QLabel()
        jira_url_label.setText("Jira URL")
        settings_layout.addWidget(jira_url_label, 0, 0)
        self.jira_url_edit = QtWidgets.QLineEdit()
        settings_layout.addWidget(self.jira_url_edit, 0, 1)

        auth_method_label = QtWidgets.QLabel()
        auth_method_label.setText("Authentication method")
        settings_layout.addWidget(auth_method_label, 1, 0)
        self.auth_method_combo_box = QtWidgets.QComboBox()
        for am in AuthMethods:
            self.auth_method_combo_box.addItem(AUTH_METHODS_PRESENTATION[am])
        self.auth_method_combo_box.currentTextChanged.connect(self._auth_method_update)
        settings_layout.addWidget(self.auth_method_combo_box, 1, 1, QtCore.Qt.AlignRight)

        self.jira_token_label = QtWidgets.QLabel()
        self.jira_token_label.setText("Jira Personal Access Token<br/> see <a href='https://confluence.atlassian.com/enterprise/using-personal-access-tokens-1026032365.html#UsingPersonalAccessTokens-CreatingPATsinapplication'>here</a> for how to get one")
        self.jira_token_label.setTextFormat(QtCore.Qt.RichText)
        self.jira_token_label.setTextInteractionFlags(QtCore.Qt.TextBrowserInteraction)
        self.jira_token_label.setOpenExternalLinks(True)
        settings_layout.addWidget(self.jira_token_label, 2, 0)
        self.jira_token_edit = QtWidgets.QLineEdit()
        settings_layout.addWidget(self.jira_token_edit, 2, 1)

        self.cookie_source_label = QtWidgets.QLabel()
        self.cookie_source_label.setText("Cookie source browser")
        settings_layout.addWidget(self.cookie_source_label, 2, 0)
        self.cookie_source_combo_box = QtWidgets.QComboBox()
        for b in Browsers:
            self.cookie_source_combo_box.addItem(b.capitalize())
        settings_layout.addWidget(self.cookie_source_combo_box, 2, 1, QtCore.Qt.AlignRight)

        tray_theme_label = QtWidgets.QLabel()
        tray_theme_label.setText("Tray theme")
        settings_layout.addWidget(tray_theme_label, 3, 0)
        self.tray_theme_combo_box = QtWidgets.QComboBox()
        self.tray_theme_combo_box.addItem("Light")
        self.tray_theme_combo_box.addItem("Dark")
        settings_layout.addWidget(self.tray_theme_combo_box, 3, 1, QtCore.Qt.AlignRight)

        flip_menu_label = QtWidgets.QLabel()
        flip_menu_label.setText("Flip menu")
        settings_layout.addWidget(flip_menu_label, 4, 0)
        self.flip_menu_check_box = QtWidgets.QCheckBox()
        settings_layout.addWidget(self.flip_menu_check_box, 4, 1, QtCore.Qt.AlignRight)

        import_auto_change_task_label = QtWidgets.QLabel()
        import_auto_change_task_label.setText("Automatically select task as active task\nafter task import")
        settings_layout.addWidget(import_auto_change_task_label, 5, 0)
        self.import_auto_change_task_check_box = QtWidgets.QCheckBox()
        settings_layout.addWidget(self.import_auto_change_task_check_box, 5, 1, QtCore.Qt.AlignRight)

        self.ok_button = QtWidgets.QPushButton()
        self.ok_button.setText("OK")
        self.ok_button.setIcon(get_icon("dialog-ok"))
        self.ok_button.pressed.connect(self.accept)
        self.ok_button.setAutoDefault(True)

        button_layout = QtWidgets.QHBoxLayout()
        button_layout.addStretch(66)
        button_layout.addWidget(self.ok_button, 33)

        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(caption_label)
        layout.addLayout(settings_layout)
        layout.addLayout(button_layout)

        self.setLayout(layout)
        self.resize(500, 0)
        self.accepted.connect(self._accepted)

    def showEvent(self, _):
        self.jira_url_edit.setText(self.config.jira_url)
        self.auth_method_combo_box.setCurrentText(AUTH_METHODS_PRESENTATION[self.config.auth_mode])
        self.jira_token_edit.setText(self.config.jira_token)
        self.cookie_source_combo_box.setCurrentText(self.config.cookie_source.capitalize())
        self.tray_theme_combo_box.setCurrentText(self.config.tray_theme.capitalize())
        self.flip_menu_check_box.setChecked(self.config.flip_menu)
        self.import_auto_change_task_check_box.setChecked(self.config.import_auto_change_task)
        self._auth_method_update()

    def _accepted(self):
        self.config.jira_url = self.jira_url_edit.text()
        self.config.auth_mode = AUTH_METHODS_VALUE[self.auth_method_combo_box.currentText()]
        self.config.jira_token = self.jira_token_edit.text()
        self.config.cookie_source = Browsers(self.cookie_source_combo_box.currentText().lower())
        self.config.tray_theme = self.tray_theme_combo_box.currentText()
        self.config.flip_menu = self.flip_menu_check_box.isChecked()
        self.config.import_auto_change_task = self.import_auto_change_task_check_box.isChecked()
        self.config.save()

    def _auth_method_update(self):
        match AUTH_METHODS_VALUE[self.auth_method_combo_box.currentText()]:
            case AuthMethods.TOKEN:
                self.jira_token_label.show()
                self.jira_token_edit.show()
                self.cookie_source_label.hide()
                self.cookie_source_combo_box.hide()
            case AuthMethods.COOKIES:
                self.jira_token_label.hide()
                self.jira_token_edit.hide()
                self.cookie_source_label.show()
                self.cookie_source_combo_box.show()
            case _:
                raise AssertionError("unhandled auth method")


# only for dev/debug
if __name__ == "__main__":
    QtCore.QCoreApplication.setApplicationName("fime")
    app = QtWidgets.QApplication()
    cfg = Config()
    settings = Settings(cfg, None)
    settings.show()
    app.exec()
