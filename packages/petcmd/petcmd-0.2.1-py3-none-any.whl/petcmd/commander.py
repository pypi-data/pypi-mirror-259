
import sys
import inspect
import logging
import traceback
from types import GenericAlias
from typing import Callable, Iterable

from .argparser import ArgParser
from .command import Command
from .exceptions import CommandException
from .interface import Interface

class Commander:

	def __init__(self, error_handler: Callable[[Exception], None] = None, debug: bool = False):
		self.__error_handler = error_handler
		self.__config_logger(debug)
		self.__commands: list[Command] = []

		@self.command("help")
		def help_command(command: str = None):
			"""
			Show help message or usage message when command is specified.
			:param command: command for which instructions for use will be displayed
			"""
			self.__help_command(command)

	def command(self, cmd: str | Iterable[str]):
		def dec(func):
			for command in self.__commands:
				if command.match(cmd):
					self.__logger.debug(f"duplicate commands: {func.__name__}, {command.func.__name__}")
					raise CommandException(f"Duplicated command: {cmd}")
			for arg, typehint in inspect.getfullargspec(func).annotations.items():
				if isinstance(typehint, GenericAlias) and any(not isinstance(gen, type) for gen in typehint.__args__):
					self.__logger.debug(f"unsupported typehint: {func.__name__}:{arg} {typehint}")
					raise CommandException("Unsupported argument typehint: petcmd supports only first level generics")
			self.__logger.debug(f"append new command: {func.__name__} ({cmd})")
			self.__commands.append(Command(cmd, func))
			return func
		return dec

	def process(self):
		argv = sys.argv[1:]
		command = self.__find_command(argv[0] if len(argv) > 0 else "help")
		try:
			args, kwargs = ArgParser.parse(argv[1:], command)
			command.func(*args, **kwargs)
		except CommandException as e:
			print("\n" + str(e), end="\n\n")
			Interface.command_usage(command)
		except Exception as e:
			print(traceback.format_exc())
			if isinstance(self.__error_handler, Callable):
				self.__error_handler(e)

	def __find_command(self, cmd: str) -> Command:
		for command in self.__commands:
			if command.match(cmd):
				return command
		return self.__find_command("help")

	def __help_command(self, cmd: str = None):
		if cmd is not None and (command := self.__find_command(cmd)).match(cmd):
			Interface.command_usage(command)
		else:
			Interface.commands_list(self.__commands)

	def __config_logger(self, debug: bool = False):
		self.__logger = logging.getLogger("petcmd")
		if not debug:
			self.__logger.disabled = True
			return
		self.__logger.setLevel(logging.DEBUG)
		handler = logging.StreamHandler()
		handler.setLevel(logging.DEBUG)
		formatter = logging.Formatter('%(asctime)s %(name)s %(levelname)s: %(message)s',
			datefmt='%Y/%m/%d %H:%M:%S')
		handler.setFormatter(formatter)
		self.__logger.addHandler(handler)

