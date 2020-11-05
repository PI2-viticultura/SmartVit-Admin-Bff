def create_response(result, status, response):
    response.status_code = status
    if isinstance(result, dict) or isinstance(result, list):
        return result
    elif isinstance(result, str):
        if status >= 400:
            result = {"error": result}
    else:
        result = {"error": "Something gone wrong"}

    return result
