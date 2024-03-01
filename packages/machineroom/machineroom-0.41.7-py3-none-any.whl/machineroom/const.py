class PROJECT1:
    REMOTE_WS: str = "...remote_locator"
    RAM_GB_REQUIREMENT: int = 4
    DISK_GB_REQUIREMENT: int = 100
    CONTAINER_NAME_IDS: list = []


class PROJECT2:
    YACHT_API_KEY: str = "---paste here---"


class Config(PROJECT1, PROJECT2):
    DATAPATH_BASE: str = "...._file....locator"
    TEMP_FILE: str = "tmp.txt"
    TEMP_JS: str = "tmp.js"
    PUB_KEY: str = "/Users/xxxx/.ssh/id_rsa.pub"
    LOCAL_KEY_HOLDER: str = "/Users/xxxx/.ssh"
    MY_KEY_FEATURE: str = "xxx@xxxx"
    HOME: str = "/root"
    DOCKER_COMPOSE_VERSION: str = "2.24.6"
