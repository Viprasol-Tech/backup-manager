"""
backup-manager - Manage incremental and full backups

Part of Viprasol Utilities: https://viprasol.com
"""

__version__ = "0.1.0"
__author__ = "Viprasol"
__email__ = "hello@viprasol.com"

from .core import BackupManager, manage, process, main

__all__ = ["BackupManager", "manage", "process", "main"]
