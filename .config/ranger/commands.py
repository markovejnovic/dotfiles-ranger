from ranger.api.commands import Command
import os
import subprocess


class fzf_select(Command):
    """
    :fzf_select
    Find a file using fzf.
    """
    def execute(self):
        fzf = self.fm.execute_command(r"fzf +m", stdout=subprocess.PIPE)
        stdout, _ = fzf.communicate()

        if fzf.returncode == 0:
            fzf_file = os.path.abspath(stdout.decode('utf-8').rstrip('\n'))

            if os.path.isdir(fzf_file):
                self.fm.cd(fzf_file)
            else:
                self.fm.select_file(fzf_file)
        else:
            self.fm.notify(f"Fzf failed with a return code {fzf.returncode}")
