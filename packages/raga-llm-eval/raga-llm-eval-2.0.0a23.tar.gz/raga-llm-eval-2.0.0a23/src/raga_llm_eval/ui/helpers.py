from signal import SIGTERM  # or SIGKILL

from psutil import process_iter


def killport(port: int):
    for proc in process_iter():
        for conns in proc.connections(kind="inet"):
            if conns.laddr.port == port:
                proc.send_signal(SIGTERM)  # or SIGKILL


def pick_matching_keys_from_dict(target_dict: dict, keys: list[str] = None):
    if keys is None or len(keys) < 1:
        return target_dict
    result = {}
    for k in list(filter(None, keys)):
        for dk in target_dict:
            if dk.startswith(k):
                result[dk] = target_dict[dk]
    return result
