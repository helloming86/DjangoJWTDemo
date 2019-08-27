from rest_framework import status


def jwt_response_payload_handler(token, user=None, request=None):
    return {
        'code': status.HTTP_200_OK,
        'message': '',
        'result': {
            'token': token,
            'user_id': user.id,
            'username': user.username
        }
    }
