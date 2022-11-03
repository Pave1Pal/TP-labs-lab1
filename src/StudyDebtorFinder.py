from Types import DataType


class StudyDebtorFinder:

    def find(self, students: DataType) -> list[str]:
        debtors: list[str] = []
        for name in students:
            subjectsInfo = students[name]
            hasDebt = False
            for subAndScore in subjectsInfo:
                score = subAndScore[1]
                if (score < 61):
                    hasDebt = True
            if hasDebt:
                debtors.append(name)
        return debtors
