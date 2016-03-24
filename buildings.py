class buildings:

    @staticmethod
    def builds(building, player, planet, *args):
        success = 0
        for key in buildings.buildings[building]["cost"].keys():
            if planet['resource'][key] - buildings.buildings[building]["cost"][key] > 0:
                success +=1

        if success == len(buildings.buildings[building]["cost"]):
            for key in buildings.buildings[building]["cost"].keys():
                planet['resource'][key] -= buildings.buildings[building]["cost"][key]      

            planet['building'][building] +=1
            return True
        else:
            return False

    buildings = {"mine": {
                        "cost":  {
                                    "REEResource": 200,
                                    "waterResource": 100
                                 },
                        "output": 100,
                        "requirements": None
                         },
                "farm": {
                        "cost": {
                                    "REEResource": 200,
                                    "waterResource": 100
                                    
                                },
                        "output": 100,
                        "requirements": None
                        },
                "desalination": {
                        "cost": {
                                    "REEResource": 200,
                                    "waterResource": 100
                                },
                        "output": 100,
                        "requirements": None
                        }

                }

    

