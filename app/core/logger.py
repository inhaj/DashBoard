import os
import aiofiles
import logging
import asyncio
from datetime import datetime
import multiprocessing

class AsyncLoggingHandler(logging.Handler):
    def __init__(self, loop, log_file) -> None:
        super().__init__()
        self.loop = loop
        self.log_file = log_file
        
    
    def emit(self, record):
        log_entry = self.format(record)
        asyncio.run_coroutine_threadsafe(self._log(log_entry), self.loop)
    
    async def _log(self, log_entry):
        async with aiofiles.open(self.log_file, 'a') as f:
            await f.write(log_entry + "\n")
            
    
def setup_logger():
    loop = asyncio.get_event_loop()
    logger = logging.getLogger("my_logger")
    logger.setLevel(logging.DEBUG)
    
    current_dir = os.path.dirname(os.path.abspath(__file__))
    root_dir = os.path.dirname(os.path.dirname(current_dir))
    log_dir = os.path.join(root_dir, 'logs')
    
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)
        
    process_id = multiprocessing.current_process().pid
    log_file = os.path.join(log_dir, f"{datetime.now().strftime('%Y%m%d')}_app_{process_id}.log")
    
    async_handler = AsyncLoggingHandler(loop, log_file)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    async_handler.setFormatter(formatter)
    logger.addHandler(async_handler)
    return logger

logger = setup_logger()