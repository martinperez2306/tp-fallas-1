from experta import *
from diagnostic import *

class ReportModel(Fact):
    """Info about the medical report."""
    pass

class MedicalRobot(KnowledgeEngine):
    @Rule(OR(ReportModel(tos='TS'), ReportModel(tos='TE')), 
          OR(ReportModel(congestion='MA'), ReportModel(congestion='MV')),
          OR(ReportModel(fiebre='F'), ReportModel(fiebre='Fe'), ReportModel(fiebre='NF')))
    def infeccion_resfriado_comun(self):
        print("IRC")
        global diagnostic
        update_diagnostic("IRC")