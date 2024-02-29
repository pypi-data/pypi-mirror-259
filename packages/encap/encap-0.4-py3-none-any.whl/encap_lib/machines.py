import subprocess
import threading
from multiprocessing.pool import ThreadPool
import os
from getpass import getuser
import encap_lib.encap_settings as settings

class Machine:
    def __init__(self):
        self.sync = False

    def write_file(self, name, content, *args, **kwargs):
        command = f"""
        echo -e {repr(content)} > "{name}"
        """
        return self.run_code(command, *args, **kwargs)
    
    def tar(self, directory, parallel=True, verbose=False, subfolders=False, threads=1):
        if subfolders:
            # Create a list of all subfolders
            dirs = self.run_code(f"find {directory} -maxdepth 1 -type d")[1:]
            if threads == 1:
                for d in dirs:
                    if d != "" and d != directory:
                        out = self.tar(d, parallel=parallel, verbose=verbose, subfolders=False)
            else:
                threads = min(threads, len(dirs))
                pool = ThreadPool(threads)
                out = pool.map(lambda x: self.tar(x, parallel=parallel, verbose=verbose, subfolders=False), dirs)
        else:
            if verbose:
                print(f"Creating tar file {directory}.tar.gz")
            if parallel:
                out = self.run_code(f"tar --use-compress-program=pigz -cf {directory}.tar.gz {directory}")
            else:
                out = self.run_code(f"tar -czf {directory}.tar.gz {directory}")
            
            self.run_code(f"rm -rf {directory}")
        return out
    
    def untar(self, directory, parallel=True, verbose=False, subfiles=False, threads=1):
        if subfiles:
            files = self.run_code(f"find {directory} -maxdepth 1 -type f -name '*.tar.gz'")
            folders = [f[:-7] for f in files]
            if threads == 1:
                for f in folders:
                    if f != "":
                        out = self.untar(f, parallel=parallel, verbose=verbose, subfiles=False)
            else:
                threads = min(threads, len(folders))
                pool = ThreadPool(threads)
                out = pool.map(lambda x: self.untar(x, parallel=parallel, verbose=verbose, subfiles=False), folders)
        else:
            if verbose:
                print(f"Extracting tar file {directory}.tar.gz")
            if parallel:
                out = self.run_code(f"tar --use-compress-program=pigz -xf {directory}.tar.gz")
            else:
                out = self.run_code(f"tar -xzf {directory}.tar.gz")
            self.run_code(f"rm -f {directory}.tar.gz")
        return out

    def run_code(self, command, *args, **kwargs):
        pass

    def push(self, name_local, name_target, directory=True, *args, **kwargs):
        pass

    def pull(self, name_vm, name_local, directory=False, *args, **kwargs):
        pass

    def sync_files(self):
        pass

    def exists(self, name):
        code = f"""
        if [ -e "{name}" ]; then
            echo "True"
        else
            echo "False"
        fi
        """
        return self.run_code(code)[0] == "True"

class SSHMachine(Machine):

    def __init__(self, ip, username, local_project_dir, remote_project_dir, ssh_options="",
                ssh_ignore=[], sync_files=[], rsync_exclude=[], sync=True, **kwargs):
        super().__init__(**kwargs)
        self.ip = ip
        self.username = username
        self.local_project_dir = local_project_dir
        self.remote_project_dir = remote_project_dir
        self.ssh_options = ssh_options
        self.ssh_ignore = ssh_ignore
        self._sync_files = sync_files
        self.rsync_exclude = rsync_exclude
        self.sync = sync

    @property
    def user(self):
        return self.username

    def run_code(self, command, *args, **kwargs):
        command = f"""
        source /etc/profile
        source ~/.bashrc
        cd {self.remote_project_dir}
        """ + command

        # Write command to txt file
        with open(settings.temp_file, "w") as text_file:
            text_file.write(command)

        if ("debug" in kwargs and kwargs["debug"]) or settings.debug:
            print(command)


        c = f"ssh {self.ssh_options} {self.username}@{self.ip}  'bash -s' < {settings.temp_file}"
        if "ignore" in kwargs:
            ignore = self.ssh_ignore + kwargs["ignore"]
            del kwargs["ignore"]
        else:
            ignore = self.ssh_ignore

        output = run_code_local(c, ignore=ignore, *args, **kwargs)
        return output

    def push(self, name_local, name_target, directory=True, *args, **kwargs):
        # Upload file to VM
        if not self.sync and name_local == name_target:
            return None

        i = name_target[::-1].find("/")
        if i == -1:
            folder = ""
        else:
            i = len(name_target) - i - 1
            folder = name_target[:i]

            code = f"mkdir -p {folder}"
            self.run_code(code, *args, **kwargs)

        if directory:
            recursiv = "-r"
        else:
            recursiv = ""

        code = f"scp {self.ssh_options} {recursiv} {self.local_project_dir}/{name_local} {self.username}@{self.ip}:{self.remote_project_dir}/{folder}"
        return run_code_local(code, *args, **kwargs)

    def pull(self, file_name_vm, file_name_local, directory=False, *args, **kwargs):
        # Download file from VM
        #assert name_local != ""
        if not self.sync and file_name_vm == file_name_local:
            return None

        i = file_name_local[::-1].find("/")
        if i == -1:
            folder = ""

        else:
            i = len(file_name_local) - i - 1
            folder = file_name_local[: i]

            code = f"mkdir -p {folder}"
            run_code_local(code, *args, **kwargs)

        if directory:
            recursiv = "-r"
        else:
            recursiv = ""

        code = f"scp {self.ssh_options} {recursiv} {self.username}@{self.ip}:{self.remote_project_dir}/{file_name_vm} {self.local_project_dir}/{folder}"
        run_code_local(code, *args, **kwargs)

    def rsync_push(self, name_local, name_target, directory=True, dry_run=False, last_timestamp_prevails=True, delete=False, *args, **kwargs):
        # Upload file to VM

        i = name_target[::-1].find("/")
        if i == -1:
            folder = ""
        else:
            i = len(name_target) - i - 1
            folder = name_target[:i]

            code = f"mkdir -p {folder}"
            self.run_code(code, *args, **kwargs)

        if directory:
            options = "-rz"
        else:
            options = "-z"

        if dry_run:
            options = "--dry-run " + options

        if last_timestamp_prevails:
            options = "--update " + options

        if delete:
            options = "--delete " + options

        for exclude in self.rsync_exclude:
            options = f"--exclude '{exclude}' " + options

        code = f"""rsync {options} -v -e "ssh {self.ssh_options}" {self.local_project_dir}/{name_local} {self.username}@{self.ip}:{self.remote_project_dir}/{folder}"""
        return run_code_local(code, *args, **kwargs)

    def sync_files(self):
        for line in self._sync_files:
            self.rsync_push(line, line, last_timestamp_prevails=True, directory=True,
                            verbose=True, ignore=self.ssh_ignore + ["sending incremental", "sent ", "total size"])

    def interactive_ssh(self):
        command = f"ssh {self.ssh_options} {self.username}@{self.ip}"

        if settings.debug:
            print(command)
        os.system(command)



class LocalMachine(Machine):
    def __init__(self, local_project_dir, **kwargs):
        self.local_project_dir = local_project_dir
        self.username = getuser()
        super().__init__(**kwargs)

    def run_code(self, command, *args, **kwargs):

        command = f'''cd {self.local_project_dir}
         ''' + command

        return run_code_local(command, *args, **kwargs)

    def push(self, name_local, name_target, directory=True, copy_full_dir=True, *args, **kwargs):
        if name_local != name_target:
            # Copy file

            i = name_target[::-1].find("/")
            if i == -1:
                folder = ""
            else:
                i = len(name_target) - i - 1
                folder = name_target[:i]

                code = f"mkdir -p {folder}"
                run_code_local(code, *args, **kwargs)

            if directory:
                recursiv = "-r"
                if not copy_full_dir:
                    name_local += "/."
            else:
                recursiv = ""

            code = f"cp {recursiv} {self.local_project_dir}/{name_local} {self.local_project_dir}/{folder}"
            run_code_local(code, *args, **kwargs)

    def pull(self, name_vm, name_local, directory=False, *args, **kwargs):
        pass

    def sync_files(self):
        pass


def run_code_local(command, output=True, verbose=False, wait=True, ignore_errors=False, debug=False, ignore=[]):
    if settings.debug:
        debug = True

    if debug: print(command)
    p = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, executable="/bin/bash")
    if wait == False:
        return p.pid

    if output:
        try:
            lines = []
            #for line in p.stdout.readlines():
            for line in p.stdout:
                lll = line.decode("utf-8")[:-1]
                if not should_it_be_ignored(lll, ignore):
                    if verbose: print(lll)
                    lines.append(lll)
            retval = p.wait()
        except KeyboardInterrupt:
            p.kill()
            exit()

        if not ignore_errors and p.returncode != 0:
            raise Exception(f"""An error ocured while executing: {command} 
{lines}""")

        return lines

    else:
        return p.pid


def should_it_be_ignored(string, ignore):
    l = len(string)
    for i, si in enumerate(ignore):
        ls = len(si)
        #print(si == string[:min(ls,l)])
        #print(si, string[:min(ls,l)])
        if l >= ls and si == string[:ls]:
            return True
    return False