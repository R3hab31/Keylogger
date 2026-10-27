import time
stats={"status":"idle",
        "current":"-",
        "duration":"00:00",
        "start_time":None,
        "total":0,
        "top":["-","-","-","-","-"],
        "running":False,
        "freq":{}}

def start_track():
     stats["status"] = "Tracking"
     stats["running"] = True
     if stats["start_time"] is None:
          stats["start_time"] = time.time()

def stop_track():
    stats["status"]="Stopped"
    stats["running"]=False

def reset():
    stats["current"]="-"
    stats["duration"]="00:00"
    stats["running"]=False
    stats["start_time"]=None
    stats["status"]="Idle"
    stats["top"]=["-","-","-","-","-"]
    stats["total"]=0
    stats["freq"]={}

def update():
    if stats["running"] and stats["start_time"]:
        elapsed=int(time.time() - stats["start_time"])
        min=elapsed//60
        sec=elapsed%60
        stats["duration"]=f"{int(min):02d}:{int(sec):02d}"

def key_press(key):
    if not stats["running"]:
        return
    stats["current"]=key

    stats["total"]+=1
    if key in stats["freq"]:
        stats["freq"][key]+=1
    else:
        stats["freq"][key] =1

def top():
    sorted_keys=sorted(stats["freq"].items(),
                             key=lambda x: x[1],
                             reverse=True)
    stats["top"]=[f"{k} -> {v}"
        for k, v in sorted_keys[:5]
    ] if sorted_keys else ["-","-","-","-","-"]



def get_stats():
    update() 
    top()
    return stats


