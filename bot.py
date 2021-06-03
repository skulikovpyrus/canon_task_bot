from pyrus import client
from pyrus.models.requests import FormRegisterRequest, TaskCommentRequest


class Bot:
	def __init__(self, login, secret, settings):
		self.login = login
		self.secret = secret
		self.settings = settings
		self.pyrusAPI = client.PyrusAPI(login=self.login, security_key=self.secret)
		self.authenticated = self.pyrusAPI.auth().success

		self.forms = self.get_forms()
		self.form_tasks = self.get_form_tasks()
		self.lists = self.get_lists()
		self.list_tasks = self.get_list_tasks()

	def get_forms(self):
		forms = self.pyrusAPI.get_forms().forms
		return forms

	def get_lists(self):
		lists = self.pyrusAPI.get_lists().lists
		return lists

	def get_list_tasks(self):
		tasks = {}
		if self.lists:
			for _list in self.lists:
				tasks[_list.id] = self.pyrusAPI.get_task_list(_list.id).tasks
			return tasks

	def get_form_tasks(self):
		tasks = {}
		request = FormRegisterRequest(include_archived=True)
		if self.forms:
			for form in self.forms:
				tasks[form.id] = self.pyrusAPI.get_registry(form.id, request).tasks
			return tasks

	def get_task(self, task_id):
		task = self.pyrusAPI.get_task(task_id).task
		return task

	def send_comment(self, **kwargs):
		comment = kwargs
		return comment
