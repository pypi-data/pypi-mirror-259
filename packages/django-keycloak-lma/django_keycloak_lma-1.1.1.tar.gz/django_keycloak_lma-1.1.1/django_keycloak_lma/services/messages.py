EXPIRED_SIGNATURE_ERROR = 'failed to authenticate due to an expired access token'
JWT_CLAIMS_ERROR = 'failed to authenticate due to failing claim checks'
JWT_ERROR = 'failed to authenticate due to a malformed access token'


def get_backend_message(backend, message):
    return f"{backend}: {message}"


def get_backend_message_with_error(backend, message, error):
    return f"{backend}: {message}: {error}"
