
import json

class JsonComposer:

    def __init__(self):
        self.elems = []

    def add_basis(self, mat3, color):
        self.elems.append({
            "type" : "basis",
            "data" : mat3.tolist(),
            "color" : color
        })

    def add_eig_basis(self, e, lam, color):
        self.elems.append({
            "type" : "eigbasis",
            "e" : (e * [lam]).tolist(),
            "lam" : lam.tolist(),
            "color" : color
        })

    def add_transform(self, mat3, color):

        self.elems.append({
            "type" : "transform",
            "data" : mat3.tolist(),
            "color" : color
        })

    def save(self):
        with open("data.json.js", "w") as f:
            f.write("json = ")
            f.write(json.dumps({
                "elems" : self.elems
            }))
