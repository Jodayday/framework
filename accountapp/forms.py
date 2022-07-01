from django.contrib.auth.forms import UserCreationForm


class AccountUpdateForm(UserCreationForm):
    "update form comstom"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['username'].disabled = True
