import glob, os, sys
test_files = glob.glob('*.py')
test_files.remove('run_all.py')
py_path = os.environ.get('PYTHONPATH')
if py_path is None:
    py_path = '.'
else:
    py_path = os.pathsep.join(['.',py_path])
os.environ['PYTHONPATH'] = py_path

for f in test_files:
    sys.stdout.write( "**********************************************\n")
    ff = os.path.join(sys.path[0],f)
    args = [sys.executable,ff]
    sys.stdout.write("Running %s\n" % f)
    status = os.spawnve(os.P_WAIT,sys.executable,args,os.environ)
    if status:
        sys.stdout.write('TEST FAILURE (status=%s)\n' % (status))
