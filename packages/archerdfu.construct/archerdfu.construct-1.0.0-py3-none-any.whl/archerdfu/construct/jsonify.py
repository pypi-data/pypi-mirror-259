import json
from io import BytesIO
from construct import Container


def remove_io_keys(data):
    if isinstance(data, dict):
        data = {
            key: remove_io_keys(value)  # Recursively process dictionary values
            for key, value in data.items()
            if key not in ['_io', '_flagsenum'] and not key.startswith('unused')  # Exclude keys with name '_io'
        }
    elif isinstance(data, list):
        data = [remove_io_keys(item) for item in data]  # Recursively process list items
    return data


class ContainerEncoder(json.JSONEncoder):
    def default(self, obj):

        if isinstance(obj, bytes):
            # Convert bytes to a string
            if obj.find(b'\x00') >= 0:
                obj = obj[:obj.index(b'\x00')]
            string = obj.decode('cp1251', errors='replace')
            return string
        elif isinstance(obj, BytesIO):
            # Convert BytesIO to a string
            # return obj.getvalue().decode('cp1251', errors='replace')[:10]
            return None
        return super().default(obj)


def jsonify(data: Container):
    return json.dumps(data, cls=ContainerEncoder)
