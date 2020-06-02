#!/usr/bin/env python
import sys
from PyQt5 import QtWidgets
from package.views import main_view
from package.entity.edata import constants, variables
import pycnbi.utils.pycnbi_utils as pu

def display_views():
    if len(sys.argv) == 2:
        amp_name = sys.argv[1]
        amp_serial = None
    elif len(sys.argv) == 3:
        amp_name, amp_serial = sys.argv[1:3]
    else:
        amp_name, amp_serial = pu.search_lsl()
        variables.Variables.set_amp_name(amp_name)
        variables.Variables.set_amp_serial(amp_serial)
    if amp_name == 'None':
        amp_name = None
    app = QtWidgets.QApplication(sys.argv)
    ex = main_view.MainView(variables.Variables.get_amp_name(), variables.Variables.get_amp_serial())
    sys.exit(app.exec_())


if __name__ == "__main__":
    variables.Variables.set_current_environment(constants.CONSTANTS.ENV_DEVELOPMENT)

    display_views()