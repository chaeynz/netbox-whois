import os
from fs import WhoisFS
from fuse import FUSE

if __name__ == "__main__":
    mountpoint = "./whoisfs"
    os.makedirs(mountpoint, exist_ok=True)
    print(f"Mounting fake whois file at {mountpoint}/whoisdb")
    FUSE(WhoisFS(), mountpoint, foreground=True)
