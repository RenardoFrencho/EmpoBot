from envparse import env

env.read_envfile()


BOT_TOKEN = env.str('BOT_TOKEN')
LOGFILE = env.str('LOGFILE')

ADMIN_ID = env.str('ADMIN_ID')
