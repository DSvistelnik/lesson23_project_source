from DAO import FileDao
from service import FileService
from checking_arguments import ArgumentsChecker
from request import Request
from constans import QUERY


dao = FileDao()
service = FileService(dao)
checker = ArgumentsChecker()
user_request = Request(service, QUERY)


