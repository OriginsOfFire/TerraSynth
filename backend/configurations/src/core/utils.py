import json

from bson import ObjectId, json_util


def encode_object_id(to_encode: ObjectId):
    return json.loads(json_util.dumps(to_encode))
