import thread

# Identify the current thread to determine whether packets in other threads should be sent as threaded with Twisted
MAIN_THREAD = thread.get_ident()

# Aliter related
MAP_CACHE_VERSION = 3
AREA_SERVER, AREA_MAP, AREA_VISIBLE = range(3)

# Character stats
STAT_SPEED  = 0x00
STAT_HP     = 0x05
STAT_MAX_HP = 0x06
STAT_SP     = 0x07
STAT_MAX_SP = 0x08
STAT_STAT_POINTS  = 0x09
STAT_BASE_LEVEL   = 0x0b
STAT_SKILL_POINTS = 0x0c
STAT_WEIGHT       = 0x18 # True weight = STAT_WEIGHT / 10
STAT_MAX_WEIGHT   = 0x19 # True max weight = STAT_MAX_WEIGHT / 10
STAT_ATK_A  = 0x29
STAT_ATK_B  = 0x2a
STAT_MATK_A = 0x2b
STAT_MATK_B = 0x2c
STAT_DEF_A  = 0x2d
STAT_DEF_B  = 0x2e
STAT_MDEF_A = 0x2f
STAT_MDEF_B = 0x30
STAT_HIT    = 0x31
STAT_FLEE_A = 0x32
STAT_FLEE_B = 0x33
STAT_ASPD   = 0x35 # In 2ms units?
STAT_JOB_LEVEL = 0x37

# ANSI colours
ANSI_DEFAULT     = '\033[0m'
ANSI_BLACK       = '\033[0;30m'
ANSI_DARK_GREY   = '\033[1;30m'
ANSI_RED         = '\033[0;31m'
ANSI_LIGHT_RED   = '\033[1;31m'
ANSI_GREEN       = '\033[0;32m'
ANSI_LIGHT_GREEN = '\033[1;32m'
ANSI_GOLD        = '\033[0;33m'
ANSI_YELLOW      = '\033[1;33m'
ANSI_BLUE        = '\033[0;34m'
ANSI_LIGHT_BLUE  = '\033[1;34m'
ANSI_PURPLE      = '\033[0;35m'
ANSI_MAGENTA     = '\033[1;35m'
ANSI_CYAN        = '\033[0;36m'
ANSI_LIGHT_CYAN  = '\033[1;36m'
ANSI_GREY        = '\033[0;37m'
ANSI_WHITE       = '\033[1;37m'

ANSI_BG_BLACK   = '\033[40m'
ANSI_BG_RED     = '\033[41m'
ANSI_BG_GREEN   = '\033[42m'
ANSI_BG_GOLD    = '\033[43m'
ANSI_BG_BLUE    = '\033[44m'
ANSI_BG_PURPLE  = '\033[45m'
ANSI_BG_CYAN    = '\033[46m'
ANSI_BG_GREY    = '\033[47m'
