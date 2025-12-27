import os
import zipfile

EXCLUDE_DIRS = {'.venv', '__pycache__'}
EXCLUDE_FILES = {"error_recovery_agent.zip"}

def should_exclude(name):
    if name in EXCLUDE_FILES:
        return True
    return False

def main():
    out_name = 'error_recovery_agent.zip'
    with zipfile.ZipFile(out_name, 'w', compression=zipfile.ZIP_DEFLATED) as zf:
        for root, dirs, files in os.walk('.'):
            # skip excluded directories
            dirs[:] = [d for d in dirs if d not in EXCLUDE_DIRS and not d.startswith('.')]
            for f in files:
                if should_exclude(f):
                    continue
                if f.endswith('.zip'):
                    continue
                path = os.path.join(root, f)
                arcname = os.path.relpath(path, '.')
                zf.write(path, arcname)

if __name__ == '__main__':
    main()
