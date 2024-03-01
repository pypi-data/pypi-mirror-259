import comet_ml
import time
import random
import os
from xspike.utils import Logger, get_file_paths_in_directory

log = Logger(__name__)
IGNORED_FILES = [".log", ".out", ".err", ".pyc", ".ipynb_checkpoints", ".git", ".idea", ".vscode", ".DS_Store", ".pt", ".pth", ".pkl", ".gz", ".zip", ".zip", ".tar", ".json", ".jsonl", ".csv", ".tsv", ".h5", ".txt", ".md", ".pdf", ".png", ".jpg", ".jpeg", ".gif", ".svg", ".doc", ".docx", ".ppt", ".pptx", ".xls", ".xlsx", ".csv", ".db", ".sqlite", ".sqlite3", ".db3", ".sql"]


class CometClient:
    
    def __init__(self, project_name=None, workspace=None, api_key=None, exp_name=None):
        self.project_name = project_name
        self.workspace = workspace
        self.api_key = api_key
        # 生成实验独一无二的 ID
        self.experiment_key = str(int(time.time() * 1000)) + str(random.randint(0, 9999))
        os.environ["COMET_EXPERIMENT_KEY"] = self.experiment_key
        
        self.experiment = comet_ml.Experiment(api_key=api_key,
                                            project_name=project_name,
                                            experiment_key=self.experiment_key)
        self.experiment.set_name(exp_name)
        self.experiment.log_other("进程ID", str(os.getpid()))
            
        log.info("Comet 实验记录已启动")
        
    def get_experiment_by_key(self):
        api = comet_ml.api.API()
        experiment = api.get_experiment_by_key(os.environ["COMET_EXPERIMENT_KEY"])
        return experiment
    
    def get_experiment(self):
        return self.experiment


    def log_directory(self, directory, ignored_files=IGNORED_FILES):
        file_paths = get_file_paths_in_directory(directory, ignored_files)
        for file_path in file_paths:
            try:
                self.experiment.log_asset(file_path)
            except Exception as e:
                log.warning(f"文件 {file_path} 上传至 Comet 失败: {e}")
                log.warning(f"请检查文件是否过大，或是否有特殊字符")
        log.info(f"目录 {directory} 下的文件已上传至 Comet")
        