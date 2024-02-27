from dataclasses import dataclass

import config

history_file = config.main_directory + "/files/history.txt"

@dataclass
class HistoriqueSynchronisation:
    date: str
    synchro_message: str

    def save_synchronisation(self):
        pass
