import lint_framework

def brd_check_testpad_on_all_nets(eagle_object, settings):
  issues = []

  #abort if eagle object is not a board
  if eagle_object.drawing.find("board") == None:
    return issues

  testpads = []
  
  #find all parts on the PCB that are Testpads (i.e. have the attribute TP_SIGNAL_NAME)
  parts_on_brd = eagle_object.drawing.board.elements
  for part in parts_on_brd.element:
    if not part.find("attribute") == None:
      for part_attribute in part.attribute:
        if part_attribute.get('name')=="TP_SIGNAL_NAME":
          testpads.append(part.get('name'))

  signals_on_brd = eagle_object.drawing.board.signals
  for signal in signals_on_brd.signal:
    signal_contains_testpad = False
    if("contactref" in signal):
      for contactref in signal.contactref:
        if contactref.get('element') in testpads:
          signal_contains_testpad = True

    if not signal_contains_testpad:
      issues.append(lint_framework.lint_issue("W", 11, "signal " + signal.get("name"), "the signal does not contain a testpad"))

  return issues
