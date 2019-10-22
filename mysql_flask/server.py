from app import app
from app.configFileReader import readConfigFile

app.run(debug=readConfigFile("server", "SERVER_DEBUG"),
        port=readConfigFile("server", "SERVER_PORT"),
        host=readConfigFile("server", "SERVER_HOST_NAME"),
)
