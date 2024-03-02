import logging

logging.getLogger("simple_toml_configurator").setLevel(logging.ERROR)
logging.getLogger("Configuration").setLevel(logging.ERROR)
logging.getLogger("ews_core_config").setLevel(logging.ERROR)

from ews_core_config.config import read_settings  # noqa: E402

EWSSettings = read_settings()

from ews_nox.utilities import git  # noqa

print(EWSSettings.get_settings())


print(git.get_username())
print(git.get_email())
print(git.get_branch())
print(git.get_status())
print(git.get_hash())
print(git.get_hash(short=True))
# print(git.check_on_main_no_changes())
