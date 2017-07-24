import webapp2
import json
import logging
from models import User,Roles,Permissions

class FeedData(webapp2.RequestHandler):
	def get(self):
		data = json.load(open('data.json'))
		if data:
		    for item in data["user_list"]:
		    	User.addItem(item["id"],item["roles"])

		    for item in data["role_list"]:
		    	Roles.addItem(item["id"],item["permissions"])

		    for item in data["permission_list"]:
		    	Permissions.addItem(item["id"],item["name"])

		    self.response.out.write("success")


class GetUser(webapp2.RequestHandler):
	def get(self, **kwargs):
		#username=self.request.get("userId")
		return_list=[];

		role_id=User.getItem(kwargs["userid"])

		id_list=[]
		for item in role_id:
			get_list=Roles.getItem(item)
			for x in get_list:
				id_list.append(x)


		for item in id_list:
			return_list.append(Permissions.getItem(item))

		
		self.response.out.write(return_list) 


class Checkpermission(webapp2.RequestHandler):
	def get(self):
		username=self.request.get("userId")
		permission=self.request.get("permissionid")

		role_id=User.getItem(username)

		id_list=[]
		for item in role_id:
			get_list=Roles.getItem(item)
			for x in get_list:
				id_list.append(x)

		if permission in id_list:
			self.response.out.write("True")
		else:
			self.response.out.write("False")


class ChangeRoles(webapp2.RequestHandler):
	def post(self,**kwargs):
		data=json.loads(self.request.body)		
		Roles.deleteItem(kwargs['roleid'])
		Roles.addItem(kwargs['roleid'],data["permissions"])
		self.response.out.write("Success")


class RemovePermission(webapp2.RequestHandler):
	def delete(self,**kwargs):

		Permissions.deleteItem(kwargs["permission_id"])
		Roles.deletePermission(kwargs["permission_id"])
			
		self.response.out.write("Success")
