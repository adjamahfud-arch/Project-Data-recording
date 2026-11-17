from dataclasses import dataclass, asdict

@dataclass
class Ini:
   nama: str
   alamat: str
   waktu: str =""
   status: bool =True

   def to_dict(self):
       return asdict(self)
     
   @classmethod
   def from_dict(cls,data):
       return cls(**data)
     