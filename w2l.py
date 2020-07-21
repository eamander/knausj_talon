from talon import speech_system
from talon.engines.w2l import WebW2lEngine, W2lEngine
engine = WebW2lEngine('https://web2letter-east-1.talonvoice.com', debug=True)
speech_system.add_engine(engine)
