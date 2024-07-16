import os
import sys
import logging

#Time<> Log Level <> Module Name <> message
logging_str = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"

#create log folder
log_dir = "logs"
log_filepath = os.path.join(log_dir,"running_logs.log")
os.makedirs(log_dir, exist_ok=True)


logging.basicConfig(
    level= logging.INFO,
    format= logging_str,

    handlers=[
        logging.FileHandler(log_filepath), #create logs and save logs
        logging.StreamHandler(sys.stdout) #Print logs in the Terminal
    ]
)

logger = logging.getLogger("mlProjectLogger")