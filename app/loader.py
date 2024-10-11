from pathlib import Path
from dotenv import load_dotenv
import logging.config

# Путь к .env и создание директорий для логов
BASE_DIR = Path(__file__).parent.resolve()
load_dotenv(BASE_DIR / ".env")

for log_dir in ["err", "out", "kivy"]:
    (BASE_DIR / "logs" / log_dir).mkdir(parents=True, exist_ok=True)

# Настройка логирования
logging.config.fileConfig(
    BASE_DIR / "logging.conf",
    defaults={
        "err_log_file": (BASE_DIR / "logs/err/err.log").as_posix(),
        "out_log_file": (BASE_DIR / "logs/out/out.log").as_posix(),
    },
    disable_existing_loggers=False
)

logger = logging.getLogger(f"root.{__name__}")





