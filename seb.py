class seb:
    @staticmethod
    def run(file_name:str):
        exec(open(file_name).read())
