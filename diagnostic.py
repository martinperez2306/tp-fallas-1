class Diagnostic:
    def __init__(self, result):
        self.result = result

diagnostic = Diagnostic("No concluyente")

def new_diagnostic():
  global diagnostic
  diagnostic.result = "No concluyente"

def update_diagnostic(result):
  global diagnostic
  diagnostic.result = result