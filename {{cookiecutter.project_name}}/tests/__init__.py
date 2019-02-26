from os.path import join, dirname

from dotenv import load_dotenv

dotenv_path = join(dirname(dirname(__file__)), '.test.env')
load_dotenv(dotenv_path)
