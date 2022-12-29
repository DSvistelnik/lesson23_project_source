from service import FileService

class Request:

    def __init__(self, service: FileService, mapper: dict) -> None:
        self.service = service
        self.mapper = mapper

    def execute(self, **kwargs) -> str:

        task_1, value_1, task_2, value_2 = self._create(**kwargs)

        query_1 = f"self.service.{task_1}(value_1)"
        query_2 = f"self.service.{task_2}(value_2)"

        exec(query_1)
        exec(query_2)

        return self.service.get_result()

    def _create(self, **kwargs):
        self.service.add_new_file(kwargs['file'])

        task_1 = self.mapper[kwargs['cmd1']]
        task_2 = self.mapper[kwargs['cmd2']]
        value_1 = kwargs['value1']
        value_2 = kwargs['value2']

        return task_1, value_1, task_2, value_2

