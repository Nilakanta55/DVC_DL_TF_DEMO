from src.utils.all_utils import read_yaml, create_directory
from src.utils.model import get_VGG_16_model, prepare_model
from src.utils.callbacks import create_and_save_tensorboard_callback, create_and_save_checkpoints_callback
import argparse
import os
import logging
import io

logging_str = "[%(asctime)s: %(levelname)s: %(module)s]: %(message)s"
log_dir = "logs"
os.makedirs(log_dir, exist_ok=True)
logging.basicConfig(filename=os.path.join(log_dir, 'running_logs.log'), level=logging.INFO, format=logging_str,
                    filemode="a")


def callbacks(config_path,params_path):
    config = read_yaml(config_path)
    params = read_yaml(params_path)

    artifatcs = config["artifacts"]
    artifatcs_dir = artifatcs["ARTIFACTS_DIR"]

    tensorboard_log_dir = os.path.join(artifatcs_dir, artifatcs["TENSORBOARD_ROOT_LOG_DIR"])

    checkpoints_dir = os.path.join(artifatcs_dir, artifatcs["CHECKPOINT_DIR"])

    callbacks_dir = os.path.join(artifatcs_dir, artifatcs["CALLBACKS_DIR"])

    create_directory([tensorboard_log_dir, checkpoints_dir, callbacks_dir])

    create_and_save_tensorboard_callback = (callbacks_dir, tensorboard_log_dir)
    create_and_save_checkpoints_callback = (callbacks_dir, checkpoints_dir)




if __name__ == '__main__':
    args = argparse.ArgumentParser()

    args.add_argument("--config", "-c", default="config/config.yaml")
    args.add_argument("--params", "-p", default="params.yaml")

    parsed_args = args.parse_args()

    try:
        logging.info(">>>>> stage three started")
        prepare_callbacks(config_path=parsed_args.config, params_path=parsed_args.params)
        logging.info("stage three completed! callbacks are prepared & saved as binary>>>>>")
    except Exception as e:
        logging.exception(e)
        raise e