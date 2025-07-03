# src/criptopipe/config/logger.py
import logging
import logging.handlers
import os
from criptopipe.src.criptopipe.config.settings import log_file


class CollectorLogger():
    """    CollectorLogger é uma classe responsável por configurar o sistema de logging para a coleta de dados de APIs
    de criptomoedas. Ela utiliza o módulo logging do Python para criar logs detalhados das operações realizadas,
    incluindo erros e informações de depuração."""

    def configure_logging(self) -> logging.Logger:
        """Configura o sistema de logging"""

        # Cria diretório se não existir
        os.makedirs("logs", exist_ok=True)

        # Retorna o logger root ou um específico
        logger = logging.getLogger('collector_logs')

        # Configura o nível do logger
        logger.setLevel(logging.DEBUG)

        # Handler para salvar em arquivo (com rotação, para não encher o disco)
        # RotatingFileHandler: cria novos arquivos de log quando o atual atinge um tamanho
        if not logger.handlers:
            file_handler = logging.handlers.RotatingFileHandler(
                log_file,
                maxBytes=10 * 1024 * 1024,  # 10 MB
                backupCount=5              # Mantém 5 arquivos de backup
            )
            file_handler.setLevel(logging.DEBUG)  # Nível para o arquivo de log

            # Handler para exibir no console (opcional, mas bom para monitoramento imediato)
            console_handler = logging.StreamHandler()
            # Pode ser mais verboso no console para debug
            console_handler.setLevel(logging.DEBUG)

            # Formato das mensagens
            message_formatter = logging.Formatter(
                '%(asctime)s - %(name)s - %(levelname)s - %(message)s')

            # Adiciona o formatador aos handlers
            file_handler.setFormatter(message_formatter)
            console_handler.setFormatter(message_formatter)

            # Adiciona os handlers ao logger
            logger.addHandler(file_handler)
            # logger.addHandler(console_handler)

        return logger
