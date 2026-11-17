import logging
import json
from pathlib import Path
from kelas import Ini

file_name =Path("Data/User_data.json")

logging.basicConfig(
      filename="Tampung.log",
      level=logging.INFO,
      format="%(levelname)s - %(message)s - %(asctime)s"
)

class Ssimpan:
   @staticmethod
   def load():
       try:
         data_u =json.loads(
               file_name.read_text(encoding="utf-8")
         )
         return [Ini.from_dict(x) for x in data_u]
         
       except FileNotFoundError:
            logging.exception("file tidak di temukan")
            print(f"file tidak di temukan")
            return []
         
       except (json.JSONDecodeError, KeyError) as jd:
            logging.exception("file rusak")
            print(f"file rusak:{jd}")
            return []
         
       except Exception as cpt:
            logging.exception("error")
            print(f"error:{cpt}")
            return []
         
   @staticmethod 
   def simpan_dta(data):
       try:
         dta_ready =[y.to_dict() for y in data]
         file_name.write_text(
            json.dumps(dta_ready,ensure_ascii=False, indent=4),
            encoding="utf-8"
            )
         return True
         
       except OSError as eo:
            logging.exception("error")
            print(f"error ({eo})")
            return False
         
       except Exception as tion:
            logging.exception("error")
            print(f"error:{tion}")
            return False