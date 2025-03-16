from hyprpy.utils.shell import run_or_fail
from hyprpy import Hyprland

instance = Hyprland()


def on_monitor_added(sender, **kwargs):
    id = kwargs["monitor_id"]
    name = kwargs["monitor_name"]
    description = kwargs["monitor_description"]
    print(f"Monitor connected: {id}, {name}, {description}")
    run_or_fail(["notify-send", F"Monitor connected: {name}, {description}"])


def on_monitor_removed(sender, **kwargs):
    name = kwargs["monitor_name"]
    print(f"Monitor removed: {name}")
    run_or_fail(["notify-send", F"Monitor removed: {name}"])


instance.signals.monitoraddedv2.connect(on_monitor_added)
instance.signals.monitorremoved.connect(on_monitor_removed)
instance.watch()

