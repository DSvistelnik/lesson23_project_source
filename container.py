from DAO import FileDao
from service import FileService
from checking_arguments import ArgumentsChecker


dao = FileDao()
service = FileService(dao)
checker = ArgumentsChecker()


