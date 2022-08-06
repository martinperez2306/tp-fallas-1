from experta import *
from diagnostic import *
from enum import Enum

class ReportModel(Fact):
    """Info about the medical report."""
    pass

class SymptomModel(Enum):
    """Info about the symptom report."""
    TS= 0
    TE= 1
    NT= 2
    MA= 3
    MV= 4 
    P= 5
    NC= 6
    F= 7
    FE= 8
    NF= 9
    DG= 10
    NDG= 11
    S= 12
    NS= 13
    O= 14
    NO= 15
    H= 16
    NH= 17
    D= 18
    ND= 19
    DT= 20
    NDT= 21
    AS= 22
    NAS= 23
    AN= 24
    NAN= 25
    DI= 26
    NDI= 27

class PhysicalExplorationModel(Enum):
    """Info about the physical exploration report."""
    pass

class DisorderModel(Enum):
    """Info about the disorder report."""
    pass

class StudyModel(Enum):
    """Info about the study report."""
    PTN= 0
    PTM= 1
    HCA= 2
    HCP= 3
    HCN= 4
    TTN= 5
    TTM= 6
    EPN= 7
    EPA= 8

class MedicalRobot(KnowledgeEngine):
    @Rule(OR(Fact(SymptomModel.TS), Fact(SymptomModel.TE)), 
          OR(Fact(SymptomModel.MA), Fact(SymptomModel.MV)),
          OR(Fact(SymptomModel.F), Fact(SymptomModel.FE), Fact(SymptomModel.NF)),
          Fact(SymptomModel.DG),
          OR(Fact(StudyModel.HCA), Fact(StudyModel.HCN))
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
          OR(ReportModel(malestar_general='MG'), ReportModel(malestar_general='NMG')),
          OR(ReportModel(hisopado_covid='HCA'), ReportModel(hisopado_covid='HCN'))
          )
    def infeccion_rinusinusitis(self):
        print("IR")
        global diagnostic
        update_diagnostic("IR")

    @Rule(ReportModel(fiebre='F'),
          ReportModel(malestar_general='MG'),
          ReportModel(disnea='D'),
          OR(ReportModel(hisopado_covid='HCA'), ReportModel(hisopado_covid='HCP'))
          )
    def infeccion_covid_caso1(self):
        print("IC")
        global diagnostic
        update_diagnostic("IC")

    @Rule(ReportModel(fiebre='F'),
          ReportModel(malestar_general='MG'),
          ReportModel(disgeusia='DI'),
          OR(ReportModel(hisopado_covid='HCA'), ReportModel(hisopado_covid='HCP')),
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