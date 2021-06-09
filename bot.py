class Bot:
    def __init__(self, settings, task):
        self.settings = settings
        self.task = task
        self.task_list_ids = self.task["list_ids"]
        self.form_steps = self.settings["steps"]
        self.steps_sublists = list(self.form_steps.values())

    def check_task(self):
        current_step = self.task["current_step"]
        necessary_sublist_id = self.form_steps[str(current_step)]
        filtered_steps_sublists = [_list for _list in self.steps_sublists if _list != necessary_sublist_id]

        if necessary_sublist_id not in self.task_list_ids:
            response = {"added_list_ids": [necessary_sublist_id]}

            if self.list_ids_has_prev_sublist(filtered_steps_sublists):
                prev_sublist_id = self.get_prev_sublist_id()
                response["removed_list_ids"] = [prev_sublist_id]
                return response
            return response

    # метод проверяет есть ли в массиве идентификаторов списков старые предыдущие подсписки
    def list_ids_has_prev_sublist(self, another_sublists):
        return any(map(lambda x: x in self.task_list_ids, another_sublists))

    # метод возвращает идентификатор предыдущего подсписка
    def get_prev_sublist_id(self):
        for sublist_id in self.steps_sublists:
            if sublist_id in self.task_list_ids:
                return sublist_id
