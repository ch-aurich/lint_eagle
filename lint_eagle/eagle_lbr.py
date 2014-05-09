def lbr_check_name_and_value(eagle_object):
  library = eagle_object.drawing.library
  for package in library.packages.package:
    value_found = False
    value_layer = -1
    name_found = False
    name_layer = -1

    name = package.get('name')

    for text in package["text"]:
        if text == ">VALUE":
          value_found = True
          value_layer = text.get('layer')
        if text == ">NAME":
          name_found = True
          name_layer = text.get('layer')

    if (value_found == False):
      print ("for package " + name + " no \">VALUE\" could be found")
    if (name_found == False):
      print ("for package " + name + " no \">NAME\" could be found")
#TODO: check for correct layers - does this need to be done based on the layer definitions in the file?

