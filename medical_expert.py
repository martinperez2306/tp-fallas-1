from ctypes.wintypes import MSG
from experta import *
from diagnostic import *
from enum import Enum

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
    PN = 100   # pulsioximetría normal
    PA = 101   # pulsioximetría anormal
    CPA = 102  # coloracion piel azulada
    CPN = 103  # coloracion piel normal
    FN = 104   # frecuencia respiratoria normal
    FB = 105   # frecuencia respiratoria baja
    FA = 106   # frecuencia respiratoria alta
    GCN = 107  # ganglios cervicales normal
    GCI = 108  # ganglios cervicales inflamados
    RRN = 109  # ruidos respiratorios normales
    RRA = 110  # ruidos respiratorios anormales

### >>>>>> TRASTORNOS <<<<<<
class DisorderModel(Enum):
    """Info about the disorder report."""
    A = 201    # asma
    NA = 202   # sin asma
    EP = 203   # epoc
    NEP = 204  # sin epoc
    BR = 205   # bronquiectasias
    NBR = 206  # sin bronquiectasias
    TU = 207   # tuberculosis
    NTU = 208  # sin tuberculosis
    DB = 209   # diabetes
    NDB = 210  # sin diabetes
    CA = 211   # cardiopatia
    NCA = 212  # sin cardiopatia

### >>>>>> ESTUDIOS <<<<<<
class StudyModel(Enum):
    """Info about the study report."""
    PTN = 300  # placa torax normal
    PTM = 301  # placa torax manchas
    HCA = 302  # hisopado ausente
    HCP = 303  # hisopado positivo
    HCN = 304  # hisopado negativo
    TTN = 305  # tomografia torax normal
    TTM = 306  # tomografia torax manchas
    EPN = 307  # espirometria normal
    EPA = 308  # espirometria anormal

### >>>>>> DIAGNOSTICO <<<<<<
class DiagnosticModel(Enum):
    """Info about the study report."""
    IRC = "IRC"  # Infeccion Resfriado Comun
    IF = "IF"    # Infeccion Faringitis
    IR = "IR"    # Infeccion Rinosinusitis
    IC = "IC"    # Infeccion COVID
    IB = "IB"    # Infeccion B
    DER = "DER"  # Derivación neumonologo

class MedicalRobot(KnowledgeEngine):
    # REGLA 1
    @Rule(OR(Fact(SymptomModel.TS), Fact(SymptomModel.TE)),
          OR(Fact(SymptomModel.MA), Fact(SymptomModel.MV)),
          OR(Fact(SymptomModel.F), Fact(SymptomModel.FE), Fact(SymptomModel.NF)),
          Fact(SymptomModel.MG),
          OR(Fact(StudyModel.HCA), Fact(StudyModel.HCN))
          )
    def infeccion_resfriado_comun(self):
        global diagnostic
        update_diagnostic(DiagnosticModel.IRC)

    # REGLA 2
    @Rule(OR(Fact(SymptomModel.TS), Fact(SymptomModel.NT)), 
          OR(Fact(SymptomModel.MA), Fact(SymptomModel.MV)),
          OR(Fact(SymptomModel.F), Fact(SymptomModel.FE), Fact(SymptomModel.NF)),
          Fact(SymptomModel.MG),
          Fact(SymptomModel.O),
          Fact(PhysicalExplorationModel.GCI),
          OR(Fact(StudyModel.HCA), Fact(StudyModel.HCN))
          )
    def infeccion_faringitis(self):
        global diagnostic
        update_diagnostic(DiagnosticModel.IF)
    
    # REGLA 3
    @Rule(OR(Fact(SymptomModel.MA), Fact(SymptomModel.MV), Fact(SymptomModel.P)),
          Fact(SymptomModel.F),
          OR(Fact(SymptomModel.MG), Fact(SymptomModel.NMG)),
          OR(Fact(StudyModel.HCA), Fact(StudyModel.HCN))
          )
    def infeccion_rinusinusitis(self):
        global diagnostic
        update_diagnostic(DiagnosticModel.IR)

    # REGLA 4
    @Rule(Fact(SymptomModel.F),
          Fact(SymptomModel.MG),
          Fact(SymptomModel.D),
          OR(Fact(StudyModel.HCA), Fact(StudyModel.HCP))
          )
    def infeccion_covid_caso1(self):
        global diagnostic
        update_diagnostic(DiagnosticModel.IC)

    # REGLA 5
    @Rule(Fact(SymptomModel.F),
          Fact(SymptomModel.MG),
          Fact(SymptomModel.DI),
          OR(Fact(StudyModel.HCA), Fact(StudyModel.HCP))
          )
    def infeccion_covid_caso2(self):
        global diagnostic
        update_diagnostic(DiagnosticModel.IC)

    # REGLA 6
    @Rule(OR(Fact(SymptomModel.TS), Fact(SymptomModel.TE)), 
          OR(Fact(SymptomModel.H), Fact(SymptomModel.NH)),
          Fact(SymptomModel.D),
          Fact(SymptomModel.DT),
          Fact(SymptomModel.AS),
          OR(Fact(StudyModel.HCA), Fact(StudyModel.HCP))
          )
    def infeccion_bronquitis(self):
        global diagnostic
        update_diagnostic(DiagnosticModel.IB)

    # REGLA 7
    @Rule(OR(Fact(SymptomModel.TMA), Fact(DisorderModel.A), Fact(DisorderModel.EP), Fact(DisorderModel.BR)),
          Fact(DisorderModel.TU),Fact(DisorderModel.DB),Fact(DisorderModel.CA))
    def derivacion_neumonologo(self):
        global diagnostic
        update_diagnostic(DiagnosticModel.DER)

    # REGLA 8
    @Rule(OR(Fact(StudyModel.PTM), Fact(StudyModel.TTM)))
    def derivacion_neumonologo(self):
        global diagnostic
        update_diagnostic(DiagnosticModel.DER)