class Diagnostic:
    def __init__(self, result):
        self.result = result

diagnostic = Diagnostic("INC")

def new_diagnostic():
  global diagnostic
  diagnostic.result = "INC"

def update_diagnostic(result):
  global diagnostic
  diagnostic.result = result