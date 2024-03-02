from loguru import logger
from pathlib import Path

from PyQt6 import QtCore
from PyQt6.QtWidgets import (QDialog, QFormLayout, QFrame,
    QLineEdit, QSpinBox, QHBoxLayout,  QVBoxLayout,
    QDialogButtonBox, QSizePolicy, QSpacerItem,
    QCheckBox,
)

from src import tug
from ..core import app_globals as ag

class Preferences(QDialog):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.setWindowTitle('Application preferences')
        self.buttonBox = QDialogButtonBox(
            QDialogButtonBox.StandardButton.Ok |
            QDialogButtonBox.StandardButton.Cancel
        )
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)

        form_layout = QFormLayout()
        form_layout.setContentsMargins(9, 9, 9, 9)
        self.set_inputs()

        form_layout.addRow('Path to DBs:', self.db_path)
        form_layout.addRow('Export path:', self.export_path)
        form_layout.addRow('Report path:', self.report_path)
        form_layout.addRow('Log file path:', self.log_path)
        form_layout.addRow('Folder history depth:', self.folder_history_depth)
        form_layout.addRow('Check duplicates:', self.check_dup)
        if tug.config['instance_control']:
            form_layout.addRow('Allow single instance only:', self.single_instance)

        v_layout = QVBoxLayout(self)
        v_layout.setContentsMargins(9, 9, 9, 9)
        v_layout.setSpacing(16)

        form = QFrame(self)
        form.setLayout(form_layout)

        spacer_item = QSpacerItem(20, 286, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)
        h_layout = QHBoxLayout()
        h_layout.addSpacerItem(spacer_item)
        h_layout.addWidget(self.buttonBox)
        v_layout.addWidget(form)
        v_layout.addLayout(h_layout)
        self.setSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        self.setModal(True)

    def sizeHint(self) -> QtCore.QSize:
        return QtCore.QSize(499,184)

    def accept(self):
        settings = {
            "DEFAULT_DB_PATH": self.db_path.text(),
            "DEFAULT_EXPORT_PATH": self.export_path.text(),
            "DEFAULT_REPORT_PATH": self.report_path.text(),
            "DEFAULT_LOG_PATH": self.log_path.text(),
            "FOLDER_HISTORY_DEPTH": self.folder_history_depth.value(),
            "CHECK_DUPLICATES": int(self.check_dup.isChecked()),
        }
        if tug.config['instance_control']:
            settings['SINGLE_INSTANCE'] = int(self.single_instance.isChecked())
            ag.single_instance = bool(settings["SINGLE_INSTANCE"])
        tug.save_app_setting(**settings)
        tug.create_dir(Path(self.db_path.text()))
        tug.create_dir(Path(self.export_path.text()))
        tug.create_dir(Path(self.report_path.text()))
        tug.create_dir(Path(self.log_path.text()))
        ag.history.set_limit(int(settings["FOLDER_HISTORY_DEPTH"]))
        self.close()

    def set_inputs(self):
        self.db_path = QLineEdit()
        pp = Path('~/fileo').expanduser()
        self.db_path.setText(
            tug.get_app_setting('DEFAULT_DB_PATH', str(pp / 'dbs'))
        )
        self.export_path = QLineEdit()
        self.export_path.setText(
            tug.get_app_setting('DEFAULT_EXPORT_PATH', str(pp / 'export'))
        )
        self.report_path = QLineEdit()
        self.report_path.setText(
            tug.get_app_setting('DEFAULT_REPORT_PATH', str(pp / 'report'))
        )
        self.log_path = QLineEdit()
        self.log_path.setText(
            tug.get_app_setting('DEFAULT_LOG_PATH', str(pp / 'log'))
        )
        self.folder_history_depth = QSpinBox()
        self.folder_history_depth.setMinimum(2)
        self.folder_history_depth.setMaximum(50)
        val = tug.get_app_setting('FOLDER_HISTORY_DEPTH', 15)
        self.folder_history_depth.setValue(int(val))
        ag.history.set_limit(int(val))
        self.check_dup = QCheckBox()
        self.check_dup.setChecked(
            int(tug.get_app_setting('CHECK_DUPLICATES', 1))
        )
        if tug.config['instance_control']:
            self.single_instance = QCheckBox()
            self.single_instance.setChecked(
                int(tug.get_app_setting('SINGLE_INSTANCE', 0))
            )
