"""
The settings for coinmaker.py
"""

class SETTINGS(object):
    source_dir = './sourcecoin'
    working_dir = './working'
    autogen_command = "./autogen.sh"
    config_command="""./configure --with-incompatible-bdb"""
    make_command="""make -s"""
    os_ext = ""
