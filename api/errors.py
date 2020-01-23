from . import api
import json


@api.errorhandler(404)
def error(er):
    return json.dumps({"status": 404, "message": str(er.description)})


