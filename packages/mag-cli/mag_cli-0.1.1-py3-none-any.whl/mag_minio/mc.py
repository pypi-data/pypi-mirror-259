import click
import subprocess

def check_mc_admin_info(alias, insecure=True, verbose=False):
    # Construct the command
    insecure_arg = ""
    
    # If insecure arg is set, then add insecure flag
    if insecure:
        insecure_arg = '--insecure'

    command = f"mc admin info {alias} {insecure_arg}"
    click.echo(f"mc command: {command}")
    try:
        # Run the command and capture the output
        result = subprocess.run(command, shell=True, check=True, text=True, capture_output=True)

        # Check if the command was successful (return code 0)
        if result.returncode == 0:
            if verbose:
                print(f"Command successful. Output:\n{result.stdout}")
            return True
        else:
            print(f"Command failed. Error:\n{result.stderr}")
            return False

    except subprocess.CalledProcessError as e:
        print(f"Command failed with an exception:\n{e}")
        return False
