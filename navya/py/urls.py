import webapp2
from py import main

url_patterns = [
    webapp2.Route('/todo/feeddata', main.FeedData),
    webapp2.Route('/todo/user/<userid>', main.GetUser),
    webapp2.Route('/todo/checkpermission', main.Checkpermission),
    webapp2.Route('/todo/roles/<roleid>', main.ChangeRoles),
    webapp2.Route('/todo/permissions/<permission_id>', main.RemovePermission),

    ]
application = webapp2.WSGIApplication(url_patterns, debug=True)

#https://third-campus-168912.appspot.com/todo/feeddata
#https://third-campus-168912.appspot.com/todo/user?userId=user1
#https://third-campus-168912.appspot.com/todo/checkpermission?userId=user1&permissionid=perm2
#https://third-campus-168912.appspot.com/todo/checkpermission?userId=user1&permissionid=perm1
#https://third-campus-168912.appspot.com/todo/permissions/perm5