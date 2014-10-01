import lint_framework

def lbr_check_name_and_value_package(eagle_object, settings):
  issues = []

  #abort if eagle object is not a library
  if eagle_object.drawing.find("library") == None:
    return issues

  library = eagle_object.drawing.library
  for package in library.packages.package:
    value_found = False
    value_layer = -1
    name_found = False
    name_layer = -1

    name = package.get('name')

    text = package.find("text")
    if text is not None:
      for text in package["text"]:
          if text == ">VALUE":
            value_found = True
            value_layer = text.get('layer')
          if text == ">NAME":
            name_found = True
            name_layer = text.get('layer')

    if (value_found == False):
      issues.append(lint_framework.lint_issue("E", 2, "package " + name, "\">VALUE\" could not be found"))
    if (name_found == False):
      issues.append(lint_framework.lint_issue("E", 1, "package " + name, "\">NAME\" could not be found"))

    if (value_found and not int(value_layer) == 27):
      issues.append(lint_framework.lint_issue("E", 7, "package " + name, "\">VALUE\" is not on layer 27, tValues"))
    if (name_found and not int(name_layer) == 25):
      issues.append(lint_framework.lint_issue("E", 5, "package " + name, "\">NAME\" is not on layer 25, tNames"))
      
    #TODO: check for correct layers; does this need to be done based on the layer definitions in the file?

  return issues
