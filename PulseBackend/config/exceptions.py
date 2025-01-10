from rest_framework.views import exception_handler
from django.utils.translation import gettext_lazy as _

def custom_exception_handler(exc, context):
    response = exception_handler(exc, context)

    if response is not None:
        response.data = {
            "reason": response.data.get("detail", _("An error occurred"))
        }

    return response
