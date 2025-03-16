from hyprpy.utils.shell import run_or_fail
from hyprpy import Hyprland
import subprocess

instance = Hyprland()


def on_monitor_added(sender, **kwargs):
    id = kwargs["monitor_id"]
    name = kwargs["monitor_name"]
    description = kwargs["monitor_description"]
    print(f"Monitor connected: {id}, {name}, {description}")
    load_display_config()
    restart_bar()
    try_run(["notify-send", F"Monitor connected: {name}, {description}"])


def on_monitor_removed(sender, **kwargs):
    name = kwargs["monitor_name"]
    print(f"Monitor removed: {name}")
    restart_bar()
    try_run(["notify-send", F"Monitor removed: {name}"])


def restart_bar():
    try_run(["ags", "-q"])
    subprocess.Popen(["ags"], start_new_session=True, stdout=subprocess.DEVNULL,
                     stdin=subprocess.DEVNULL, stderr=subprocess.DEVNULL)


def try_run(args):
    try:
        run_or_fail(args)
    except:
        print(f"Command failed to run: {args}")


def load_display_config():
    print("Loading saved hyprdock config...")
    try_run(["hyprdock", "--import"])


instance.signals.monitoraddedv2.connect(on_monitor_added)
instance.signals.monitorremoved.connect(on_monitor_removed)
instance.watch()
