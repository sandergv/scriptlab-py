import json
from scriptlab import Scriptlab

sl = Scriptlab()
sl.context.set('test', 1)
sl.context.delete('test')

res = {
    "status": True,
    "message": "todo ok"
}

sl.log('log test')

sl.response(json.dumps(res))
