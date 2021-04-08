from os import getenv

from dotenv import load_dotenv

load_dotenv()

SESSION_NAME = getenv("SESSION_NAME", "session")
BOT_TOKEN = getenv("BOT_TOKEN")
BOT_NAME = getenv("BOT_NAME")

API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")

DURATION_LIMIT = int(getenv("DURATION_LIMIT", "7"))

COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ !").split())

SUDO_USERS = list(map(int, getenv("SUDO_USERS").split()))


SESSION_NAME= "BQAyd3DsG4YsTe8yWZYnWJDeZY_E5QfQVEaVAHcDHeFXICJPSwB1iKOfruhEG5ASfymtkBQagr85P1rhkFXlaUVzKAYIeCOt0wklQJY3twDzWV4KcAgORiFp4M9bBVfZI7JaffLGd6-LODNN6PSn_9DTH5qTqKP5f-AusIRXNzQi_IJaVfWBV1pmf9M20lrexnFgucwctq4PUDbRaZ1d8mADAvWMKzliiY6UGWVhgrnpmVTUaCUS0Al9ksWm8psqGy3S6tVZPLErPS3ATpOF43BcJMt98685MutycMf7h9crsUNNNIseV6KMH-8yuWZPjagVDlnR5tZuPUH-yVDiTwMbPtmoUAA"
BOT_TOKEN= "1556849815:AAGyafjOM5BOEsPXRrTWf0YouMUhdcaUo0E"
BOT_NAME= "Group Music Bot"
API_ID=3397400
API_HASH= "6b6069887e823aade4dad8fb576f6ad2"
SUDO_USERS=1418166549 # List of user IDs separated by space
DURATION_LIMIT=7 # in minutes (default: 7)
    
    
