from login import LogFileMixin, LogPrintMixin

lp = LogPrintMixin()
lp.log_error('Voce errou o login')
lp.log_sucess('Bem vindo')

lf = LogFileMixin()
lf.log_error('Voce errou o login')
lf.log_sucess('Bem vindo')