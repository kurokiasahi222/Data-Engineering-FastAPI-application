import logging
import os
from global_utils import make_dir

CURRENT_FOLDER_NAME = os.path.dirname(os.path.abspath(__file__))


class Logger:
    def __init__(self, log_file_name: str, module_name: str):
        """
        :param log_file_name: name of the log file
        :param module_name: name of the module (can be kept same as the log_file_name without the extension)
        """
        # Create a custom logger
        self.logger = logging.getLogger(module_name)
        make_dir(directory=os.path.join(CURRENT_FOLDER_NAME, 'logs'))

        self.f_handler = logging.FileHandler(os.path.join(CURRENT_FOLDER_NAME, 'logs', log_file_name))

        # Create formatters and add it to handlers
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        # set the logging formatter to the f_handler
        self.f_handler.setFormatter(formatter)
        # setlevel to DEBUG && Add handlers to the logger
        self.logger.addHandler(self.f_handler)
        self.logger.setLevel(logging.DEBUG)

    def warning(self, msg):
        '''This level indicates something unexpected happened, 
        and it's usually indicative of some problem. 
        '''
        self.logger.warning(msg)

    def error(self, msg):
        '''This level indicates a more serious problem. 
        The software is unable to perform some function.'''
        self.logger.error(msg)

    def info(self, msg):
        ''' 
        This level is used to confirm things are working as expected. 
        '''
        self.logger.info(msg)

    def debug(self, msg):
        ''' 
        This level provides detailed information for diagnosing problems. 
        '''
        self.logger.debug(msg)


server_logger = Logger(log_file_name='server_logs.txt', module_name='server_logs')
main_logger = Logger(log_file_name='main_logs.txt', module_name='main_logs')



