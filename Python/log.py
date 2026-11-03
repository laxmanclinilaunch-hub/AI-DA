import logging
import os
import sys



log_dir="loogings"

log_file="app.log"


os.makedirs(log_dir,exist_ok=True)

log_path=os.path.join(log_dir,log_file)


logging.basicConfig(filename=log_path,level=logging.INFO,format="[%(asctime)s] %(name)s -%(levelname)s - %(message)s",force=True)


