from experta import *
from diagnostic import *

class ReportModel(Fact):
    """Info about the medical report."""
    pass

class MedicalRobot(KnowledgeEngine):
    @Rule(OR(ReportModel(tos='TS'), ReportModel(tos='TE')), 
          OR(ReportModel(congestion='MA'), ReportModel(congestion='MV')),
          OR(ReportModel(fiebre='F'), ReportModel(fiebre='Fe'), ReportModel(fiebre='NF')),
          ReportModel(malestar_general='MG'),
          OR(ReportModel(hisopado_covid='HCA'), ReportModel(hisopado_covid='HCN'))
          )
    def infeccion_resfriado_comun(self):
        print("IRC")
        global diagnostic
        update_diagnostic("IRC")

    @Rule(OR(ReportModel(tos='TS'), ReportModel(tos='NT')), 
          OR(ReportModel(congestion='MA'), ReportModel(congestion='MV')),
          OR(ReportModel(fiebre='F'), ReportModel(fiebre='Fe'), ReportModel(fiebre='NF')),
          ReportModel(malestar_general='MG'),
          ReportModel(odinofagia='O'),
          ReportModel(ganglios_cervicales='GCI'),
          OR(ReportModel(hisopado_covid='HCA'), ReportModel(hisopado_covid='HCN'))
          )
    def infeccion_faringitis(self):
        print("IF")
        global diagnostic
        update_diagnostic("IF")

    @Rule(OR(ReportModel(congestion='MA'), ReportModel(congestion='MV'), ReportModel(congestion='P')),
          ReportModel(fiebre='F'),
          OR(ReportModel(malestar_general='MG'), ReportModel(malestar_general='NMG'))
          OR(ReportModel(hisopado_covid='HCA'), ReportModel(hisopado_covid='HCN'))
          )
    def infeccion_rinusinusitis(self):
        print("IR")
        global diagnostic
        update_diagnostic("IR")

    @Rule(ReportModel(fiebre='F'),
          ReportModel(malestar_general='MG')
          ReportModel(disnea='D')
          OR(ReportModel(hisopado_covid='HCA'), ReportModel(hisopado_covid='HCP'))
          )
    def infeccion_covid_caso1(self):
        print("IC")
        global diagnostic
        update_diagnostic("IC")

    @Rule(ReportModel(fiebre='F'),
          ReportModel(malestar_general='MG')
          ReportModel(disgeusia='DI')
          OR(ReportModel(hisopado_covid='HCA'), ReportModel(hisopado_covid='HCP'))
          )
    def infeccion_covid_caso2(self):
        print("IC")
        global diagnostic
        update_diagnostic("IC")

    @Rule(OR(ReportModel(tos='TS'), ReportModel(tos='TE')), 
          OR(ReportModel(hemoptitis='H'), ReportModel(hemoptitis='NH')),
          ReportModel(disnea='D'),
          ReportModel(dolor_toracico='DT'),
          ReportModel(astenia='AS'),
          OR(ReportModel(hisopado_covid='HCA'), ReportModel(hisopado_covid='HCP'))
          )
    def infeccion_bronquitis(self):
        print("IB")
        global diagnostic
        update_diagnostic("IB")