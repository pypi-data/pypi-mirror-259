from .__version__ import __version__
from abc import ABC, abstractmethod
from collections.abc import Iterable
from typing import Tuple

import hashlib
from pathlib import Path
import sqlite3
from datetime import datetime as dt

N = 2


class RepoException(Exception):
    """Any Exception thrown by a Repo method"""

class Repo(ABC):
    """"""
    @abstractmethod
    def reproduce(self, cid:str) -> Tuple[dt, any]:
        raise RepoException()

    @abstractmethod
    def remember(self, cid:str, sig:str, result:any, start:dt, end:dt):
        raise RepoException()


class TextFileRepo(Repo):
    def __init__(self, store: str, sqlite: str = None):
        self.db = sqlite or f'{store}/memo.sqlite'
        try:
            con = sqlite3.connect(self.db)
        except sqlite3.OperationalError as oe:
            raise RepoException(f"cannot connect to {self.db}") from oe
        cur = con.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS store (cid TEXT PRIMARY KEY, signature TEXT, start TEXT, end TEXT)")
        con.close()

        self.store = store

    def file_path(self, cid):
        return Path(f'{self.store}/{cid[:N]}/{cid}')

    def reproduce(self, cid:str) -> Tuple[dt, str|Iterable]:
        con = sqlite3.connect(self.db)
        try:
            cur = con.cursor()
            cur.execute("SELECT start FROM store WHERE cid = ?", (cid,))
            [(start,)] = cur.fetchall()
        except Exception as e:
            raise RepoException() from e
        finally:
            con.close()

        fpath = self.file_path(cid)
        if fpath.is_file():
            with fpath.open('r', encoding='utf-8') as fp:
                return dt.fromisoformat(start), fp.read()
        elif fpath.is_dir():
            results = []
            for i in range(len(list(fpath.iterdir()))):
                with (fpath / f"{i}").open('r', encoding='utf-8') as fp:
                    results.append(fp.read())
            return dt.fromisoformat(start), results
        else:
            con = sqlite3.connect(self.db)
            try:
                cur = con.cursor()
                cur.execute("DELETE FROM store WHERE cid = ?", (cid,))
                con.commit()
            except Exception as e:
                raise RepoException() from e
            finally:
                con.close()
            raise RepoException("Cannot find the cached result in filesystem. Try again.")

    def remember(self, cid:str, sig: str, result: str|Iterable, start: dt, end: dt):
        fpath = self.file_path(cid)
        fpath.parent.mkdir(exist_ok=True)
        if isinstance(result, str):
            with fpath.open('w', encoding='utf-8') as fp:
                fp.write(result)
        elif isinstance(result, Iterable):
            if fpath.is_file():
                fpath.unlink()
            if fpath.is_dir():
                for fl in fpath.iterdir():
                    fl.unlink()
            fpath.mkdir(exist_ok=True)

            result = list(result)  # at this point a generator will be consumed

            for i, part in enumerate(result):
                with (fpath / f"{i}").open('w', encoding='utf-8') as fp:
                    fp.write(part)
        else:
            raise ValueError("can only remember strings and lists of strings")

        con = sqlite3.connect(self.db)
        try:
            cur = con.cursor()
            cur.execute("INSERT INTO store (cid, signature, start, end) VALUES (?, ?, ?, ?)",
                        (cid, sig, start.isoformat(), end.isoformat()))
            con.commit()
        finally:
            con.close()

        return result  # the input parameter is returned as is but all Iterables are lists now

    def when(self, cid:str):
        con = sqlite3.connect(self.db)
        try:
            cur = con.cursor()
            cur.execute("SELECT start, end FROM store WHERE cid = ?", (cid,))
            [(start, end)] = cur.fetchall()
        finally:
            con.close()
        return start, end


def hash_str(string: str):
    h = hashlib.md5()
    h.update(string.encode())
    return h.hexdigest()


def a_str(args: list):
    return str(args)[1:-1] if args else ""


def kw_str(args, kwargs: dict):
    if not kwargs:
        return ""
    prefix = ", " if args else ""
    kwsigs = []
    for k,v in sorted(kwargs.items()):
        kwsigs.append(f"{k}={str([v])[1:-1]}")
    return prefix + ", ".join(kwsigs)


def signature(func, args, kwargs):
    return f"{func.__name__}({a_str(args)}{kw_str(args, kwargs)})"


def cached(store: Repo):
    def sd_cached(func):
        def cached_func(*args, **kargs):
            sig = signature(func, args, kargs)
            cid = hash_str(sig)
            try:
                return store.reproduce(cid)
            except RepoException:
                start = dt.now(tz=None)
                result = func(*args, **kargs)
                end = dt.now(tz=None)
                try:
                    result = store.remember(cid, sig, result, start, end)
                except RepoException:
                    pass
                return start, result
        return cached_func
    return sd_cached
