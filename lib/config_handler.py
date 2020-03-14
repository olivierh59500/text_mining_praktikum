import os
import sys
import json


class ConfigException(Exception):
    pass


class Config:
    def __init__(self, config):
        self.__config = str()
        self.__mode = str()
        self.__source = str()
        self.__dump_text = False
        self.__output_dir = str()
        self.__hash_data = dict()

        self.load(config)

    @property
    def config(self):
        """ Path to config """
        return self.__config

    @config.setter
    def config(self, config):
        if os.path.isfile(str(config)):
            self.__config = config
        else:
            raise ConfigException("{} is not a file!".format(config))

    @property
    def mode(self):
        """ Selected hashing algorithm """
        return self.__mode

    @mode.setter
    def mode(self, __mode):
        self.__mode = __mode

    @property
    def source(self):
        """ Path to data archive """
        return self.__source

    @source.setter
    def source(self, __source):
        self.__source = __source

    @property
    def dump_text(self):
        """ Bool if text should be dumped too. Memory intense! """
        return self.__dump_text

    @dump_text.setter
    def dump_text(self, __dump_text):
        self.__dump_text = __dump_text

    @property
    def output_dir(self):
        """ Path to directory where the results are stored """
        return self.__output_dir

    @output_dir.setter
    def output_dir(self, __output_dir):
        self.__output_dir = __output_dir

    @property
    def hash_data(self):
        return self.__hash_data

    @hash_data.setter
    def hash_data(self, __hash_data):
        """ The additional data as dictionary used for the hashing algorithm """
        self.__hash_data = __hash_data

    @property
    def bool_map(self):
        return {"True": True, "False": False}

    def load(self, config):
        """
        This function is called on class-creation. It will load all config entries from the config file.
        All values loaded from the config are stored as class arguments.
        """
        print("#########################   CONFIG   #########################\n")

        for key, value in config.items():

            if hasattr(self, key):
                if key == "hash_data":
                    for _key, _value in value.items():
                        print("        {}: {}".format(_key, _value))
                else:
                    setattr(self, key, value)
                    print("    {}: {}".format(key, value))



        print("\n##############################################################")

    def dump(self):
        """
        This functions dumps the config into a string.

        :return: dict() - config as a dict.
        """
        ret = {"mode": self.mode, "source": self.source, "dump_text": self.dump_text, "output_dir": self.output_dir,
               "hash_data": self.hash_data}

        return ret
