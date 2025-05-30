from fuse import FUSE, Operations
import os, time, stat
from whois import get_content

class WhoisFS(Operations):
    def __init__(self):
        self.filename = "whoisdb"

    @property
    def content(self):
        return get_content()

    def getattr(self, path, fh=None):
        now = time.time()
        if path == "/":
            return {
                "st_mode": stat.S_IFDIR | 0o755,
                "st_nlink": 2,
                "st_ctime": now,
                "st_mtime": now,
                "st_atime": now,
            }
        elif path == f"/{self.filename}":
            return {
                "st_mode": stat.S_IFREG | 0o444,
                "st_nlink": 1,
                "st_size": len(self.content),
                "st_ctime": now,
                "st_mtime": now,
                "st_atime": now,
            }
        else:
            raise FileNotFoundError()

    def readdir(self, path, fh):
        return [".", "..", self.filename]

    def open(self, path, flags):
        if path != f"/{self.filename}":
            raise FileNotFoundError()
        return 0

    def read(self, path, size, offset, fh):
        if path != f"/{self.filename}":
            raise FileNotFoundError()
        return self.content.encode("utf-8")[offset:offset + size]
