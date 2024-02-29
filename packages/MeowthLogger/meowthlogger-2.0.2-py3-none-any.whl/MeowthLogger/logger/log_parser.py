import datetime
import io
import os
import re

from ..errors import (
    NotDateLogString,
    NotValidLogsDateFormat
)
from ..constants import (
    REQUEST_DATESTRING_FORMAT,
    LOGSTRING_DATE_FORMAT,
    FOLDER_DATE_FORMAT,
    FILE_DATE_FORMAT
)
from .settings import LoggerSettings

class LogParser:
    settings: LoggerSettings

    @staticmethod
    def convert_request_datestring(request_date_string):
        try:
            d = datetime.datetime.strptime(request_date_string, REQUEST_DATESTRING_FORMAT)
            return d
        except:
            raise NotValidLogsDateFormat

    @staticmethod
    def get_date_from_log_string(log_string):
        log_string = log_string.decode("utf-8")
        date_pattern = re.compile(r'\[(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2})\]')
        match = date_pattern.search(log_string)
        if not match:
            raise NotDateLogString
        return datetime.datetime.strptime(
            match.group(1), 
            LOGSTRING_DATE_FORMAT
        )

    @staticmethod
    def date_by_foldername(foldername):
        return datetime.datetime.strptime(
            foldername, 
            FOLDER_DATE_FORMAT
        )

    @staticmethod
    def date_by_filename(foldername, filename):
        return datetime.datetime.strptime(
            f"{foldername} {filename.split('-')[0]}",
            f"{FOLDER_DATE_FORMAT} {FILE_DATE_FORMAT}"
        )

    def iterate_folders(self, reverse=False, start_with=None):
        folders_list = os.listdir(self.settings.path)
        try:
            folders_list.remove(self.settings.filename)
        except:
            pass

        folders_list = sorted(folders_list, key=lambda foldername: self.date_by_foldername(foldername))

        try:
            idx = folders_list.index(start_with)
            folders_list = folders_list[idx::]
        except:
            pass

        if reverse:
            folders_list.reverse()

        for foldername in folders_list:
            yield foldername

    def get_foldername_from(self, date):
        current_folder = None
        for foldername in self.iterate_folders(reverse=True):
            if self.date_by_foldername(foldername) < date:
                return foldername
            else:
                current_folder = foldername
            
            return current_folder


    def iterate_files(self, foldername, reverse=False, start_with=None):
        files_list = os.listdir(
            os.path.join(self.settings.path, foldername)
        )

        files_list = sorted(files_list, key=lambda filename: self.date_by_filename(foldername, filename))

        try:
            idx = files_list.index(start_with)
            files_list = files_list[idx::]
        except:
            pass

        if reverse:
            files_list.reverse()

        for filename in files_list:
            yield filename

    def get_filename_from(self, date, foldername):
        for filename in self.iterate_files(foldername, reverse=True):
            if self.date_by_filename(foldername, filename) < date:
                return filename



    def iterate_log_file_paths(self, date_from):
        foldername_from = self.get_foldername_from(date_from)
        
        if foldername_from:
            filename_from = self.get_filename_from(date_from, foldername_from)
            for foldername in self.iterate_folders(start_with=foldername_from):
                for filename in self.iterate_files(foldername, start_with=filename_from):
                    yield(os.path.join(self.settings.path, foldername, filename))

        yield(os.path.join(self.settings.path, self.settings.filename))

    @staticmethod
    def iterate_file_lines(filename):
        with open(filename, "rb") as file:
            while True:
                line = file.readline()
                if not line:
                    break
                yield line

    def is_logs_exists(self):
        return os.path.exists(self.settings.path), 

    def stream_logs(self, date_from, date_to = None):
        logs_BIO = io.BytesIO()

        date_from = self.convert_request_datestring(date_from)
        if date_to:
            date_to = self.convert_request_datestring(date_to)

        date_from_flag = False
        date_to_flag = False

        for logs_path in self.iterate_log_file_paths(date_from):
            if date_to_flag:
                break
            for line in self.iterate_file_lines(logs_path):
                if not date_from_flag:
                    try:
                        date = self.get_date_from_log_string(line)
                    except NotDateLogString:
                        continue
                    if date < date_from:
                        continue
                    date_from_flag = True

                if date_to:
                    try:
                        date = self.get_date_from_log_string(line)
                        if date > date_to:
                            date_to_flag=True
                            break
                    except NotDateLogString:
                        pass            
                logs_BIO.write(line)
        logs_BIO.seek(0)
        return logs_BIO