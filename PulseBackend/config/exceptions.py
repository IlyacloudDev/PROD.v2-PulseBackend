from rest_framework.views import exception_handler
from rest_framework.exceptions import ErrorDetail
from django.utils.translation import gettext_lazy as _

def custom_exception_handler(exc, context):
    """
    Custom exception handler to format all errors as {"reason": [...]},
    with a list of error messages.
    """
    response = exception_handler(exc, context)

    if response is not None:
        if "detail" in response.data:
            reason = [response.data["detail"]]
        elif isinstance(response.data, dict):
            errors = []
            for field, messages in response.data.items():
                if isinstance(messages, list):
                    errors.extend(messages)
                elif isinstance(messages, (str, ErrorDetail)):
                    errors.append(str(messages))
            reason = errors
        else:
            reason = [_("An unexpected error occurred.")]
        response.data = {
            "reason": reason
        }

    return response
