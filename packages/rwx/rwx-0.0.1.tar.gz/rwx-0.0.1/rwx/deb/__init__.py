import cmd
import ps

cmd.need('debootstrap')

BOOTSTRAP_ARCHITECTURE = 'amd64'
BOOTSTRAP_VARIANT = 'minbase'


def bootstrap(root_path: str, suite: str, mirror_location: str):
    command = [
        ('debootstrap',),
        ('--arch', BOOTSTRAP_ARCHITECTURE),
        ('--variant', BOOTSTRAP_VARIANT),
        (suite,),
        (root_path,),
        (mirror_location,),
    ]
    completed_process = ps.run(command)
    return completed_process
