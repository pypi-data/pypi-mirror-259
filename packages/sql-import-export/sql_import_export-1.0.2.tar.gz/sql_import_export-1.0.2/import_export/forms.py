from django import forms
from django.db import DEFAULT_DB_ALIAS
from django.utils.translation import gettext_lazy as _
from django.conf import settings

from wagtail.admin.forms.models import WagtailAdminModelForm

from .models import DatabaseDumpSchedule


DATABASES = settings.DATABASES

def get_database_choices():
    choices = []
    for name, _ in DATABASES.items():
        choices.append((name, name.title()))
    return choices


def DatabaseSelectForm(import_export, request=None, *args, **kwargs):
    class _DatabaseForm(forms.Form):
        default = DEFAULT_DB_ALIAS
        database = forms.ChoiceField(
            choices=get_database_choices(),
            label=_("Database"),
            help_text=_("Select the database you want to %(import_export)s from.") % {
                "import_export": import_export,
            },
            required=True,
        )

        @property
        def selected_database(self):
            cleaned_data = getattr(self, "cleaned_data", None)
            if not cleaned_data:
                return self.default
            return cleaned_data["database"]
        
    data = None
    if request:
        data = request.POST or None

    return _DatabaseForm(data, *args, **kwargs)

from django import forms

class PasswordRequiredForm(forms.Form):
    INVALID_ERROR_MESSAGE = _("The password you entered is incorrect.")

    password = forms.CharField(
        label=_("Account Password"),
        help_text=_("Enter your account password to perform this action."),
        required=True,
        widget=forms.PasswordInput(attrs={"autocomplete": "off"}),
    )

    def __init__(self, user, *args, password_correct: callable=None, **kwargs):
        self.user = user
        self.password_correct_callback = password_correct
        super().__init__(*args, **kwargs)

    def clean_password(self):
        password = self.cleaned_data["password"]
        if not self.user.check_password(password):
            raise forms.ValidationError(self.INVALID_ERROR_MESSAGE)
        return password

    def save(self):
        if not self.is_valid():
            raise forms.ValidationError(_("Form is not valid."))
        
        self.password_correct()
    
    def password_correct(self):
        if self.password_correct_callback:
            self.password_correct_callback()
        else:
            raise NotImplementedError("Subclasses must implement this method.")

class DatabaseDumpForm(PasswordRequiredForm):
    def password_correct(self):
        pass

class DatabaseDumpScheduleForm(WagtailAdminModelForm):

    interval = forms.ChoiceField(
        choices=DatabaseDumpSchedule.INTERVALS.choices,
        label=_("Interval"),
        help_text=_("Select the interval to run the database dump on."),
        required=True,
    )

    class Meta:
        model = DatabaseDumpSchedule
        fields = [
            "start_on",
            "interval",
            "period",
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["start_on"].widget.attrs["autocomplete"] = "off"
