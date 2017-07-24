from google.appengine.ext import ndb
import logging
from datetime import datetime


class User(ndb.Model):	
	user_name = ndb.StringProperty()
	role_name = ndb.JsonProperty()#StringProperty(required=True)# required=True denotes that it can accept multiple values

	@classmethod
	def addItem(self, user_name, role_name):
		obj=self(user_name=user_name, role_name=role_name)
		obj.put()

	@classmethod
	def getItem(self,user_name):
		obj=User.query(User.user_name==user_name).get()
		return obj.role_name


class Roles(ndb.Model):	
	role_name = ndb.StringProperty()
	permission_id = ndb.JsonProperty()#StringProperty(required=True)# required=True denotes that it can accept multiple values

	@classmethod
	def addItem(self, role_name, permission_id):
		obj=self(role_name=role_name, permission_id=permission_id)
		obj.put()

	@classmethod
	def getItem(self,role_name):
		obj=self.query(Roles.role_name==role_name).get()
		return obj.permission_id

	@classmethod
	def deleteItem(self, role_name):
		obj=Roles.query(Roles.role_name==role_name).get()
		if obj:
			obj.key.delete()

	@classmethod
	def deletePermission(self, permission_id):
		objs=Roles.query()
		for obj in objs:
			if permission_id in obj.permission_id:
				obj.permission_id.remove(permission_id)	
				obj.put()


class Permissions(ndb.Model):	
	permission_name = ndb.StringProperty()
	permissions = ndb.StringProperty()

	@classmethod
	def addItem(self, permission_name, permissions):
		obj=self(permission_name=permission_name, permissions=permissions)
		obj.put()

	@classmethod
	def getItem(self,permission_name):
		obj=self.query(Permissions.permission_name==permission_name).get()
		return obj.permissions

	@classmethod
	def deleteItem(self, permission_name):
		obj=Permissions.query(Permissions.permission_name==permission_name).get()
		logging.info(obj)
		if obj:
			obj.key.delete()
