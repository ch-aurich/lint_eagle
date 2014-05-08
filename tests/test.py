from subprocess import call
import subprocess
import os

def run_lint_eagle_with_error(parameters):
  try:
    shutup = open(os.devnull, 'w')
    lint_eagle_process = subprocess.Popen(["python", "lint_eagle", parameters], stdout=shutup, stderr=shutup)
    stream_data = lint_eagle_process.communicate()[0]
    assert lint_eagle_process.returncode != 0
  except OSError as e:
    print "error executing: " + str(e)
    assert 0

def run_lint_eagle_without_error(parameters):
  try:
    shutup = open(os.devnull, 'w')
    lint_eagle_process = subprocess.Popen(["python", "lint_eagle", parameters], stdout=shutup, stderr=shutup)
    stream_data = lint_eagle_process.communicate()[0]
    assert lint_eagle_process.returncode == 0
  except OSError as e:
    print "error executing: " + str(e)
    assert 0

def test_commandline_interface():
  yield run_lint_eagle_with_error, "" 		#run without any arguments
  yield run_lint_eagle_without_error, "-h"		#run with argument to output the help screen
#TODO: implement more commandline interface tests

def test_E1():
  #TODO: load file and get XML tree
  #TODO: call E1 check function
  assert 0

def test_E2():
  #TODO: load file and get XML tree
  #TODO: call E2 check function
  assert 0

def test_E3():
  #TODO: load file and get XML tree
  #TODO: call E3 check function
  assert 0

def test_E4():
  #TODO: load file and get XML tree
  #TODO: call E4 check function
  assert 0

def test_W1():
  #TODO: load file and get XML tree
  #TODO: call W1 check function
  assert 0

def test_W3():
  #TODO: load file and get XML tree
  #TODO: call W3 check function
  assert 0


