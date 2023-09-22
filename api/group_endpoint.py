''' this file contains the endpoints for group activities'''


@app_views.route('/api/<userId>/<groupId>', methods=['PUT'], strict_slashes=False)
def update_Group(userId, groupId):
    '''updates a group name'''

    if request.json():
        data = request.json()
        name = data['title']
        group = model.storage.query(Group, groupId).filter_by(group_id=groupId).first()
        group.title = name
        model.storage.save()
