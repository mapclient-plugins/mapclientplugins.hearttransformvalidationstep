from math import sqrt

from PySide6 import QtWidgets

from cmlibs.maths.vectorops import sub, dot, reshape

from mapclientplugins.hearttransformvalidationstep.view.ui_hearttransformvalidationwidget \
    import Ui_HeartTransformValidationWidget

T_LIMITS = [2, 20]
R_LIMITS = [0.5, 5]
ANSWER_T = [7.542893880483713, -30.00245783135635, -12.065013443763675]
ANSWER_R = [[0.524975715317517, -0.5704818654890634, -0.6316256323764731],
            [-0.20542408183881694, -0.8051023517173368, 0.5564271289754775],
            [-0.8259548685779027, -0.16235961445917443, -0.5398498964204104]]


class HeartTransformValidationWidget(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super(HeartTransformValidationWidget, self).__init__(parent)
        self._ui = Ui_HeartTransformValidationWidget()
        self._ui.setupUi(self)

        self._callback = None
        self._transform = None

        self._make_connections()

    def _make_connections(self):
        self._ui.continue_push_button.clicked.connect(self._continue_button_clicked)

    def register_continue_execution(self, callback):
        self._callback = callback

    def _continue_button_clicked(self):
        self._callback()

    def set_transform(self, transform):
        self._transform = transform

    def validate_transform(self):
        if self._transform is None:
            self._process_invalid_transform()
        else:
            self._process_valid_transform()

    def _process_invalid_transform(self):
        self._ui.rms_display_label.setText('inf, inf.')
        self._ui.validation_result_label('There was an error validating the transform.')

    def _process_valid_transform(self):
        r = self._transform.getRotationMatrix()
        t = self._transform.getTranslationVector()

        t_difference = sub(t, ANSWER_T)
        reshape_r = reshape(r, 9)
        reshape_answer_r = reshape(ANSWER_R, 9)
        r_difference = sub(reshape_r, reshape_answer_r)
        r_err = sqrt(dot(r_difference, r_difference))
        t_err = sqrt(dot(t_difference, t_difference))
        self._ui.rms_display_label.setText('Transformation error: R = {0}, T = {1}'.format(r_err, t_err))
        self._set_validation_result(r_err, t_err)

    def _set_validation_result(self, r_err, t_err):

        r_text, r_colour = _determine_text(r_err, R_LIMITS)
        t_text, t_colour = _determine_text(t_err, T_LIMITS)

        self._ui.validation_result_label.setText(
            'Validation results: R is <font color="{0}">{1}</font>, T is <font color="{2}">{3}</font>.'
                .format(r_colour, r_text, t_colour, t_text))


def _determine_text(value, limits):
    limits.append(value)
    limits.sort()
    index = limits.index(value)

    text = 'Poor'
    colour = 'red'
    if index == 0:
        text = 'Great'
        colour = 'green'
    elif index == 1:
        text = 'Ok'
        colour = 'orange'

    return text, colour
