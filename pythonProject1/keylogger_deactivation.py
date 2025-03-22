import psutil
import os
import signal
import sys


def get_suspicious_processes():
    suspicious_keywords = ["keylog", "hook", "spy", "capture", "record", "monitor"]
    suspicious_processes = []

    for process in psutil.process_iter(attrs=['pid', 'name']):
        try:
            process_name = process.info['name'].lower()
            process_pid = process.info['pid']

            # Check for suspicious keywords in process name
            if any(keyword in process_name for keyword in suspicious_keywords):
                suspicious_processes.append((process_pid, process_name))

            # Check if the process has a suspicious command line
            cmdline = psutil.Process(process_pid).cmdline()
            if any(keyword in ' '.join(cmdline).lower() for keyword in suspicious_keywords):
                suspicious_processes.append((process_pid, process_name))

        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            continue

    return suspicious_processes


def detect_keylogger():
    suspicious_processes = get_suspicious_processes()

    if suspicious_processes:
        print("Potential keyloggers detected:")
        for pid, name in suspicious_processes:
            print(f"PID: {pid}, Process Name: {name}")
    else:
        print("No suspicious keyloggers detected.")


def deactivate_keyloggers():
    suspicious_processes = get_suspicious_processes()

    if suspicious_processes:
        print("Terminating detected keyloggers...")
        for pid, name in suspicious_processes:
            try:
                process = psutil.Process(pid)
                process.terminate()
                process.wait(timeout=3)
                print(f"Terminated: PID {pid}, Process Name: {name}")
            except (psutil.NoSuchProcess, psutil.ZombieProcess):
                print(f"Process already terminated: PID {pid}, Process Name: {name}")
            except psutil.AccessDenied:
                print(f"Permission denied to terminate: PID {pid}, Process Name: {name}. Forcing termination...")
                try:
                    os.kill(pid, signal.SIGKILL)  # Force kill process
                    print(f"Force terminated: PID {pid}, Process Name: {name}")
                except Exception as e:
                    print(f"Failed to force terminate: PID {pid}, Process Name: {name}. Error: {e}")
    else:
        print("No keyloggers found to terminate.")


if __name__ == "__main__":
    detect_keylogger()
    deactivate_keyloggers()