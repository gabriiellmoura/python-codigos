# Abstração.
from pathlib import Path
LOG_FILE = Path(__file__).parent / 'log.txt'

class Log:
    def _log(self, msg):
        raise NotImplementedError('implemente o metodo log')

    def log_error(self, msg):
        return self._log(f'Error: {msg}')

    def log_sucess(self, msg):
        return self._log(f'Sucess: {msg}')


class LogFileMixin(Log):
    def _log(self, msg):
        msg_formatada = (f'{msg} ({self.__class__.__name__})')
        with open(LOG_FILE, 'a') as arquivo:
            arquivo.write(msg_formatada)
            arquivo.write('\n')

class LogPrintMixin(Log):
    def _log(self, msg):
        print(f'{msg} ({self.__class__.__name__})')

if __name__ == '__main__':
    
    lp = LogPrintMixin()
    lp.log_error('Voce errou o login')
    lp.log_sucess('Bem vindo')

    lf = LogFileMixin()
    lf.log_error('Voce errou o login')
    lf.log_sucess('Bem vindo')