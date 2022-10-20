from Types import DataType
from StudyDebtorFinder import StudyDebtorFinder
import pytest


class TestDebtorFinder:

    @pytest.fixture()
    def input_data(self) -> DataType:
        studentsInfo: DataType = {}
        studentsInfo["Вася Пупков"] = [
            ('Выш мат', 80),
            ('Философия', 60),
            ('Ракетопуляние', 54)
        ]
        studentsInfo["Илон Маск"] = [
            ('Кириловеденье', 90),
            ('Квантовая физика', 100),
            ('Ракетостроение', 61)
        ]
        return studentsInfo

    def test_find_debtor(self, input_data: DataType):
        debtorFinder = StudyDebtorFinder()
        debtors = debtorFinder.find(input_data)
        assert len(debtors) == 1
        assert "Вася Пупков" == debtors[0]
