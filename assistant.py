
################################################################
# By: MaxJ02
# April 2023
#
# Voice-controlled ChatGPT virtual assistant.
################################################################

import os
import io
import sys
import asyncio
import argparse
import pyaudio
import wave
from google.cloud import speech
from google.cloud import texttospeech
from ChatGPT_lite.ChatGPT import Chatbot
