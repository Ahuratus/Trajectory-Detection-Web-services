 from app.config import *
from app import tracker_module
if __name__ =="__main__":
    assert tracker_module.getTrajectory(TestVideoPath,BUFFER)==STATUS_OK