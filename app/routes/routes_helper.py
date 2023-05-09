from flask import abort, make_response


def get_valid_item_by_id(model, id):
    try:
        task_id = int(id)
    except:
        abort(make_response({"details": "Invalid data"}, 400))
    
    item = model.query.get(id)
    
    return item if item else abort(make_response({'msg': f"No {model.__name__.lower()} with id {id}"}, 404))
