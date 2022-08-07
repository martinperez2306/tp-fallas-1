from ctypes.wintypes import MSG
from experta import *
from diagnostic import *
from enum import Enum

class ReportModel(Fact):
    """Info about the medical report."""
    pass

### >>>>>> SINTOMAS <<<<<<
class SymptomModel(Enum):
    """Info about the symptom report."""
    TS = 0   # tos seca
    TE = 1   # tos expectoracion
    NT = 2   # sin tos
    MA = 3   # moco acuoso
    MV = 4   # moco verde
    P = 5    # pus
    NC = 6   # sin congestion
    NF = 7   # sin fiebre
    FE = 8   # febricula
    F = 9    # fiebre
    MG = 10  # malestar general
    NMG = 11 # sin malestar general
    S = 12   # sibilancias
    NS = 13  # sin sibilancias
    O = 14   # odinofagia
    NO = 15  # sin odinofagia
    H = 16   # hemoptisis
    NH = 17  # sin hemoptisis
    D = 18   # disnea
    ND = 19  # sin disnea
    DT = 20  # dolor toraxico
    NDT = 21 # sin dolor toraxico
    AS = 22  # astenia
    NAS = 23 # sin astenia
    AN = 24  # anosmia
    NAN = 25 # sin anosmia
    DI = 26  # disgeusia
    NDI = 27 # sin disgeusia
    TMA = 28 # tiempo mayor 2 semanas
    TME = 29 # tiempo menor a 2 semanas

### >>>>>> EXPLORACION <<<<<<
class PhysicalExplorationModel(Enum):
    """Info about the physical exploration report."""
    PN = 0   # pulsioximetría normal
    PA = 1   # pulsioximetría anormal
    CPA = 2  # coloracion piel azulada
    CPN = 3  # coloracion piel normal
    FN = 4   # frecuencia respiratoria normal
    FB = 5   # frecuencia respiratoria baja
    FA = 6   # frecuencia respiratoria alta
    GCN = 7  # ganglios cervicales normal
    GCI = 8  # ganglios cervicales inflamados
    RRN = 9  # ruidos respiratorios normales
    RRA = 10 # ruidos respiratorios anormales

### >>>>>> TRASTORNOS <<<<<<
class DisorderModel(Enum):
    """Info about the disorder report."""
    A = 0    # asma
    NA = 1   # sin asma
    EP = 2   # epoc
    NEP = 3  # sin epoc
    BR = 4   # bronquiectasias
    NBR = 5  # sin bronquiectasias
    TU = 6   # tuberculosis
    NTU = 7  # sin tuberculosis
    DI = 8   # diabetes
    NDI = 9  # sin diabetes
    CA = 10  # cardiopatia
    NCA = 11 # sin cardiopatia

### >>>>>> ESTUDIOS <<<<<<
class StudyModel(Enum):
    """Info about the study report."""
    PTN = 0  # placa torax normal
    PTM = 1  # placa torax manchas
    HCA = 2  # hisopado ausente
    HCP = 3  # hisopado positivo
    HCN = 4  # hisopado negativo
    TTN = 5  # tomografia torax normal
    TTM = 6  # tomografia torax manchas
    EPN = 7  # espirometria normal
    EPA = 8  # espirometria anormal

class MedicalRobot(KnowledgeEngine):
    @Rule(OR(Fact(SymptomModel.TS), Fact(SymptomModel.TE)), 
          OR(Fact(SymptomModel.MA), Fact(SymptomModel.MV)),
          OR(Fact(SymptomModel.F), Fact(SymptomModel.FE), Fact(SymptomModel.NF)),
          Fact(SymptomModel.D),
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