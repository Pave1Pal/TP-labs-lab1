from DataReader import DataReader
from Types import DataType
import json


class JsonDataReader(DataReader):

    def read(self, path: str) -> DataType:
        students: DataType = {}
        with open(path, encoding='utf-8') as file:
            jsonStudents = json.loads(file.read())
            for name in jsonStudents:
                students[name] = []
                jsonSubjects = jsonStudents[name]

                for subj in jsonSubjects:
                    score = jsonSubjects[subj]
                    students[name].append((subj, int(score)))

        return students
