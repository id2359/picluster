from fabric.api import *

env.user = "pi"
env.hosts = ["pi1", "pi2", "pi3", "pi4"]


@task
def reboot():
	run("sudo reboot")
	
@task
def poweroff():
	run("sudo poweroff")

@task
@hosts(["pi1"])
def test_mpi():
	run("mpiexec -f pifile hostname")
	
@task
@hosts(['pi1'])
def mpiexec(prog="hostname"):
	run("mpiexec -f pifile %s" % prog)

@task
@hosts(['pi1'])
def spread(prog):
	run("spread %s" % prog)
		
@task
def hostname():
	run("hostname")
	
@task
def clean():
	attempt("rm *.o")
	attempt("rm *.tmp")
	
@task
def tidy():
	run("mytidy")

	
def attempt(cmd):
	try:
		run(cmd)
	except:
		pass
	
	
