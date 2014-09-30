class lint_issue:
  issue_type = ""
  number = 0
  text = ""
  context = ""
  def __init__(self, issue_type, number, context, text):
    self.issue_type = issue_type 
    self.number = number
    self.text = text
    self.context = context
  def __str__(self):
    string_representation = ""
    string_representation = str(self.issue_type) + \
                            str(self.number) + " " + \
                            str(self.context) + ": " + \
                            str(self.text)
    return string_representation
