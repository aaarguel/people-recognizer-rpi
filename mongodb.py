import pymongo,time

def getStateLab(maxTemp,maxPersons) -> bool:
    """
    param maxTemp: Maximum temperature accepted
    param maxPersons:  Maximum number of people accepted
    returns: True -> If the current value exceed the limits set as params, False -> in any other case
    """
    db = pymongo.MongoClient('mongodb+srv://test_user:KKQ4itT08tqQy5MC@testcluster.9rx9v.mongodb.net/testDB')
    
    cursor_measure_camera = db.testDB.measurecameras.find().sort([('createdAt', -1)]).limit(1)
    last_measure_camera = list(cursor_measure_camera)[0]

    cursor_measure_sensors = db.testDB.measuresensors.find().sort([('createdAt', -1)]).limit(1)
    last_measure_sensors = list(cursor_measure_sensors)[0]
    print(last_measure_camera['persons'])
    print(last_measure_sensors['value'])
    if last_measure_camera['persons'] >=  maxPersons and last_measure_sensors['value'] >= maxTemp:
        return True

    return False
    
state = False
while True:
    
    if state != getStateLab(25,1):
        #TODO: Ejecutar el estado nuevo
        state = not state
        if state:
            print("Encendi")
        else: 
            print("Apagado")
    time.sleep(1)
    

